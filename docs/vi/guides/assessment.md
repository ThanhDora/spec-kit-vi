<a id="idea-assessment-quickstart"></a>

# Hướng dẫn nhanh đánh giá ý tưởng

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../guides/assessment.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Dùng quy trình này để quyết định một ý tưởng có đáng đầu tư hay không trước khi cam kết
với một giải pháp. Quy trình dùng được cho cả ý tưởng phần mềm lẫn các quyết định ngoài phần mềm.
Không cần có sẵn mã nguồn.

Extension **assess** đi kèm (bundled), chỉ chạy khi bạn chủ động bật, có năm bước:
**intake → research → define → shape → decide** (tiếp nhận → nghiên cứu → định nghĩa → định hình → quyết định). Kết quả là một quyết định
`go`, `needs-clarification` hoặc `kill` có bằng chứng hỗ trợ, không phải một phần triển khai.

<a id="set-up"></a>

## Thiết lập

[Cài Spec Kit và khởi tạo dự án](../installation.md). Một dự án rỗng
là đủ, hoặc bạn có thể dùng một
[repository có sẵn](existing-projects.md) khi ý tưởng liên quan đến code trong đó.
Trong terminal, tại thư mục gốc của dự án đã khởi tạo, cài extension:

```bash
specify extension add assess
```

Sau đó mở agent lập trình trong thư mục đó. Các ví dụ dưới đây dùng
chế độ skills mặc định của GitHub Copilot (`--integration copilot`). Các agent khác
dùng [cú pháp gọi lệnh](../../integrations/cli.md#command-invocation)
riêng.
Gọi từng skill `/speckit-assess-*` riêng biệt trong khung chat của agent, review
artifact trước khi đi tiếp. Đây là skill của agent, không phải lệnh terminal;
lệnh terminal ở trên chỉ để cài extension.

<a id="1-capture-the-idea"></a>

## 1. Ghi nhận ý tưởng

```text
/speckit-assess-intake "Let users work offline and sync when they reconnect." slug=offline-mode
```

Bạn cũng có thể cung cấp URL, ticket hoặc vị trí trong codebase. Agent ghi
đầu vào vào `.specify/assessments/offline-mode/intake.md`.
Slug là định danh chung cho cả năm bước.

<a id="2-research-the-evidence"></a>

## 2. Nghiên cứu bằng chứng

```text
/speckit-assess-research slug=offline-mode
```

Agent thu thập bằng chứng ủng hộ và phản bác trong `research.md`. Hãy review
nguồn và mức độ tin cậy: giả định không có trích dẫn không phải là sự thật đã được xác lập.
Bước này nên thách thức ý tưởng, chứ không chỉ tìm lý lẽ bênh vực nó.

<a id="3-define-the-problem"></a>

## 3. Định nghĩa vấn đề

```text
/speckit-assess-define slug=offline-mode
```

Agent ghi `problem.md`, mô tả người dùng bị ảnh hưởng, vấn đề, mục tiêu,
những gì không phải mục tiêu, chỉ số thành công và cái giá của việc không làm gì.

<a id="4-shape-possible-solutions"></a>

## 4. Định hình các giải pháp khả thi

```text
/speckit-assess-shape slug=offline-mode
```

Agent so sánh các phương án ở mức ý tưởng, các ràng buộc, mức đầu tư sẵn sàng bỏ ra (appetite) và các đánh đổi
trong `concept.md`. Kiến trúc chi tiết, tác vụ triển khai và thay đổi mã nguồn
được cố ý để ngoài quy trình này.

<a id="5-make-the-decision"></a>

## 5. Đưa ra quyết định

```text
/speckit-assess-decide slug=offline-mode
```

Agent ghi bảng điểm, lý do và kết luận vào `decision.md`.

| Kết luận | Ý nghĩa | Việc cần làm |
| --- | --- | --- |
| `go` | Vấn đề và bằng chứng đủ thuyết phục, có một ý tưởng được khuyến nghị | Quyết định có hành động hay không; có thể chuyển ý tưởng phần mềm sang SDD |
| `needs-clarification` | Vẫn còn những điểm chưa biết cụ thể cản trở một quyết định có cơ sở | Bổ sung thông tin còn thiếu vào các artifact liên quan |
| `kill` | Ý tưởng chưa đáng theo đuổi lúc này | Giữ lại lý do đã ghi; dừng lại cũng là một kết quả thành công |

Cả năm artifact nằm trong `.specify/assessments/offline-mode/`. Không lệnh
đánh giá nào sửa mã nguồn.

<a id="resolve-unknowns-by-refining-the-artifacts"></a>

## Giải quyết điểm chưa biết bằng cách bổ sung artifact

Thông thường mỗi lệnh chỉ chạy một lần. Khi một artifact chứa
`[NEEDS CLARIFICATION: ...]`, hãy sửa trực tiếp file Markdown đó hoặc nhờ agent
qua chat tự do để đưa thông tin còn thiếu vào:

```text
Update .specify/assessments/offline-mode/problem.md with these confirmed success metrics: <your metrics>. Update any dependent wording and revise decision.md if this resolves the blocker. Preserve source and confidence tags.
```

Đừng tự động sinh lại toàn bộ bước. Hãy yêu cầu agent xem xét
liệu các thông tin mới có gỡ được điểm vướng hay không và sửa lại bảng điểm, kết luận
hoặc phần bàn giao ở phía sau cho phù hợp. Chạy lại một lệnh chỉ là ngoại lệ, chẳng hạn khi
thay một bản nháp đã bị bỏ, và không được ghi đè các artifact hiện có
khi chưa được xác nhận.

<a id="optional-handoff-to-sdd"></a>

## Bàn giao sang SDD (tùy chọn)

Đánh giá ý tưởng là quy trình độc lập: nó không tự động gọi SDD hay tự chen vào
quy trình đặc tả. Nếu bạn quyết định xây dựng một ý tưởng phần mềm có kết luận
`go`, hãy thiết lập hiến chương dự án nếu cần, rồi truyền phần tóm tắt bàn giao trong
quyết định cho lệnh đặc tả:

```text
/speckit-specify Use the handoff summary in .specify/assessments/offline-mode/decision.md to specify the approved offline-mode concept.
```

Tiếp tục với [hướng dẫn nhanh SDD](../quickstart.md). Để biết điều kiện tiên quyết của từng bước,
quy tắc đặt slug và yêu cầu về bằng chứng, xem
[tài liệu tham khảo lệnh đánh giá ý tưởng](../../reference/agentic-assessment.md).
