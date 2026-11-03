---
description: Thực thi kế hoạch triển khai bằng cách xử lý và thực hiện mọi tác vụ được định nghĩa trong tasks.md
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
  py: scripts/python/check_prerequisites.py --json --require-tasks --include-tasks
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi triển khai)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_implement`
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

1. Chạy `{SCRIPT}` từ thư mục gốc repo và parse FEATURE_DIR cùng danh sách AVAILABLE_DOCS. Mọi đường dẫn phải là đường dẫn tuyệt đối. Với dấu nháy đơn trong đối số như "I'm Groot", dùng cú pháp escape: ví dụ 'I'\''m Groot' (hoặc dùng nháy kép nếu được: "I'm Groot").

2. **Kiểm tra trạng thái checklist** (nếu có FEATURE_DIR/checklists/):
   - Coi các dấu đánh dấu checklist là một cổng kiểm soát chỉ đọc: quét trạng thái checkbox, báo cáo trạng thái và hỏi trước khi tiếp tục khi cần; KHÔNG sửa file checklist hay các dấu đánh dấu
   - `checklists/requirements.md` là checklist chất lượng đặc tả có sẵn, do `__SPECKIT_COMMAND_SPECIFY__` và `__SPECKIT_COMMAND_CLARIFY__` quản lý; các checklist tùy chỉnh do `__SPECKIT_COMMAND_CHECKLIST__` sinh ra là artifact review chất lượng yêu cầu, thuộc về người review
   - Với checklist tùy chỉnh, `[x]` nghĩa là người review đã xác định tiêu chí chất lượng yêu cầu được đáp ứng; nó KHÔNG có nghĩa là phần việc triển khai đã xong
   - Quét mọi file checklist trong thư mục checklists/
   - Với mỗi checklist, đếm:
     - Tổng số mục: Mọi dòng khớp `- [ ]` hoặc `- [X]` hoặc `- [x]`
     - Số mục đã đánh dấu: Các dòng khớp `- [X]` hoặc `- [x]`
     - Số mục chưa đánh dấu: Các dòng khớp `- [ ]`
   - Tạo bảng trạng thái:

     ```text
     | Checklist | Tổng | Đã đánh dấu | Chưa đánh dấu | Trạng thái |
     |-----------|------|-------------|---------------|------------|
     | ux.md     | 12   | 12          | 0             | ✓ ĐẠT      |
     | test.md   | 8    | 5           | 3             | ✗ CHƯA ĐẠT |
     | security.md | 6  | 6           | 0             | ✓ ĐẠT      |
     ```

   - Tính trạng thái tổng thể:
     - **ĐẠT**: Mọi checklist đều không còn mục chưa đánh dấu
     - **CHƯA ĐẠT**: Có ít nhất một checklist còn mục chưa đánh dấu

   - **Nếu có checklist còn mục chưa đánh dấu**:
     - Hiển thị bảng kèm số mục chưa đánh dấu
     - **DỪNG LẠI** và hỏi: "Một số checklist vẫn còn mục chưa được đánh dấu. Bạn vẫn muốn tiếp tục triển khai chứ? (có/không)"
     - Chờ người dùng trả lời rồi mới tiếp tục
     - Nếu người dùng trả lời "không", "chờ" hoặc "dừng" (hoặc "no", "wait", "stop"), dừng thực thi
     - Nếu người dùng trả lời "có", "tiếp tục" hoặc "làm tiếp" (hoặc "yes", "proceed", "continue"), chuyển sang bước 3

   - **Nếu mọi checklist đều đã đánh dấu đủ**:
     - Hiển thị bảng cho thấy mọi checklist đều đạt
     - Tự động chuyển sang bước 3

3. Nạp và phân tích bối cảnh triển khai:
   - **BẮT BUỘC**: Đọc tasks.md để lấy danh sách tác vụ đầy đủ và kế hoạch thực thi
   - **BẮT BUỘC**: Đọc plan.md để lấy tech stack, kiến trúc và cấu trúc file
   - **NẾU CÓ**: Đọc data-model.md để lấy các thực thể và quan hệ
   - **NẾU CÓ**: Đọc contracts/ để lấy đặc tả API và yêu cầu kiểm thử
   - **NẾU CÓ**: Đọc research.md để lấy các quyết định và ràng buộc kỹ thuật
   - **NẾU CÓ**: Đọc /memory/constitution.md để lấy các ràng buộc quản trị
   - **NẾU CÓ**: Đọc quickstart.md để lấy các kịch bản tích hợp

4. **Kiểm tra thiết lập dự án**:
   - **BẮT BUỘC**: Tạo/kiểm tra các file ignore dựa trên thiết lập thực tế của dự án:

   **Logic phát hiện & tạo file**:
   - Kiểm tra lệnh sau có chạy thành công không để xác định repository có phải git repo không (nếu đúng thì tạo/kiểm tra .gitignore):

     ```sh
     git rev-parse --git-dir 2>/dev/null
     ```

   - Kiểm tra có Dockerfile* hoặc plan.md có nhắc tới Docker không → tạo/kiểm tra .dockerignore
   - Kiểm tra có .eslintrc* không → tạo/kiểm tra .eslintignore
   - Kiểm tra có eslint.config.* không → đảm bảo các mục `ignores` của file cấu hình bao phủ các pattern cần thiết
   - Kiểm tra có .prettierrc* không → tạo/kiểm tra .prettierignore
   - Kiểm tra có .npmrc hoặc package.json không → tạo/kiểm tra .npmignore (nếu có publish)
   - Kiểm tra có file terraform (*.tf) không → tạo/kiểm tra .terraformignore
   - Kiểm tra có cần .helmignore không (có helm chart) → tạo/kiểm tra .helmignore

   **Nếu file ignore đã tồn tại**: Kiểm tra xem nó có các pattern thiết yếu chưa, chỉ bổ sung các pattern quan trọng còn thiếu
   **Nếu chưa có file ignore**: Tạo mới với bộ pattern đầy đủ cho công nghệ đã phát hiện

   **Pattern phổ biến theo công nghệ** (dựa trên tech stack trong plan.md):
   - **Node.js/JavaScript/TypeScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
   - **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
   - **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
   - **C#/.NET**: `bin/`, `obj/`, `*.user`, `*.suo`, `packages/`
   - **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
   - **Ruby**: `.bundle/`, `log/`, `tmp/`, `*.gem`, `vendor/bundle/`
   - **PHP**: `vendor/`, `*.log`, `*.cache`, `*.env`
   - **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`, `*.rlib`, `*.prof*`, `.idea/`, `*.log`, `.env*`
   - **Kotlin**: `build/`, `out/`, `.gradle/`, `.idea/`, `*.class`, `*.jar`, `*.iml`, `*.log`, `.env*`
   - **C++**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.so`, `*.a`, `*.exe`, `*.dll`, `.idea/`, `*.log`, `.env*`
   - **C**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.a`, `*.so`, `*.exe`, `*.dll`, `autom4te.cache/`, `config.status`, `config.log`, `.idea/`, `*.log`, `.env*`
   - **Swift**: `.build/`, `DerivedData/`, `*.swiftpm/`, `Packages/`
   - **R**: `.Rproj.user/`, `.Rhistory`, `.RData`, `.Ruserdata`, `*.Rproj`, `packrat/`, `renv/`
   - **Dùng chung**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `.vscode/`, `.idea/`

   **Pattern theo công cụ**:
   - **Docker**: `node_modules/`, `.git/`, `Dockerfile*`, `.dockerignore`, `*.log*`, `.env*`, `coverage/`
   - **ESLint**: `node_modules/`, `dist/`, `build/`, `coverage/`, `*.min.js`
   - **Prettier**: `node_modules/`, `dist/`, `build/`, `coverage/`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - **Terraform**: `.terraform/`, `*.tfstate*`, `*.tfvars`, `.terraform.lock.hcl`
   - **Kubernetes/k8s**: `*.secret.yaml`, `secrets/`, `.kube/`, `kubeconfig*`, `*.key`, `*.crt`

5. Parse cấu trúc tasks.md và rút ra:
   - **Các giai đoạn tác vụ**: Thiết lập, Kiểm thử, Lõi, Tích hợp, Hoàn thiện
   - **Phụ thuộc giữa tác vụ**: Quy tắc thực thi tuần tự hay song song
   - **Chi tiết tác vụ**: ID, mô tả, đường dẫn file, dấu song song [P]
   - **Luồng thực thi**: Thứ tự và các yêu cầu về phụ thuộc

6. Thực hiện triển khai theo kế hoạch tác vụ:
   - **Thực thi theo từng giai đoạn**: Hoàn tất mỗi giai đoạn rồi mới chuyển sang giai đoạn tiếp theo
   - **Tôn trọng phụ thuộc**: Chạy tác vụ tuần tự theo đúng thứ tự, các tác vụ song song [P] có thể chạy cùng lúc
   - **Làm theo TDD**: Chạy tác vụ kiểm thử trước tác vụ triển khai tương ứng
   - **Phối hợp theo file**: Các tác vụ đụng tới cùng file phải chạy tuần tự
   - **Điểm kiểm tra**: Xác nhận từng giai đoạn đã hoàn tất trước khi đi tiếp

7. Quy tắc khi thực hiện triển khai:
   - **Thiết lập trước**: Khởi tạo cấu trúc dự án, thư viện phụ thuộc, cấu hình
   - **Test trước code**: Nếu cần viết test cho contract, thực thể và kịch bản tích hợp
   - **Phát triển phần lõi**: Triển khai model, service, lệnh CLI, endpoint
   - **Phần tích hợp**: Kết nối cơ sở dữ liệu, middleware, ghi log, dịch vụ bên ngoài
   - **Hoàn thiện và kiểm chứng**: Unit test, tối ưu hiệu năng, tài liệu

8. Theo dõi tiến độ và xử lý lỗi:
   - Báo cáo tiến độ sau mỗi tác vụ hoàn tất
   - Dừng thực thi nếu bất kỳ tác vụ không song song nào thất bại
   - Với các tác vụ song song [P], tiếp tục với các tác vụ thành công và báo cáo các tác vụ thất bại
   - Đưa ra thông báo lỗi rõ ràng, kèm bối cảnh để gỡ lỗi
   - Đề xuất bước tiếp theo nếu không thể tiếp tục triển khai
   - **QUAN TRỌNG** Với các tác vụ đã hoàn tất, nhớ đánh dấu tác vụ đó là [X] trong file tasks.

9. Kiểm chứng khi hoàn tất:
   - Xác nhận mọi tác vụ bắt buộc đều đã hoàn tất
   - Kiểm tra các tính năng đã triển khai khớp với đặc tả ban đầu
   - Kiểm chứng các test đều chạy qua và độ phủ đạt yêu cầu
   - Xác nhận phần triển khai tuân theo kế hoạch kỹ thuật

Lưu ý: Lệnh này giả định tasks.md đã có bản phân rã tác vụ đầy đủ. Nếu tác vụ chưa đầy đủ hoặc bị thiếu, hãy đề xuất chạy `__SPECKIT_COMMAND_TASKS__` trước để sinh lại danh sách tác vụ.

## Hook bắt buộc sau khi thực thi

**Bạn PHẢI hoàn thành mục này trước khi báo hoàn tất cho người dùng.**

Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu không tồn tại, hoặc không có hook nào đăng ký dưới `hooks.after_implement`, chuyển thẳng tới phần Báo cáo hoàn tất.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_implement`.
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

Báo cáo trạng thái cuối cùng kèm bản tóm tắt phần việc đã hoàn thành.

## Hoàn tất khi

- [ ] Mọi tác vụ trong tasks.md đã hoàn tất và được đánh dấu `[X]`
- [ ] Phần triển khai đã được kiểm chứng theo đặc tả, kế hoạch và độ phủ kiểm thử
- [ ] Đã gọi hoặc bỏ qua các hook của extension theo đúng quy tắc trong mục Hook bắt buộc sau khi thực thi ở trên
- [ ] Đã báo hoàn tất cho người dùng, kèm bản tóm tắt phần việc đã hoàn thành
