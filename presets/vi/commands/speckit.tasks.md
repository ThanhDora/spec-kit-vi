---
description: Sinh tasks.md cho tính năng, gồm các tác vụ cụ thể, thực hiện được và sắp xếp theo phụ thuộc, dựa trên các artifact thiết kế hiện có.
handoffs:
  - label: Phân tích tính nhất quán
    agent: speckit.analyze
    prompt: Chạy phân tích tính nhất quán cho dự án
    send: true
  - label: Triển khai dự án
    agent: speckit.implement
    prompt: Bắt đầu triển khai theo từng giai đoạn
    send: true
scripts:
  sh: scripts/bash/setup-tasks.sh --json
  ps: scripts/powershell/setup-tasks.ps1 -Json
  py: scripts/python/setup_tasks.py --json
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi sinh tác vụ)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_tasks`
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

    Chờ kết quả của lệnh hook trước khi chuyển sang phần Các bước thực hiện.
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua

## Các bước thực hiện

1. **Thiết lập**: Chạy `{SCRIPT}` từ thư mục gốc repo và parse FEATURE_DIR, TASKS_TEMPLATE_CONTENT, TASKS_TEMPLATE cùng danh sách AVAILABLE_DOCS. Khi được cung cấp, `FEATURE_DIR` và `TASKS_TEMPLATE` phải là đường dẫn tuyệt đối. `AVAILABLE_DOCS` là danh sách tên tài liệu/đường dẫn tương đối có trong `FEATURE_DIR` (ví dụ `research.md` hoặc `contracts/`). Với dấu nháy đơn trong đối số như "I'm Groot", dùng cú pháp escape: ví dụ 'I'\''m Groot' (hoặc dùng nháy kép nếu được: "I'm Groot").

2. **Nạp tài liệu thiết kế**: Đọc từ FEATURE_DIR:
   - **Bắt buộc**: plan.md (tech stack, thư viện, cấu trúc), spec.md (các user story kèm độ ưu tiên)
   - **Tùy chọn**: data-model.md (thực thể), contracts/ (contract giao diện), research.md (các quyết định), quickstart.md (kịch bản kiểm thử)
   - **NẾU CÓ**: Nạp `/memory/constitution.md` để lấy các nguyên tắc dự án và ràng buộc quản trị
   - Lưu ý: Không phải dự án nào cũng có đủ mọi tài liệu. Hãy sinh tác vụ dựa trên những gì đang có.

3. **Thực thi workflow sinh tác vụ**:
   - Nạp plan.md và rút ra tech stack, thư viện, cấu trúc dự án
   - Nạp spec.md và rút ra các user story kèm độ ưu tiên (P1, P2, P3, v.v.)
   - Nếu có data-model.md: Rút ra các thực thể và ánh xạ vào user story
   - Nếu có contracts/: Ánh xạ các contract giao diện vào user story
   - Nếu có research.md: Rút ra các quyết định để làm tác vụ thiết lập
   - Sinh tác vụ được tổ chức theo user story (xem Quy tắc sinh tác vụ bên dưới)
   - Sinh đồ thị phụ thuộc thể hiện thứ tự hoàn tất các user story
   - Tạo ví dụ thực thi song song cho từng user story
   - Kiểm tra tính đầy đủ của tác vụ (mỗi user story có đủ tác vụ cần thiết và kiểm thử độc lập được)

4. **Sinh tasks.md**: Dùng TASKS_TEMPLATE_CONTENT (từ đầu ra JSON ở trên) làm cấu trúc. Để tương thích với các script thiết lập cũ không trả về TASKS_TEMPLATE_CONTENT, hãy đọc TASKS_TEMPLATE thay thế. Điền vào:
   - Tên tính năng chính xác lấy từ plan.md
   - Giai đoạn 1: Tác vụ thiết lập (khởi tạo dự án)
   - Giai đoạn 2: Tác vụ nền tảng (điều kiện tiên quyết chặn mọi user story)
   - Giai đoạn 3 trở đi: Mỗi user story một giai đoạn (theo thứ tự ưu tiên trong spec.md)
   - Mỗi giai đoạn gồm: mục tiêu của story, tiêu chí kiểm thử độc lập, test (nếu có yêu cầu), các tác vụ triển khai
   - Giai đoạn cuối: Hoàn thiện & các vấn đề xuyên suốt
   - Mọi tác vụ phải tuân thủ nghiêm ngặt định dạng checklist (xem Quy tắc sinh tác vụ bên dưới)
   - Đường dẫn file rõ ràng cho từng tác vụ
   - Mục phụ thuộc thể hiện thứ tự hoàn tất các story
   - Ví dụ thực thi song song cho từng story
   - Mục chiến lược triển khai (MVP trước, bàn giao tăng dần)

## Hook bắt buộc sau khi thực thi

**Bạn PHẢI hoàn thành mục này trước khi báo hoàn tất cho người dùng.**

Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu không tồn tại, hoặc không có hook nào đăng ký dưới `hooks.after_tasks`, chuyển thẳng tới phần Báo cáo hoàn tất.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_tasks`.
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi chuyển tới phần Báo cáo hoàn tất.
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook bắt buộc** (`optional: false`) — **Bạn PHẢI xuất `EXECUTE_COMMAND:` cho mỗi hook bắt buộc**:
    ```
    ## Hook của extension

    **Hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
  - **Hook tùy chọn** (`optional: true`):
    ```
    ## Hook của extension

    **Hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```

## Báo cáo hoàn tất

Xuất đường dẫn tới tasks.md đã sinh và bản tóm tắt:
- Tổng số tác vụ
- Số tác vụ cho mỗi user story
- Các cơ hội làm song song đã xác định
- Tiêu chí kiểm thử độc lập cho từng story
- Phạm vi MVP đề xuất (thường chỉ gồm user story 1)
- Kiểm tra định dạng: Xác nhận TẤT CẢ tác vụ đều đúng định dạng checklist (checkbox, ID, nhãn, đường dẫn file)

Bối cảnh để sinh tác vụ: {ARGS}

tasks.md phải thực thi được ngay: mỗi tác vụ phải đủ cụ thể để một LLM hoàn thành mà không cần thêm bối cảnh.

## Quy tắc sinh tác vụ

**QUAN TRỌNG**: Tác vụ PHẢI được tổ chức theo user story để có thể triển khai và kiểm thử độc lập.

**Test là TÙY CHỌN**: Chỉ sinh tác vụ kiểm thử khi đặc tả tính năng yêu cầu rõ ràng hoặc khi người dùng yêu cầu làm theo TDD.

### Định dạng checklist (BẮT BUỘC)

Mọi tác vụ PHẢI tuân thủ nghiêm ngặt định dạng sau:

```text
- [ ] [TaskID] [P?] [Story?] Mô tả kèm đường dẫn file
```

**Các thành phần của định dạng**:

1. **Checkbox**: LUÔN bắt đầu bằng `- [ ]` (checkbox markdown)
2. **Task ID**: Số thứ tự tăng dần (T001, T002, T003...) theo thứ tự thực hiện
3. **Dấu [P]**: CHỈ thêm khi tác vụ chạy song song được (khác file, không phụ thuộc tác vụ chưa xong)
4. **Nhãn [Story]**: BẮT BUỘC, nhưng chỉ cho tác vụ thuộc giai đoạn user story
   - Định dạng: [US1], [US2], [US3], v.v. (ánh xạ tới user story trong spec.md)
   - Giai đoạn Thiết lập: KHÔNG có nhãn story
   - Giai đoạn Nền tảng: KHÔNG có nhãn story
   - Các giai đoạn user story: PHẢI có nhãn story
   - Giai đoạn Hoàn thiện: KHÔNG có nhãn story
5. **Mô tả**: Hành động rõ ràng kèm đường dẫn file chính xác

**Ví dụ**:

- ✅ ĐÚNG: `- [ ] T001 Create project structure per implementation plan`
- ✅ ĐÚNG: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ ĐÚNG: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ ĐÚNG: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ SAI: `- [ ] Create User model` (thiếu ID và nhãn Story)
- ❌ SAI: `T001 [US1] Create model` (thiếu checkbox)
- ❌ SAI: `- [ ] [US1] Create User model` (thiếu Task ID)
- ❌ SAI: `- [ ] T001 [US1] Create model` (thiếu đường dẫn file)

Lưu ý: các ví dụ trên giữ nguyên tiếng Anh để minh họa định dạng; khi sinh tasks.md, hãy viết phần mô tả bằng tiếng Việt (ví dụ: "Tạo model User trong src/models/user.py").

### Tổ chức tác vụ

1. **Từ user story (spec.md)** - CÁCH TỔ CHỨC CHÍNH:
   - Mỗi user story (P1, P2, P3...) có một giai đoạn riêng
   - Ánh xạ mọi thành phần liên quan vào story tương ứng:
     - Các model cần cho story đó
     - Các service cần cho story đó
     - Giao diện/UI cần cho story đó
     - Nếu có yêu cầu test: Các test riêng cho story đó
   - Đánh dấu phụ thuộc giữa các story (đa số story nên độc lập)

2. **Từ contract**:
   - Ánh xạ mỗi contract giao diện → vào user story mà nó phục vụ
   - Nếu có yêu cầu test: Mỗi contract giao diện → một tác vụ contract test [P] đặt trước phần triển khai trong giai đoạn của story đó

3. **Từ mô hình dữ liệu**:
   - Ánh xạ mỗi thực thể vào (các) user story cần nó
   - Nếu thực thể phục vụ nhiều story: Đặt vào story sớm nhất hoặc giai đoạn Thiết lập
   - Quan hệ → tác vụ ở tầng service trong giai đoạn story phù hợp
   - Với mỗi trường có ràng buộc trong data-model.md (độ dài tối đa, nullable/bắt buộc, giá trị enum, quy tắc kiểm tra), hãy trích nguyên văn ràng buộc đó vào mô tả tác vụ để không phụ thuộc vào sự tùy ý lúc triển khai

4. **Từ thiết lập/hạ tầng**:
   - Hạ tầng dùng chung → giai đoạn Thiết lập (Giai đoạn 1)
   - Tác vụ nền tảng/chặn các phần khác → giai đoạn Nền tảng (Giai đoạn 2)
   - Thiết lập riêng cho một story → nằm trong giai đoạn của story đó

### Cấu trúc giai đoạn

- **Giai đoạn 1**: Thiết lập (khởi tạo dự án)
- **Giai đoạn 2**: Nền tảng (điều kiện tiên quyết chặn các phần khác - PHẢI xong trước các user story)
- **Giai đoạn 3 trở đi**: Các user story theo thứ tự ưu tiên (P1, P2, P3...)
  - Trong mỗi story: Test (nếu có yêu cầu) → Model → Service → Endpoint → Tích hợp
  - Mỗi giai đoạn phải là một phần tăng trưởng hoàn chỉnh, kiểm thử độc lập được
- **Giai đoạn cuối**: Hoàn thiện & Các vấn đề xuyên suốt

## Hoàn tất khi

- [ ] Đã sinh tasks.md với đủ các giai đoạn, Task ID và đường dẫn file
- [ ] Đã gọi hoặc bỏ qua các hook của extension theo đúng quy tắc trong mục Hook bắt buộc sau khi thực thi ở trên
- [ ] Đã báo hoàn tất cho người dùng, kèm số lượng tác vụ, phân bổ theo story và phạm vi MVP
