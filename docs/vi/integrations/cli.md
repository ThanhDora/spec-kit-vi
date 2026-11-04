<a id="integration-cli-reference"></a>

# Tài liệu tham khảo CLI integration

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/cli.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Tài liệu này mô tả các lệnh `specify integration` dùng chung, việc quản lý catalog và hành vi trong vòng đời integration. Để biết thiết lập, đường dẫn cài đặt, tùy chọn và giới hạn riêng của từng agent, hãy bắt đầu từ [hướng dẫn integration](index.md).

Chạy các lệnh này trong một dự án đã khởi tạo bằng `specify init`. Với dự án mới, dùng `specify init <project> --integration <key>`.

<a id="supported-ai-coding-agents"></a>

## Các agent lập trình AI được hỗ trợ

[Danh mục integration](index.md#choose-an-integration) liệt kê các agent được hỗ trợ cùng khóa chính xác của chúng, mỗi integration có một hướng dẫn riêng. Chạy `specify integration list` để xem những gì có sẵn trên máy.

<a id="command-invocation"></a>

## Cách gọi lệnh

Gọi các bước quy trình của Spec Kit bên trong agent lập trình, không phải trong terminal. Ở chế độ mặc định của GitHub Copilot, đây là các skill bạn gọi trong khung chat của agent. Các lệnh cài đặt và thiết lập CLI là thao tác terminal riêng. Các bước giống nhau ở mọi integration, nhưng cách viết tùy thuộc vào agent và chế độ đã cài:

| Integration hoặc chế độ | Ví dụ SDD | Ví dụ extension |
| --- | --- | --- |
| GitHub Copilot, chế độ skills mặc định | `/speckit-specify` | `/speckit-bug-assess` |
| Ký pháp slash command dấu chấm dùng trong tài liệu tham khảo | `/speckit.specify` | `/speckit.bug.assess` |
| Skill của Codex, Command Code, ZCode | `$speckit-specify` | `$speckit-bug-assess` |
| Skill của Kimi | `/skill:speckit-specify` | `/skill:speckit-bug-assess` |

Hãy dùng dạng mà agent của bạn cung cấp. Xem [hướng dẫn GitHub Copilot](copilot.md) để biết bố cục skills và commands của nó, hoặc chọn agent khác từ [danh mục integration](index.md).

<a id="list-available-integrations"></a>

## Liệt kê các integration có sẵn

```bash
specify integration list
```

| Tùy chọn | Mô tả |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- |
| `--catalog` | Duyệt cả catalog, bao gồm các integration bên ngoài chưa được cài trong dự án này. |

Hiển thị các integration có sẵn và các integration bên ngoài đã cài và được tin cậy, yêu cầu thiết lập của chúng và khai báo an toàn khi cài nhiều integration. Integration đã cài và integration mặc định được đánh dấu riêng. Cột `CLI Required` cho biết yêu cầu CLI của agent được khai báo bởi `config.requires_cli`, không cho biết integration có chỉ chạy trong IDE hay không. Adapter bên ngoài có thể yêu cầu riêng các file thực thi qua `requires.tools` trong file mô tả; quá trình cài đặt và `specify check` kiểm tra các yêu cầu công cụ đó kể cả khi `CLI Required` là `no`.

<a id="search-available-integrations"></a>

## Tìm kiếm integration

```bash
specify integration search [query]
```

| Tùy chọn | Mô tả |
| ---------- | ------------------ |
| `--tag` | Lọc theo tag |
| `--author` | Lọc theo tác giả |

Tìm trong chồng catalog đang hoạt động. Khi không có từ khóa, liệt kê mọi integration có sẵn.

<a id="integration-info"></a>

## Thông tin integration

```bash
specify integration info <integration_id>
specify integration info <integration_id> --versions
```

Hiển thị metadata catalog của một integration, catalog nguồn và việc integration đó có đang hoạt động hay không. `--versions` liệt kê các phiên bản hiện tại và lịch sử được công bố trong catalog được chọn, bản hiện tại đứng đầu và các bản cũ hơn xếp theo phiên bản giảm dần. Nguồn chỉ dùng để tìm kiếm được gắn nhãn tương ứng.

<a id="install-an-integration"></a>

## Cài một integration

```bash
specify integration install <key>
```

| Tùy chọn | Mô tả |
| ------------------------ | ------------------------------------------------------------------------ |
| `--script sh\|ps\|py` | Loại script: `sh` (bash/zsh), `ps` (PowerShell) hoặc `py` (Python) |
| `--force` | Chủ động cho phép cài cạnh các integration không được khai báo an toàn khi cài nhiều integration |
| `--integration-options` | Tùy chọn riêng của integration (ví dụ `--integration-options="--commands-dir .myagent/cmds"`) |
| `--trust-integration` | Sau khi review code, cho phép trước việc thực thi Python của adapter bên ngoài mà không cần hỏi xác nhận tin cậy tương tác |

Cài integration vào dự án hiện tại. Việc cài nhiều integration chỉ tự động tiến hành khi mọi integration liên quan đều được khai báo an toàn. Nếu không, dùng `switch` để thay integration mặc định hoặc `--force` để chủ động cho phép cài nhiều integration. Thiết lập thất bại sẽ kích hoạt rollback.

**Lịch sử catalog chỉ là metadata.** `integration install` vẫn phân giải trực tiếp các phần triển khai có sẵn đã đăng ký, hoặc bản phát hành adapter bên ngoài hiện tại từ một catalog cho phép cài đặt, chứ không dùng các bản ghi lịch sử của catalog. Không có `integration install --version`. Catalog cộng đồng mặc định vẫn chỉ dùng để tìm kiếm.

Cài thêm một integration không làm thay đổi integration mặc định. Dùng `specify integration use <key>` để đổi integration mặc định.

Extension và preset chỉ đi theo integration mặc định. Dùng `use <key>` hoặc `switch <key>` để kích hoạt integration khác và đăng ký lệnh của chúng cho integration đó.

<a id="catalog-installed-external-adapters"></a>

### Adapter bên ngoài cài từ catalog

Đăng ký một catalog đã review trong dự án đã khởi tạo, rồi cài adapter của nó:

```bash
specify integration catalog add https://example.com/catalog.json --name samples
specify integration install sample-agent
specify integration use sample-agent
```

Quá trình cài đặt hỏi xác nhận tin cậy **trước khi** tải/import Python. Để tự động hóa, hãy cho phép rõ ràng code mà bạn đã review:

```bash
specify integration install sample-agent --trust-integration
specify integration upgrade sample-agent --trust-integration
```

Nguồn phải có `install_allowed: true`. Catalog cộng đồng mặc định chỉ dùng để tìm kiếm; cả `--force` lẫn cờ trust đều không vượt qua được chính sách đó. Các thao tác list/search/info trên catalog không import code của catalog. Xem [schema của catalog](catalog.md#catalog-schema) để biết metadata bắt buộc và các URL archive được hỗ trợ. Search gợi ý `specify integration install <id>` cho các nguồn cho phép cài đặt; kết quả từ nguồn chỉ dùng để tìm kiếm thì không gợi ý cài đặt.

`specify check` dò các công cụ bắt buộc trong file mô tả của adapter bên ngoài thay vì ID catalog của nó. Khi không khai báo công cụ bắt buộc nào, adapter CLI được kiểm tra bằng file thực thi lúc chạy của nó; công cụ tùy chọn không gây lỗi thiếu công cụ. Các kiểm tra này không chạy file thực thi và không gọi các phép dò phiên bản chung.

Code adapter đã cài được lưu riêng với các file agent được sinh ra. Các tiến trình CLI mới nạp package đã tin cậy mà không tra cứu catalog. Code bị thiếu, bị sửa hoặc không tương thích là lỗi, chứ không âm thầm chuyển sang phương án dự phòng. Upgrade tải phiên bản hiện tại trong catalog; uninstall gỡ package nhưng mặc định giữ lại các file được sinh ra đã bị sửa. Các lệnh chỉ đọc metadata `workflow status` và `workflow info` vẫn dùng được mà không cần nạp code adapter, kể cả khi adapter đã cài bị hỏng. Việc thực thi và tiếp tục workflow vẫn báo rõ lỗi khi nạp adapter.

Sự đồng ý cho thực thi là cục bộ theo người dùng và gắn với dự án, integration và nội dung package đã xác minh. Sao chép metadata dự án không chuyển giao sự đồng ý. Sau khi sao chép dự án hoặc đổi người dùng, hãy review adapter và cấp lại quyền từ một catalog cho phép cài đặt:

```bash
specify integration upgrade sample-agent --force --trust-integration
```

Gỡ cài đặt cưỡng bức vẫn hoạt động khi code package không được tin cậy hoặc toàn bộ thư mục của nó bị mất; lệnh này không import code đó.

Khi khởi tạo, một catalog dự án/người dùng hoặc `SPECKIT_INTEGRATION_CATALOG_URL` có thể cung cấp adapter bên ngoài:

```bash
specify init my-project --integration sample-agent --trust-integration
```

Hãy review [API adapter bên ngoài](https://github.com/github/spec-kit/blob/main/design/integration.md#external-adapter-package-contract) trước khi phát hành package. Adapter chỉ dùng API của host và thư viện chuẩn thì không cần cài bằng pip hay sửa source registry.

Nếu CLI của bạn từ chối cài nhiều integration, hãy kiểm tra `specify version` và làm theo [hướng dẫn nâng cấp](../upgrade.md). Một lần gọi `uvx` dùng một lần không cập nhật file thực thi `specify` lâu dài trên `PATH` của bạn.

<a id="uninstall-an-integration"></a>

## Gỡ một integration

```bash
specify integration uninstall [<key>]
```

| Tùy chọn | Mô tả |
| --------- | --------------------------------------------------- |
| `--force` | Xóa file kể cả khi chúng đã bị sửa |

Gỡ integration được chỉ định, hoặc integration mặc định nếu không truyền khóa. Các file được sinh ra theo dõi bằng manifest dùng hash nội dung để dọn dẹp:

- **File chưa sửa** được xóa tự động.
- **File đã sửa** (nơi bạn đã chỉnh tay) được giữ lại để không mất các tùy biến của bạn.
- Dùng `--force` để xóa cả file được theo dõi đã bị sửa.

Đây là quy tắc cho các file được sinh ra theo dõi bằng manifest. Việc dọn dẹp riêng của từng integration có thể khác: [Skill toàn cục của Hermes](hermes.md#global-ownership-and-removal) và [skill kiểu cũ của Kimi](kimi.md#legacy-cleanup-on-uninstall) có thể bị xóa mà không được bảo vệ như file đã sửa. Hãy đọc hướng dẫn của agent trước khi gỡ hoặc chuyển sang integration khác.

Uninstall cũng gỡ các artifact extension và preset đã đăng ký cho integration; bản thân các extension và preset vẫn được giữ cài đặt. Gỡ integration mặc định sẽ chọn một integration còn lại và đăng ký các đóng góp đang bật cho nó. Gỡ integration cuối cùng không tự động cài `none`.

<a id="switch-to-a-different-integration"></a>

## Chuyển sang integration khác

```bash
specify integration switch <key>
```

| Tùy chọn | Mô tả |
| ------------------------ | ------------------------------------------------------------------------ |
| `--script sh\|ps\|py` | Loại script: `sh` (bash/zsh), `ps` (PowerShell) hoặc `py` (Python) |
| `--force` | Buộc xóa file đã sửa khi gỡ cài đặt; khi đích đã được cài, ghi đè template dùng chung được quản lý trong lúc đổi mặc định |
| `--refresh-shared-infra` | Ghi đè cả file hạ tầng dùng chung dù bạn đã tùy biến chúng (nếu không, các tùy biến được giữ lại) |
| `--integration-options` | Tùy chọn cho integration đích khi nó chưa được cài |
| `--trust-integration` | Cho phép tải và thực thi một adapter bên ngoài đã review mà không cần hỏi xác nhận tin cậy tương tác |

- **Đích chưa được cài:** gỡ integration mặc định hiện tại, cài đích và đặt nó làm mặc định. Các integration đã cài khác vẫn được giữ.
- **Đích đã được cài:** đổi mặc định mà không gỡ integration nào, giống `use`. Để đổi tùy chọn thiết lập của nó, trước hết chạy `upgrade <key> --integration-options ...`, rồi `use <key>`; `switch` từ chối tùy chọn thiết lập với đích đã cài.

Cả hai trường hợp đều đăng ký các extension và preset đang bật cho integration mặc định mới. Xem bảng tùy chọn để biết các ý nghĩa khác nhau của `--force`.

Khi chuyển sang một adapter bên ngoài cần được tải và cài, chỉ dùng `--trust-integration` sau khi đã review code của nó:

```bash
specify integration switch sample-agent --trust-integration
```

Chuyển sang adapter đã cài vẫn kiểm tra lại độ tin cậy hiện có của nó. Cờ này không bỏ qua việc kiểm tra đó, cũng không bỏ qua chính sách chỉ tìm kiếm của catalog. Xem [adapter bên ngoài cài từ catalog](#catalog-installed-external-adapters) để biết các yêu cầu về độ tin cậy.

<a id="use-an-installed-integration"></a>

## Dùng một integration đã cài

```bash
specify integration use <key>
```

| Tùy chọn | Mô tả |
| --------- | --------------------------------------------------- |
| `--force` | Ghi đè template dùng chung được quản lý trong lúc đổi mặc định |

Đặt integration mặc định mà không gỡ integration đã cài nào khác. Lệnh này cũng làm mới template dùng chung được quản lý để tham chiếu lệnh khớp với kiểu gọi của integration mặc định mới. Template dùng chung đã sửa hoặc không được theo dõi sẽ được giữ, trừ khi dùng `--force`.

Nó cũng đăng ký lệnh hoặc skill của extension và preset đang bật cho integration mặc định mới, kể cả những đóng góp được cài khi một integration khác đang hoạt động.

<a id="upgrade-an-integration"></a>

## Nâng cấp một integration

```bash
specify integration upgrade [<key>]
```

| Tùy chọn | Mô tả |
| ------------------------ | ------------------------------------------------------------------------ |
| `--force` | Ghi đè file kể cả khi chúng đã bị sửa |
| `--script sh\|ps\|py` | Loại script: `sh` (bash/zsh), `ps` (PowerShell) hoặc `py` (Python) |
| `--integration-options` | Tùy chọn cho integration |
| `--trust-integration` | Cho phép tải/import adapter bên ngoài thay thế đã được review |

Cài lại một integration đã cài với template và lệnh đã cập nhật (ví dụ sau khi nâng cấp Spec Kit). Mặc định là integration mặc định; nếu truyền khóa, khóa đó phải là một trong các integration đã cài. Phát hiện file đã sửa cục bộ và chặn việc nâng cấp, trừ khi dùng `--force`. File cũ từ lần cài trước không còn cần đến sẽ được xóa tự động. Template dùng chung vẫn khớp với integration mặc định, kể cả khi nâng cấp một integration không phải mặc định.

Extension và preset đang bật chỉ được đăng ký lại khi nâng cấp integration đang hoạt động (mặc định). Nâng cấp một integration không phải mặc định vẫn làm mới các lệnh lõi của nó, nhưng không đăng ký lại lớp extension hay preset — hãy `use`/`switch` integration đó sau đó để dựng lại chúng.

Nếu thiếu manifest của các file được sinh ra, upgrade báo không có gì để nâng cấp và giữ nguyên package adapter đã cài, các file được sinh ra và bản ghi quyền sở hữu phục vụ khôi phục cục bộ, kể cả khi dùng `--force`. Code thay thế chỉ được lưu sau khi upgrade sinh lại thành công các file được quản lý.

Nếu một lần nâng cấp sẽ đổi integration giữa bố cục commands và skills trong khi có artifact preset đã đăng ký cho nó, việc nâng cấp bị từ chối trước khi thay đổi file. Hãy gỡ các preset bị ảnh hưởng, chạy bản nâng cấp đổi bố cục, rồi cài lại chúng.

Với adapter bên ngoài, upgrade hoặc uninstall cưỡng bức có thể khôi phục package bị hỏng hoặc không nạp được nhờ các bản ghi quyền sở hữu cục bộ theo người dùng. Không có bằng chứng đó, các file được sinh ra chỉ thuộc bản cũ sẽ được giữ lại kèm cảnh báo cần dọn dẹp thủ công. Việc khôi phục giữ lại các trình phân phối event dùng chung và các thiết lập chỉ sở hữu một phần; một bản thay thế đáng tin cậy vẫn có thể ghi đè các đích đã khai báo của nó khi chạy `upgrade --force`. Việc khôi phục không bỏ qua chính sách catalog hay độ tin cậy của package thay thế.

Thao tác thất bại chỉ rollback các thay đổi của chính nó, không đụng đến file không liên quan của người dùng hay tiến độ workflow. Các chỉnh sửa đồng thời xung đột được báo cáo, và các snapshot khôi phục được giữ lại. Tác giả adapter nên tuân theo [hợp đồng về lưu trữ, nạp và vòng đời](https://github.com/github/spec-kit/blob/main/design/integration.md#storage-loading-and-lifecycle) về các yêu cầu quyền sở hữu, ghi nhật ký và khôi phục.

<a id="report-integration-status"></a>

## Báo cáo trạng thái integration

```bash
specify integration status
specify integration status --json
```

Báo cáo trạng thái integration của dự án hiện tại mà không thay đổi file. Báo cáo trạng thái gồm integration mặc định, các integration đã cài, độ an toàn khi cài nhiều integration, file được quản lý bị thiếu, file được quản lý đã sửa, đường dẫn manifest không hợp lệ, tình trạng hạ tầng Spec Kit dùng chung, manifest chưa được kiểm tra, và integration đích cho các template dùng chung phụ thuộc vào mặc định. Dạng JSON dành cho CI và agent lập trình cần dữ liệu trạng thái ổn định, máy đọc được; nó cũng báo các integration được ghi nhận nguyên gốc và các manifest integration đã được kiểm tra khi heuristic sửa trạng thái khác với file đã ghi nhận. Lệnh thoát với mã 0 khi trạng thái báo cáo là `ok` hoặc `warning`; chỉ thoát với mã 1 khi trạng thái là `error`. Trong đầu ra JSON, `multi_install_safe` là `null` khi không thể đánh giá tập integration đã cài nào, chẳng hạn khi trạng thái integration bị thiếu, không đọc được, không có danh sách integration ghi nhận hợp lệ, hoặc không ghi nhận integration nào đã cài.

<a id="catalog-management"></a>

## Quản lý catalog

Catalog integration quyết định nơi các lệnh tìm kiếm (`search` và `info`) tìm integration. Các catalog được kiểm tra theo thứ tự ưu tiên.

Quản lý catalog, `integration list --catalog` và `integration info` không thực thi code adapter. Việc liệt kê, thiết lập, chọn, xem trạng thái, đăng ký integration thông thường và điều phối workflow đều nạp các phần triển khai đã cài và được tin cậy.

<a id="list-catalogs"></a>

### Liệt kê catalog

```bash
specify integration catalog list
```

Hiển thị các nguồn catalog đang hoạt động. Nguồn cấp dự án (khi đã cấu hình) có thể gỡ theo chỉ số; nếu không, các nguồn đang hoạt động được hiển thị là không gỡ được.

<a id="add-a-catalog"></a>

### Thêm catalog

```bash
specify integration catalog add <url>
```

| Tùy chọn | Mô tả |
| --------------- | ----------------------------- |
| `--name <name>` | Tên tùy chọn cho catalog |

Thêm một URL catalog tùy chỉnh vào `.specify/integration-catalogs.yml` của dự án. URL phải dùng HTTPS (trừ `http://localhost`, `http://127.0.0.1` hoặc `http://[::1]` để kiểm thử cục bộ).

Thêm lại cùng URL với cùng tên sẽ thành công mà không đổi cấu hình; tên khác sẽ bị từ chối.

<a id="remove-a-catalog"></a>

### Gỡ catalog

```bash
specify integration catalog remove <index>
```

Gỡ một nguồn catalog dự án theo chỉ số bắt đầu từ 0 trong `catalog list`.

<a id="catalog-resolution-order"></a>

### Thứ tự phân giải catalog

Lớp được cấu hình đầu tiên thay thế các lớp thấp hơn. Trong lớp đó, giá trị priority nhỏ hơn được ưu tiên:

1. **Biến môi trường** — `SPECKIT_INTEGRATION_CATALOG_URL` ghi đè mọi catalog
2. **Cấu hình dự án** — `.specify/integration-catalogs.yml`
3. **Cấu hình người dùng** — `~/.specify/integration-catalogs.yml`
4. **Mặc định có sẵn** — catalog chính thức + catalog cộng đồng

<a id="historical-integration-metadata"></a>

### Metadata integration theo lịch sử

Một mục integration có thể giữ các trường cấp cao nhất hiện có cho bản phát hành hiện tại được công bố và thêm một mapping `releases` từ phiên bản lịch sử sang metadata. Mục chỉ có một phiên bản vẫn hợp lệ khi không có khóa `releases`. Ví dụ:

```json
{
  "id": "my-agent",
  "name": "My Agent",
  "version": "2.0.0",
  "description": "Current release",
  "releases": {
    "1.0.0": {
      "description": "Historical release",
      "repository": "https://example.com/my-agent/v1",
      "requires": {"speckit_version": ">=0.7"}
    }
  }
}
```

Các trường cấp cao nhất giữ nguyên ý nghĩa ban đầu đối với client cũ hơn và với các lệnh `search`, `info`, `list --catalog` và `install` không chỉ định phiên bản. Bản ghi lịch sử có thể chứa `name`, `description`, `author`, `repository`, `license`, `tags` (danh sách chuỗi) và `requires` (một mapping). Định danh, tên, tác giả và chính sách nguồn dùng chung được giữ lại; metadata chỉ thuộc bản hiện tại như mô tả, repository, tag và yêu cầu **không** được bản cũ hơn kế thừa, trừ khi được cung cấp rõ ràng trong bản ghi của nó. Bản ghi phát hành không thể ghi đè `id`, `version`, `releases` hay chính sách nguồn, và không thể công bố URL tải về hay archive.

Để tra cứu metadata bằng lập trình, `IntegrationCatalog.get_integration_info(id, version="1.0.0")` chọn đúng bản ghi lịch sử từ nguồn được chọn, hoặc trả về `None` nếu thiếu phiên bản đó. `get_integration_versions(id)` trả về các phiên bản được chính nguồn đó công bố. Các cách viết tương đương theo PEP 440 (như `v1.0` và `1.0.0`) khớp cùng một bản phát hành nhưng vẫn giữ cách viết trong catalog. Không được lặp lại bản phát hành hiện tại trong `releases`; bản ghi sai định dạng và các phiên bản tương đương bị trùng sẽ bị từ chối. Một phiên bản không có sẽ không bao giờ rơi xuống nguồn có độ ưu tiên thấp hơn hay âm thầm chọn bản hiện tại. Các phép tra cứu này không cài integration.

<a id="integration-specific-options"></a>

## Tùy chọn riêng của integration

Truyền tùy chọn thiết lập riêng của agent qua `--integration-options`. Ngữ nghĩa, ví dụ và lưu ý khi chuyển đổi của chúng nằm trong hướng dẫn của agent tương ứng:

| Integration | Hướng dẫn |
| --- | --- |
| Generic | [Thư mục đầu ra và chế độ skills](generic.md#output-options-and-invocation) |
| GitHub Copilot | [Bố cục skills và commands](copilot.md#commands-layout) |
| IBM Bob | [Lệnh kiểu cũ và chuyển đổi](bob.md#legacy-commands-and-migration) |
| Kimi Code | [Chuyển đổi từ kiểu cũ](kimi.md#legacy-migration) |

Các chi tiết riêng khác của từng agent được liệt kê trong [danh mục integration](index.md).

<a id="runtime-events"></a>

## Runtime event

Các integration hỗ trợ event nhận `--events true|false` qua chuỗi `--integration-options` khi thiết lập; mặc định là bật. Định nghĩa trình xử lý đến từ mặc định của integration, các extension đã cài và `.specify/integration-events.yml`. Bật event không tạo trình xử lý ở nơi chưa cấu hình, và một integration chỉ phát ra các event gốc mà nó hỗ trợ.

Để cấu hình ghi đè cho dự án, hãy tạo `.specify/integration-events.yml`. Thay `<key>` bằng khóa integration của bạn và thay lệnh ví dụ bằng một lệnh Spec Kit đã cài có dùng script:

```yaml
integrations:
  <key>:
    events:
      post_tool_use:
        - command: speckit.my-extension.check
          matcher: "*"
          timeout: 60
```

Mỗi event nhận một mapping trình xử lý hoặc một danh sách trình xử lý. Một trình xử lý cần chuỗi `command` không rỗng; `matcher` là chuỗi lọc gốc tùy chọn, và `timeout` là số nguyên dương tùy chọn tính bằng giây.

Mặc định của integration và trình xử lý của extension được cộng dồn. Một ghi đè dự án hợp lệ **thay thế toàn bộ map event của integration đó**, chứ không chỉ các event được liệt kê trong ghi đè. Đặt `events: {}` dưới khóa integration để tắt mọi trình xử lý của nó. Nếu không đọc hoặc phân tích được ghi đè, hoặc một event không qua kiểm tra hợp lệ, Spec Kit cảnh báo và giữ lại mặc định cùng trình xử lý của extension. `--events false` được ưu tiên hơn mọi nguồn này.

Khi event đang bật, áp dụng thay đổi cấu hình bằng `specify integration upgrade <key>`.

Với một integration hỗ trợ event, tắt trình xử lý event của Spec Kit trong lúc nâng cấp:

```bash
specify integration upgrade <key> --integration-options="--events false"
```

Truyền `--integration-options` sẽ thay thế các tùy chọn thiết lập đã lưu, nên hãy lặp lại các tùy chọn khác bạn muốn giữ. Tập event bị tắt sẽ gỡ các hook Spec Kit đã cài trước đó, chứ không chỉ dừng việc sinh hook mới. Hướng dẫn của từng agent nêu rõ đường dẫn cấu hình event gốc và các giới hạn. Các runtime event này khác với hook lệnh của extension.

<a id="workflow-cli-dispatch"></a>

## Điều phối workflow qua CLI

Hướng dẫn của các agent phân biệt thiết lập IDE với khả năng hỗ trợ workflow qua CLI. Một số integration IDE có thể điều phối workflow step nếu có CLI riêng của chúng; số khác nói rõ là không hỗ trợ điều phối command/prompt. Adapter hỗ trợ nghĩa là Spec Kit dựng được lời gọi, chứ không có nghĩa mọi bản phát hành CLI của nhà cung cấp đều đã được thử nghiệm với nó.

Adapter có CLI hỗ trợ `SPECKIT_INTEGRATION_<KEY>_EXECUTABLE` để chọn file thực thi và `SPECKIT_INTEGRATION_<KEY>_EXTRA_ARGS` để thêm đối số CLI, trong đó `<KEY>` viết hoa và dấu gạch ngang được thay bằng dấu gạch dưới. Đối số bổ sung được phân tích theo quy tắc trích dẫn của POSIX shell. Vị trí đặt và cách xử lý cờ trùng lặp khác nhau tùy adapter; xem hướng dẫn của agent, đặc biệt với Docker Agent và Goose.

`--integration-options` khi thiết lập tách biệt với [`integration_args` và `integration_options`](../reference/workflows.md#per-step-integration-configuration) của workflow. Adapter từ chối cấu hình theo từng step không rỗng trừ khi chúng có triển khai nó; hiện Docker Agent cung cấp cấu hình agent/an toàn có cấu trúc. Cờ phê duyệt headless, việc chuyển tiếp mô hình và hỗ trợ đầu ra có cấu trúc cũng tùy adapter, không phải bảo đảm chung.

<a id="faq"></a>

## Câu hỏi thường gặp

<a id="can-i-install-multiple-integrations-in-the-same-project"></a>

### Tôi có thể cài nhiều integration trong cùng một dự án không?

Có, nhưng điều này nhằm phục vụ tính di động trong nhóm hơn là thiết lập mặc định. Nhiều integration chỉ được cho phép tự động khi integration đã cài và integration mới đều được Spec Kit khai báo là an toàn khi cài nhiều integration. Với các tổ hợp khác, truyền `--force` để xác nhận rằng nhiều agent có thể thấy chỉ dẫn hoặc lệnh riêng của agent khác không liên quan.

Spec Kit theo dõi một integration mặc định trong `.specify/integration.json` bằng `default_integration`, mọi integration đã cài bằng `installed_integrations`, thiết lập lúc chạy theo từng integration bằng `integration_settings`, và một `integration_state_schema` riêng cho các lần chuyển đổi trạng thái trong tương lai. Trường `integration` kiểu cũ vẫn được giữ làm bí danh cho integration mặc định.

<a id="which-integrations-are-multi-install-safe"></a>

### Những integration nào an toàn khi cài nhiều integration?

Với integration sinh file agent, an toàn đòi hỏi đường dẫn đầu ra tĩnh và duy nhất, thiết lập gọi lệnh ổn định, và một manifest riêng có các file được quản lý không chồng lấn với integration an toàn khác. Test của registry bảo đảm các bất biến này. Template Spec Kit dùng chung vẫn khớp với một integration mặc định duy nhất.

Chạy `specify integration list` để xem khai báo của từng integration. Hướng dẫn của mỗi integration ghi rõ trạng thái an toàn và các thư mục lệnh được cài.

Integration dùng chung thư mục lệnh với integration khác, cần đường dẫn cài động như `--commands-dir`, hoặc gộp thiết lập công cụ dùng chung thì mặc định không được khai báo là an toàn. Chúng vẫn có thể được cài cạnh integration khác bằng `--force`.

<a id="what-happens-to-my-changes-when-i-uninstall-or-switch"></a>

### Điều gì xảy ra với thay đổi của tôi khi gỡ hoặc chuyển integration?

File theo dõi bằng manifest mà bạn đã sửa được tự động giữ lại. Chỉ các file được theo dõi chưa sửa (khớp hash SHA-256 ban đầu) mới bị xóa. Dùng `--force` để ghi đè hành vi này. Xem [gỡ cài đặt](#uninstall-an-integration) để biết các ngoại lệ dọn dẹp riêng của từng integration.

<a id="how-do-i-know-which-key-to-use"></a>

### Làm sao biết nên dùng khóa nào?

Chạy `specify integration list` để xem mọi integration có sẵn cùng khóa của chúng, hoặc xem [danh mục integration](index.md#choose-an-integration).

<a id="do-i-need-the-ai-coding-agent-installed-to-use-an-integration"></a>

### Tôi có cần cài agent lập trình AI để dùng integration không?

Integration dựa trên CLI yêu cầu công cụ đó đã được cài. Integration dựa trên IDE hoạt động qua chính IDE và có thể không cần CLI riêng để thiết lập. Điều phối workflow có thể có thêm yêu cầu về CLI; xem hướng dẫn của integration bạn dùng. `specify integration list` hiển thị yêu cầu thiết lập của từng integration.

Nếu một integration không có template lệnh, `specify init` giữ hướng dẫn về thư mục dự án và chỉ cách chọn integration bằng `specify integration list` rồi chuyển sang nó bằng `specify integration switch <key>`, thay vì gợi ý các lệnh agent không có sẵn.

<a id="when-should-i-use-upgrade-vs-switch"></a>

### Khi nào nên dùng `upgrade`, khi nào dùng `switch`?

Dùng `upgrade` khi bạn đã nâng cấp Spec Kit và muốn làm mới các file được quản lý của một integration đã cài. Dùng `switch` khi muốn thay integration mặc định hiện tại bằng integration khác; nếu đích đã được cài, `switch` hoạt động giống `use`.

<a id="do-extensions-and-presets-i-install-apply-to-every-installed-integration"></a>

### Extension và preset tôi cài có áp dụng cho mọi integration đã cài không?

Không. Extension (`specify extension add`) và preset (`specify preset add`) chỉ đăng ký các ghi đè lệnh cho integration đang hoạt động (mặc định), kể cả khi đã cài các integration khác. Integration không phải mặc định sẽ không nhận các artifact đó cho đến khi nó trở thành mặc định: `specify integration use <key>` (hoặc `switch <key>`) dựng lại mọi extension và preset đang bật cho integration vừa được kích hoạt. `specify integration upgrade` theo cùng quy tắc — nó chỉ đăng ký lại extension và preset khi nâng cấp integration đang hoạt động.
