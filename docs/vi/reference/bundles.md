<a id="bundles"></a>

# Bundle

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/bundles.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Bundle kết hợp các thành phần Spec Kit hiện có — extension, preset, workflow và step — thành một đơn vị duy nhất, có phiên bản và cài đặt được. Trong khi extension và preset là các thành phần cơ bản, bundle là một chồng được tuyển chọn, khai báo mọi thứ một nhóm hay một vai trò cần và cài đặt tất cả trong một bước thông qua cơ chế riêng của từng thành phần. Bundle không tự thêm hành vi lúc chạy nào: chúng là một lớp phân phối và kết hợp trên các thành phần cơ bản bạn đã dùng.

Bundle được mô tả bằng manifest `bundle.yml` và được tìm thấy qua cùng chồng catalog như các thành phần khác. Cài một bundle sẽ phân giải các thành phần được khai báo theo phiên bản đã ghim, kiểm tra xung đột với integration đang hoạt động và xung đột phiên bản thành phần dùng chung, rồi áp dụng từng thành phần một cách idempotent với đầy đủ theo dõi nguồn gốc để sau này có thể gỡ hoặc làm mới sạch sẽ.

Để có điểm khởi đầu cụ thể, xem [các manifest bundle mẫu](https://github.com/github/spec-kit/tree/main/examples/bundles) dành cho product manager, business analyst, nhà nghiên cứu bảo mật và lập trình viên. Chúng minh họa cách đóng gói thiết lập theo vai trò, không phải các đặc tả tính năng đã được sinh đầy đủ; để xem ví dụ sử dụng trọn vẹn, xem [hướng dẫn từng bước của cộng đồng](../../community/walkthroughs.md).

<a id="first-party-bundles"></a>

## Bundle chính chủ

Spec Kit đi kèm một catalog bundle chính chủ trong `bundles/catalog.json`. Các bundle này được tuyển chọn, đánh dấu `verified: true` và được phân giải qua nguồn catalog có sẵn `builtin://default`.

| Bundle | Vai trò | Thành phần | Trường hợp sử dụng |
| --------- | ----------- | ----------------------------------------------------- | --------------------------------------- |
| `bugfix` | `developer` | Extension `bug` + workflow `bugfix` | Quy trình có hướng dẫn assess → gate → fix → test |
| `assess` | `developer` | Extension `assess` + workflow `assess` | Sàng lọc ý tưởng trước khi Phát triển hướng đặc tả |

Cài một bundle chính chủ giống như cài bất kỳ bundle nào (`add` là bí danh của `install`):

```bash
specify bundle install bugfix
specify bundle add assess
```

Catalog chính chủ được tải trực tuyến từ repository và khi offline sẽ quay về snapshot đóng gói trong wheel, để việc tìm kiếm vẫn hoạt động khi không có mạng. Manifest bundle cục bộ có thể cài các extension và workflow đi kèm bằng `--offline`. Manifest bundle tìm thấy qua catalog vẫn được phân giải từ `download_url` của chúng, nên hiện `specify bundle add <id>` cần mạng; việc cài từ catalog hoàn toàn offline đang được theo dõi như phần việc tiếp theo.

<a id="search-available-bundles"></a>

## Tìm bundle có sẵn

```bash
specify bundle search [query]
```

| Tùy chọn | Mô tả |
| ----------- | ---------------------------- |
| `--offline` | Không truy cập mạng |
| `--json` | Xuất JSON máy đọc được |

Tìm trong mọi catalog đang hoạt động các bundle khớp từ khóa. Khi không có từ khóa, liệt kê mọi bundle có sẵn cùng phiên bản, vai trò, nguồn và chỉ báo tin cậy (`verified` cho mục catalog do tổ chức tuyển chọn, ngược lại là `community`) để bạn đánh giá độ tin cậy trước khi cài.

<a id="bundle-info"></a>

## Thông tin bundle

```bash
specify bundle info <bundle_id>
specify bundle info <bundle_id> --versions
```

| Tùy chọn | Mô tả |
| ------------ | --------------------------------- |
| `--offline` | Không truy cập mạng |
| `--json` | Xuất JSON máy đọc được |
| `--versions` | Liệt kê các bản phát hành hiện tại và lịch sử trong catalog |

Hiển thị đầy đủ metadata của một bundle cùng **tập thành phần đã mở rộng hoàn toàn** mà nó cài — mọi extension, preset, step và workflow kèm phiên bản đã ghim, cùng priority và strategy của preset. Đầu ra cũng có chỉ báo tin cậy (`verified` hay `community`) để bạn đánh giá độ tin cậy trước khi cài. Bản xem trước này chính là kế hoạch mà `install` áp dụng, nên bạn thấy chính xác những gì sẽ được thêm trước khi cam kết. Với bundle có tham chiếu, đầu ra văn bản có phần tóm tắt `References`, kèm mức tin cậy riêng của từng bundle được tham chiếu (`verified` hoặc `community`), và đánh dấu các thành phần được tham chiếu với chuỗi nguồn gốc ngắn nhất; thành phần bị ghi đè hiển thị phiên bản và nguồn gốc bị ghi đè. JSON thêm các mục `references` với `id`, `version`, `source` đã phân giải, `install_policy`, `via`, cùng `verified` và `trust` riêng của bundle được tham chiếu; với bundle có tham chiếu, các mục thành phần cũng có `source` khi manifest khai báo (bundle phẳng bỏ trường này), `origin` (chuỗi các bundle đã đóng góp thành phần) khi thành phần đến từ một bundle được tham chiếu, và `overrides` bất cứ khi nào mục đó thay thế các khai báo khác, kể cả khai báo của chính bundle cha, vốn không có `origin`. Mỗi mục `overrides` mang `version` và `origin` bị thay thế, cùng `source`, `priority` hoặc `strategy` nếu có; một mục ghi đè nêu tên mọi bundle khác nhau đã khai báo giá trị bị thay thế (giữ đường ngắn nhất tới từng bundle), chứ không chỉ đường đầu tiên. Tham chiếu chỉ dùng để tìm kiếm được đánh dấu `discovery-only, not installable`. Các chồng lấn và xung đột phiên bản có thể thấy trước với các thành phần mà bundle đã cài yêu cầu cũng được hiển thị ở đây; một bundle có thể yêu cầu một thành phần mà không cài nó.

Dùng `specify bundle info <bundle_id> --versions` để xem lịch sử catalog mà không cần tải manifest bundle. Với `--json`, nó xuất ID bundle, các phiên bản có sẵn, phiên bản hiện tại, nguồn và chính sách cài đặt.

<a id="install-a-bundle"></a>

## Cài một bundle

```bash
specify bundle install <bundle_id | path>
```

| Tùy chọn | Mô tả |
| ---------------- | ------------------------------------------------------------------ |
| `--integration` | Ghi đè integration được dùng khi khởi tạo/cài đặt |
| `--offline` | Không truy cập mạng |
| `--refresh` | Làm mới các thành phần thuộc sở hữu từ nguồn bundle được cung cấp |
| `--version` | Cài đúng một bản phát hành lịch sử hoặc hiện tại trong catalog |

Cài toàn bộ tập thành phần của bundle thông qua cơ chế của từng thành phần cơ bản. Đối số có thể là ID bundle trong catalog, hoặc đường dẫn cục bộ tới artifact `.zip` đã build, thư mục bundle hoặc file `bundle.yml`; nguồn cục bộ được cài trực tiếp mà không tra cứu chồng catalog, trừ khi manifest khai báo `provides.bundles`. Một bundle cha cục bộ có tham chiếu bundle sẽ phân giải các bundle con qua chồng catalog lúc chạy lệnh, nên nó cần catalog và truy cập mạng (xem [Tham chiếu bundle](#bundle-references)).

Nếu thư mục hiện tại chưa phải dự án Spec Kit, `install` sẽ khởi tạo trước để một bản checkout mới đạt trạng thái hoạt động chỉ bằng một lệnh. `--integration` chọn integration khi khởi tạo dự án mới, và xác nhận đích khi một bundle ghim một integration cụ thể nhưng không xác định được integration đang hoạt động của dự án (`.specify/integration.json` bị thiếu hoặc không đọc được). Nó **không** ghi đè integration đang hoạt động của một dự án đã khởi tạo: nếu bundle nhắm tới integration khác với của dự án, việc cài đặt bị hủy mà không thay đổi gì. Bundle không gắn với integration nào sẽ kế thừa integration đang hoạt động của dự án. Khi không có `--refresh`, việc cài đặt là idempotent — các thành phần đã cài khớp với phiên bản ghim sẽ được bỏ qua, các bản vá đóng gói tương thích thuộc sở hữu của bundle cũng vậy, kèm cảnh báo (xem bên dưới). Các phiên bản đã cài khác biệt hoặc bị thiếu khác không thể đáp ứng phiên bản ghim. Chỉ `--refresh` mới sửa được một phiên bản bị lệch thuộc sở hữu riêng của bundle này; các thành phần được cài độc lập bị bỏ qua và không bao giờ bị nhận làm của bundle hay bị thay thế. Khi thất bại, không có bản ghi nguồn gốc nào được ghi (lần cài thất bại không ghi gì), và các thành phần đã cài trong lần chạy đó được gỡ theo khả năng tốt nhất — lỗi khi gỡ bị bỏ qua, nên trạng thái dở dang trên đĩa có thể còn lại.

Bản ghi bundle đã cài lưu các phiên bản ghim của thành phần bắt buộc tách biệt với các thành phần được đóng góp. Một thành phần tương thích được cài độc lập đáp ứng yêu cầu của bundle nhưng vẫn thuộc sở hữu độc lập: phiên bản ghim của nó vẫn chặn bundle sau cài phiên bản không tương thích, còn việc gỡ bundle không gỡ nó. Một lần cài hoặc làm mới không ghim phiên bản không thể thay thế một thành phần mà bundle khác yêu cầu ở phiên bản đã ghim; vẫn được phép dùng chung một phiên bản khớp đã cài mà không làm mới. Các bundle dùng chung cũng phải thống nhất về nguồn của thành phần và, với preset, cả priority và strategy trước khi cài hoặc làm mới thành phần dùng chung. Các bản ghi cũ không có danh sách yêu cầu giữ lại các phiên bản ghim đã đóng góp đã biết; hãy cài lại hoặc làm mới bundle để ghi đầy đủ yêu cầu của nó.

Lần cài thông thường từ chối thay đổi phiên bản của một bundle đã được ghi nhận hay metadata của thành phần nó sở hữu (phiên bản, nguồn, priority hoặc strategy của preset), kể cả việc bỏ một thành phần thuộc sở hữu. Điều này áp dụng kể cả khi manifest cục bộ giữ nguyên phiên bản bundle. Sắp xếp lại các thành phần không đổi hoặc thêm thành phần mới không cần làm mới. Để áp dụng thay đổi cho một bundle cục bộ mà không thêm nó vào catalog, hãy truyền nguồn đã sửa kèm `--refresh`:

```bash
specify bundle install ./new-release/bundle.yml --refresh
```

Nguồn cũng có thể là thư mục bundle hoặc artifact `.zip`. Làm mới dùng cùng đường cập nhật của thành phần cơ bản như `bundle update`, áp dụng lại các thành phần thuộc sở hữu của bundle, và gỡ các thành phần từng thuộc sở hữu nhưng bị bỏ khỏi manifest mới, trừ khi bundle khác vẫn cần chúng. Các thành phần được cài độc lập vẫn giữ nguyên và không bị nhận làm của bundle. Bản tóm tắt khi thành công có số lượng thành phần được làm mới và bị gỡ. Bản ghi bundle chỉ được cập nhật sau khi thao tác thành công; giống `bundle update`, các thành phần đã cài bị sửa trong một lần làm mới thất bại không được rollback.

Nguồn bundle cục bộ cung cấp manifest, không cung cấp nội dung của các thành phần. Thành phần phân giải qua catalog vẫn cần truy cập mạng để làm mới, kể cả khi đã được cài. Chỉ thêm `--offline` khi các thành phần đang được cài hoặc làm mới đi kèm Spec Kit; nếu không, lệnh sẽ báo thành phần nào cần truy cập mạng. Chạy lại không có `--offline` để tải thành phần đó qua catalog của nó.

**Tương thích bản vá đóng gói.** Khi một extension, preset hoặc workflow đi kèm CLI là bản vá ổn định mới hơn trong cùng phiên bản major/minor đã ghim, việc cài và làm mới sẽ cảnh báo và dùng bản đóng gói đó. Ví dụ, một bundle ghim `bug` ở `1.0.0` có thể dùng `bug` `1.0.1` đóng gói sẵn mà không phải sửa manifest. Việc kiểm tra hợp lệ cũng báo cùng cảnh báo. Hạ phiên bản, lệch major/minor và các phiên bản prerelease khác nhau vẫn là lỗi; một `source` thành phần được khai báo rõ cũng vẫn bắt buộc khớp chính xác phiên bản ghim. Thành phần phân giải qua catalog vẫn phải khớp chính xác. Ngoại lệ này cải thiện khả năng tương thích qua các lần nâng cấp CLI, nhưng bản vá không bảo đảm hành vi không thay đổi.

Bản ghi bundle giữ các phiên bản được yêu cầu trong `required_components` và `contributed_components`, và lưu các phiên bản thực tế đã biết là đã cài trong `installed_versions`, theo khóa `kind:id` (ví dụ `"extensions:bug": "1.0.1"`). Chúng cũng hiển thị trong `specify bundle list --json`. Không hỗ trợ khoảng phiên bản thành phần, `latest` hay bỏ trống phiên bản extension.

> **Nội dung step chỉ được phân giải qua catalog step.** Các mục `provides.steps` của bundle vẫn chỉ được phân giải qua các catalog step đang hoạt động. Nội dung `steps/<id>/` cục bộ trong bundle và các ghi đè `provides.steps[].source` tương đối **không** được phân giải trong bản phát hành này, nên step khai báo theo cách đó không thể cài offline. Để phát hành step cùng bundle hiện nay, hãy công bố nó lên một catalog step mà người dùng bundle truy cập được.

<a id="bundle-references"></a>

## Tham chiếu bundle

Một bundle có thể kết hợp các bundle khác bằng tham chiếu chính xác, đã ghim trong `provides.bundles`. Danh sách tham chiếu không rỗng yêu cầu schema manifest `1.1`; danh sách rỗng hoặc null được coi là không có tham chiếu. Mỗi tham chiếu có ID bundle, `version` SemVer chính xác và `source` tùy chọn nêu tên catalog bundle dự kiến sẽ thắng (không phải URL). ID tham chiếu là slug an toàn, phải duy nhất trong manifest và không được trùng tên bundle cha:

```yaml
schema_version: "1.1"
bundle:
  id: team
  name: Team setup
  version: 1.0.0
  role: developer
  description: A team bundle
  author: Example team
  license: MIT
requires:
  speckit_version: ">=0.1.0"
provides:
  bundles:
    - id: bugfix
      version: 1.0.1
      source: default
    - id: qa-pack
      version: 2.0.0
```

Tham chiếu được phân giải lúc chạy lệnh qua chồng catalog bundle hiệu lực. Mục thắng của chồng được chọn cho từng phiên bản ghim chính xác; `source` khai báo rõ là một khẳng định rằng đây là catalog thắng, không phải yêu cầu thay đổi thứ tự ưu tiên; nếu không khớp sẽ là lỗi và không chuyển sang catalog khác. Bundle được tham chiếu từ nguồn chỉ dùng để tìm kiếm có thể được xem bằng `info`, nhưng `install`, `update` và `validate` trực tuyến sẽ từ chối vì không cài được. Mỗi ID bundle chỉ được có một phiên bản trong một lần mở rộng; vòng lặp và phiên bản thứ hai cho cùng ID là lỗi. Hãy giải quyết phiên bản thứ hai bằng cách chọn các bản phát hành của các bundle tham chiếu thống nhất về nó.

Kết quả mở rộng là một kế hoạch thành phần phẳng. Các bundle được tham chiếu được duyệt đệ quy theo thứ tự khai báo (theo chiều sâu), rồi đến các thành phần của chính bundle khai báo, vẫn giữ cách nhóm extension, preset, step và workflow hiện có. Mỗi thành phần được cài tối đa một lần cho mỗi `kind:id`. Các bản sao thống nhất khi phiên bản và `source` của chúng khớp nhau (giá trị `source` bỏ trống và có đặt được coi là khác nhau); bản sao extension và preset còn phải có cùng `priority`, và bản sao preset còn phải có cùng `strategy`. Extension có thể bỏ qua `priority`; giá trị bỏ qua nghĩa là mặc định `10`, nên nó thống nhất với `10` được khai báo rõ. Preset phải khai báo `priority` là số nguyên. Các khác biệt khác giữa các tham chiếu ngang hàng là xung đột cần được sửa ở bundle cha. Ở mọi cấp, khai báo của chính một bundle thắng các tham chiếu của nó, chiếm vị trí của khai báo, và phát cảnh báo mô tả việc ghi đè cùng chuỗi nguồn gốc.

Việc mở rộng cho phép tối đa 10 cấp lồng tham chiếu và 50 ID bundle được tham chiếu khác nhau, không tính bundle gốc. Vòng lặp bị từ chối kèm chuỗi tham chiếu của nó. Khi cài và cập nhật, yêu cầu phiên bản Spec Kit được kiểm tra cho mọi bundle trong đồ thị, và yêu cầu không tương thích là lỗi cứng, trong khi bundle gốc vẫn là cổng integration duy nhất: integration khác biệt hoặc không xác định của một bundle được tham chiếu chỉ là cảnh báo. `requires.tools` và `requires.mcp` được hợp nhất trên toàn đồ thị và hiển thị qua các cảnh báo công cụ và MCP hiện có.

Bản ghi bundle cha đã cài chứa tập thành phần đã mở rộng và một khóa JSON tùy chọn `bundle_references` liệt kê mỗi tham chiếu trực tiếp và bắc cầu một lần, kèm nguồn catalog đã phân giải. Không có bản ghi riêng cho bundle con. `bundle update` đi theo manifest hiện tại của bundle cha và các tham chiếu đã ghim của nó; remove và refresh giữ nguyên các quy tắc quyền sở hữu và vòng đời thành phần hiện có.

Manifest được tham chiếu cần truy cập mạng. Với manifest gốc cục bộ, `install` có thể xác định tham chiếu đầu tiên và thất bại khi offline, kèm tên tham chiếu đó. Trong khi đó, `install`, `info` hoặc `update` với gốc từ catalog có thể thất bại sớm hơn khi tải catalog hoặc manifest gốc, trước khi biết được tham chiếu nào. `validate --offline` cảnh báo một lần cho mỗi tham chiếu được khai báo rằng nó chưa được mở rộng. `bundle build` chỉ thực hiện các kiểm tra cấu trúc đối với tham chiếu, không phân giải hay nhúng chúng.

**Hạn chế đã biết.**

- Chưa hỗ trợ phân giải offline và cục bộ cho bundle được tham chiếu; manifest được tham chiếu cần tải từ catalog qua mạng.
- Catalog bundle chính chủ không giữ lịch sử phát hành, nên ghim chính xác một bundle chính chủ có thể hỏng khi bundle đó phát hành bản tiếp theo.
- Không thể xem trước bundle cục bộ có tham chiếu bằng `bundle info`; việc xem trước cục bộ được hoãn lại.
- Việc quản lý phiên bản schema rộng hơn và các kiểm tra/khoảng tương thích CLI được hoãn lại.

<a id="catalog-release-history"></a>

## Lịch sử phát hành trong catalog

Một mục catalog có thể công bố bản phát hành hiện tại và các bản phát hành lịch sử đã được duyệt. Catalog cũ chỉ có một phiên bản vẫn hoạt động như trước.

```json
{
  "id": "team-setup",
  "version": "1.2.0",
  "download_url": "https://example.com/team-setup-1.2.0.zip",
  "sha256": "<sha256 for 1.2.0>",
  "releases": {
    "1.1.0": {
      "download_url": "https://example.com/team-setup-1.1.0.zip",
      "sha256": "<sha256 for 1.1.0>"
    }
  }
}
```

Mỗi bản phát hành lịch sử cần `download_url` riêng và digest SHA-256 gồm 64 ký tự; giống bản hiện tại, digest có thể dùng tiền tố `sha256:` không phân biệt hoa thường và khoảng trắng bao quanh, còn các tiền tố thuật toán khác bị từ chối. Các trường `requires`, `provides` và `verified` của một bản phát hành không được kế thừa từ bản hiện tại: hãy đặt chúng trong bản ghi của bản phát hành đó, nếu không bản phát hành không có yêu cầu, không có số lượng cung cấp và được hiển thị là `community`. Metadata dùng chung khác, như tên, mô tả và tác giả, được kế thừa, và bản ghi phát hành có thể ghi đè chúng. Bản ghi phát hành không được chứa `id`, `version` hay `releases`.

`specify bundle install team-setup --version 1.1.0` chọn bản phát hành của bundle, tải artifact của bản đó, xác minh digest và kiểm tra manifest khai báo đúng ID catalog và cùng phiên bản với bản đã chọn. Các cách viết tương đương như `v1.1.0` và `1.1.0` đều khớp; cách viết của khóa catalog chỉ dùng để hiển thị. Nó không bao giờ ghi đè các phiên bản ghim của thành phần bên trong `bundle.yml`. `--version` chỉ dùng với catalog, nên không được để trống, dùng với đường dẫn cục bộ hay kết hợp với `--refresh`.

Chỉ catalog có độ ưu tiên cao nhất liệt kê bundle mới được tra cứu; phiên bản bị thiếu không rơi xuống catalog có độ ưu tiên thấp hơn. Nguồn chỉ dùng để tìm kiếm vẫn không cài được, kể cả các bản phát hành lịch sử chính xác. Khóa JSON trùng lặp ở bất kỳ đâu trong catalog đều bị từ chối khi đọc. Giá trị `download_url` lịch sử phải dùng HTTPS (hoặc HTTP trên localhost), và khóa phát hành phải là giá trị SemVer nghiêm ngặt so sánh được theo PEP 440. Các khóa phiên bản phải khác nhau, kể cả các cách viết tương đương theo PEP 440 như `1.0.0-rc.1` và `1.0.0-rc1`, và không được lặp lại phiên bản hiện tại. `bundle update` luôn chọn bản phát hành hiện tại. Catalog chính chủ và catalog cộng đồng hiện công bố một bản phát hành cho mỗi bundle.

Lịch sử phát hành được kiểm tra khi nguồn catalog của nó được nạp. Mapping `releases` sai định dạng khiến `install`, `info`, `update` và `search` thất bại khi nguồn đó được tra cứu. Việc phân giải dừng sau nguồn đầu tiên liệt kê bundle, nên một nguồn ưu tiên thấp hơn bị sai định dạng sẽ không bị phát hiện khi nguồn ưu tiên cao hơn đã cung cấp ID đó; `search` nạp mọi nguồn, nên một mục sai định dạng bị che vẫn khiến lệnh này thất bại.

<a id="update-bundles"></a>

## Cập nhật bundle

```bash
specify bundle update [<bundle_id>]
```

| Tùy chọn | Mô tả |
| ---------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--all` | Cập nhật mọi bundle đã cài |
| `--integration` | Ghi đè integration được dùng khi làm mới thành phần; chỉ áp dụng khi không xác định được integration đang hoạt động của dự án |
| `--offline` | Không truy cập mạng |

Phân giải lại một bundle và **làm mới** các thành phần của nó qua đường cập nhật của từng thành phần cơ bản, đưa các thành phần đã cài lên phiên bản mới được ghim của bundle (hoặc bản vá đóng gói mới hơn tương thích, kèm cảnh báo) trong khi vẫn giữ các ghi đè ở cấp thành phần cơ bản (như priority của preset). Truyền ID bundle, hoặc dùng `--all` để cập nhật mọi thứ đã cài.

**Bản phát hành catalog đã ghim.** Extension, preset, workflow và step có phiên bản ghim sẽ chọn đúng bản phát hành đó từ mục catalog đang hoạt động có độ ưu tiên cao nhất. Bản phát hành lịch sử phải được công bố trong `releases` với URL artifact và digest SHA-256 riêng; công cụ đóng gói bundle không bao giờ đoán URL cũ từ URL hiện tại hay chuyển sang catalog khác. Các mục extension và preset kiểu cũ không công bố phiên bản là ngoại lệ: công cụ đóng gói bundle dùng nguyên mục thắng và không thể bắt buộc phiên bản ghim hay xác minh phiên bản của archive đã cài. Hãy công bố một mục có phiên bản để phiên bản ghim đó được bắt buộc. Trình cài của thành phần cơ bản dùng bản ghi workflow hoặc step đã chọn mà không đọc lại catalog, và xác minh archive đã tải hoặc metadata workflow/step theo bản phát hành đó. Một workflow đã ghim đi kèm Spec Kit sẽ dùng bản đóng gói sẵn khi phiên bản khớp, và dùng bản phát hành trong catalog khi khác phiên bản và được phép truy cập mạng. Step không có phiên bản ghim sẽ cài bản phát hành hiện tại trong catalog.

Khi không có `source` khai báo rõ, extension và preset đóng gói sẵn được ưu tiên hơn bản phát hành trong catalog. Việc kiểm tra hợp lệ từ chối phiên bản ghim không tương thích kể cả khi có bản phát hành khớp trong catalog; các bản vá ổn định đóng gói sẵn mới hơn và tương thích chỉ tạo cảnh báo. Chỉ định catalog thắng làm `source` để chủ động dùng đúng bản phát hành của nó.

> **Mỗi ID thành phần chỉ có một phiên bản được cài.** Các bundle dùng chung một thành phần phải thống nhất về phiên bản ghim của nó. Phiên bản ghim khác hoặc không xác định từ bundle khác bị từ chối trước khi cài, kể cả trong `bundle update`; làm mới một bundle không thể thay thế phiên bản mà bundle khác yêu cầu.

Một bundle chỉ được liệt kê một ID thành phần một lần cho mỗi kind; tham chiếu trùng lặp trong cùng manifest là không hợp lệ, kể cả khi phiên bản ghim của chúng khớp nhau.

`source` tùy chọn trong một tham chiếu `provides.<kind>` nêu tên catalog thành phần dự kiến sẽ thắng (như hiển thị bởi `specify <kind> catalog list`, hoặc `specify workflow step catalog list` với step). Nó **không** phải URL artifact và không ghi đè thứ tự ưu tiên hay chính sách cài đặt của catalog. Khi được chỉ định, thành phần được xác minh theo catalog đó kể cả khi đã cài, thay vì phân giải từ bản đóng gói kèm Spec Kit; một catalog thắng khác hoặc nguồn chỉ dùng để tìm kiếm sẽ ngăn việc cài đặt. Nếu nhiều catalog đang hoạt động trùng tên nguồn, việc kiểm tra và cài bundle sẽ từ chối vì mơ hồ; hãy đặt tên duy nhất cho mỗi catalog. Xác minh một nguồn khai báo rõ cần truy cập mạng. URL `--from` trực tiếp của thành phần cơ bản là một con đường riêng, phải được yêu cầu rõ ràng.

<a id="remove-a-bundle"></a>

## Gỡ một bundle

```bash
specify bundle remove <bundle_id>
```

Chỉ gỡ các thành phần mà bundle này đã đóng góp, giữ lại mọi thành phần mà bundle đã cài khác vẫn cần (không gỡ kéo theo). Nếu không bundle nào khác sở hữu một thành phần được giữ lại, phần đóng góp của nó được chuyển sang một bundle còn lại có yêu cầu nó, để sau này gỡ bundle đó có thể dọn dẹp thành phần. Thành phần được cài độc lập không bao giờ bị nhận làm của bundle.

<a id="list-installed-bundles"></a>

## Liệt kê bundle đã cài

```bash
specify bundle list
```

| Tùy chọn | Mô tả |
| -------- | ---------------------------- |
| `--json` | Xuất JSON máy đọc được |

Liệt kê các bundle đã cài trong dự án kèm phiên bản, số thành phần bắt buộc (kể cả thành phần được cung cấp độc lập) và thời điểm cài. Với `--json`, bản ghi có tham chiếu còn có `bundle_references`, chứa mỗi tham chiếu trực tiếp hoặc bắc cầu đã phân giải và nguồn catalog thắng của nó.

<a id="initialize-a-project-with-a-bundle"></a>

## Khởi tạo dự án bằng bundle

```bash
specify bundle init [<bundle_id>]
```

| Tùy chọn | Mô tả |
| ---------------- | ---------------------------------------- |
| `--integration` | Ghi đè integration |
| `--offline` | Không truy cập mạng |

Bảo đảm thư mục hiện tại là dự án Spec Kit (khởi tạo idempotent nếu cần), rồi có thể cài bundle được chỉ định. Hữu ích như một bước khởi động rõ ràng, chỉ một lệnh, cho bản checkout mới.

Lặp lại `bundle init` sẽ bỏ qua các thành phần bundle đã cài và giữ nguyên các chỉnh sửa cục bộ của chúng. Nó tuân theo cùng quy tắc như [`bundle install`](#install-a-bundle) thông thường: thành phần mới được thêm vào manifest sẽ được cài và ghi nhận, nhưng lệnh thất bại mà không thay đổi bundle đã cài nếu manifest đổi phiên bản bundle đã ghi nhận, đổi phiên bản, nguồn, priority hoặc strategy preset của một thành phần thuộc sở hữu, hoặc bỏ một thành phần thuộc sở hữu. Để làm mới thành phần hoặc áp dụng những thay đổi như vậy, dùng `bundle update <id>` cho bundle từ catalog hoặc `bundle install <path> --refresh` cho nguồn cục bộ.

<a id="validate-a-bundle"></a>

## Kiểm tra hợp lệ một bundle

```bash
specify bundle validate
```

| Tùy chọn | Mô tả |
| ------------ | ------------------------------------------------------------------- |
| `--path` | Thư mục bundle hoặc `bundle.yml` (mặc định: thư mục hiện tại) |
| `--offline` | Chỉ xác minh tham chiếu với các thành phần đóng gói sẵn/đã cài |

Báo `bundle.yml` có đúng định dạng không và mọi tham chiếu thành phần được khai báo có phân giải được ở phiên bản ghim không. Với manifest có tham chiếu, kiểm tra trực tuyến mở rộng toàn bộ đồ thị tham chiếu và kiểm tra mọi thành phần trong kế hoạch đã mở rộng, gồm các kiểm tra cấu trúc, vòng lặp, phiên bản, nguồn, xung đột và chính sách cài đặt. Tham chiếu được kiểm tra với các thành phần đóng gói sẵn hoặc đã cài khớp và — khi trực tuyến — với đúng bản phát hành trong catalog thắng cho phép cài đặt. `source` khai báo rõ được xác minh theo catalog thắng thay vì phân giải cục bộ. Bản phát hành bị thiếu, nguồn không khớp, nguồn chỉ dùng để tìm kiếm và metadata catalog sai định dạng làm việc kiểm tra thất bại; tham chiếu thành phần không kiểm tra được khi offline hoặc do catalog không truy cập được sẽ tạo cảnh báo. Lỗi khi tải tham chiếu bundle (như catalog bundle không truy cập được hoặc tải manifest con thất bại) làm kiểm tra trực tuyến thất bại, còn `--offline` giữ cảnh báo theo từng tham chiếu. Ở chế độ `--offline`, mỗi tham chiếu bundle được khai báo tạo một cảnh báo rằng nó chưa được mở rộng. Nếu một catalog có độ ưu tiên cao hơn không truy cập được trước khi tìm thấy mục khớp, việc tra cứu vẫn chưa được xác minh; mục khớp ở độ ưu tiên thấp hơn không thể giải quyết nó. Việc kiểm tra hợp lệ không đánh giá `requires.speckit_version` với CLI đang chạy; `install` và `update` mới bắt buộc cổng tương thích lúc chạy đó. Giống cài đặt, các mục extension và preset kiểu cũ không công bố phiên bản được chấp nhận mà không xác minh phiên bản ghim.

<a id="build-a-bundle-artifact"></a>

## Build artifact bundle

```bash
specify bundle build
```

| Tùy chọn | Mô tả |
| ----------- | ------------------------------------------------------- |
| `--path` | Thư mục bundle (mặc định: thư mục hiện tại) |
| `--output` | Thư mục đầu ra cho artifact |

Tạo một artifact `.zip` duy nhất, có phiên bản, phân phối được từ một thư mục bundle. Artifact nhúng manifest và có thể cài trực tiếp bằng `specify bundle install <artifact.zip>`.

<a id="publish-a-bundle"></a>

## Phát hành bundle

Tác giả bundle kiểm tra và đóng gói bundle cục bộ, rồi lưu trữ artifact được sinh ra cùng metadata catalog ở nơi người dùng truy cập được. Mục catalog bundle trỏ tới artifact bundle, nhưng các thành phần khai báo bên trong `bundle.yml` vẫn được phân giải qua thành phần đóng gói sẵn, thành phần đã cài, hoặc các catalog extension, preset, workflow và step đang hoạt động.

Nếu bundle của bạn tham chiếu thành phần từ catalog không mặc định, hãy ghi lại các URL catalog đó và kiểm thử đường cài đặt từ một dự án sạch đã thêm các catalog đó. Bài gửi bundle cộng đồng nên kèm bằng chứng phân giải phụ thuộc đó trong issue [Bundle Submission](https://github.com/github/spec-kit/issues/new?template=bundle_submission.yml).

<a id="what-happens-after-you-submit"></a>

### Điều gì xảy ra sau khi bạn gửi

1. GitHub gắn kết luận `triage-must-have` khi issue được mở qua form Bundle Submission. Bài gửi bundle cùng với bài gửi extension và preset dùng tự động hóa tiếp nhận này; tiêu chí triage thủ công cho các issue khác giữ nguyên.
2. Người duy trì review issue trong quá trình triage và gắn nhãn riêng `bundle-submission`, nhãn này khởi động việc kiểm tra catalog tự động. Trên repository công khai này, người đóng góp không thể tự gắn nhãn đó, nên không cần gắn nhãn hay yêu cầu lại — issue chỉ đơn giản chờ trong hàng triage.
3. Workflow tự động kiểm tra bài gửi và, khi kiểm tra đạt, cập nhật `bundles/catalog.community.json` và `docs/community/bundles.md` trong một draft pull request
4. Người duy trì review pull request được sinh ra và merge khi chấp thuận
5. Bundle của bạn có thể được tìm thấy qua `specify bundle search`

<a id="manage-catalog-sources"></a>

## Quản lý nguồn catalog

Bundle được tìm thấy qua một chồng nguồn catalog sắp theo độ ưu tiên (phạm vi dự án, người dùng và có sẵn). Các nguồn có sẵn là:

- `builtin://default` — bundle chính chủ đi kèm trong `bundles/catalog.json` (`bugfix`, `assess`, ...), cho phép cài đặt.
- `builtin://community` — bài gửi của cộng đồng trong `bundles/catalog.community.json`, chỉ dùng để tìm kiếm.

Mỗi nguồn có một chính sách cài đặt. Có thể cài từ nguồn `install-allowed`; nguồn `discovery-only` xuất hiện trong `search` và `info` nhưng từ chối cài đặt. Hãy xem chồng đang hoạt động trước khi cài bundle từ một nguồn không mặc định.

> **Thẩm định cả nguồn bundle lẫn các catalog thành phần của nó.** Một dự án có thể cung cấp catalog bundle riêng và các catalog thành phần `install-allowed` (extension, preset, workflow và step) trong `.specify/`; việc cấu hình dự án đó tồn tại không chứng minh rằng bất cứ thứ gì trong đó đã được review. Trước khi cài bundle từ một dự án lạ, hãy chạy `specify bundle catalog list` — cùng các lệnh tương đương `extension`/`preset`/`workflow catalog list` và `specify workflow step catalog list` cho các thành phần mà nó kéo vào — và coi mọi nguồn bạn không tự thêm là chưa được thẩm định cho đến khi bạn review.

Với thành phần workflow, hãy kiểm tra các trường shell `run` và `env` cùng code được chúng tham chiếu, kể cả các thay đổi do overlay đang hoạt động đưa vào. Điều này áp dụng cả với step `strict: true`: binding môi trường có thể thay đổi việc tìm file thực thi hoặc việc nạp lúc chạy. Xem [Review việc thực thi shell](workflows.md#reviewing-shell-execution).

<a id="list-the-catalog-stack"></a>

### Liệt kê chồng catalog

```bash
specify bundle catalog list
```

In chồng catalog đang hoạt động, sắp theo độ ưu tiên, kèm phạm vi và chính sách cài đặt của từng nguồn.

<a id="add-a-catalog-source"></a>

### Thêm nguồn catalog

```bash
specify bundle catalog add <url>
```

| Tùy chọn | Mô tả |
| ------------- | ------------------------------------------------------- |
| `--policy` | `install-allowed` hoặc `discovery-only` |
| `--priority` | Độ ưu tiên của nguồn (nhỏ hơn = ưu tiên cao hơn; mặc định 10) |
| `--id` | ID nguồn khai báo rõ |

Đăng ký một nguồn catalog phạm vi dự án và lưu lại.

Thêm lại cùng nguồn với cùng ID, URL, chính sách và độ ưu tiên sẽ thành công mà không đổi cấu hình; thiết lập khác sẽ bị từ chối.

<a id="remove-a-catalog-source"></a>

### Gỡ nguồn catalog

```bash
specify bundle catalog remove <id_or_url>
```

Gỡ một nguồn catalog phạm vi dự án. Không thể xóa các nguồn mặc định có sẵn.

> **Lưu ý:** `search` và `info` hoạt động ở mọi nơi — khi không có dự án, chúng quay về chồng catalog có sẵn/người dùng. Các lệnh thay đổi trạng thái còn lại (`list`, `update`, `remove`, `catalog`) yêu cầu dự án đã được khởi tạo bằng `specify init`. `install` và `init` sẽ khởi tạo dự án khi cần nếu chạy trong thư mục chưa khởi tạo.
