<a id="customize-spec-kit"></a>

# Tùy biến Spec Kit

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../guides/customization.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Ba quy trình chính thức (first-party) là điểm khởi đầu, không phải giới hạn. Hãy giữ
quy trình SDD có sẵn, thêm sửa lỗi hoặc đánh giá ý tưởng, điều chỉnh quy trình cho phù hợp với
tổ chức của bạn, hoặc mang vào một quy trình hoàn toàn khác.

<a id="choose-the-right-building-block"></a>

## Chọn đúng thành phần

| Mục tiêu | Dùng |
| --- | --- |
| Kết nối Spec Kit với một agent lập trình hoặc điều chỉnh cách phân phối lệnh/skill của nó | Integration |
| Thêm lệnh, khả năng hoặc quy trình mới | Extension |
| Tích hợp công cụ hoặc dịch vụ bên ngoài | Extension |
| Thay đổi định dạng hoặc thuật ngữ của đặc tả, kế hoạch hay danh sách tác vụ | Preset |
| Áp các tiêu chuẩn của tổ chức hoặc quy định pháp lý vào template hiện có | Preset |
| Phân phối template chuyên ngành dùng lại được | Preset cho việc ghi đè; extension cho template đi kèm lệnh mới |
| Điều chỉnh template một lần trong một dự án | Ghi đè cục bộ trong dự án |
| Tự động hóa một quy trình nhiều bước | Workflow |
| Thêm loại step thực thi tùy chỉnh cho workflow | Workflow step package |
| Thiết lập trọn bộ theo vai trò chỉ trong một thao tác | Bundle |

Integration quyết định cách lệnh và skill được đưa tới agent lập trình
của bạn; chúng khác với extension, vốn kết nối tới công cụ hoặc
dịch vụ bên ngoài. Xem [hướng dẫn integration](../../integrations/index.md) để biết các
agent được hỗ trợ và cách thiết lập, hoặc [đóng góp integration](../../integrations/contributing.md)
để phát triển một adapter.

Workflow step package mở rộng các loại step mà workflow có thể dùng. Xem
[custom step package](../../reference/workflows.md#custom-step-packages) để biết cách
cài đặt và thực thi, và
[workflow step của cộng đồng](../../community/workflow-steps.md) để tìm kiếm và nhận
hướng dẫn đóng góp. Hãy review các package thực thi được trước khi cài hoặc dùng chúng.

<a id="extensions-add-capabilities"></a>

## Extension: thêm khả năng

Extension mở rộng **những gì Spec Kit làm được** thông qua lệnh, template, script
và hook. Chúng có thể thêm quy trình chuyên ngành, tích hợp bên ngoài hoặc
các giai đoạn phát triển ngoài phần lõi.

```bash
specify extension search
specify extension add <extension-name>
```

Ví dụ gồm tích hợp Jira, review code sau khi triển khai, truy vết test theo V-Model
và chẩn đoán sức khỏe dự án. Các extension đi kèm
[bug](bugfix.md) và [assess](assessment.md) là ví dụ chính thức.
Duyệt [extension của cộng đồng](../../community/extensions.md), hoặc dùng
[tài liệu tham khảo extension](../../reference/extensions.md) để biết cách quản lý và cấu hình.

<a id="presets-change-how-a-process-works"></a>

## Preset: thay đổi cách một quy trình vận hành

Preset ghi đè template và lệnh do phần lõi **và các extension đã cài**
cung cấp. Chúng tùy chỉnh artifact và chỉ dẫn được tạo ra mà không
cần công cụ mới.

```bash
specify preset search
specify preset add <preset-name>
```

Hãy dùng preset để yêu cầu truy vết theo quy định pháp lý, áp thứ tự tác vụ test trước,
thêm cổng review bảo mật vào kế hoạch, hoặc bản địa hóa một quy trình. Preset cũng có thể điều chỉnh
phương pháp luận theo Agile, Kanban, Waterfall, jobs-to-be-done hoặc domain-driven
design.
[Bản demo giọng cướp biển](https://github.com/mnriem/spec-kit-pirate-speak-preset-demo)
cho thấy thuật ngữ có thể được thay đổi sâu rộng đến mức nào.

Nhiều preset có thể xếp chồng lên nhau theo độ ưu tiên. Xem
[preset của cộng đồng](../../community/presets.md) để có ví dụ và
[tài liệu tham khảo preset](../../reference/presets.md) để biết cách cài đặt, các chiến lược
kết hợp và thứ tự ưu tiên.

<a id="project-local-overrides-and-resolution"></a>

## Ghi đè cục bộ trong dự án và thứ tự phân giải

Với tùy chỉnh chỉ dùng một lần cho dự án, hãy đặt template ghi đè trong
`.specify/templates/overrides/` thay vì tạo một preset dùng lại được.
Thứ tự thay thế mặc định là:

1. Ghi đè cục bộ trong dự án.
2. Các preset đã cài, theo thứ tự ưu tiên.
3. Các extension đã cài, theo thứ tự ưu tiên.
4. Template lõi của Spec Kit trong `.specify/templates/`.

Template được phân giải khi cần, mặc định lấy kết quả khớp đầu tiên.
Lệnh thì khác: việc cài extension hoặc preset sẽ ghi file lệnh
vào thư mục của integration đang dùng. Agent không phân giải lại
chồng đó mỗi lần gọi lệnh. Gỡ một thành phần đang ghi đè
sẽ khôi phục lớp lệnh còn lại thông qua bước đồng bộ lại.

Khi không có tùy chỉnh nào, các giá trị mặc định của phần lõi được áp dụng.
[Tài liệu tham khảo về phân giải file](../../reference/presets.md#file-resolution) là
hướng dẫn chính thức về đường dẫn, độ ưu tiên và cách kết hợp prepend/append/wrap.

<a id="bundles-role-based-setups"></a>

## Bundle: thiết lập theo vai trò

Bundle đóng gói một tập extension, preset, workflow và workflow
step được tuyển chọn thành một thiết lập có phiên bản cho một vai trò hoặc một nhóm. Manifest `bundle.yml` của nó ghim
các thành phần và có thể nhắm tới một integration; bundle không gắn với integration nào sẽ dùng
integration đang hoạt động của dự án.

```bash
specify bundle search
specify bundle info <bundle-id>
specify bundle install <bundle-id>
```

Xem `info` trước khi cài để biết tập thành phần sau khi phân giải. Xem
[tài liệu tham khảo bundle](../../reference/bundles.md) để biết về cập nhật, gỡ bỏ, chính sách catalog,
giới hạn khi offline, kiểm định và phát hành, và
[các manifest mẫu](https://github.com/github/spec-kit/tree/main/examples/bundles)
cho các thiết lập dành cho product manager, business analyst, nhà nghiên cứu bảo mật và lập trình viên.

<a id="share-your-customizations"></a>

## Chia sẻ tùy chỉnh của bạn

Các thành phần cộng đồng được duy trì độc lập. Hãy review mã nguồn trước khi
cài và tự cân nhắc khi sử dụng. Truy cập
[hướng dẫn cộng đồng](../../community/overview.md) để tìm thành phần hoặc phát hành thành phần
của riêng bạn, và [tài liệu tham khảo workflow](../../reference/workflows.md) để tự động hóa một quy trình.
