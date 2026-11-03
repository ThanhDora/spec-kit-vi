<a id="quick-start-guide"></a>
<a id="spec-driven-development-quickstart"></a>

# Hướng dẫn nhanh Phát triển hướng đặc tả

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../quickstart.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hướng dẫn này giúp bạn bắt đầu Phát triển hướng đặc tả (Spec-Driven Development — SDD) với Spec Kit. Xuyên suốt bài, mỗi bước được minh họa bằng một ví dụ chạy liền mạch: **Taskify**, một nền tảng nhỏ giúp nhóm làm việc hiệu quả hơn.

Hãy dùng SDD để xây dựng một tính năng hoặc ứng dụng từ đặc tả. Khi cần sửa lỗi,
hãy làm theo [hướng dẫn nhanh sửa lỗi](guides/bugfix.md); khi cần quyết định một ý tưởng
có đáng đầu tư hay không, hãy làm theo [hướng dẫn nhanh đánh giá ý tưởng](guides/assessment.md).
Đây là các quy trình độc lập, không phải điều kiện tiên quyết của hướng dẫn này.

> [!NOTE]
> Các script tự động hóa có ba biến thể: Bash (`.sh`), PowerShell (`.ps1`) và Python (`.py`). Khi chạy tương tác, `specify init` sẽ hỏi bạn chọn một loại; khi chạy không tương tác (không có TTY, hoặc có `--non-interactive`), mặc định là biến thể shell của hệ điều hành. Truyền `--script sh|ps|py` để chọn rõ ràng.

Các bước trong bài dùng chế độ skills mặc định của GitHub Copilot (`/speckit-*`).
Với agent hoặc chế độ khác, xem
[Cách gọi lệnh](../integrations/cli.md#command-invocation).
Gọi từng skill `/speckit-*` riêng biệt trong khung chat của agent và review
kết quả trước khi sang bước tiếp theo. Đây là skill của agent, không phải lệnh
terminal; chỉ việc cài CLI và thiết lập dự án mới dùng terminal.

<a id="recommended-process"></a>

## Quy trình khuyến nghị

> [!TIP]
> **Nhận biết ngữ cảnh**: Spec Kit theo dõi tính năng đang làm thông qua thư mục tính năng được ghi trong `.specify/feature.json` (có thể ghi đè bằng biến môi trường `SPECIFY_FEATURE_DIRECTORY`). Các lệnh xác định tính năng từ trạng thái đó, **không** dựa vào Git branch đang checkout — không cần Git. Extension **git** (bật khi cần) bổ sung feature branch được đánh số (ví dụ `001-feature-name`) để tổ chức công việc trong hệ thống quản lý phiên bản, nhưng tính năng đang làm vẫn là thư mục mà trạng thái kia trỏ tới; chỉ `git checkout` thôi thì không làm thay đổi nó. Để các lệnh làm việc với tính năng khác, hãy cập nhật `.specify/feature.json` (hoặc đặt `SPECIFY_FEATURE_DIRECTORY`).

Sau khi cài Spec Kit, mỗi skill bên dưới là một bước trong quy trình. Có hai lộ trình phổ biến:

Hãy thiết lập hiến chương (constitution) một lần cho mỗi dự án bằng `/speckit-constitution` trước
khi bắt đầu bất kỳ lộ trình nào.

**Lộ trình ngắn** — cho tính năng nhỏ:

1. `/speckit-specify`
2. `/speckit-plan`
3. `/speckit-tasks`
4. `/speckit-implement`
5. `/speckit-converge`

**Lộ trình đầy đủ** — cho tính năng chạy production, bổ sung `/speckit-clarify`, `/speckit-checklist` và `/speckit-analyze` làm cổng kiểm soát chất lượng:

1. `/speckit-constitution` (một lần cho mỗi dự án)
2. `/speckit-specify`
3. `/speckit-clarify`
4. `/speckit-plan`
5. `/speckit-checklist`
6. `/speckit-tasks`
7. `/speckit-analyze`
8. `/speckit-implement`
9. `/speckit-converge`

<a id="install-specify"></a>

### Cài Specify

**Trong terminal**, cài CLI từ PyPI (cần [uv](install/uv.md)), rồi khởi tạo dự án:

```bash
uv tool install specify-cli
specify init taskify --integration copilot
cd taskify
```

`init` cho phép bạn chọn agent lập trình theo kiểu tương tác, hoặc truyền rõ bằng `--integration` (ví dụ `--integration copilot`). Với CI và môi trường chạy agent AI, hãy thêm `--non-interactive` để các lựa chọn chưa chỉ định dùng giá trị mặc định đã được mô tả trong tài liệu, thay vì treo ở bước chọn bằng phím mũi tên.

> [!NOTE]
> Bạn muốn dùng `pipx`, chạy một lần bằng `uvx`, ghim một bản phát hành hay thiết lập offline/air-gapped? Xem [Hướng dẫn cài đặt](installation.md) để biết mọi cách được hỗ trợ.
> Thêm Spec Kit vào repository đã có code? Hãy làm theo
> [Áp dụng Spec Kit vào dự án có sẵn](guides/existing-projects.md) trước khi
> bắt đầu quy trình dưới đây.

Mở agent lập trình trong thư mục dự án. Lần lượt gọi từng skill sau
trong khung chat của agent.

<a id="step-1-speckitconstitution--set-the-ground-rules"></a>
<a id="step-1-speckit-constitution--set-the-ground-rules"></a>

### Bước 1: `/speckit-constitution` — đặt ra nguyên tắc nền tảng

Thiết lập các nguyên tắc định hướng của dự án; mọi bước về sau đều được đánh giá dựa trên các nguyên tắc này. Chạy một lần ngay từ đầu, truyền các nguyên tắc của bạn làm đối số.

```text
/speckit-constitution Taskify is a "Security-First" application. All user inputs must be validated. We use a microservices architecture. Code must be fully documented.
```

<a id="step-2-speckitspecify--describe-what-to-build"></a>
<a id="step-2-speckit-specify--describe-what-to-build"></a>

### Bước 2: `/speckit-specify` — mô tả thứ cần xây dựng

Tạo đặc tả tính năng từ mô tả bằng ngôn ngữ tự nhiên. Tập trung vào **cái gì** và **tại sao**, không phải tech stack.

```text
/speckit-specify Develop Taskify, a team productivity platform where predefined users create projects, assign tasks, comment, and move tasks across Kanban columns (To Do, In Progress, In Review, Done). Five users (one product manager, four engineers), three sample projects, no login for this first phase.
```

<a id="step-3-speckitclarify--resolve-ambiguities"></a>
<a id="step-3-speckit-clarify--resolve-ambiguities"></a>

### Bước 3: `/speckit-clarify` — giải quyết các điểm mơ hồ

Đặt các câu hỏi có trọng tâm về những chỗ chưa được đặc tả đủ và đưa câu trả lời của bạn vào lại đặc tả, để bạn không lập kế hoạch trên nền móng mơ hồ. Chạy trước khi lập kế hoạch, có thể kèm một vùng cần tập trung.

```text
/speckit-clarify Focus on task card behavior — status changes, comment permissions, and user assignment.
```

<a id="step-4-speckitplan--choose-the-tech-stack"></a>
<a id="step-4-speckit-plan--choose-the-tech-stack"></a>

### Bước 4: `/speckit-plan` — chọn tech stack

Sinh các artifact thiết kế từ đặc tả. Đây là nơi dành cho chi tiết triển khai — hãy cung cấp tech stack và kiến trúc của bạn.

```text
/speckit-plan Use .NET Aspire with Postgres. The frontend is Blazor Server with drag-and-drop boards and real-time updates. Expose REST APIs for projects, tasks, and notifications.
```

<a id="step-5-speckitchecklist--validate-the-spec"></a>
<a id="step-5-speckit-checklist--validate-the-spec"></a>

### Bước 5: `/speckit-checklist` — kiểm định đặc tả

Sinh một checklist chất lượng tùy chỉnh — "unit test cho yêu cầu của bạn" — để xác nhận đặc tả đầy đủ, rõ ràng và nhất quán trước khi phân rã công việc. Các checklist tùy chỉnh này là artifact dùng để review chất lượng yêu cầu và thuộc quyền của người review: chỉ đánh dấu một mục `[x]` khi người review xác định tiêu chí chất lượng yêu cầu đó đã được đáp ứng. Mục tùy chỉnh đã được đánh dấu không có nghĩa là phần việc triển khai đã xong.

```text
/speckit-checklist
```

<a id="step-6-speckittasks--break-the-work-down"></a>
<a id="step-6-speckit-tasks--break-the-work-down"></a>

### Bước 6: `/speckit-tasks` — phân rã công việc

Sinh file `tasks.md` gồm các tác vụ có thể thực hiện, sắp xếp theo thứ tự phụ thuộc, từ các artifact thiết kế.

```text
/speckit-tasks
```

<a id="step-7-speckitanalyze--check-consistency"></a>
<a id="step-7-speckit-analyze--check-consistency"></a>

### Bước 7: `/speckit-analyze` — kiểm tra tính nhất quán

Báo cáo các mâu thuẫn, lỗ hổng và điểm mơ hồ giữa `spec.md`, `plan.md` và `tasks.md`. Lệnh này chỉ đọc — nếu nó báo vấn đề, hãy sửa tận gốc rồi chạy lại trước khi triển khai.

```text
/speckit-analyze
```

<a id="step-8-speckitimplement--build-it"></a>
<a id="step-8-speckit-implement--build-it"></a>

### Bước 8: `/speckit-implement` — xây dựng

Thực hiện các tác vụ trong `tasks.md` theo thứ tự phụ thuộc. Trước khi triển khai, lệnh đọc trạng thái các ô đánh dấu trong checklist như một cổng kiểm soát và hỏi lại trước khi tiếp tục nếu còn mục chưa được đánh dấu; lệnh không thay đổi bất kỳ file checklist hay dấu đánh dấu nào. Checklist có sẵn `checklists/requirements.md` do `/speckit-specify` và `/speckit-clarify` duy trì, còn các checklist tùy chỉnh vẫn thuộc quyền của người review. Chạy một lần để xây dựng mọi thứ, hoặc giới hạn mỗi lần một giai đoạn với tính năng lớn.

```text
/speckit-implement
```

<a id="step-9-speckitconverge--verify-completeness"></a>
<a id="step-9-speckit-converge--verify-completeness"></a>

### Bước 9: `/speckit-converge` — xác minh độ hoàn thiện

Đối chiếu codebase với đặc tả, kế hoạch và danh sách tác vụ. Nếu phát hiện thiếu sót, lệnh bổ sung tác vụ mới vào `tasks.md`; hãy chạy `/speckit-implement` rồi converge lại cho đến khi lệnh báo **Converged**. Nếu không còn thiếu sót, bạn đã xong — chuyển sang review hoặc mở PR.

```text
/speckit-converge
```

> [!TIP]
> Để xem tài liệu tham khảo đầy đủ về từng lệnh — đối số, đầu ra, triển khai theo giai đoạn và cách các lệnh phối hợp với nhau — xem [Agentic SDD](../reference/agentic-sdd.md).

<a id="key-principles"></a>

## Nguyên tắc chính

- **Nói rõ** bạn đang xây dựng cái gì và tại sao
- **Đừng tập trung vào tech stack** ở giai đoạn đặc tả
- **Lặp lại và tinh chỉnh** đặc tả trước khi triển khai
- **Kiểm định** yêu cầu và kế hoạch trước khi bắt đầu viết code
- **Để agent lập trình lo** các chi tiết triển khai

<a id="next-steps"></a>

## Bước tiếp theo

- Xem tài liệu tham khảo [Agentic SDD](../reference/agentic-sdd.md) để biết đầy đủ chi tiết của từng lệnh
- Tìm hiểu cách [tùy biến quy trình](guides/customization.md) bằng extension, preset, workflow và bundle
- Đọc [toàn bộ phương pháp luận](https://github.com/github/spec-kit/blob/main/spec-driven.md) để có hướng dẫn chuyên sâu
- So sánh [các template lõi](https://github.com/github/spec-kit/tree/main/templates) với
  [các walkthrough của cộng đồng](../community/walkthroughs.md) để thấy Phát triển hướng đặc tả được dùng thế nào trong dự án thực tế
- Khám phá [mã nguồn trên GitHub](https://github.com/github/spec-kit)
