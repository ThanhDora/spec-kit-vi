<a id="core-commands"></a>

# Lệnh lõi

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/core.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Các lệnh `specify` lõi xử lý việc khởi tạo dự án, kiểm tra hệ thống và thông tin phiên bản.

<a id="initialize-a-project"></a>

## Khởi tạo dự án

```bash
specify init [<project_name>]
```

| Tùy chọn | Mô tả |
| ------------------------ | ------------------------------------------------------------------------ |
| `--integration <key>` | Integration agent lập trình AI cần dùng (ví dụ `copilot`, `claude`, `gemini`). Xem [danh mục integration](../integrations/index.md) để biết mọi khóa có sẵn |
| `--integration-options` | Tùy chọn cho integration (ví dụ `--integration-options="--commands-dir .myagent/cmds"`) |
| `--script sh\|ps\|py` | Loại script: `sh` (bash/zsh), `ps` (PowerShell) hoặc `py` (Python) |
| `--here` | Khởi tạo trong thư mục hiện tại thay vì tạo thư mục mới |
| `--force` | Buộc gộp/ghi đè khi khởi tạo trong thư mục đã có |
| `--allow-symlinks` | Lưu quyền cho các symlink nằm bên trong trong các thao tác FileHelper đã chuyển đổi; mặc định là từ chối |
| `--ignore-agent-tools` | Bỏ qua kiểm tra công cụ CLI của agent lập trình AI |
| `--preset <id>` | Cài một preset trong lúc khởi tạo |

Tạo dự án Spec Kit mới với cấu trúc thư mục, template, script và file integration agent lập trình AI cần thiết.

> [!NOTE]
> Việc khởi tạo repository Git và tạo nhánh do **extension git** quản lý, vốn không được cài mặc định. Chạy `specify extension add git` sau init để bật workflow git.

Dùng `<project_name>` để tạo thư mục mới, hoặc `--here` (hay `.`) để khởi tạo trong thư mục hiện tại. Nếu thư mục đã có file, dùng `--force` để gộp mà không cần xác nhận.

Khi bỏ qua `--integration`, terminal tương tác sẽ hỏi bạn chọn integration. Các phiên không tương tác, như CI hoặc lần chạy qua pipe, mặc định dùng GitHub Copilot; truyền `--integration <key>` để chọn rõ integration khác, hoặc đặt `SPECKIT_INTEGRATION_DEFAULT` để đổi giá trị dự phòng (xem [Biến môi trường](#environment-variables)).

<a id="persisted-filesystem-policy"></a>

### Chính sách filesystem được lưu

Chỉ `init` nhận `--allow-symlinks`. Nó ghi `allow_symlinks: true` vào `.specify/init-options.json`; bỏ qua thì ghi `false`, kể cả khi khởi tạo lại. Các lệnh CLI phạm vi dự án đọc giá trị hiện tại ở mỗi lần gọi, nên chỉnh sửa thủ công có hiệu lực ngay. File hoặc khóa bị thiếu nghĩa là từ chối; giá trị phải là boolean JSON, không phải chuỗi, số hay null. Cấu hình không hợp lệ/không đọc được là lỗi, không phải trường hợp dùng giá trị dự phòng. Các tùy chọn init đã ghi không liên quan được giữ nguyên.

Cây khởi động cấu hình (`.specify` và `init-options.json`) luôn phải không phải symlink bên dưới thư mục gốc dự án đáng tin cậy, kể cả ở chế độ cho phép. Help, version, check và các thao tác công cụ/catalog không cần dự án sẽ không bị thêm yêu cầu phải có dự án. Init dùng đích được chỉ định rõ, không dùng `SPECIFY_INIT_DIR`. `check` có thể dùng các integration đã cài trong dự án: nó kiểm tra mọi chính sách hiện có tại cwd được chọn hoặc ranh giới `SPECIFY_INIT_DIR` trước khi nạp chúng hoặc kiểm tra công cụ. Nó vẫn hoạt động trong một cwd không có dự án, không có `.specify` hay tùy chọn init. Help và version không đọc chính sách dự án.

**Giới hạn chuyển đổi:** chính sách được thực thi bởi các thao tác FileHelper, hiện bao gồm I/O khởi động init-options. Việc nạp chính sách chưa định tuyến mọi thao tác filesystem khác của lệnh qua FileHelper. Hạ tầng dùng chung, đăng ký, lưu trữ được quản lý, script và thao tác lúc chạy giữ nguyên hành vi hiện có cho đến khi được chuyển đổi. Xem [thiết kế FileHelper](../../../design/file-helper.md) để biết ranh giới và hợp đồng bàn giao.

<a id="examples"></a>

### Ví dụ

```bash
# Create a new project with an integration
specify init my-project --integration copilot

# Initialize in the current directory
specify init --here --integration copilot

# Force merge into a non-empty directory
specify init --here --force --integration copilot

# Use PowerShell scripts (Windows/cross-platform)
specify init my-project --integration copilot --script ps

# Install a preset during initialization
specify init my-project --integration copilot --preset compliance
```

<a id="environment-variables"></a>

### Biến môi trường

| Biến | Mô tả |
| ----------------- | ------------------------------------------------------------------------ |
| `SPECKIT_INTEGRATION_DEFAULT` | Ghi đè integration dự phòng mà `specify init` dùng khi bỏ qua `--integration` (mặc định của lời nhắc tương tác và giá trị dự phòng không tương tác). Đặt thành bất kỳ khóa integration đã đăng ký nào (ví dụ `gemini`, `claude`). Giá trị không nhận diện được sẽ bị bỏ qua kèm cảnh báo và dùng mặc định có sẵn (`copilot`). `--integration <key>` khai báo rõ luôn được ưu tiên. |
| `SPECIFY_INIT_DIR` | Nhắm tới một dự án thành viên từ bên ngoài thư mục của nó (ví dụ thư mục gốc monorepo) mà không cần `cd`, dùng cho chế độ không tương tác / CI. Đặt thành **thư mục gốc dự án** — thư mục *chứa* `.specify/` (đường dẫn tương đối được phân giải theo thư mục hiện tại). Đường dẫn phải tồn tại và chứa `.specify/`, nếu không lệnh sẽ báo lỗi và **không** quay về thư mục hiện tại. Được phân giải một lần trong helper gốc lõi (`get_repo_root` trong Bash, `Get-RepoRoot` trong PowerShell), nên nó được các script tính năng lõi (`/speckit.plan`, `/speckit.tasks`, …) và việc tạo nhánh tính năng của extension Git tôn trọng, vì chúng kế thừa nó. CLI `specify` áp dụng **cùng** quy tắc kiểm tra cho mọi lệnh con phạm vi dự án (`specify integration …`, `specify extension …`, `specify workflow …`, `specify preset …`, và các lệnh khác thao tác trên dự án `.specify/`), nên chúng cũng có thể nhắm tới một dự án thành viên. Khi không đặt, các helper Bash/PowerShell giữ cách tìm ngược lên hiện có; CLI `specify` giữ resolver phạm vi dự án chỉ dựa trên cwd, trừ khi một lệnh định nghĩa rõ cách phát hiện rộng hơn (ví dụ các lệnh bundle). |
| `SPECIFY_FEATURE_DIRECTORY` | Ghi đè thư mục tính năng đang hoạt động (ưu tiên hơn `.specify/feature.json`). Đường dẫn tương đối được nối với thư mục gốc dự án mà không kiểm tra phạm vi chứa, nên giá trị như `../shared-feature` vẫn phân giải ra bên ngoài; đường dẫn tuyệt đối được dùng nguyên trạng và cũng có thể trỏ ra ngoài thư mục gốc dự án. Thư mục gốc dự án vẫn xác định dự án Spec Kit và ngữ cảnh lệnh/cấu hình của nó, nhưng bản thân thư mục tính năng được chọn không bắt buộc nằm bên dưới nó. Kết hợp với `SPECIFY_INIT_DIR` để chọn cả dự án lẫn tính năng mà không cần tương tác. |
| `SPECIFY_FEATURE` | Ghi đè rõ **nhãn** tính năng đang hoạt động (ví dụ `001-photo-albums`) — định danh mà các helper lõi báo là tính năng/nhánh hiện tại (`get_current_branch` trong Bash, `Get-CurrentBranch` trong PowerShell). Các helper đó không bao giờ kiểm tra Git: khi biến được đặt, chúng trả về nguyên văn giá trị, và khi không đặt, chúng trả về chuỗi rỗng. Giá trị dự phòng theo basename xảy ra sau — `get_feature_paths` / `Get-FeaturePathsEnv` thay bằng basename của thư mục tính năng đã phân giải để nhãn được báo vẫn dùng được — nên gọi trực tiếp các helper nêu trên **không** cho bạn giá trị dự phòng đó. Bạn tự đặt nó: các script tính năng Bash và Python chỉ **in** gợi ý dạng comment `export SPECIFY_FEATURE=…` / `$env:SPECIFY_FEATURE = …` để bạn chạy, vì tiến trình con không thể thay đổi môi trường của tiến trình cha, và `/speckit.specify` lưu `feature_directory` vào `.specify/feature.json` thay vì đặt biến này. (Các script tính năng PowerShell có gán `$env:SPECIFY_FEATURE`, nhưng giá trị đó chỉ đến được với bạn khi script chạy bên trong phiên PowerShell hiện tại.) Nó **không** định vị thư mục tính năng: khi chỉ đặt `SPECIFY_FEATURE`, `get_feature_paths` thất bại với thông báo *"Feature directory not found. Set `SPECIFY_FEATURE_DIRECTORY` or run the specify command to create `.specify/feature.json`."* Hãy dùng `SPECIFY_FEATURE_DIRECTORY` (ở trên) hoặc `.specify/feature.json` để chọn thư mục. |
| `SPECIFY_FEATURE_NO_PERSIST` | Đặt thành `1` hoặc `true` để mọi script lõi không ghi `.specify/feature.json`, kể cả khi bình thường nó sẽ lưu `SPECIFY_FEATURE_DIRECTORY` lúc đọc. Hữu ích khi nhiều agent chạy đồng thời trên cùng một bản checkout, mỗi agent có `SPECIFY_FEATURE_DIRECTORY` riêng: nếu không có nó, bước lưu của mỗi lần gọi có thể ghi đè thư mục tính năng đã ghim của agent khác. |

> **Hai trục phân giải.** `SPECIFY_INIT_DIR` chọn **dự án** (thư mục nào chứa `.specify/`); `SPECIFY_FEATURE_DIRECTORY` / `.specify/feature.json` chọn **tính năng** — vị trí mặc định của nó nằm trong `specs/` của dự án đó, nhưng thư mục tính năng được chọn rõ không bị giới hạn phải nằm bên trong. Chúng độc lập với nhau — dự án trước, rồi đến tính năng.
>
> **Quản lý phiên bản mã nguồn.** `specify init` dựng một `.specify/.gitignore` được quản lý, loại trừ trạng thái cục bộ theo máy — `feature.json` (con trỏ tính năng hiện tại, được ghi lại mỗi khi đổi tính năng) và các ghi đè extension theo máy `extensions/*/local-config.yml` — trong khi mọi thứ khác trong `.specify/` (constitution, template, script, cấu hình extension) vẫn chia sẻ được để cả nhóm thống nhất. Giống các script và template dùng chung khác trong `.specify/`, file này được theo dõi trong manifest hạ tầng dùng chung: chỉnh sửa của bạn được giữ khi khởi tạo lại và `specify init --here --force` khôi phục nội dung được quản lý. Nó được cố ý giữ lại khi chạy `specify integration uninstall`, lệnh chỉ gỡ file riêng của agent bị gỡ.
>
> **Thư mục gốc dự án là symlink.** Một bí danh thư mục gốc dự án được thiết lập rõ ràng sẽ được tin cậy, kể cả các thư mục tổ tiên của hệ điều hành phía trên nó. Cây cấu hình bên dưới thư mục gốc đó luôn được kiểm tra ở chế độ từ chối: `.specify/` và `init-options.json` không được là symlink. Các thao tác chưa chuyển đổi ở những nơi khác trong dự án giữ nguyên hành vi symlink hiện có.

<a id="naming-features-with-the-helper-scripts"></a>

## Đặt tên tính năng bằng các script helper

Khi gọi trực tiếp các script helper `create-new-feature` đi kèm, tên được sinh giữ chữ cái Unicode và chữ số thập phân ở dạng UTF-8, nên mô tả như `添加用户` tạo ra `001-添加用户`. Mô tả chỉ gồm dấu câu vẫn có thể tạo hậu tố rỗng như `001-`; các script cảnh báo trên stderr khi điều này xảy ra, kể cả khi chạy thử. Đầu ra JSON vẫn phân tích được.

Để chọn tên khác, hãy giữ mô tả gốc và cung cấp một tên ngắn:

```bash
bash .specify/scripts/bash/create-new-feature.sh --json --short-name 用户管理 "添加用户"
```

Helper Python cũng nhận `--short-name`; helper PowerShell dùng `-ShortName`. Tên ngắn được cung cấp cũng được làm sạch theo cùng quy tắc, nên nó phải chứa ít nhất một chữ cái hoặc chữ số. Với tên ngoài ASCII, helper Bash cần một locale UTF-8 đã cài và trình thông dịch Python 3 để phân loại Unicode. Đầu vào ASCII, kể cả tab và xuống dòng, được làm sạch mà không cần cả hai yêu cầu đó. Nếu `LC_ALL` không rỗng, Bash dùng locale đó thay vì chọn locale khác: Tên Unicode sẽ báo lỗi nếu locale được chọn không dùng được cho tên UTF-8. Khi `LC_ALL` không đặt hoặc rỗng, Bash chọn một locale UTF-8 đã cài kể cả khi `LANG` hoặc `LC_CTYPE` chỉ định locale không phải UTF-8. Chữ hoa ASCII được chuyển thành chữ thường; kiểu chữ hoa/thường của chữ cái ngoài ASCII được giữ nguyên ở mọi biến thể script.

<a id="check-installed-tools"></a>

## Kiểm tra công cụ đã cài

```bash
specify check
```

Kiểm tra các agent lập trình AI dựa trên CLI có sẵn trên hệ thống của bạn. Agent dựa trên IDE được bỏ qua vì chúng không cần công cụ CLI.

Các integration đã cài trong dự án được đưa vào khi có. Mọi chính sách filesystem hiện có tại ranh giới dự án được chọn phải hợp lệ; cwd không có dự án vẫn được hỗ trợ mà không cần cấu hình.

Lệnh này không truy cập mạng. Nếu một lệnh hoạt động như phiên bản Spec Kit cũ hơn hoặc thiếu một tính năng CLI mong đợi, hãy chạy `specify self check` để kiểm tra CLI cục bộ có đang chậm hơn bản phát hành mới nhất không.

<a id="version-information"></a>

## Thông tin phiên bản

```bash
specify version
```

Hiển thị phiên bản Spec Kit CLI, phiên bản Python, nền tảng và kiến trúc.

Để xem khả năng của CLI cục bộ mà không kiểm tra mạng:

```bash
specify version --features
```

Để in đầy đủ thông tin phiên bản, runtime, hệ thống và tính năng dưới dạng JSON, dùng:

```bash
specify version --json
```

Kết hợp `--features` và `--json` cho cùng đầu ra JSON đầy đủ; `--features` không lọc kết quả ở chế độ JSON. Nếu không có thông tin OpenSSL, `runtime.openssl` là `null`. Đầu ra JSON thành công chỉ được ghi ra stdout. Khi thất bại, stdout để trống và một đối tượng lỗi JSON đã làm sạch được ghi ra stderr.

Cũng có thể kiểm tra nhanh phiên bản bằng:

```bash
specify --version
specify -V
```

<a id="experimental-mcp-server"></a>

## MCP server thử nghiệm

```bash
specify mcp
```

Khởi động MCP server thử nghiệm chỉ dùng stdio. Server ban đầu chỉ cung cấp lệnh JSON ổn định `version` thông qua các công cụ chung list, describe và run. Xem [tài liệu tham khảo MCP server](mcp.md) để biết tên công cụ, hợp đồng kết quả và các giới hạn hiện tại.
