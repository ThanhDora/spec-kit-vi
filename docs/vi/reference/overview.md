<a id="reference"></a>

# Tài liệu tham khảo

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/overview.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Specify CLI (`specify`) quản lý toàn bộ vòng đời Phát triển hướng đặc tả — từ khởi tạo dự án đến tự động hóa workflow. Phần này là tài liệu tham khảo chi tiết về các lệnh và thành phần cơ bản của CLI, cùng các quy trình có agent `/speckit.*` mà agent lập trình của bạn chạy.

<a id="core-commands"></a>

## Lệnh lõi

Các lệnh nền tảng để tạo và quản lý dự án Spec Kit. Khởi tạo dự án mới với cấu trúc thư mục, template và script cần thiết. Xác minh hệ thống của bạn đã cài các công cụ cần thiết. Xem phiên bản và thông tin hệ thống.

[Core Commands reference →](core.md)

## MCP server

Lệnh thử nghiệm `specify mcp` cung cấp các lệnh JSON ổn định của CLI cho client MCP qua một server stdio cục bộ.

[MCP Server reference →](mcp.md)

<a id="integrations"></a>

## Integration

Integration kết nối Spec Kit với agent lập trình AI của bạn. Mỗi integration thiết lập các file lệnh và cấu trúc thư mục phù hợp cho một agent cụ thể. Mỗi dự án chỉ có một integration hoạt động tại một thời điểm, và bạn có thể chuyển đổi giữa chúng bất cứ lúc nào.

[Hướng dẫn thiết lập theo từng agent →](../integrations/index.md)

[Tài liệu tham khảo quản lý integration →](../integrations/cli.md)

<a id="catalogs"></a>

## Catalog

Catalog là các chỉ mục sắp theo độ ưu tiên để tìm integration, extension, preset, workflow, loại workflow step và bundle. Spec Kit có các nguồn có sẵn và hỗ trợ catalog riêng tư do tổ chức quản lý, với chính sách tìm kiếm và cài đặt rõ ràng.

[Catalogs reference →](catalogs.md)

<a id="extensions"></a>

## Extension

Extension bổ sung khả năng mới cho Spec Kit — lệnh chuyên biệt theo lĩnh vực, tích hợp công cụ bên ngoài, cổng chất lượng và nhiều hơn nữa. Chúng được tìm thấy qua catalog và có thể được cài, cập nhật, bật, tắt hoặc gỡ một cách độc lập. Nhiều extension có thể cùng tồn tại trong một dự án.

[Extensions reference →](extensions.md)

<a id="presets"></a>

## Preset

Preset tùy biến cách Spec Kit hoạt động — ghi đè file lệnh, file template và file script mà không thay đổi công cụ nào. Chúng cho phép bạn áp dụng tiêu chuẩn của tổ chức, điều chỉnh workflow theo phương pháp của bạn, hoặc bản địa hóa toàn bộ trải nghiệm. Nhiều preset có thể xếp chồng theo thứ tự ưu tiên để phân lớp các tùy biến.

[Presets reference →](presets.md)

<a id="artifacts"></a>

## Artifact

Artifact là các command, template và script mà một dự án cung cấp, bất kể lớp nào đóng góp chúng. Nhóm lệnh `specify artifact` là bề mặt chỉ đọc để tra cứu danh mục đó — một danh sách phẳng mọi thứ hiển thị, cùng toàn bộ chồng kết hợp phía sau từng mục, gồm cả lớp nào thắng và lớp nào bị che.

[Artifacts reference →](artifacts.md)

<a id="workflows"></a>

## Workflow

Workflow tự động hóa các quy trình Phát triển hướng đặc tả nhiều bước thành chuỗi có thể lặp lại. Chúng nối các command, prompt, step shell và điểm kiểm tra của con người, hỗ trợ logic điều kiện, vòng lặp, fan-out/fan-in, và khả năng tạm dừng rồi tiếp tục từ đúng điểm bị gián đoạn.

[Workflows reference →](workflows.md)

<a id="bundles"></a>

## Bundle

Bundle kết hợp các extension, preset, workflow và step hiện có thành một đơn vị duy nhất, có phiên bản và cài đặt được. Thay vì thêm hành vi mới, bundle tuyển chọn một chồng thành phần cơ bản — mọi thứ một nhóm hay vai trò cần — và cài trong một bước qua cơ chế riêng của từng thành phần, với ghim phiên bản, kiểm tra xung đột và theo dõi nguồn gốc để cập nhật và gỡ sạch sẽ.

[Bundles reference →](bundles.md)

<a id="agentic-commands"></a>

## Lệnh có agent

Các phần trên đề cập các thành phần cơ bản do CLI `specify` quản lý. Các phần sau là những quy trình độc lập do agent lập trình của bạn chạy, không phải lệnh terminal. Tài liệu tham khảo dùng ký pháp `/speckit.*`; xem [Cách gọi lệnh](../integrations/cli.md#command-invocation) để biết cú pháp của agent bạn dùng. Để có ví dụ có hướng dẫn, hãy bắt đầu với [SDD](../quickstart.md), [sửa lỗi](../guides/bugfix.md) hoặc [đánh giá ý tưởng](../guides/assessment.md).

<a id="agentic-sdd"></a>

### SDD có agent

Các slash command `/speckit.*` điều khiển quy trình lõi Phát triển hướng đặc tả mà agent lập trình của bạn chạy từng bước: constitution, specify, clarify, plan, checklist, tasks, analyze, implement và converge. Chạy chúng theo thứ tự, thêm các cổng chất lượng clarify/checklist/analyze cho bất cứ thứ gì có độ mơ hồ đáng kể.

[Agentic SDD reference →](agentic-sdd.md)

<a id="agentic-bug-fix"></a>

### Sửa lỗi có agent

Extension **bug** đi kèm bổ sung quy trình phân loại lỗi ba bước — đánh giá, sửa và xác nhận — với mỗi bug được theo dõi trong thư mục riêng tại `.specify/bugs/`. Cài nó bằng `specify extension add bug`.

[Agentic Bug Fix reference →](agentic-bugfix.md)

<a id="agentic-idea-assessment"></a>

### Đánh giá ý tưởng có agent

Extension **assess** đi kèm, cần chủ động bật, đánh giá một ý tưởng qua intake, research, định nghĩa, định hình và quyết định go / needs-clarification / kill. Nó hoạt động mà không cần mã nguồn, không yêu cầu và không tự động bắt đầu SDD. Cài nó bằng `specify extension add assess`.

[Agentic Idea Assessment reference →](agentic-assessment.md)
