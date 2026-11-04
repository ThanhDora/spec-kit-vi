---
description: Chạy workflow lập kế hoạch triển khai bằng template kế hoạch để sinh các artifact thiết kế.
handoffs:
  - label: Tạo danh sách tác vụ
    agent: speckit.tasks
    prompt: Chia kế hoạch thành các tác vụ
    send: true
  - label: Tạo checklist
    agent: speckit.checklist
    prompt: Tạo checklist cho lĩnh vực sau...
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
  py: scripts/python/setup_plan.py --json
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi lập kế hoạch)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_plan`
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

1. **Thiết lập**: Chạy `{SCRIPT}` từ thư mục gốc repo và parse JSON để lấy FEATURE_SPEC, IMPL_PLAN, FEATURE_DIR, BRANCH. Với dấu nháy đơn trong đối số như "I'm Groot", dùng cú pháp escape: ví dụ 'I'\''m Groot' (hoặc dùng nháy kép nếu được: "I'm Groot").

2. **Nạp bối cảnh**: Đọc FEATURE_SPEC và `/memory/constitution.md`. Nạp template IMPL_PLAN (đã được sao chép sẵn).

3. **Thực thi workflow lập kế hoạch**: Làm theo cấu trúc trong template IMPL_PLAN để:
   - Điền mục Bối cảnh kỹ thuật (đánh dấu những điểm chưa biết là "NEEDS CLARIFICATION")
   - Điền mục Kiểm tra hiến chương dựa trên hiến chương
   - Đánh giá các cổng kiểm soát (báo LỖI nếu có vi phạm không được giải trình)
   - Giai đoạn 0: Sinh research.md (giải quyết mọi NEEDS CLARIFICATION)
   - Giai đoạn 1: Sinh data-model.md, contracts/, quickstart.md
   - Đánh giá lại mục Kiểm tra hiến chương sau khi thiết kế

## Hook bắt buộc sau khi thực thi

**Bạn PHẢI hoàn thành mục này trước khi báo hoàn tất cho người dùng.**

Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu không tồn tại, hoặc không có hook nào đăng ký dưới `hooks.after_plan`, chuyển thẳng tới phần Báo cáo hoàn tất.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_plan`.
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

Lệnh kết thúc sau phần thiết kế ở Giai đoạn 1. Báo cáo branch, đường dẫn IMPL_PLAN và các artifact đã sinh.

## Các giai đoạn

### Giai đoạn 0: Phác thảo & Nghiên cứu

1. **Rút ra những điểm chưa biết từ mục Bối cảnh kỹ thuật** ở trên:
   - Mỗi NEEDS CLARIFICATION → một tác vụ nghiên cứu
   - Mỗi thư viện phụ thuộc → một tác vụ tìm best practice
   - Mỗi tích hợp → một tác vụ tìm pattern

2. **Sinh và giao việc cho các agent nghiên cứu**:

   ```text
   Với mỗi điểm chưa biết trong Bối cảnh kỹ thuật:
     Task: "Nghiên cứu {unknown} cho {feature context}"
   Với mỗi lựa chọn công nghệ:
     Task: "Tìm best practice cho {tech} trong {domain}"
   ```

3. **Tổng hợp kết quả** vào `research.md` theo định dạng:
   - Quyết định: [đã chọn gì]
   - Lý do: [vì sao chọn]
   - Các phương án đã cân nhắc: [đã đánh giá những gì khác]

**Đầu ra**: research.md với mọi NEEDS CLARIFICATION đã được giải quyết

### Giai đoạn 1: Thiết kế & Contract

**Điều kiện tiên quyết:** `research.md` đã hoàn tất

1. **Rút các thực thể từ đặc tả tính năng** → `data-model.md`:
   - Tên thực thể, các trường, quan hệ
   - Quy tắc kiểm tra dữ liệu rút ra từ yêu cầu
   - Chuyển trạng thái nếu có

2. **Định nghĩa contract giao diện** (nếu dự án có giao diện ra bên ngoài) → `/contracts/`:
   - Xác định dự án cung cấp những giao diện nào cho người dùng hoặc hệ thống khác
   - Ghi lại contract theo định dạng phù hợp với loại dự án
   - Ví dụ: API công khai cho thư viện, schema lệnh cho công cụ CLI, endpoint cho dịch vụ web, ngữ pháp cho parser, UI contract cho ứng dụng
   - Bỏ qua nếu dự án hoàn toàn nội bộ (script build, công cụ dùng một lần, v.v.)

3. **Tạo hướng dẫn kiểm chứng quickstart** → `quickstart.md`:
   - Ghi lại các kịch bản kiểm chứng chạy được, chứng minh tính năng hoạt động từ đầu tới cuối
   - Bao gồm điều kiện tiên quyết, lệnh thiết lập, lệnh test/chạy và kết quả mong đợi
   - Dùng link hoặc tham chiếu tới contract và chi tiết mô hình dữ liệu thay vì chép lại
   - Không đưa vào code triển khai đầy đủ, phần thân model/service/controller, migration hay bộ test hoàn chỉnh
   - Giữ artifact này ở vai trò hướng dẫn kiểm chứng/chạy; chi tiết triển khai thuộc về `tasks.md` và giai đoạn triển khai

**Đầu ra**: data-model.md, /contracts/*, quickstart.md

## Quy tắc chính

- Dùng đường dẫn tuyệt đối cho thao tác với filesystem; dùng đường dẫn tương đối theo dự án khi tham chiếu trong tài liệu
- Báo LỖI khi không qua cổng kiểm soát hoặc còn điểm cần làm rõ chưa giải quyết

## Hoàn tất khi

- [ ] Đã chạy workflow lập kế hoạch và sinh các artifact thiết kế
- [ ] Đã gọi hoặc bỏ qua các hook của extension theo đúng quy tắc trong mục Hook bắt buộc sau khi thực thi ở trên
- [ ] Đã báo hoàn tất cho người dùng, kèm branch, đường dẫn kế hoạch và các artifact đã sinh
