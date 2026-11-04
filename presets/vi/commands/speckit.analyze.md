---
description: Phân tích tính nhất quán và chất lượng giữa các artifact spec.md, plan.md và tasks.md sau khi sinh tác vụ, không sửa đổi bất kỳ file nào.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-spec --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireSpec -RequireTasks -IncludeTasks
  py: scripts/python/check_prerequisites.py --json --require-spec --require-tasks --include-tasks
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi phân tích)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_analyze`
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi tiếp tục như bình thường
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook tùy chọn** (`optional: true`):
    ```
    ## Hook của extension

    **Pre-hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```
  - **Hook bắt buộc** (`optional: false`):
    ```
    ## Hook của extension

    **Pre-hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}

    Chờ kết quả của lệnh hook trước khi chuyển sang phần Mục tiêu.
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua

## Mục tiêu

Xác định các điểm không nhất quán, trùng lặp, mơ hồ và chưa được đặc tả đủ trong ba artifact cốt lõi (`spec.md`, `plan.md`, `tasks.md`) trước khi triển khai. Lệnh này CHỈ được chạy sau khi `__SPECKIT_COMMAND_TASKS__` đã tạo thành công một `tasks.md` hoàn chỉnh.

## Ràng buộc khi vận hành

**CHỈ ĐỌC, TUYỆT ĐỐI KHÔNG GHI**: **Không** sửa bất kỳ file nào. Xuất một báo cáo phân tích có cấu trúc. Có thể đề xuất kế hoạch khắc phục tùy chọn (người dùng phải phê duyệt rõ ràng trước khi bất kỳ lệnh chỉnh sửa tiếp theo nào được gọi thủ công).

**Thẩm quyền của hiến chương**: Hiến chương dự án (`/memory/constitution.md`) là **không thể thương lượng** trong phạm vi phân tích này. Xung đột với hiến chương mặc nhiên là CRITICAL và đòi hỏi điều chỉnh đặc tả, kế hoạch hoặc tác vụ, chứ không được làm loãng, diễn giải lại hay âm thầm bỏ qua nguyên tắc. Nếu bản thân một nguyên tắc cần thay đổi, việc đó phải diễn ra trong một lần cập nhật hiến chương riêng, rõ ràng, bên ngoài `__SPECKIT_COMMAND_ANALYZE__`.

## Các bước thực thi

### 1. Khởi tạo bối cảnh phân tích

Chạy `{SCRIPT}` một lần từ thư mục gốc repo và parse JSON để lấy FEATURE_DIR và AVAILABLE_DOCS. Suy ra các đường dẫn tuyệt đối:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md

Dừng lại kèm thông báo lỗi nếu thiếu bất kỳ file bắt buộc nào (hướng dẫn người dùng chạy lệnh tiên quyết còn thiếu).
Với dấu nháy đơn trong đối số như "I'm Groot", dùng cú pháp escape: ví dụ 'I'\''m Groot' (hoặc dùng nháy kép nếu được: "I'm Groot").

### 2. Nạp artifact (nạp dần theo nhu cầu)

Chỉ nạp phần bối cảnh tối thiểu cần thiết từ mỗi artifact:

**Từ spec.md:**

- Tổng quan/Bối cảnh
- Yêu cầu chức năng
- Tiêu chí thành công (kết quả đo lường được — ví dụ hiệu năng, bảo mật, tính sẵn sàng, mức độ thành công của người dùng, tác động kinh doanh)
- User story
- Trường hợp biên (nếu có)

**Từ plan.md:**

- Lựa chọn kiến trúc/stack
- Tham chiếu mô hình dữ liệu
- Các giai đoạn
- Ràng buộc kỹ thuật

**Từ tasks.md:**

- Task ID
- Mô tả
- Cách nhóm theo giai đoạn
- Dấu song song [P]
- Đường dẫn file được tham chiếu

**Từ hiến chương:**

- Nạp `/memory/constitution.md` để kiểm tra theo nguyên tắc

### 3. Xây dựng mô hình ngữ nghĩa

Tạo các biểu diễn nội bộ (không đưa nguyên văn artifact vào đầu ra):

- **Danh mục yêu cầu**: Với mỗi yêu cầu chức năng (FR-###) và tiêu chí thành công (SC-###), ghi lại một khóa ổn định. Dùng mã định danh FR-/SC- làm khóa chính khi có, và có thể suy ra thêm một slug từ cụm động từ mệnh lệnh cho dễ đọc (ví dụ "User can upload file" → `user-can-upload-file`). Chỉ đưa vào các tiêu chí thành công cần phần việc xây dựng được (ví dụ hạ tầng load test, công cụ audit bảo mật), và loại các chỉ số kết quả sau khi ra mắt hay KPI kinh doanh (ví dụ "Giảm 50% số yêu cầu hỗ trợ").
- **Danh mục user story/hành động**: Các hành động riêng lẻ của người dùng kèm tiêu chí chấp nhận
- **Ánh xạ độ phủ của tác vụ**: Ánh xạ mỗi tác vụ tới một hoặc nhiều yêu cầu hoặc story (suy ra theo từ khóa / mẫu tham chiếu rõ ràng như ID hay cụm từ khóa)
- **Bộ quy tắc hiến chương**: Rút ra tên các nguyên tắc và các câu quy phạm PHẢI/NÊN (MUST/SHOULD)

### 4. Các lượt phát hiện (phân tích tiết kiệm token)

Tập trung vào các phát hiện có giá trị cao. Giới hạn tổng cộng 50 phát hiện; gom phần còn lại vào bản tóm tắt phần vượt.

#### A. Phát hiện trùng lặp

- Xác định các yêu cầu gần như trùng nhau
- Đánh dấu cách diễn đạt kém hơn để gộp lại

#### B. Phát hiện mơ hồ

- Gắn cờ các tính từ mơ hồ (nhanh, dễ mở rộng, an toàn, trực quan, mạnh mẽ) không có tiêu chí đo lường được
- Gắn cờ các placeholder chưa xử lý (TODO, TKTK, ???, `<placeholder>`, v.v.)

#### C. Đặc tả chưa đủ

- Yêu cầu có động từ nhưng thiếu đối tượng hoặc kết quả đo lường được
- User story chưa khớp với tiêu chí chấp nhận
- Tác vụ tham chiếu tới file hoặc thành phần chưa được định nghĩa trong đặc tả/kế hoạch

#### D. Phù hợp với hiến chương

- Bất kỳ yêu cầu hay thành phần nào của kế hoạch xung đột với một nguyên tắc PHẢI (MUST)
- Thiếu các mục hoặc cổng kiểm soát chất lượng mà hiến chương bắt buộc

#### E. Lỗ hổng về độ phủ

- Yêu cầu không có tác vụ nào liên quan
- Tác vụ không được ánh xạ tới yêu cầu/story nào
- Tiêu chí thành công cần phần việc xây dựng được (hiệu năng, bảo mật, tính sẵn sàng) nhưng không có trong tác vụ

#### F. Không nhất quán

- Lệch thuật ngữ (cùng một khái niệm nhưng gọi tên khác nhau giữa các file)
- Thực thể dữ liệu được nhắc trong kế hoạch nhưng không có trong đặc tả (hoặc ngược lại)
- Thứ tự tác vụ mâu thuẫn (ví dụ tác vụ tích hợp đặt trước tác vụ thiết lập nền tảng mà không ghi chú phụ thuộc)
- Yêu cầu xung đột nhau (ví dụ một bên yêu cầu Next.js trong khi bên kia chỉ định Vue)

### 5. Gán mức độ nghiêm trọng

Dùng quy tắc kinh nghiệm sau để xếp ưu tiên các phát hiện:

- **CRITICAL**: Vi phạm một nguyên tắc PHẢI của hiến chương, thiếu artifact đặc tả cốt lõi, hoặc yêu cầu không có độ phủ nào làm chặn chức năng cơ bản
- **HIGH**: Yêu cầu trùng lặp hoặc xung đột, thuộc tính bảo mật/hiệu năng mơ hồ, tiêu chí chấp nhận không kiểm thử được
- **MEDIUM**: Lệch thuật ngữ, thiếu độ phủ cho tác vụ phi chức năng, trường hợp biên chưa được đặc tả đủ
- **LOW**: Cải thiện văn phong/câu chữ, dư thừa nhỏ không ảnh hưởng thứ tự thực hiện

### 6. Xuất báo cáo phân tích ngắn gọn

Xuất một báo cáo Markdown (không ghi file) theo cấu trúc sau:

## Báo cáo phân tích đặc tả

| ID | Loại | Mức độ | Vị trí | Tóm tắt | Khuyến nghị |
|----|------|--------|--------|---------|-------------|
| A1 | Trùng lặp | HIGH | spec.md:L120-134 | Hai yêu cầu tương tự nhau ... | Gộp cách diễn đạt; giữ bản rõ ràng hơn |

(Thêm một dòng cho mỗi phát hiện; sinh ID ổn định với tiền tố là chữ cái đầu của loại.)

**Bảng tóm tắt độ phủ:**

| Khóa yêu cầu | Có tác vụ? | Task ID | Ghi chú |
|--------------|------------|---------|---------|

**Vấn đề về phù hợp hiến chương:** (nếu có)

**Tác vụ chưa được ánh xạ:** (nếu có)

**Số liệu:**

- Tổng số yêu cầu
- Tổng số tác vụ
- Tỷ lệ phủ % (số yêu cầu có >=1 tác vụ)
- Số điểm mơ hồ
- Số điểm trùng lặp
- Số vấn đề CRITICAL

### 7. Đề xuất các bước tiếp theo

Ở cuối báo cáo, xuất một khối Bước tiếp theo ngắn gọn:

- Nếu có vấn đề CRITICAL: Khuyến nghị xử lý trước khi chạy `__SPECKIT_COMMAND_IMPLEMENT__`
- Nếu chỉ có LOW/MEDIUM: Người dùng có thể tiếp tục, nhưng hãy đưa ra gợi ý cải thiện
- Đưa ra gợi ý lệnh cụ thể: ví dụ "Chạy __SPECKIT_COMMAND_SPECIFY__ để tinh chỉnh", "Chạy __SPECKIT_COMMAND_PLAN__ để điều chỉnh kiến trúc", "Sửa tasks.md thủ công để bổ sung độ phủ cho 'performance-metrics'"

### 8. Đề xuất khắc phục

Hỏi người dùng: "Bạn có muốn tôi đề xuất các chỉnh sửa khắc phục cụ thể cho N vấn đề hàng đầu không?" (KHÔNG tự động áp dụng.)

### 9. Kiểm tra hook của extension

Sau khi báo cáo, kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_analyze`
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi tiếp tục như bình thường
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook tùy chọn** (`optional: true`):
    ```
    ## Hook của extension

    **Hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```
  - **Hook bắt buộc** (`optional: false`):
    ```
    ## Hook của extension

    **Hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua

## Nguyên tắc vận hành

### Hiệu quả bối cảnh

- **Ít token nhưng giá trị cao**: Tập trung vào các phát hiện có thể hành động được, không viết tài liệu dàn trải
- **Nạp dần theo nhu cầu**: Nạp artifact từng phần; không đổ toàn bộ nội dung vào phân tích
- **Đầu ra tiết kiệm token**: Giới hạn bảng phát hiện ở 50 dòng; tóm tắt phần vượt
- **Kết quả tất định**: Chạy lại khi không có thay đổi phải cho ra ID và số đếm nhất quán

### Hướng dẫn phân tích

- **KHÔNG BAO GIỜ sửa file** (đây là phân tích chỉ đọc)
- **KHÔNG BAO GIỜ bịa ra các mục còn thiếu** (nếu thiếu, hãy báo cáo chính xác)
- **Ưu tiên các vi phạm hiến chương** (những vi phạm này luôn là CRITICAL)
- **Dùng ví dụ thay vì liệt kê quy tắc dàn trải** (dẫn ra trường hợp cụ thể, không nêu mẫu chung chung)
- **Báo cáo không có vấn đề một cách gọn gàng** (xuất báo cáo thành công kèm thống kê độ phủ)

## Bối cảnh

{ARGS}
