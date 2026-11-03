<a id="catalogs"></a>

# Catalog

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/catalogs.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Catalog là các chỉ mục giúp Specify tìm integration, extension, preset, workflow, loại workflow step và bundle. Spec Kit có các catalog có sẵn, gồm cả catalog cộng đồng khi có, và cho phép dự án hoặc người dùng thêm nguồn catalog riêng tư.

Catalog không phải một registry dùng chung cho mọi loại thành phần. Mỗi loại thành phần có schema catalog, nhóm lệnh, cấu hình và chồng phân giải riêng. Một tổ chức tuyển chọn nhiều loại thành phần thường công bố một file catalog cho mỗi loại.

<a id="discover-components"></a>

## Tìm thành phần

Tìm kiếm dùng mọi catalog đang hoạt động của loại thành phần đó:

```bash
specify integration search <query>
specify extension search <query>
specify preset search <query>
specify workflow search <query>
specify workflow step search <query>
specify bundle search <query>
```

Dùng chế độ xem phiên bản tương ứng để xem các bản phát hành được công bố:

```bash
specify integration info <id> --versions
specify extension info <id> --versions
specify preset info <id> --versions
specify workflow info <id> --versions
specify workflow step info <id> --versions
specify bundle info <id> --versions
```

Đầu ra `info` thông thường và chi tiết hiển thị bởi `--versions` khác nhau tùy loại thành phần. Chế độ xem phiên bản liệt kê các bản phát hành hiện tại và lịch sử trong catalog và, khi được hỗ trợ, gắn nhãn nguồn thắng là cài được hay chỉ dùng để tìm kiếm. Bản phát hành chỉ dùng để tìm kiếm vẫn không cài được theo ID kể cả khi xuất hiện trong danh sách phiên bản. Dùng lệnh `catalog list` của thành phần để xác nhận nguồn đang hoạt động và chính sách cài đặt thay vì dựa vào đầu ra `info` thông thường.

Bạn cũng có thể duyệt các danh sách cộng đồng được duy trì cho [extension](../../community/extensions.md), [preset](../../community/presets.md), [bundle](../../community/bundles.md) và [loại workflow step](../../community/workflow-steps.md).

<a id="inspect-and-manage-catalog-sources"></a>

## Xem và quản lý nguồn catalog

Liệt kê chồng catalog đang hoạt động trước khi cài thành phần từ một dự án lạ:

| Loại thành phần | Liệt kê catalog đang hoạt động | Tài liệu tham khảo chi tiết |
| --- | --- | --- |
| Integration | `specify integration catalog list` | [Integration](../integrations/cli.md#catalog-management) |
| Extension | `specify extension catalog list` | [Extension](extensions.md#catalog-management) |
| Preset | `specify preset catalog list` | [Preset](presets.md#catalog-management) |
| Workflow | `specify workflow catalog list` | [Workflow](workflows.md#catalog-management) |
| Workflow step | `specify workflow step catalog list` | [Workflow](workflows.md#catalog-management) |
| Bundle | `specify bundle catalog list` | [Bundle](bundles.md#manage-catalog-sources) |

Mỗi nhóm lệnh cũng có `catalog add` và `catalog remove`. Tùy chọn, định danh, chính sách cài đặt và tên file cấu hình khác nhau tùy loại thành phần, nên hãy xem tài liệu tham khảo được liên kết trước khi thay đổi chồng catalog.

Phạm vi và thứ tự ưu tiên của catalog dùng hai mô hình:

- **Integration, extension, preset, workflow và workflow step** chọn một lớp cấu hình. Biến môi trường ghi đè thay thế mọi thứ; nếu không, file catalog dự án thay thế lớp người dùng và lớp có sẵn, file người dùng thay thế lớp có sẵn, và catalog có sẵn chỉ được dùng khi không có lớp cao hơn nào được cấu hình. Trong lớp được chọn, các mục được sắp theo priority dạng số. Vì vậy, thêm catalog dự án đầu tiên sẽ loại các nguồn có sẵn khỏi chồng đang hoạt động, trừ khi bạn liệt kê cả các nguồn đó trong file dự án.
- **Bundle** gộp các nguồn có sẵn, người dùng và dự án theo ID nguồn. Định nghĩa ở phạm vi cao hơn thay thế nguồn ở phạm vi thấp hơn có cùng ID, rồi mọi nguồn còn lại được sắp theo priority dạng số. Nguồn dự án không tự động xếp trên một nguồn có sẵn có tên khác.

Trong các catalog được nạp thành công, mục có độ ưu tiên cao hơn cung cấp một định danh sẽ thắng. Một số trình đọc thành phần bỏ qua các lỗi tải thông thường và tiếp tục với các nguồn còn lại, nên một nguồn ưu tiên cao không truy cập được có thể khiến nguồn ưu tiên thấp hơn phân giải cùng định danh. Đừng coi độ ưu tiên của nguồn là một cơ chế kiểm soát bảo mật kiểu fail-closed.

<a id="discovery-and-trust"></a>

## Tìm kiếm và độ tin cậy

Việc được liệt kê trong catalog không phải là kiểm định hay bảo chứng. Catalog có thể là:

- **Install-allowed**: nguồn bạn tin cậy để cài đặt theo ID thành phần.
- **Discovery-only**: tìm kiếm được để đánh giá, nhưng bị chặn cài đặt theo ID qua catalog đó.

Chính sách discovery-only không chặn việc cài trực tiếp từ nguồn được yêu cầu riêng, như URL `--from` hoặc đường dẫn `--dev` được hỗ trợ. Hãy review nguồn đó một cách độc lập trước khi dùng con đường cài trực tiếp.

Catalog cộng đồng là bề mặt để tìm kiếm và nên giữ ở chế độ discovery-only. Hãy review mã nguồn và artifact phát hành của một thành phần trước khi dùng. Để dùng lại các thành phần đã review trong cả nhóm, hãy sao chép các mục đã thẩm định vào một catalog do tổ chức của bạn kiểm soát thay vì chuyển một catalog công khai chưa thẩm định sang install-allowed.

Cấu hình catalog của dự án cũng là đầu vào không đáng tin cậy. Một repository có thể thêm hoặc ưu tiên các nguồn catalog trong `.specify/`, nhưng sự hiện diện của cấu hình đó không có nghĩa là các nguồn hay thành phần của nó đã được phê duyệt. Hãy chạy lệnh `catalog list` tương ứng và kiểm tra mọi nguồn install-allowed trước khi cài hoặc chạy thành phần từ một dự án lạ.

<a id="host-a-private-catalog"></a>

## Lưu trữ catalog riêng tư

1. Review và phê duyệt các mục và artifact phát hành trước khi đăng ký một nguồn install-allowed.
2. Chọn loại thành phần và làm theo schema catalog hoặc hướng dẫn phát hành của nó.
3. Công bố JSON catalog tại một URL HTTPS mà người dùng dự kiến truy cập được.
4. Thêm URL đó bằng lệnh `catalog add` của thành phần.
5. Xác nhận nguồn, thứ tự ưu tiên và chính sách cài đặt kết quả bằng `catalog list`.

Mặc định về độ tin cậy của `catalog add` khác nhau tùy loại thành phần:

| Loại thành phần | Mặc định khi thêm |
| --- | --- |
| Integration | Install-allowed |
| Extension | Discovery-only; cần `--install-allowed` để cho phép cài đặt |
| Preset | Discovery-only; cần `--install-allowed` để cho phép cài đặt |
| Workflow | Install-allowed |
| Workflow step | Install-allowed |
| Bundle | Install-allowed; dùng `--policy discovery-only` để giới hạn |

Vì việc thêm integration, workflow, workflow step và bundle có thể cho phép cài đặt ngay lập tức, đừng đăng ký một nguồn chưa review với ý định phê duyệt sau.

Dùng hướng dẫn phát hành riêng của từng thành phần khi viết mục catalog:

| Loại thành phần | Hướng dẫn phát hành |
| --- | --- |
| Integration | [Đóng góp vào catalog integration](../integrations/contributing.md) |
| Extension | [Hướng dẫn phát hành extension](../extensions/publishing.md) |
| Preset | [Hướng dẫn phát hành preset](https://github.com/github/spec-kit/blob/main/presets/PUBLISHING.md) |
| Workflow | [Hướng dẫn phát hành workflow](https://github.com/github/spec-kit/blob/main/workflows/PUBLISHING.md) |
| Workflow step | [Loại workflow step của cộng đồng](../../community/workflow-steps.md) |
| Bundle | [Bundle của cộng đồng](../../community/bundles.md) |

Ví dụ, một catalog extension đã review có thể được đăng ký bằng:

```bash
specify extension catalog add https://catalog.example.com/extensions.json \
  --name approved-extensions \
  --priority 5 \
  --install-allowed
```

Dùng các file catalog và lệnh riêng cho preset, integration, workflow, workflow step và bundle. Tài liệu tham khảo chi tiết của chúng mô tả các tùy chọn được hỗ trợ và định dạng mục mong đợi.

<a id="private-and-offline-environments"></a>

## Môi trường riêng tư và offline

Nếu catalog hoặc việc tải thành phần của nó cần thông tin xác thực, hãy cấu hình [xác thực catalog và tải về](authentication.md). Xác thực là tùy chọn chủ động và chỉ áp dụng cho các host được cấu hình rõ ràng.

Phía sau tường lửa, hãy lưu trữ catalog và artifact trên các endpoint HTTPS nội bộ đã được phê duyệt và thêm các endpoint đó vào chồng catalog tương ứng. Trong môi trường hoàn toàn mất kết nối, hãy chuyển CLI và các artifact thành phần đã review qua quy trình được phê duyệt của bạn; tài nguyên có sẵn vẫn dùng được khi không có mạng. Xem [Cài đặt cho doanh nghiệp / air-gapped](../install/air-gapped.md) để cài CLI offline.

Adapter integration bên ngoài không có con đường cài trực tiếp hay cục bộ. Cài một adapter như vậy cần cả catalog integration install-allowed lẫn archive mà nó tham chiếu luôn truy cập được. Xem [Adapter bên ngoài cài từ catalog](../integrations/cli.md#catalog-installed-external-adapters).

Chỉ metadata catalog thì chưa đủ để cài offline: mọi artifact phát hành được chọn và mọi phụ thuộc do bundle cung cấp cũng phải truy cập được hoặc được chuyển vào môi trường.
