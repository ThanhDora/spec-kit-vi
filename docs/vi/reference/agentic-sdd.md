<a id="agentic-sdd"></a>

# SDD có agent

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/agentic-sdd.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Các slash command `/speckit.*` điều khiển quy trình lõi Phát triển hướng đặc tả (SDD) — một **quy trình có agent** mà agent lập trình của bạn chạy từng bước. Để chạy trọn vẹn có hướng dẫn, xem [Hướng dẫn bắt đầu nhanh](../quickstart.md); trang này là tài liệu tham khảo chi tiết cho từng lệnh — gồm đối số, đầu ra và cách chúng tương tác. Về triết lý đằng sau quy trình, xem [SDD là gì?](../concepts/sdd.md). Về phân loại lỗi, xem [Sửa lỗi có agent](agentic-bugfix.md).

Các lệnh được thiết kế để chạy theo thứ tự, nhưng chỉ `/speckit.specify` là thực sự bắt buộc trước `/speckit.plan`. Các lệnh clarify, checklist và analyze là các cổng chất lượng bạn thêm vào cho bất cứ thứ gì có độ mơ hồ đáng kể.

Để đánh giá một ý tưởng trước khi cam kết viết đặc tả, xem [Đánh giá ý tưởng có agent](agentic-assessment.md). Đánh giá là tùy chọn và độc lập với quy trình SDD.

> [!NOTE]
> Trang này viết các lệnh ở dạng `/speckit.*`. Chế độ skills mặc định của GitHub Copilot dùng `/speckit-*`; một số agent khác dùng `$speckit-*` (ví dụ Codex, ZCode) hoặc `/skill:speckit-*` (ví dụ Kimi). Xem [Cách gọi lệnh](../integrations/cli.md#command-invocation).

```text
/speckit.constitution -> /speckit.specify -> /speckit.clarify -> /speckit.plan -> /speckit.checklist -> /speckit.tasks -> /speckit.analyze -> /speckit.implement -> /speckit.converge
```

<a id="command-overview"></a>

## Tổng quan các lệnh

Sau `specify init`, các lệnh này có sẵn trong integration đã chọn. Các integration hỗ trợ chế độ skills tùy chọn có thể chọn nó bằng `--integration-options="--skills"`; một số integration, kể cả Copilot, mặc định dùng skills.

| Lệnh | Skill của agent | Mục đích |
| --- | --- | --- |
| `/speckit.constitution` | `speckit-constitution` | Thiết lập hoặc cập nhật các nguyên tắc của dự án |
| `/speckit.specify` | `speckit-specify` | Xác định yêu cầu và user story |
| `/speckit.plan` | `speckit-plan` | Tạo kế hoạch triển khai kỹ thuật |
| `/speckit.tasks` | `speckit-tasks` | Chia kế hoạch thành các task có thể thực hiện |
| `/speckit.implement` | `speckit-implement` | Thực thi các task |
| `/speckit.converge` | `speckit-converge` | Đánh giá phần triển khai so với các artifact và bổ sung phần việc còn lại |
| `/speckit.clarify` | `speckit-clarify` | Giải quyết điểm mơ hồ trước khi lập kế hoạch (cổng chất lượng tùy chọn; trước đây là `/quizme`) |
| `/speckit.analyze` | `speckit-analyze` | Kiểm tra tính nhất quán của artifact sau khi có task và trước khi triển khai (cổng chất lượng tùy chọn) |
| `/speckit.checklist` | `speckit-checklist` | Sinh checklist chất lượng yêu cầu (cổng chất lượng tùy chọn) |

## `/speckit.constitution`

Tạo hoặc cập nhật **constitution** của dự án — các nguyên tắc định hướng mà mọi giai đoạn sau được đánh giá theo — và giữ các template phụ thuộc đồng bộ. Chạy một lần từ đầu và cập nhật mỗi khi nguyên tắc của bạn thay đổi. Truyền các nguyên tắc làm đối số.

```text
/speckit.constitution This project follows a "Library-First" approach. All features must be implemented as standalone libraries first. We use TDD strictly. We prefer functional programming patterns.
```

Để có điểm khởi đầu tổng quát hơn:

```text
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements.
```

## `/speckit.specify`

Tạo hoặc cập nhật **đặc tả** tính năng từ một mô tả bằng ngôn ngữ tự nhiên. Tập trung vào **cái gì** và **tại sao** — hành vi và mục tiêu hướng tới người dùng — chứ không phải tech stack, vốn thuộc về `/speckit.plan`.

Workflow này cũng có thể duy trì `checklists/requirements.md`, checklist chất lượng đặc tả có sẵn mà `/speckit.specify` tạo ra và `/speckit.clarify` đánh giá lại. Vòng đời đó tách biệt với các checklist tùy chỉnh do `/speckit.checklist` sinh ra.

```text
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

## `/speckit.clarify`

Đặt tối đa năm câu hỏi có trọng tâm về những phần chưa được đặc tả đủ trong spec hiện tại và ghi câu trả lời của bạn trở lại `spec.md`. Chạy bao nhiêu lần tùy cần trước khi lập kế hoạch, mỗi lần xử lý một phần khác nhau. Có thể truyền một phần trọng tâm làm đối số.

```text
/speckit.clarify Focus on the task card behavior: status changes, comment limits, and who can be assigned.
```

Làm rõ trước khi lập kế hoạch giúp bạn không thiết kế trên nền những điểm mơ hồ. Nếu sau này `/speckit.analyze` phát hiện thiếu sót trong yêu cầu, hãy quay lại chạy `/speckit.clarify` (hoặc `/speckit.specify`) lần nữa.

Khi `checklists/requirements.md` tồn tại, `/speckit.clarify` có thể cập nhật trạng thái đánh giá của nó như một phần của việc thắt chặt spec. Ngoại lệ này chỉ áp dụng cho checklist yêu cầu có sẵn, không áp dụng cho các checklist review tùy chỉnh.

## `/speckit.plan`

Chạy quy trình lập kế hoạch để sinh các artifact thiết kế từ spec. Đây là nơi dành cho chi tiết triển khai — hãy cung cấp tech stack, kiến trúc và ràng buộc kỹ thuật làm đối số.

```text
/speckit.plan Use .NET Aspire with Postgres. The frontend is Blazor Server with drag-and-drop boards and real-time updates. Expose REST APIs for projects, tasks, and notifications.
```

Với ví dụ album ảnh ở trên:

```text
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

## `/speckit.checklist`

Sinh checklist chất lượng cho tính năng — hãy coi nó như **"unit test cho yêu cầu của bạn."** Thay vì kiểm thử code, nó kiểm tra bản thân spec có đầy đủ, rõ ràng, không mơ hồ và nhất quán không (ví dụ: "Quy tắc kéo-thả đã được định nghĩa cho mọi cột chưa?", "Hành vi khi người dùng được giao bị xóa đã được đặc tả chưa?").

Checklist tùy chỉnh do lệnh này sinh ra là artifact review chất lượng yêu cầu thuộc quyền người review. Agent có thể giúp đánh giá chúng khi được yêu cầu rõ ràng, nhưng bước triển khai không được âm thầm tự phê duyệt chúng. Trong checklist tùy chỉnh, `[x]` nghĩa là người review đã xác định tiêu chí chất lượng yêu cầu được đáp ứng; nó không có nghĩa là phần việc triển khai đã xong.

Chạy không có đối số để rà soát rộng, hoặc truyền một phần trọng tâm để nhắm vào một khía cạnh:

```text
/speckit.checklist
```

```text
/speckit.checklist Focus on the Kanban board interactions and comment permissions.
```

Review checklist được sinh ra. Nếu nó phát hiện thiếu sót, hãy quay lại `/speckit.clarify` hoặc `/speckit.specify` để thắt chặt spec trước khi chia nhỏ công việc, rồi chỉ đánh dấu `[x]` cho từng mục checklist tùy chỉnh sau khi tiêu chí chất lượng yêu cầu đã được review và đáp ứng.

## `/speckit.tasks`

Sinh `tasks.md` có thể thực hiện, sắp theo thứ tự phụ thuộc, từ các artifact thiết kế. Task được tổ chức thành các giai đoạn: **Setup**, **Foundational** (điều kiện tiên quyết mang tính chặn), rồi **mỗi user story một giai đoạn** theo thứ tự ưu tiên, và một giai đoạn **Polish** cuối cùng cho các vấn đề xuyên suốt. Test được sinh trong giai đoạn của user story khi được yêu cầu thay vì thành một giai đoạn riêng, và task được đánh dấu chạy song song khi có thể.

```text
/speckit.tasks
```

## `/speckit.analyze`

Thực hiện phân tích **chỉ đọc** về tính nhất quán và chất lượng xuyên suốt các artifact `spec.md`, `plan.md` và `tasks.md`, báo cáo xung đột, thiếu sót và điểm mơ hồ (ví dụ một task không có yêu cầu tương ứng, hoặc một lựa chọn trong plan mâu thuẫn với spec). Nó không bao giờ sửa file — nó tạo báo cáo và có thể đề xuất cách khắc phục để bạn phê duyệt.

```text
/speckit.analyze
```

Chạy nó trước khi triển khai, khi việc điều chỉnh artifact vẫn còn rẻ. Nếu nó phát hiện vấn đề, hãy **quay lại bước trước sở hữu vấn đề đó** và sửa tận gốc — `/speckit.specify` hoặc `/speckit.clarify` cho vấn đề về yêu cầu, `/speckit.plan` cho vấn đề thiết kế, `/speckit.tasks` để sinh lại danh sách task — rồi chạy lại `/speckit.analyze` cho đến khi kết quả sạch. Bạn cũng có thể chạy lại `/speckit.analyze` sau khi triển khai như một lần review bổ sung.

## `/speckit.implement`

Thực thi các task trong `tasks.md`, chạy từng giai đoạn theo thứ tự phụ thuộc và tôn trọng các marker song song.

Trước khi thực thi task, nó đọc trạng thái checkbox của checklist như một cổng kiểm soát. Marker của checklist là chỉ đọc đối với lệnh này: `/speckit.implement` đếm các mục đã đánh dấu và chưa đánh dấu, và hỏi trước khi tiếp tục nếu còn mục chưa đánh dấu, nhưng không được thay đổi marker của checklist. Với checklist tùy chỉnh, mục đã đánh dấu nghĩa là người review đã phê duyệt chất lượng yêu cầu, không phải phần việc triển khai đã hoàn tất.

Với tính năng nhỏ, chạy một lần để xây dựng mọi thứ:

```text
/speckit.implement
```

Với tính năng lớn, hãy làm theo từng đợt để tránh làm quá tải ngữ cảnh của agent — giới hạn phạm vi mỗi lần chạy bằng một đối số, xác nhận kết quả, rồi tiếp tục:

```text
/speckit.implement Implement only the Setup and Foundational phases: project scaffolding and the project/task data model with basic CRUD. Stop before the user-story features.
```

```text
/speckit.implement Now implement the Kanban board user story: drag-and-drop between columns.
```

Xác nhận mỗi đợt hoạt động trước khi chuyển sang đợt tiếp theo.

## `/speckit.converge`

Đánh giá codebase so với spec, plan và tasks của tính năng để xác nhận không bỏ sót gì. Nó **chỉ bổ sung**: không bao giờ sửa hay xóa code, và thao tác ghi duy nhất có thể có là thêm task vào `tasks.md`. Chỉ chạy nó sau khi `/speckit.implement` đã chạy trên `tasks.md` hiện tại.

```text
/speckit.converge
```

Trước tiên nó in bản tóm tắt phát hiện được phân cấp theo mức độ nghiêm trọng, rồi đi đến một trong hai kết quả:

- **Converged** — không tìm thấy thiếu sót. `tasks.md` được giữ nguyên từng byte và bạn sẽ thấy kết quả sạch như `✅ Converged — the implementation satisfies the spec, plan, and tasks.` Bạn đã xong; hãy chuyển sang review hoặc mở PR.
- **Tasks appended** — có thiếu sót. Converge bổ sung chúng thành task mới trong mục Convergence của `tasks.md` và cho bạn biết có bao nhiêu. Chạy lại `/speckit.implement` để hoàn thành chúng, rồi chạy `/speckit.converge` thêm lần nữa. Mỗi lượt tìm ra ít mục hơn; lặp lại cho đến khi nó báo converged.
