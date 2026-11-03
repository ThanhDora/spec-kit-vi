<div align="center">
    <img src="https://raw.githubusercontent.com/github/spec-kit/main/media/logo_large.webp" alt="Logo Spec Kit" width="200" height="200"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>Xây dựng từ đặc tả, sửa lỗi, hay thẩm định ý tưởng — cùng agent lập trình của bạn.</em></h3>
</div>

<p align="center">
    <a href="https://github.com/github/spec-kit/releases/latest"><img src="https://img.shields.io/github/v/release/github/spec-kit" alt="Bản phát hành mới nhất"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="Giấy phép"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Tài liệu"/></a>
</p>

<p align="center">
    <a href="./README.md">English</a> ·
    <a href="./README.zh-CN.md">简体中文</a> ·
    <a href="./README.ja.md">日本語</a> ·
    <a href="./README.ko.md">한국어</a> ·
    <strong>Tiếng Việt</strong>
</p>

> [!NOTE]
> Đây là bản dịch tiếng Việt do cộng đồng duy trì. Nếu có chỗ khác biệt, [bản tiếng Anh](./README.md) là bản chính thức. Thuật ngữ dùng trong bản dịch được thống nhất tại [Bảng thuật ngữ](./docs/vi/GLOSSARY.md).

Spec Kit là bộ công cụ mã nguồn mở giúp các agent lập trình AI làm việc theo quy trình có cấu trúc, dùng template tái sử dụng được và để lại kết quả được ghi chép đầy đủ. Bạn có thể bắt đầu với một quy trình dựng sẵn, tùy biến nó, hoặc mang quy trình của riêng mình vào.

## Chọn quy trình

| Bạn cần gì | Quy trình | Kết quả |
| --- | --- | --- |
| Xây dựng một tính năng hoặc ứng dụng | [Phát triển hướng đặc tả](#spec-driven-development) | Một bản đặc tả được theo sát qua các bước lập kế hoạch, triển khai và hội tụ |
| Chẩn đoán và sửa hành vi bị lỗi | [Sửa lỗi](#bug-fixing) | Nguyên nhân đã được đánh giá, bản sửa có phạm vi rõ ràng và kết quả kiểm chứng được ghi lại |
| Quyết định một ý tưởng có đáng đầu tư không | [Thẩm định ý tưởng](#idea-assessment) | Quyết định tiếp tục, cần làm rõ, hoặc dừng lại, có bằng chứng đi kèm |
| Áp dụng hoặc tự tạo một quy trình khác | [Quy trình của riêng bạn](#capabilities) | Một quy trình được điều chỉnh hoặc lắp ghép từ các thành phần nền tảng tái sử dụng được |

Đây là các điểm khởi đầu độc lập, không phải các giai đoạn bắt buộc. SDD có sẵn trong phần lõi; sửa lỗi và thẩm định là các extension đi kèm, bạn cài khi cần. Các thành phần nền tảng bên dưới cho phép bạn áp dụng hoặc tự tạo những quy trình khác.

<a id="capabilities"></a>

## Các khả năng

Spec Kit kết hợp các quy trình dùng được ngay với những cơ chế có thể lắp ghép:

| Khả năng | Cơ chế của Spec Kit |
| --- | --- |
| Kết nối hoặc chuyển đổi giữa các agent lập trình | [Integration](./docs/vi/integrations/index.md) |
| Thêm một lệnh, một cổng kiểm soát chất lượng hoặc cả một quy trình | [Extension](./docs/vi/reference/extensions.md) |
| Kết nối quy trình với công cụ hoặc dịch vụ bên ngoài | [Extension](./docs/vi/reference/extensions.md) |
| Phản hồi các sự kiện trong vòng đời của agent lập trình | [Sự kiện runtime của extension](./docs/vi/reference/extensions.md#extension-runtime-events) |
| Chạy lệnh của extension trước hoặc sau các lệnh Spec Kit | [Extension hook](./docs/vi/reference/extensions.md#project-extension-and-hook-configuration) |
| Điều chỉnh template, lệnh, thuật ngữ hoặc phương pháp | [Preset](./docs/vi/reference/presets.md) |
| Áp dụng tiêu chuẩn của tổ chức hoặc quy định pháp lý | [Preset](./docs/vi/reference/presets.md) |
| Ghi đè một template cho riêng một dự án | [Ghi đè cục bộ trong dự án](./docs/vi/guides/customization.md#project-local-overrides-and-resolution) |
| Tự động hóa prompt, lệnh, cổng kiểm soát và tác vụ shell | [Workflow](./docs/vi/reference/workflows.md) |
| Sửa một workflow đã cài mà không cần fork | [Workflow overlay](./docs/vi/reference/workflows.md#workflow-overlays) |
| Thêm hành vi thực thi tái sử dụng được vào workflow | [Workflow step](./docs/vi/reference/workflows.md#custom-step-packages) |
| Cài một bộ thiết lập chọn lọc cho một vai trò hoặc một nhóm | [Bundle](./docs/vi/reference/bundles.md) |
| Khám phá các thành phần do cộng đồng đóng góp | [Catalog](./docs/vi/reference/catalogs.md) |
| Tự host một catalog riêng gồm các thành phần đã được duyệt | [Catalog](./docs/vi/reference/catalogs.md) |
| Truy cập catalog riêng và tải thành phần | [Xác thực](./docs/vi/reference/authentication.md) |
| Làm việc offline hoặc sau tường lửa | [Nguồn cục bộ và catalog tự host](./docs/vi/install/air-gapped.md) |
| Xem lớp nào đang cung cấp một lệnh, template hoặc script | [Kiểm kê artifact](./docs/vi/reference/artifacts.md) |

Tìm trong các catalog đang bật bằng những lệnh như `specify extension search`, `specify preset search`, `specify workflow search` và `specify bundle search`. Spec Kit có sẵn các catalog cộng đồng, và tổ chức có thể thêm nguồn chọn lọc của riêng mình. Việc có mặt trong catalog không có nghĩa là thành phần đó đã được kiểm định hay bảo chứng, vì vậy hãy xem mã nguồn của thành phần cộng đồng trước khi cài hoặc chạy.

<a id="-get-started"></a>
<a id="-prerequisites"></a>
<a id="get-started"></a>

## Bắt đầu

Bạn cần Python 3.11 trở lên, [uv](./docs/vi/install/uv.md) và một agent lập trình AI được hỗ trợ, trên Linux, macOS hoặc Windows.

Chạy các lệnh sau trong terminal để cài Spec Kit và tạo dự án. Ví dụ này dùng GitHub Copilot.

```bash
uv tool install specify-cli
specify init my-project --integration copilot
cd my-project
```

<a id="-supported-ai-coding-agent-integrations"></a>

Sau khi cài Specify CLI và tạo dự án, hãy mở agent lập trình trong thư mục dự án rồi chọn một quy trình bên dưới.

Với các cách thiết lập khác:

- [Cài đặt](./docs/vi/installation.md): ghim phiên bản cụ thể, các trình cài đặt khác, CI và xử lý sự cố.
- [Dự án có sẵn](./docs/vi/guides/existing-projects.md): bắt đầu với mã nguồn bạn đang có.
- [Các agent khác](./docs/vi/integrations/index.md): khóa integration và [cú pháp gọi lệnh](./docs/vi/integrations/cli.md#command-invocation).
- [Nâng cấp](./docs/vi/upgrade.md): cập nhật bản cài đặt hiện có.

<a id="-what-is-spec-driven-development"></a>
<a id="sdd-quickstart"></a>
<a id="spec-driven-development"></a>

## Phát triển hướng đặc tả

Xác định cần xây dựng cái gì và vì sao, rồi biến bản đặc tả thành kế hoạch, danh sách tác vụ và mã chạy được.

Dưới đây là luồng tối thiểu. Tạo hiến chương (constitution) một lần cho mỗi dự án, rồi lặp lại các bước còn lại cho từng tính năng. Chạy lần lượt từng skill trong khung chat của agent, không phải trong terminal, và xem lại kết quả của mỗi bước trước khi đi tiếp.

Ví dụ này dùng cú pháp skill mặc định của GitHub Copilot. Với agent khác, hãy dùng [cú pháp gọi lệnh tương ứng](./docs/vi/integrations/cli.md#command-invocation).

```text
/speckit-constitution Tạo các nguyên tắc tập trung vào chất lượng mã, kiểm thử và khả năng bảo trì.
/speckit-specify Xây dựng ứng dụng sắp xếp ảnh, gom album theo ngày và hiển thị ảnh xem trước dạng lưới cho từng album.
/speckit-plan Dùng Vite với JavaScript thuần. Ảnh lưu cục bộ, metadata lưu trong SQLite.
/speckit-tasks
/speckit-implement
/speckit-converge
```

Lặp lại implement và converge cho đến khi bước hội tụ báo `Converged`. Về làm rõ yêu cầu, checklist và phân tích tính nhất quán, xem hướng dẫn từng bước của SDD.

[Hướng dẫn SDD từng bước](./docs/vi/quickstart.md) ·
[Tham chiếu lệnh](./docs/vi/reference/agentic-sdd.md)

<a id="-bug-fixing-with-spec-kit"></a>
<a id="bug-fix-quickstart"></a>
<a id="bug-fixing"></a>

## Sửa lỗi

Đánh giá nguyên nhân, sửa lỗi và kiểm chứng rằng triệu chứng ban đầu đã hết. Không cần chạy workflow tính năng của SDD trước.

Cài extension sửa lỗi trong terminal, từ thư mục dự án:

```bash
specify extension add bug
```

Chạy lần lượt từng skill trong khung chat của agent, không phải trong terminal, và xem lại kết quả của mỗi bước trước khi đi tiếp.

Ví dụ này dùng cú pháp skill mặc định của GitHub Copilot. Với agent khác, hãy dùng [cú pháp gọi lệnh tương ứng](./docs/vi/integrations/cli.md#command-invocation).

```text
/speckit-bug-assess "Gửi mật khẩu trống làm form đăng nhập bị crash." slug=login-crash
/speckit-bug-fix slug=login-crash
/speckit-bug-test slug=login-crash
```

Xem các báo cáo trong `.specify/bugs/login-crash/`. Kết luận cuối cùng là `verified`, `partial` hoặc `failed`; chỉ `verified` mới xác nhận lỗi đã được sửa thành công.

[Hướng dẫn sửa lỗi từng bước](./docs/vi/guides/bugfix.md) ·
[Tham chiếu lệnh](./docs/vi/reference/agentic-bugfix.md)

<a id="-assessing-ideas-with-spec-kit"></a>
<a id="idea-assessment-quickstart"></a>
<a id="idea-assessment"></a>

## Thẩm định ý tưởng

Thu thập bằng chứng để quyết định một ý tưởng có đáng theo đuổi hay không. Không cần mã nguồn hay workflow tính năng của SDD.

Cài extension thẩm định trong terminal, từ thư mục dự án:

```bash
specify extension add assess
```

Chạy lần lượt từng skill trong khung chat của agent, không phải trong terminal, và xem lại kết quả của mỗi bước trước khi đi tiếp.

Ví dụ này dùng cú pháp skill mặc định của GitHub Copilot. Với agent khác, hãy dùng [cú pháp gọi lệnh tương ứng](./docs/vi/integrations/cli.md#command-invocation).

```text
/speckit-assess-intake "Cho phép người dùng làm việc offline và đồng bộ khi có mạng trở lại." slug=offline-mode
/speckit-assess-research slug=offline-mode
/speckit-assess-define slug=offline-mode
/speckit-assess-shape slug=offline-mode
/speckit-assess-decide slug=offline-mode
```

Xem các artifact trong `.specify/assessments/offline-mode/` và quyết định cuối cùng: `go`, `needs-clarification` hoặc `kill`. Hãy giải quyết các điểm chưa rõ bằng cách sửa trực tiếp các artifact Markdown hiện có, tự tay hoặc nhờ agent, thay vì chạy lại cả một giai đoạn. Nếu bạn quyết định xây dựng một ý tưởng phần mềm đã nhận kết luận `go`, hãy lập hiến chương dự án nếu chưa có, rồi chuyển phần tóm tắt bàn giao trong `decision.md` cho `/speckit-specify`. Dừng lại với lý do được ghi chép rõ ràng cũng là một kết quả có ích.

[Hướng dẫn thẩm định từng bước](./docs/vi/guides/assessment.md) ·
[Tham chiếu lệnh](./docs/vi/reference/agentic-assessment.md)

<a id="-making-spec-kit-your-own-extensions--presets"></a>
<a id="-bundles-role-based-setups"></a>
<a id="-community"></a>

## Tùy biến hoặc dùng quy trình của riêng bạn

Tùy biến quy trình Phát triển hướng đặc tả, sửa lỗi hay thẩm định ý tưởng cho khớp với tiêu chuẩn của nhóm. Hoặc mang quy trình riêng vào mà không cần dùng quy trình nào ở trên. Kết hợp các [khả năng ở trên](#capabilities) tùy theo mục tiêu:

- Điều chỉnh một quy trình có sẵn bằng preset, ví dụ yêu cầu kế hoạch phải truy vết được theo quy định pháp lý. Với thay đổi template chỉ dùng một lần, hãy dùng ghi đè cục bộ trong dự án.
- Mang quy trình riêng vào bằng cách thêm các lệnh của nó qua một extension, rồi đưa các lệnh đó tới agent lập trình qua một integration.
- Tự động hóa lệnh và các bước kiểm tra trong một workflow. Dùng overlay để điều chỉnh workflow đã cài mà không cần fork, hoặc thêm workflow step tùy chỉnh khi các loại có sẵn chưa đủ.
- Chia sẻ một bộ thiết lập tái sử dụng được bằng cách đóng gói extension, preset, workflow và workflow step vào một bundle.

Hãy bắt đầu từ thay đổi nhỏ nhất đáp ứng được nhu cầu; bạn không cần thay cả quy trình.

[Hướng dẫn tùy biến](./docs/vi/guides/customization.md) ·
[Thành phần và hướng dẫn từ cộng đồng](./docs/vi/community/overview.md)

<a id="-specify-cli-reference"></a>
<a id="available-slash-commands"></a>
<a id="-learn-more"></a>
<a id="-core-philosophy"></a>
<a id="-development-phases"></a>
<a id="-experimental-goals"></a>
<a id="-does-spec-kit-use-spec-kit"></a>

## Tài liệu

- [Tham chiếu CLI](./docs/vi/reference/overview.md) và [các lệnh của quy trình](./docs/vi/reference/agentic-sdd.md#command-overview)
- [Triết lý SDD](./docs/vi/concepts/sdd.md), [phương pháp đầy đủ](./spec-driven.vi.md) ([bản tiếng Anh](./spec-driven.md)) và [phát triển tiếp các đặc tả đã có](./docs/vi/guides/evolving-specs.md)
- [Lịch sử dự án](./docs/vi/history.md)
- [Spec Kit dùng chính Spec Kit như thế nào](./CONTRIBUTING.md#does-spec-kit-use-spec-kit)
- [Tài liệu tiếng Việt](./docs/vi/index.md) (cài đặt, hướng dẫn nhanh, khái niệm, hướng dẫn, nâng cấp), [Bảng thuật ngữ tiếng Việt](./docs/vi/GLOSSARY.md) và [preset tiếng Việt](./presets/vi/README.md)

## Trên truyền thông

- [Open Source Friday: Spec Kit Part 2](https://www.youtube.com/watch?v=8hHCpNVLhmI) (16/10/2026) — Manfred Riem và Nicole Haugen trao đổi về Spec Kit 1.0 và bộ công cụ mở rộng.
- [Open Source Friday with Spec Kit](https://www.youtube.com/watch?v=2IArMAhkJcE) (08/05/2026) — Giới thiệu và demo SDD cùng Manfred Riem.

## Lịch sử star

<p align="center">
    <a href="https://www.star-history.com/#github/spec-kit&Date">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=github%2Fspec-kit&type=Date&theme=dark"/>
            <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=github%2Fspec-kit&type=Date"/>
            <img src="https://api.star-history.com/svg?repos=github%2Fspec-kit&type=Date" alt="Biểu đồ lịch sử star của Spec Kit"/>
        </picture>
    </a>
</p>

<p align="center">
    <em>Cảm ơn tất cả những ai đã góp sức giúp Spec Kit tỏa sáng.</em>
</p>

<a id="-support"></a>

## Hỗ trợ và đóng góp

[Báo lỗi hoặc đề xuất tính năng](https://github.com/github/spec-kit/issues/new) ·
[Hướng dẫn đóng góp](./CONTRIBUTING.md) · [Quy tắc ứng xử](./CODE_OF_CONDUCT.md)

<a id="-license"></a>

Spec Kit được phát hành theo [giấy phép MIT](./LICENSE).
