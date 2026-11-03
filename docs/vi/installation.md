<a id="installation-guide"></a>

# Hướng dẫn cài đặt

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../installation.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

<a id="prerequisites"></a>

## Yêu cầu trước

- **Linux/macOS** (hoặc Windows; script PowerShell đã được hỗ trợ mà không cần WSL)
- Agent lập trình AI: [Claude Code](https://www.anthropic.com/claude-code), [GitHub Copilot](https://code.visualstudio.com/), [CodeBuddy CLI](https://www.codebuddy.cn/docs/cli/installation), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Pi Coding Agent](https://pi.dev) hoặc [Oh My Pi](https://www.npmjs.com/package/@oh-my-pi/pi-coding-agent)
- [uv](https://docs.astral.sh/uv/) để quản lý package (khuyến nghị) hoặc [pipx](https://pipx.pypa.io/) để cài đặt lâu dài
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) *(tùy chọn — chỉ cần khi bật extension git)*

<a id="installation"></a>

## Cài đặt

> [!IMPORTANT]
> Spec Kit được phân phối qua hai kênh chính thức, cả hai đều do nhóm maintainer Spec Kit phát hành và duy trì: repository GitHub [github/spec-kit](https://github.com/github/spec-kit) (cài từ mã nguồn) và package [`specify-cli`](https://pypi.org/project/specify-cli/) trên [PyPI](https://pypi.org/project/specify-cli/). Cả hai cách đều được hỗ trợ cho việc cài đặt thông thường — hãy dùng các lệnh bên dưới. Sau khi cài, chạy `specify version` để kiểm tra nhanh phiên bản và môi trường chạy cục bộ. Lệnh này xác nhận `specify` đã sẵn sàng và cho biết phiên bản, nhưng không chứng minh file thực thi đến từ PyPI hay GitHub. Với môi trường offline hoặc air-gapped, wheel được build cục bộ từ repository này cũng hợp lệ.

Spec Kit hỗ trợ hai cách cài đặt:

1. **Cài từ mã nguồn (GitHub)** — cách được khuyến nghị, ghim theo một tag phát hành.
2. **Cài từ PyPI** — cài package `specify-cli` đã phát hành bằng công cụ Python bạn vẫn dùng.

<a id="install-from-source--persistent-installation-recommended"></a>

### Cài từ mã nguồn — cài đặt lâu dài (khuyến nghị)

Cài một lần, dùng ở mọi nơi. Thay `vX.Y.Z` bằng một tag phát hành trong [Releases](https://github.com/github/spec-kit/releases) — giữ chữ `v` ở đầu (ví dụ `v0.12.11`, không phải `0.12.11`):

> [!NOTE]
> Lệnh dưới đây cần **[uv](https://docs.astral.sh/uv/)**. Nếu bạn gặp lỗi `command not found: uv`, hãy [cài uv trước](install/uv.md).

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

Sau đó khởi tạo dự án:

```bash
specify init <PROJECT_NAME> --integration copilot
```

<a id="install-from-pypi"></a>

### Cài từ PyPI

Spec Kit cũng được phát hành trên PyPI dưới tên [`specify-cli`](https://pypi.org/project/specify-cli/), nên bạn có thể cài bằng trình quản lý package Python quen thuộc mà không cần trỏ tới URL Git:

```bash
# Using uv (recommended)
uv tool install specify-cli

# Or using pipx
pipx install specify-cli

# Or using pip
pip install specify-cli
```

Nếu `specify-cli` đã được cài, các lệnh này sẽ giữ nguyên phiên bản hiện có, kể cả khi đã có bản mới hơn. Hãy so phiên bản mà `specify version` hiển thị với [phiên bản mới nhất trên PyPI](https://pypi.org/project/specify-cli/). Để thay bản cài cũ, dùng đúng công cụ đã cài ban đầu: `uv tool install --force specify-cli`, `pipx install --force specify-cli` hoặc `pip install --upgrade specify-cli`. Dùng công cụ khác có thể cài thêm một bản thứ hai và để `specify` cũ đứng trước trên `PATH`. CLI cũ không thể thiết lập dự án từ các bản phát hành hiện tại: chẳng hạn với 0.1.6, `specify init --integration ...` báo lỗi `No such option: --integration`, còn `specify init --ai ...` báo lỗi `No matching release asset found`.

Để cài một bản phát hành cụ thể, hãy ghim phiên bản — ví dụ `uv tool install specify-cli==0.12.11`. Xem [hướng dẫn cài đặt từ PyPI](install/pypi.md) để biết chi tiết, bao gồm cách nâng cấp và cách [cài từ package index tùy chỉnh hoặc riêng tư](install/pypi.md#install-from-a-custom-or-private-package-index).

<a id="one-time-usage"></a>

### Dùng một lần

Chạy trực tiếp mà không cần cài — xem hướng dẫn [Dùng một lần (uvx)](install/one-time.md).

<a id="alternative-package-managers"></a>

### Trình quản lý package khác

- **PyPI** — xem [hướng dẫn cài đặt từ PyPI](install/pypi.md)
- **pipx** — xem [hướng dẫn cài đặt bằng pipx](install/pipx.md)
- **Doanh nghiệp / Air-gapped** — xem [hướng dẫn cài đặt air-gapped](install/air-gapped.md)

<a id="specify-integration"></a>

### Chọn integration

Trong terminal tương tác, bạn sẽ được hỏi chọn integration cho agent lập trình khi khởi tạo. Các phiên không tương tác, như CI hoặc khi chạy qua pipe, mặc định dùng GitHub Copilot trừ khi bạn truyền `--integration`.

Bạn có thể chỉ định trước integration cho agent lập trình khi khởi tạo:

```bash
specify init <project_name> --integration claude
specify init <project_name> --integration gemini
specify init <project_name> --integration copilot
specify init <project_name> --integration codebuddy
specify init <project_name> --integration pi
specify init <project_name> --integration omp
```

Các ví dụ trong README dùng chế độ skills mặc định của GitHub Copilot. Để dùng
agent được hỗ trợ khác, thay `copilot` bằng
[khóa integration](integrations/index.md) của agent đó. Xem
[Cách gọi lệnh](integrations/cli.md#command-invocation) để biết cú pháp
mà từng agent và chế độ sử dụng.

<a id="specify-script-type-shell-powershell-or-python"></a>

### Chọn loại script (Shell, PowerShell hoặc Python)

Các script tự động hóa có ba biến thể: Bash (`.sh`), PowerShell (`.ps1`) và Python (`.py`).

Hành vi tự động:

- Mặc định trên Windows: `ps`
- Mặc định trên hệ điều hành khác: `sh`
- Chế độ tương tác: bạn sẽ được hỏi, trừ khi đã truyền `--script`

Bắt buộc dùng một loại script cụ thể:

```bash
specify init <project_name> --script sh
specify init <project_name> --script ps
specify init <project_name> --script py
```

<a id="ci-and-ai-agent-harnesses"></a>

### CI và môi trường chạy agent AI

Với môi trường không có bàn phím, hoặc PTY không gửi được phím mũi tên, hãy truyền
`--non-interactive` để quá trình khởi tạo không bao giờ chờ ở bước chọn:

```bash
specify init my-project --non-interactive --ignore-agent-tools
```

`--ignore-agent-tools` bỏ qua bước kiểm tra file thực thi của agent khi agent sẽ chạy
ở nơi khác; bỏ cờ này nếu bạn muốn giữ bước kiểm tra. Khởi tạo không tương tác
mặc định dùng Copilot, trừ khi bạn chọn rõ một integration khác.

Với thư mục không rỗng, `--force` xác nhận rằng bạn đã đọc cảnh báo gộp file. Hãy xem
[hướng dẫn cho dự án có sẵn](guides/existing-projects.md) và commit hoặc sao lưu các thay đổi
cục bộ trước khi khởi tạo:

```bash
specify init --here --force --non-interactive --integration claude
```

<a id="ignore-agent-tools-check"></a>

### Bỏ qua kiểm tra công cụ của agent

Nếu bạn chỉ muốn lấy template mà không kiểm tra công cụ cần thiết:

```bash
specify init <project_name> --integration claude --ignore-agent-tools
```

<a id="verification"></a>

## Kiểm tra

Sau khi cài đặt, chạy lệnh sau để kiểm tra phiên bản và môi trường chạy cục bộ:

```bash
specify version
```

Lệnh này xác nhận `specify` đã sẵn sàng và báo đúng phiên bản mong đợi. Nó không chứng minh file thực thi đó đến từ PyPI hay GitHub.

**Luôn cập nhật:** Thỉnh thoảng hãy chạy `specify self check` để biết đã có bản phát hành mới hơn chưa — lệnh này chỉ đọc và không bao giờ sửa bản cài của bạn. Khi sẵn sàng nâng cấp, hãy làm theo [Hướng dẫn nâng cấp](upgrade.md).

Sau khi khởi tạo, bạn sẽ thấy các lệnh sau trong agent lập trình:

- `/speckit.specify` - Tạo đặc tả
- `/speckit.plan` - Sinh kế hoạch triển khai
- `/speckit.tasks` - Phân rã thành các tác vụ có thể thực hiện
- `/speckit.implement` - Thực hiện các tác vụ triển khai
- `/speckit.analyze` - Kiểm tra tính nhất quán giữa các artifact
- `/speckit.clarify` - Phát hiện và giải quyết các điểm mơ hồ
- `/speckit.checklist` - Sinh checklist chất lượng
- `/speckit.constitution` - Tạo hoặc cập nhật các nguyên tắc của dự án
- `/speckit.converge` - Đối chiếu codebase với các artifact và bổ sung những tác vụ còn thiếu

Script được cài vào thư mục con tương ứng với loại script đã chọn:

- `.specify/scripts/bash/` — chứa các script `.sh` (mặc định trên Linux/macOS)
- `.specify/scripts/powershell/` — chứa các script `.ps1` (mặc định trên Windows)
- `.specify/scripts/python/` — chứa các script `.py` (chọn bằng `--script py`; đồng thời cài script shell dự phòng của nền tảng)

<a id="choose-a-process"></a>

## Chọn quy trình

Sau khi khởi tạo, mở agent lập trình trong thư mục dự án và
làm theo [hướng dẫn nhanh SDD](quickstart.md),
[hướng dẫn nhanh sửa lỗi](guides/bugfix.md) hoặc
[hướng dẫn nhanh đánh giá ý tưởng](guides/assessment.md). Đây là các điểm bắt đầu
độc lập. SDD dùng được ngay; các hướng dẫn còn lại chỉ cách cài extension
đi kèm (bundled) mà bạn chủ động bật.

<a id="troubleshooting"></a>

## Xử lý sự cố

<a id="enterprise--air-gapped-installation"></a>

### Cài đặt cho doanh nghiệp / air-gapped

Nếu môi trường của bạn chặn truy cập PyPI hoặc GitHub, xem hướng dẫn [Cài đặt cho doanh nghiệp / air-gapped](install/air-gapped.md) để biết từng bước tạo gói wheel mang đi được.

<a id="git-credential-manager-on-linux"></a>

### Git Credential Manager trên Linux

Nếu bạn gặp vấn đề xác thực Git trên Linux, xem [hướng dẫn cài đặt air-gapped](install/air-gapped.md#git-credential-manager-on-linux) để biết cách thiết lập Git Credential Manager.
