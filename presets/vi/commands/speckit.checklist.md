---
description: Sinh một checklist tùy chỉnh cho tính năng hiện tại dựa trên yêu cầu của người dùng.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --template checklist-template
  ps: scripts/powershell/check-prerequisites.ps1 -Json -Template checklist-template
  py: scripts/python/check_prerequisites.py --json --template checklist-template
---

## Mục đích của checklist: "Unit test cho văn bản yêu cầu"

**KHÁI NIỆM CỐT LÕI**: Checklist là **UNIT TEST CHO VIỆC VIẾT YÊU CẦU** - chúng kiểm tra chất lượng, độ rõ ràng và mức độ đầy đủ của các yêu cầu trong một lĩnh vực nhất định.

**KHÔNG dùng để kiểm chứng/kiểm thử phần triển khai**:

- ❌ KHÔNG phải "Kiểm tra nút bấm hoạt động đúng"
- ❌ KHÔNG phải "Test xem xử lý lỗi có chạy không"
- ❌ KHÔNG phải "Xác nhận API trả về 200"
- ❌ KHÔNG phải kiểm tra code/phần triển khai có khớp với đặc tả không

**DÙNG để kiểm tra chất lượng yêu cầu**:

- ✅ "Đã định nghĩa yêu cầu về phân cấp thị giác cho mọi loại card chưa?" (đầy đủ)
- ✅ "'Hiển thị nổi bật' đã được định lượng bằng kích thước/vị trí cụ thể chưa?" (rõ ràng)
- ✅ "Yêu cầu về trạng thái hover có nhất quán giữa mọi phần tử tương tác không?" (nhất quán)
- ✅ "Đã định nghĩa yêu cầu về khả năng tiếp cận cho điều hướng bằng bàn phím chưa?" (độ phủ)
- ✅ "Đặc tả có định nghĩa điều gì xảy ra khi ảnh logo không tải được không?" (trường hợp biên)

**Phép ẩn dụ**: Nếu đặc tả của bạn là code viết bằng ngôn ngữ tự nhiên, thì checklist chính là bộ unit test của nó. Bạn đang kiểm tra xem các yêu cầu có được viết tốt, đầy đủ, rõ ràng và sẵn sàng để triển khai hay không - KHÔNG phải kiểm tra phần triển khai có chạy hay không.

**Quyền sở hữu và vòng đời của checkbox**:

- Các checklist tùy chỉnh do lệnh này sinh ra là artifact review chất lượng yêu cầu, thuộc về người review.
- `[x]` nghĩa là người review đã xác định tiêu chí chất lượng yêu cầu được đáp ứng.
- `[x]` KHÔNG có nghĩa là phần việc triển khai đã xong.
- Lệnh này sinh hoặc bổ sung các mục checklist; nó KHÔNG ĐƯỢC đánh dấu `[x]` cho các mục được sinh ra.
- Agent chỉ được hỗ trợ đánh giá các mục khi người review yêu cầu rõ ràng.
- `checklists/requirements.md` là một checklist chất lượng đặc tả có sẵn, riêng biệt, do `__SPECKIT_COMMAND_SPECIFY__` và `__SPECKIT_COMMAND_CLARIFY__` quản lý; đừng áp ngoại lệ đó cho các checklist tùy chỉnh được sinh ở đây.

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi sinh checklist)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_checklist`
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

    Chờ kết quả của lệnh hook trước khi chuyển sang phần Các bước thực thi.
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua

## Các bước thực thi

1. **Thiết lập**: Chạy `{SCRIPT}` từ thư mục gốc repo và parse JSON để lấy FEATURE_DIR, danh sách AVAILABLE_DOCS và TEMPLATE_CONTENT.
   - Mọi đường dẫn file phải là đường dẫn tuyệt đối.
   - Với dấu nháy đơn trong đối số như "I'm Groot", dùng cú pháp escape: ví dụ 'I'\''m Groot' (hoặc dùng nháy kép nếu được: "I'm Groot").

2. **NẾU CÓ**: Nạp `/memory/constitution.md` để lấy các nguyên tắc dự án và ràng buộc quản trị.

3. **Làm rõ ý định (linh hoạt)**: Suy ra tối đa BA câu hỏi làm rõ ban đầu theo bối cảnh (không dùng danh mục soạn sẵn). Các câu hỏi PHẢI:
   - Được sinh từ cách diễn đạt của người dùng + các tín hiệu rút ra từ spec/plan/tasks
   - Chỉ hỏi về thông tin làm thay đổi đáng kể nội dung checklist
   - Được bỏ qua từng câu nếu điều đó đã rõ ràng trong `$ARGUMENTS`
   - Ưu tiên độ chính xác hơn độ bao quát

   Thuật toán sinh câu hỏi:
   1. Rút ra các tín hiệu: từ khóa lĩnh vực của tính năng (ví dụ auth, độ trễ, UX, API), dấu hiệu rủi ro ("quan trọng", "bắt buộc", "tuân thủ"), gợi ý về các bên liên quan ("QA", "review", "đội bảo mật") và các sản phẩm bàn giao được nêu rõ ("a11y", "rollback", "contract").
   2. Gom các tín hiệu thành những vùng trọng tâm ứng viên (tối đa 4), xếp hạng theo mức độ liên quan.
   3. Xác định đối tượng sử dụng & thời điểm dùng khả dĩ (tác giả, người review, QA, phát hành) nếu chưa được nêu rõ.
   4. Phát hiện các chiều còn thiếu: độ rộng phạm vi, độ sâu/độ nghiêm ngặt, trọng tâm rủi ro, ranh giới loại trừ, tiêu chí chấp nhận đo lường được.
   5. Soạn câu hỏi theo các dạng mẫu sau:
      - Thu hẹp phạm vi (ví dụ "Checklist có nên bao gồm các điểm tích hợp với X và Y, hay chỉ giới hạn ở tính đúng đắn của module cục bộ?")
      - Ưu tiên rủi ro (ví dụ "Trong các vùng rủi ro tiềm ẩn này, vùng nào cần có bước kiểm tra chặn bắt buộc?")
      - Hiệu chỉnh độ sâu (ví dụ "Đây là danh sách kiểm tra nhanh trước khi commit hay là một cổng phát hành chính thức?")
      - Xác định đối tượng (ví dụ "Checklist này chỉ do tác giả dùng hay cả đồng nghiệp dùng khi review PR?")
      - Loại trừ ranh giới (ví dụ "Có nên loại hẳn các mục tối ưu hiệu năng trong đợt này không?")
      - Khoảng trống về nhóm kịch bản (ví dụ "Không thấy luồng phục hồi nào—rollback / lỗi một phần có nằm trong phạm vi không?")

   Quy tắc định dạng câu hỏi:
   - Nếu đưa ra các phương án, sinh một bảng ngắn gọn với các cột: Phương án | Ứng viên | Vì sao quan trọng
   - Giới hạn tối đa từ A đến E; bỏ bảng nếu câu trả lời tự do rõ ràng hơn
   - Không bao giờ yêu cầu người dùng nhắc lại điều họ đã nói
   - Tránh các nhóm phỏng đoán (không bịa). Nếu không chắc, hỏi thẳng: "Xác nhận giúp X có nằm trong phạm vi không."

   Giá trị mặc định khi không thể tương tác:
   - Độ sâu: Tiêu chuẩn
   - Đối tượng: Người review (PR) nếu liên quan tới code; còn lại là tác giả
   - Trọng tâm: 2 cụm liên quan nhất

   Xuất các câu hỏi (đánh nhãn Q1/Q2/Q3). Sau khi có câu trả lời: nếu còn ≥2 nhóm kịch bản (Thay thế / Ngoại lệ / Phục hồi / Phi chức năng) chưa rõ, bạn CÓ THỂ hỏi thêm tối đa HAI câu tiếp theo có trọng tâm (Q4/Q5), mỗi câu kèm một dòng giải thích (ví dụ "Rủi ro về luồng phục hồi chưa được giải quyết"). Không vượt quá tổng cộng năm câu hỏi. Bỏ qua việc hỏi thêm nếu người dùng nói rõ không muốn.

4. **Hiểu yêu cầu của người dùng**: Kết hợp `$ARGUMENTS` + các câu trả lời làm rõ:
   - Suy ra chủ đề checklist (ví dụ bảo mật, review, deploy, ux)
   - Gom các mục bắt buộc phải có mà người dùng nêu rõ
   - Ánh xạ các lựa chọn trọng tâm vào khung các nhóm
   - Suy ra bối cảnh còn thiếu từ spec/plan/tasks (KHÔNG bịa)

5. **Nạp bối cảnh tính năng**: Đọc từ FEATURE_DIR:
   - spec.md: Yêu cầu và phạm vi tính năng
   - plan.md (nếu có): Chi tiết kỹ thuật, phụ thuộc
   - tasks.md (nếu có): Các tác vụ triển khai

   **Chiến lược nạp bối cảnh**:
   - Chỉ nạp những phần cần thiết liên quan tới các vùng trọng tâm đang xét (tránh đổ nguyên file)
   - Ưu tiên tóm tắt các mục dài thành những gạch đầu dòng ngắn gọn về kịch bản/yêu cầu
   - Nạp dần theo nhu cầu: chỉ truy xuất thêm khi phát hiện thiếu sót
   - Nếu tài liệu nguồn lớn, sinh các mục tóm tắt tạm thay vì nhúng nguyên văn

6. **Sinh checklist** - Dùng TEMPLATE_CONTENT làm template cấu trúc và tạo "Unit test cho yêu cầu":
   - Tạo thư mục `FEATURE_DIR/checklists/` nếu chưa có
   - Sinh tên file checklist không trùng lặp:
     - Dùng tên ngắn, mô tả đúng lĩnh vực (ví dụ `ux.md`, `api.md`, `security.md`)
     - Định dạng: `[domain].md`
   - Cách xử lý file:
     - Nếu file CHƯA tồn tại: Tạo file mới và đánh số các mục bắt đầu từ CHK001
     - Nếu file đã tồn tại: Bổ sung mục mới vào file hiện có, đánh số tiếp từ CHK ID cuối cùng (ví dụ nếu mục cuối là CHK015 thì mục mới bắt đầu từ CHK016)
   - Không bao giờ xóa hay thay nội dung checklist hiện có - luôn giữ lại và bổ sung
   - Để mọi mục mới sinh ở trạng thái chưa đánh dấu (`[ ]`); trạng thái checkbox thuộc về người review

   **NGUYÊN TẮC CỐT LÕI - Kiểm tra yêu cầu, không kiểm tra phần triển khai**:
   Mỗi mục checklist PHẢI đánh giá CHÍNH CÁC YÊU CẦU về:
   - **Đầy đủ**: Đã có đủ mọi yêu cầu cần thiết chưa?
   - **Rõ ràng**: Yêu cầu có rõ ràng và cụ thể không?
   - **Nhất quán**: Các yêu cầu có khớp với nhau không?
   - **Đo lường được**: Yêu cầu có kiểm chứng khách quan được không?
   - **Độ phủ**: Đã xử lý mọi kịch bản/trường hợp biên chưa?

   **Cấu trúc nhóm** - Nhóm các mục theo các chiều chất lượng yêu cầu:
   - **Mức độ đầy đủ của yêu cầu** (Đã ghi lại mọi yêu cầu cần thiết chưa?)
   - **Độ rõ ràng của yêu cầu** (Yêu cầu có cụ thể và rõ ràng không?)
   - **Tính nhất quán của yêu cầu** (Các yêu cầu có khớp nhau, không xung đột không?)
   - **Chất lượng tiêu chí chấp nhận** (Tiêu chí thành công có đo lường được không?)
   - **Độ phủ kịch bản** (Đã xử lý mọi luồng/trường hợp chưa?)
   - **Độ phủ trường hợp biên** (Đã định nghĩa các điều kiện biên chưa?)
   - **Yêu cầu phi chức năng** (Hiệu năng, bảo mật, khả năng tiếp cận, v.v. - đã được đặc tả chưa?)
   - **Phụ thuộc & giả định** (Đã được ghi lại và kiểm chứng chưa?)
   - **Mơ hồ & xung đột** (Điều gì cần làm rõ?)

   **CÁCH VIẾT MỤC CHECKLIST - "Unit test cho văn bản yêu cầu"**:

   ❌ **SAI** (Kiểm thử phần triển khai):
   - "Kiểm tra trang chủ hiển thị 3 card tập podcast"
   - "Test trạng thái hover hoạt động trên desktop"
   - "Xác nhận bấm vào logo sẽ về trang chủ"

   ✅ **ĐÚNG** (Kiểm tra chất lượng yêu cầu):
   - "Số lượng và bố cục chính xác của các tập nổi bật đã được đặc tả chưa?" [Đầy đủ]
   - "'Hiển thị nổi bật' đã được định lượng bằng kích thước/vị trí cụ thể chưa?" [Rõ ràng]
   - "Yêu cầu về trạng thái hover có nhất quán giữa mọi phần tử tương tác không?" [Nhất quán]
   - "Đã định nghĩa yêu cầu điều hướng bằng bàn phím cho mọi UI tương tác chưa?" [Độ phủ]
   - "Đã đặc tả hành vi dự phòng khi ảnh logo không tải được chưa?" [Trường hợp biên]
   - "Đã định nghĩa trạng thái đang tải cho dữ liệu tập podcast được tải bất đồng bộ chưa?" [Đầy đủ]
   - "Đặc tả có định nghĩa phân cấp thị giác cho các phần tử UI cạnh tranh nhau không?" [Rõ ràng]

   **CẤU TRÚC MỘT MỤC**:
   Mỗi mục nên theo mẫu sau:
   - Dạng câu hỏi về chất lượng yêu cầu
   - Tập trung vào những gì ĐƯỢC VIẾT (hoặc chưa được viết) trong spec/plan
   - Ghi chiều chất lượng trong ngoặc vuông [Đầy đủ/Rõ ràng/Nhất quán/v.v.]
   - Tham chiếu mục trong đặc tả `[Đặc tả §X.Y]` khi kiểm tra các yêu cầu hiện có
   - Dùng dấu `[Thiếu]` khi kiểm tra các yêu cầu còn thiếu

   **VÍ DỤ THEO TỪNG CHIỀU CHẤT LƯỢNG**:

   Đầy đủ:
   - "Đã định nghĩa yêu cầu xử lý lỗi cho mọi kiểu lỗi của API chưa? [Thiếu]"
   - "Đã đặc tả yêu cầu về khả năng tiếp cận cho mọi phần tử tương tác chưa? [Đầy đủ]"
   - "Đã định nghĩa yêu cầu về breakpoint mobile cho bố cục responsive chưa? [Thiếu]"

   Rõ ràng:
   - "'Tải nhanh' đã được định lượng bằng ngưỡng thời gian cụ thể chưa? [Rõ ràng, Đặc tả §NFR-2]"
   - "Tiêu chí chọn 'các tập liên quan' đã được định nghĩa rõ chưa? [Rõ ràng, Đặc tả §FR-5]"
   - "'Nổi bật' đã được định nghĩa bằng các thuộc tính thị giác đo lường được chưa? [Mơ hồ, Đặc tả §FR-4]"

   Nhất quán:
   - "Yêu cầu điều hướng có thống nhất giữa mọi trang không? [Nhất quán, Đặc tả §FR-10]"
   - "Yêu cầu về component card có nhất quán giữa trang chủ và trang chi tiết không? [Nhất quán]"

   Độ phủ:
   - "Đã định nghĩa yêu cầu cho kịch bản trạng thái rỗng (không có tập nào) chưa? [Độ phủ, Trường hợp biên]"
   - "Đã xử lý các kịch bản người dùng tương tác đồng thời chưa? [Độ phủ, Thiếu]"
   - "Đã đặc tả yêu cầu cho tình huống tải dữ liệu lỗi một phần chưa? [Độ phủ, Luồng ngoại lệ]"

   Đo lường được:
   - "Yêu cầu về phân cấp thị giác có đo lường/kiểm thử được không? [Tiêu chí chấp nhận, Đặc tả §FR-1]"
   - "'Trọng lượng thị giác cân bằng' có kiểm chứng khách quan được không? [Đo lường được, Đặc tả §FR-2]"

   **Phân loại kịch bản & độ phủ** (Trọng tâm: chất lượng yêu cầu):
   - Kiểm tra đã có yêu cầu cho: kịch bản Chính, Thay thế, Ngoại lệ/Lỗi, Phục hồi, Phi chức năng chưa
   - Với mỗi nhóm kịch bản, hỏi: "Yêu cầu cho [loại kịch bản] đã đầy đủ, rõ ràng và nhất quán chưa?"
   - Nếu thiếu một nhóm kịch bản: "Yêu cầu cho [loại kịch bản] được cố ý loại trừ hay đang bị thiếu? [Thiếu]"
   - Bao gồm khả năng chống chịu/rollback khi có thay đổi trạng thái: "Đã định nghĩa yêu cầu rollback khi migration thất bại chưa? [Thiếu]"

   **Yêu cầu về truy vết**:
   - TỐI THIỂU: ≥80% số mục PHẢI có ít nhất một tham chiếu truy vết
   - Mỗi mục nên tham chiếu: mục trong đặc tả `[Đặc tả §X.Y]`, hoặc dùng các dấu: `[Thiếu]`, `[Mơ hồ]`, `[Xung đột]`, `[Giả định]`
   - Nếu chưa có hệ thống ID: "Đã thiết lập cách đánh ID cho yêu cầu & tiêu chí chấp nhận chưa? [Truy vết]"

   **Nêu ra & giải quyết vấn đề** (Vấn đề về chất lượng yêu cầu):
   Đặt câu hỏi về chính các yêu cầu:
   - Mơ hồ: "Thuật ngữ 'nhanh' đã được định lượng bằng chỉ số cụ thể chưa? [Mơ hồ, Đặc tả §NFR-1]"
   - Xung đột: "Yêu cầu điều hướng ở §FR-10 và §FR-10a có xung đột nhau không? [Xung đột]"
   - Giả định: "Giả định 'API podcast luôn sẵn sàng' đã được kiểm chứng chưa? [Giả định]"
   - Phụ thuộc: "Yêu cầu đối với API podcast bên ngoài đã được ghi lại chưa? [Phụ thuộc, Thiếu]"
   - Thiếu định nghĩa: "'Phân cấp thị giác' đã được định nghĩa bằng tiêu chí đo lường được chưa? [Thiếu]"

   **Gom gọn nội dung**:
   - Giới hạn mềm: Nếu số mục ứng viên thô > 40, xếp ưu tiên theo rủi ro/mức ảnh hưởng
   - Gộp các mục gần trùng nhau cùng kiểm tra một khía cạnh của yêu cầu
   - Nếu có >5 trường hợp biên ít ảnh hưởng, tạo một mục: "Yêu cầu đã xử lý các trường hợp biên X, Y, Z chưa? [Độ phủ]"

   **🚫 TUYỆT ĐỐI CẤM** - Những điều này biến checklist thành test cho phần triển khai, không phải test cho yêu cầu:
   - ❌ Mọi mục bắt đầu bằng "Kiểm tra", "Test", "Xác nhận", "Kiểm chứng" + hành vi của phần triển khai
   - ❌ Tham chiếu tới việc thực thi code, thao tác của người dùng, hành vi của hệ thống
   - ❌ "Hiển thị đúng", "hoạt động bình thường", "chạy như mong đợi"
   - ❌ "Bấm", "điều hướng", "render", "tải", "thực thi"
   - ❌ Test case, kế hoạch kiểm thử, quy trình QA
   - ❌ Chi tiết triển khai (framework, API, thuật toán)

   **✅ MẪU BẮT BUỘC** - Những mẫu này kiểm tra chất lượng yêu cầu:
   - ✅ "[Loại yêu cầu] đã được định nghĩa/đặc tả/ghi lại cho [kịch bản] chưa?"
   - ✅ "[Thuật ngữ mơ hồ] đã được định lượng/làm rõ bằng tiêu chí cụ thể chưa?"
   - ✅ "Yêu cầu giữa [mục A] và [mục B] có nhất quán không?"
   - ✅ "[Yêu cầu] có đo lường/kiểm chứng khách quan được không?"
   - ✅ "[Các trường hợp biên/kịch bản] đã được xử lý trong yêu cầu chưa?"
   - ✅ "Đặc tả có định nghĩa [khía cạnh còn thiếu] không?"

7. **Tham chiếu cấu trúc**: Sinh checklist theo template chuẩn trong `templates/checklist-template.md` cho tiêu đề, phần metadata, heading các nhóm, ghi chú về quyền sở hữu, phần ghi chú và định dạng ID. Nếu không có template, dùng: tiêu đề H1, các dòng metadata mục đích/ngày tạo, một ghi chú quyền sở hữu giải thích rằng `[x]` nghĩa là người review phê duyệt chất lượng yêu cầu, các mục nhóm `##` chứa các dòng `- [ ] CHK### <requirement item>` với ID tăng dần trên toàn file bắt đầu từ CHK001, và ghi chú rằng `__SPECKIT_COMMAND_IMPLEMENT__` đọc trạng thái checklist nhưng không sửa các dấu đánh dấu.

8. **Báo cáo**: Xuất đường dẫn đầy đủ tới file checklist, số lượng mục, và tóm tắt lần chạy này tạo file mới hay bổ sung vào file có sẵn. Tóm tắt:
   - Các vùng trọng tâm đã chọn
   - Mức độ sâu
   - Đối tượng/thời điểm sử dụng
   - Mọi mục bắt buộc phải có mà người dùng nêu rõ và đã được đưa vào

**Quan trọng**: Mỗi lần gọi lệnh `__SPECKIT_COMMAND_CHECKLIST__` dùng một tên file checklist ngắn, mang tính mô tả, và hoặc tạo file mới hoặc bổ sung vào file có sẵn. Điều này cho phép:

- Có nhiều checklist thuộc các loại khác nhau (ví dụ `ux.md`, `test.md`, `security.md`)
- Tên file đơn giản, dễ nhớ, thể hiện mục đích của checklist
- Dễ nhận biết và tìm kiếm trong thư mục `checklists/`

Để tránh lộn xộn, hãy dùng tên loại mang tính mô tả và dọn các checklist lỗi thời khi đã xong.

## Ví dụ về các loại checklist & mục mẫu

**Chất lượng yêu cầu UX:** `ux.md`

Mục mẫu (kiểm tra yêu cầu, KHÔNG kiểm tra phần triển khai):

- "Yêu cầu về phân cấp thị giác đã được định nghĩa bằng tiêu chí đo lường được chưa? [Rõ ràng, Đặc tả §FR-1]"
- "Số lượng và vị trí các phần tử UI đã được đặc tả rõ chưa? [Đầy đủ, Đặc tả §FR-1]"
- "Yêu cầu về trạng thái tương tác (hover, focus, active) có được định nghĩa nhất quán không? [Nhất quán]"
- "Đã đặc tả yêu cầu về khả năng tiếp cận cho mọi phần tử tương tác chưa? [Độ phủ, Thiếu]"
- "Đã định nghĩa hành vi dự phòng khi ảnh không tải được chưa? [Trường hợp biên, Thiếu]"
- "'Hiển thị nổi bật' có đo lường khách quan được không? [Đo lường được, Đặc tả §FR-4]"

**Chất lượng yêu cầu API:** `api.md`

Mục mẫu:

- "Đã đặc tả định dạng phản hồi lỗi cho mọi kịch bản lỗi chưa? [Đầy đủ]"
- "Yêu cầu giới hạn tần suất đã được định lượng bằng ngưỡng cụ thể chưa? [Rõ ràng]"
- "Yêu cầu xác thực có nhất quán trên mọi endpoint không? [Nhất quán]"
- "Đã định nghĩa yêu cầu retry/timeout cho các phụ thuộc bên ngoài chưa? [Độ phủ, Thiếu]"
- "Chiến lược quản lý phiên bản đã được ghi lại trong yêu cầu chưa? [Thiếu]"

**Chất lượng yêu cầu hiệu năng:** `performance.md`

Mục mẫu:

- "Yêu cầu hiệu năng đã được định lượng bằng chỉ số cụ thể chưa? [Rõ ràng]"
- "Đã định nghĩa mục tiêu hiệu năng cho mọi hành trình người dùng quan trọng chưa? [Độ phủ]"
- "Đã đặc tả yêu cầu hiệu năng dưới các mức tải khác nhau chưa? [Đầy đủ]"
- "Yêu cầu hiệu năng có đo lường khách quan được không? [Đo lường được]"
- "Đã định nghĩa yêu cầu về suy giảm dịch vụ cho kịch bản tải cao chưa? [Trường hợp biên, Thiếu]"

**Chất lượng yêu cầu bảo mật:** `security.md`

Mục mẫu:

- "Đã đặc tả yêu cầu xác thực cho mọi tài nguyên được bảo vệ chưa? [Độ phủ]"
- "Đã định nghĩa yêu cầu bảo vệ dữ liệu cho thông tin nhạy cảm chưa? [Đầy đủ]"
- "Mô hình mối đe dọa đã được ghi lại và các yêu cầu có bám theo nó không? [Truy vết]"
- "Yêu cầu bảo mật có nhất quán với các nghĩa vụ tuân thủ không? [Nhất quán]"
- "Đã định nghĩa yêu cầu phản ứng khi có sự cố/xâm phạm bảo mật chưa? [Thiếu, Luồng ngoại lệ]"

## Phản ví dụ: những điều KHÔNG nên làm

**❌ SAI - Những mục này kiểm thử phần triển khai, không phải yêu cầu:**

```markdown
- [ ] CHK001 - Kiểm tra trang chủ hiển thị 3 card tập podcast [Đặc tả §FR-001]
- [ ] CHK002 - Test trạng thái hover hoạt động đúng trên desktop [Đặc tả §FR-003]
- [ ] CHK003 - Xác nhận bấm logo sẽ chuyển về trang chủ [Đặc tả §FR-010]
- [ ] CHK004 - Kiểm tra mục tập liên quan hiển thị 3-5 mục [Đặc tả §FR-005]
```

**✅ ĐÚNG - Những mục này kiểm tra chất lượng yêu cầu:**

```markdown
- [ ] CHK001 - Số lượng và bố cục của các tập nổi bật đã được đặc tả rõ chưa? [Đầy đủ, Đặc tả §FR-001]
- [ ] CHK002 - Yêu cầu về trạng thái hover có được định nghĩa nhất quán cho mọi phần tử tương tác không? [Nhất quán, Đặc tả §FR-003]
- [ ] CHK003 - Yêu cầu điều hướng có rõ ràng cho mọi phần tử thương hiệu bấm được không? [Rõ ràng, Đặc tả §FR-010]
- [ ] CHK004 - Tiêu chí chọn các tập liên quan đã được ghi lại chưa? [Thiếu, Đặc tả §FR-005]
- [ ] CHK005 - Đã định nghĩa yêu cầu trạng thái đang tải cho dữ liệu tập podcast tải bất đồng bộ chưa? [Thiếu]
- [ ] CHK006 - Yêu cầu về "phân cấp thị giác" có đo lường khách quan được không? [Đo lường được, Đặc tả §FR-001]
```

**Khác biệt chính:**

- Sai: Kiểm thử xem hệ thống có chạy đúng không
- Đúng: Kiểm tra xem yêu cầu có được viết đúng không
- Sai: Kiểm chứng hành vi
- Đúng: Thẩm định chất lượng yêu cầu
- Sai: "Nó có làm X không?"
- Đúng: "X đã được đặc tả rõ chưa?"

## Kiểm tra sau khi thực thi

**Kiểm tra hook của extension (sau khi sinh checklist)**:
Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_checklist`
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
