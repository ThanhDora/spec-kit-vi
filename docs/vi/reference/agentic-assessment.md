<a id="agentic-idea-assessment"></a>

# Đánh giá ý tưởng có agent

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/agentic-assessment.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Extension **assess** đi kèm, cần chủ động bật, đánh giá một ý tưởng qua các bước **intake → research → define → shape → decide**. Đây là một quy trình độc lập: nó có thể chạy trong một dự án đã khởi tạo mà chưa có mã nguồn, chỉ sinh ra artifact đánh giá và không tự động bắt đầu SDD. Để xem ví dụ có hướng dẫn, xem [Bắt đầu nhanh với đánh giá ý tưởng](../guides/assessment.md).

Cài nó từ thư mục gốc của một dự án đã khởi tạo:

```bash
specify extension add assess
```

Các lệnh bên dưới dùng ký pháp `/speckit.assess.*`. Chế độ skills mặc định của GitHub Copilot dùng `/speckit-assess-*`; các integration khác có thể dùng tiền tố khác. Xem [Cách gọi lệnh](../integrations/cli.md#command-invocation).

<a id="commands-and-artifacts"></a>

## Lệnh và artifact

Mọi artifact đều được ghi trong `.specify/assessments/<slug>/`.

| Lệnh | Mục đích | Đầu ra |
| --- | --- | --- |
| `/speckit.assess.intake` | Ghi nhận ý tưởng từ văn bản, URL, ticket hoặc một tham chiếu tới codebase | `intake.md` |
| `/speckit.assess.research` | Thu thập bằng chứng ủng hộ và phản bác ý tưởng, kèm nguồn và độ tin cậy | `research.md` |
| `/speckit.assess.define` | Xác định người dùng, vấn đề, mục tiêu, phi mục tiêu, chỉ số và cái giá của việc không hành động | `problem.md` |
| `/speckit.assess.shape` | So sánh các phương án ở mức khái niệm, mức đầu tư chấp nhận được và các đánh đổi | `concept.md` |
| `/speckit.assess.decide` | Ghi lại bảng điểm, kết luận, lý do và phần bàn giao SDD tùy chọn | `decision.md` |

Truyền ý tưởng ban đầu và một slug cho intake, rồi dùng lại slug đó:

```text
/speckit.assess.intake "Let users work offline and sync when they reconnect." slug=offline-mode
/speckit.assess.research slug=offline-mode
/speckit.assess.define slug=offline-mode
/speckit.assess.shape slug=offline-mode
/speckit.assess.decide slug=offline-mode
```

<a id="prerequisites-and-scope"></a>

## Điều kiện tiên quyết và phạm vi

Chuỗi năm giai đoạn là lộ trình thông thường, nhưng không phải giai đoạn nào cũng bắt buộc:

- `define` có thể làm việc trực tiếp từ đầu vào của người dùng; intake và research là tùy chọn khi tạo định nghĩa vấn đề.
- `shape` cần `problem.md` và chỉ ở mức khái niệm. Kiến trúc, mô hình dữ liệu, API, task và triển khai thuộc về giai đoạn bàn giao, không thuộc đánh giá.
- `decide` cần `problem.md` và đọc mọi artifact đánh giá có sẵn. Kết luận `go` còn cần một khái niệm đã được định hình và bằng chứng đầy đủ; bỏ qua research không miễn trừ yêu cầu về bằng chứng.

<a id="slugs-and-existing-artifacts"></a>

## Slug và artifact hiện có

Slug xác định thư mục của một ý tưởng. Slug do người dùng cung cấp được chuẩn hóa thành kebab-case chữ thường và giữ nguyên, không thêm timestamp hay số. Nếu không cung cấp slug, intake sẽ hỏi tương tác; các lần chạy tự động sinh slug duy nhất. Các giai đoạn sau có thể dùng lại slug từ ngữ cảnh khi thư mục của nó tồn tại.

Artifact hiện có không bị ghi đè khi chưa được xác nhận. Ở chế độ tự động, các lệnh từ chối ghi đè chúng. Để làm rõ thông thường, hãy tinh chỉnh artifact hiện có thay vì chạy lại lệnh.

<a id="decisions-and-evidence"></a>

## Quyết định và bằng chứng

Bảng điểm quyết định chấm các tiêu chí là `strong`, `adequate`, `weak` hoặc `unknown`, kèm giải thích rút ra từ các artifact.

| Kết luận | Yêu cầu hoặc ý nghĩa |
| --- | --- |
| `go` | Tính xác đáng của vấn đề và độ mạnh của bằng chứng ít nhất là `adequate`, và có một phương án khái niệm được đề xuất |
| `needs-clarification` | Các điểm chưa biết được nêu tên sẽ chặn quyết định; bằng chứng yếu hoặc chưa biết, hoặc thiếu khái niệm, không thể biện minh cho `go` |
| `kill` | Ý tưởng chưa đáng theo đuổi lúc này; lý do quyết định được ghi lại rõ ràng |

Research phải bao gồm bằng chứng phản bác ý tưởng. Nhận định không có nguồn vẫn được đánh dấu `ASSUMPTION`; đừng bịa trích dẫn hay trình bày bằng chứng không chắc chắn như sự thật. Một quyết định dừng có ghi chép rõ ràng cũng là kết quả hữu ích.

<a id="refining-an-assessment"></a>

## Tinh chỉnh một bản đánh giá

Theo luồng thông thường, chạy mỗi giai đoạn một lần. Để xử lý các marker cần làm rõ hoặc kết luận `needs-clarification`, hãy sửa trực tiếp Markdown liên quan hoặc yêu cầu agent bổ sung các dữ kiện còn thiếu qua chat tự do. Giữ nguyên nguồn và tag độ tin cậy, rồi review các artifact phụ thuộc và sửa `decision.md` khi cần. Đây là tinh chỉnh artifact, không phải chạy lại lệnh nhiều lần.

Chạy lại một lệnh trước đó chỉ dành cho ngoại lệ, chẳng hạn slug sai hoặc bản nháp bị bỏ. Xem [ví dụ làm rõ có hướng dẫn](../guides/assessment.md#resolve-unknowns-by-refining-the-artifacts).

<a id="handoff-and-guardrails"></a>

## Bàn giao và rào chắn an toàn

Quyết định `go` có kèm bản tóm tắt bàn giao mà bạn có thể chọn truyền cho `/speckit.specify`. Không có hook vòng đời nào cài đánh giá thành điều kiện tiên quyết của SDD, và ý tưởng không phải phần mềm hoàn toàn không cần đi vào SDD.

Các lệnh đánh giá chỉ ghi trong `.specify/assessments/<slug>/`; chúng không sửa mã nguồn. Extension kiểm tra slug và đường dẫn, coi nội dung tải về là dữ liệu không đáng tin cậy và áp dụng chính sách tin cậy URL của nó. Tham khảo [tài liệu của extension](https://github.com/github/spec-kit/blob/main/extensions/assess/README.md) để biết đầy đủ các rào chắn an toàn và mối quan hệ với các extension khác.
