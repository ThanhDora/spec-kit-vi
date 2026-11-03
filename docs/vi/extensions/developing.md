<a id="developing-extensions"></a>

# Phát triển extension

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../extensions/developing.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hướng dẫn tạo extension cho Spec Kit bằng bố cục skills của GitHub Copilot. Gọi skill trong khung chat Copilot bằng tên có gạch nối như `/speckit-my-ext-hello`. Manifest extension vẫn dùng định danh lệnh dấu chấm như `speckit.my-ext.hello`; Spec Kit hiển thị chúng thành skill Copilot khi cài đặt.

---

<a id="quick-start"></a>

## Bắt đầu nhanh

<a id="1-create-extension-directory"></a>

### 1. Tạo thư mục extension

```bash
mkdir my-extension
cd my-extension
```

<a id="2-create-extensionyml-manifest"></a>

### 2. Tạo manifest `extension.yml`

```yaml
schema_version: "1.0"

extension:
  id: "my-ext"                          # Lowercase, alphanumeric + hyphens only
  name: "My Extension"
  version: "1.0.0"                      # Semantic versioning
  description: "My custom extension"
  author: "Your Name"
  repository: "https://github.com/you/spec-kit-my-ext"
  license: "MIT"

requires:
  speckit_version: ">=0.1.0"            # Minimum spec-kit version
  tools:                                # Optional: External tools required
    - name: "my-tool"
      required: true
      version: ">=1.0.0"
  commands:                             # Optional: Core commands needed
    - "speckit.tasks"

provides:
  commands:
    - name: "speckit.my-ext.hello"      # Must follow pattern: speckit.{ext-id}.{cmd}
      file: "commands/hello.md"
      description: "Say hello"

  config:                               # Optional: Config files
    - name: "my-ext-config.yml"
      template: "my-ext-config.template.yml"
      description: "Extension configuration"
      required: false

hooks:                                  # Optional: Integration hooks
  after_tasks:
    command: "speckit.my-ext.hello"
    optional: true
    prompt: "Run hello command?"

tags:                                   # Optional: For catalog search
  - "example"
  - "utility"
```

<a id="3-create-commands-directory"></a>

### 3. Tạo thư mục commands

```bash
mkdir commands
```

<a id="4-create-command-file"></a>

### 4. Tạo file lệnh

**File**: `commands/hello.md`

````markdown
---
description: "Say hello command"
tools:                              # Optional: AI tools this command uses
  - 'some-tool/function'
scripts:                            # Optional: Helper scripts
  sh: ../../scripts/bash/helper.sh
  ps: ../../scripts/powershell/helper.ps1
---

# Hello Command

This command says hello!

## User Input

$ARGUMENTS

## Steps

1. Greet the user
2. Show extension is working

```bash
echo "Hello from my extension!"
echo "Arguments: $ARGUMENTS"
```

## Extension Configuration

Load extension config from `.specify/extensions/my-ext/my-ext-config.yml`.
````

<a id="5-test-locally"></a>

### 5. Kiểm thử cục bộ

```bash
cd /path/to/spec-kit-project
specify integration install copilot --integration-options="--skills"
specify extension add --dev /path/to/my-extension
```

Với dự án mới, khởi tạo bằng `specify init my-project --integration copilot --integration-options="--skills"`. Nếu Copilot đã được cài theo bố cục commands, hãy làm theo [hướng dẫn chuyển đổi Copilot](../integrations/copilot.md#commands-layout) thay vì cài lại.

<a id="6-verify-installation"></a>

### 6. Xác minh cài đặt

```bash
specify extension list

# Should show:
#  ✓ My Extension (v1.0.0)
#     My custom extension
#     Commands: 1 | Hooks: 1 | Status: Enabled
```

<a id="7-test-skill"></a>

### 7. Thử skill

Mở khung chat GitHub Copilot và gọi skill:

```text
/speckit-my-ext-hello world
```

Skill được sinh ra có tại `.github/skills/speckit-my-ext-hello/SKILL.md`. Lời gọi này thực hiện trong khung chat Copilot, không phải trong terminal.

---

<a id="manifest-schema-reference"></a>

## Tài liệu tham khảo schema manifest

<a id="required-fields"></a>

### Trường bắt buộc

#### `schema_version`

Phiên bản schema của manifest extension. Hiện tại: `"1.0"`

#### `extension`

Khối metadata của extension.

**Trường con bắt buộc**:

- `id`: Định danh extension (chữ thường, chữ và số, gạch nối)
- `name`: Tên dễ đọc
- `version`: Phiên bản ngữ nghĩa (ví dụ "1.0.0")
- `description`: Mô tả ngắn

**Trường con tùy chọn**:

- `author`: Tác giả extension
- `repository`: URL mã nguồn
- `license`: Định danh giấy phép SPDX
- `homepage`: URL trang chủ của extension

#### `requires`

Yêu cầu tương thích.

**Trường con bắt buộc**:

- `speckit_version`: Đặc tả phiên bản ngữ nghĩa (ví dụ ">=0.1.0,<2.0.0")

**Trường con tùy chọn**:

- `tools`: Công cụ bên ngoài cần có (mảng đối tượng công cụ)
- `commands`: Các lệnh lõi spec-kit cần có (mảng tên lệnh)
- `scripts`: Các script lõi cần có (mảng tên script)

#### `provides`

Những gì extension cung cấp.

**Trường con tùy chọn:**

- `commands`: Mảng đối tượng lệnh
- `templates`: Mảng đối tượng template
- `scripts`: Mảng đối tượng script

`hooks` và `events` là các trường manifest cấp cao nhất riêng biệt (ngang hàng với `provides`, không lồng bên trong — xem [`hooks`](#hooks) bên dưới). Cần ít nhất một trong `provides.commands`, `provides.templates`, `provides.scripts`, `hooks` hoặc `events`.

**Đối tượng lệnh**:

- `name`: Tên lệnh (phải khớp `speckit.{ext-id}.{command}`)
- `file`: Đường dẫn tới file lệnh (tương đối với thư mục gốc extension)
- `description`: Mô tả lệnh (tùy chọn)

**Đối tượng template**:

- `name`: Tên template (chữ thường, chữ và số, gạch nối — ví dụ `myext-template`)
- `file`: Đường dẫn tới file template (tương đối với thư mục gốc extension)
- `description`: Mô tả template (tùy chọn)

**Đối tượng script**:

- `name`: Tên script (chữ thường, chữ và số, gạch nối — ví dụ `myext-collect`)
- `file`: Đường dẫn tới file script (tương đối với thư mục gốc extension)
- `description`: Mô tả script (tùy chọn)
- `runtimes`: Các runtime mà script hỗ trợ (tùy chọn, mảng; tập con của `bash`, `powershell`, `python` — chỉ mang tính thông tin, không dùng để chọn hay gọi script)

Template và script do extension cung cấp luôn được phân giải theo `replace`; manifest có khóa `strategy` trên một trong các mục này sẽ bị từ chối với `ValidationError`. Các strategy kết hợp (`wrap`/`prepend`/`append`) chỉ dành cho preset.

<a id="optional-fields"></a>

### Trường tùy chọn

#### `hooks`

Hook tích hợp để tự động thực thi.

Các điểm hook có sẵn:

- `before_specify` / `after_specify`: Trước/sau khi sinh đặc tả
- `before_plan` / `after_plan`: Trước/sau khi lập kế hoạch triển khai
- `before_tasks` / `after_tasks`: Trước/sau khi sinh task
- `before_implement` / `after_implement`: Trước/sau khi triển khai
- `before_analyze` / `after_analyze`: Trước/sau khi phân tích chéo các artifact
- `before_checklist` / `after_checklist`: Trước/sau khi sinh checklist
- `before_clarify` / `after_clarify`: Trước/sau khi làm rõ đặc tả
- `before_constitution` / `after_constitution`: Trước/sau khi cập nhật constitution
- `before_bug_assess` / `after_bug_assess`: Trước/sau khi đánh giá bug (extension `bug` đi kèm)
- `before_bug_fix` / `after_bug_fix`: Trước/sau khi khắc phục bug (extension `bug` đi kèm)
- `before_bug_test` / `after_bug_test`: Trước/sau khi kiểm chứng bug (extension `bug` đi kèm)

Mỗi event nhận một đối tượng hook hoặc một danh sách đối tượng hook (nhiều lệnh trên một event).

Đối tượng hook:

- `command`: Lệnh cần thực thi (thường lấy từ `provides.commands`, nhưng có thể tham chiếu bất kỳ lệnh nào đã đăng ký)
- `priority`: Thứ tự chạy trong event (số nguyên ≥ 1, mặc định 10; nhỏ hơn chạy trước; priority bằng nhau giữ thứ tự khai báo)
- `optional`: Nếu là true, hỏi người dùng trước khi thực thi
- `prompt`: Văn bản lời nhắc cho hook tùy chọn
- `description`: Mô tả hook
- `condition`: Điều kiện thực thi (dự kiến trong tương lai)

#### `tags`

Mảng tag để tìm kiếm trong catalog.

#### `defaults`

Giá trị cấu hình mặc định của extension.

#### `config_schema`

JSON Schema để kiểm tra hợp lệ cấu hình extension.

---

<a id="command-file-format"></a>

## Định dạng file lệnh

### Frontmatter (YAML)

```yaml
---
description: "Command description"          # Required
tools:                                      # Optional
  - 'tool-name/function'
scripts:                                    # Optional
  sh: ../../scripts/bash/helper.sh
  ps: ../../scripts/powershell/helper.ps1
---
```

<a id="body-markdown"></a>

### Thân (Markdown)

Dùng Markdown chuẩn với các placeholder đặc biệt:

- `$ARGUMENTS`: Đối số do người dùng cung cấp
- `{SCRIPT}`: Được thay bằng đường dẫn script khi đăng ký
- `__SPECKIT_COMMAND_<NAME>__`: Được thay bằng lời gọi một lệnh khác, hiển thị theo ký tự phân tách của integration đang hoạt động (xem [Tham chiếu tới lệnh khác](#referencing-other-commands))

**Ví dụ**:

````markdown
## Steps

1. Parse arguments
2. Execute logic

```bash
args="$ARGUMENTS"
echo "Running with args: $args"
```
````

<a id="referencing-other-commands"></a>

### Tham chiếu tới lệnh khác

Thân lệnh là một *template* mà Spec Kit hiển thị thành skill Copilot. Khi tham chiếu tới lệnh khác từ thân đó, **đừng viết cứng cách gọi lệnh**. Hãy dùng token tham chiếu lệnh để Spec Kit hiển thị đúng cú pháp skill và extension vẫn dùng được ở nơi khác.

Dùng token `__SPECKIT_COMMAND_<NAME>__`. Trong bố cục skills của Copilot, Spec Kit phân giải nó thành lời gọi `/speckit-...`.

Mã hóa tên lệnh bằng chữ hoa, bỏ tiền tố `speckit.` và đổi mỗi dấu chấm phân tách đoạn thành dấu gạch dưới. Dấu gạch nối bên trong một đoạn được giữ nguyên là gạch nối:

| File lệnh | Token |
| --- | --- |
| `speckit.plan.md` | `__SPECKIT_COMMAND_PLAN__` |
| `speckit.bug.fix.md` | `__SPECKIT_COMMAND_BUG_FIX__` |
| `speckit.git.commit.md` | `__SPECKIT_COMMAND_GIT_COMMIT__` |
| `speckit.agent-context.update.md` | `__SPECKIT_COMMAND_AGENT-CONTEXT_UPDATE__` |

Dấu gạch dưới phân tách các đoạn lệnh, còn dấu gạch nối thuộc về đoạn chứa nó, nên `AGENT-CONTEXT_UPDATE` là hai đoạn `agent-context` và `update` chứ không phải ba. Copilot hiển thị nó thành `/speckit-agent-context-update`.

**Ví dụ** — thân lệnh chỉ cho người dùng bước tiếp theo:

```markdown
Once the assessment exists, the next step is `__SPECKIT_COMMAND_BUG_FIX__ slug=<slug>`.
```

Nó được hiển thị thành `/speckit-bug-fix slug=<slug>` trong khung chat Copilot. Các extension `bug` và `git` chính chủ chỉ dùng token này; xem `extensions/bug/commands/` để có ví dụ hoạt động.

Về định dạng gọi của các integration khác, xem [tài liệu tham khảo cách gọi lệnh](../integrations/cli.md#command-invocation) dùng chung.

<a id="script-path-rewriting"></a>

### Viết lại đường dẫn script

Lệnh extension dùng đường dẫn tương đối, được viết lại khi đăng ký:

**Trong extension**:

```yaml
scripts:
  sh: ../../scripts/bash/helper.sh
```

**Sau khi đăng ký**:

```yaml
scripts:
  sh: .specify/scripts/bash/helper.sh
```

Nhờ đó script có thể tham chiếu tới script lõi của spec-kit.

---

<a id="configuration-files"></a>

## File cấu hình

<a id="config-template"></a>

### Template cấu hình

**File**: `my-ext-config.template.yml`

```yaml
# My Extension Configuration
# Copy this to my-ext-config.yml and customize

# Example configuration
api:
  endpoint: "https://api.example.com"
  timeout: 30

features:
  feature_a: true
  feature_b: false

credentials:
  # DO NOT commit credentials!
  # Use environment variables instead
  api_key: "${MY_EXT_API_KEY}"
```

<a id="config-loading"></a>

### Nạp cấu hình

Trong lệnh của bạn, nạp cấu hình theo thứ tự ưu tiên phân lớp:

1. Mặc định của extension (`extension.yml` → `defaults`)
2. Cấu hình dự án (`.specify/extensions/my-ext/my-ext-config.yml`)
3. Ghi đè cục bộ (`.specify/extensions/my-ext/my-ext-config.local.yml` - được gitignore)
4. Biến môi trường (`SPECKIT_MY_EXT_*`)

**Ví dụ script nạp cấu hình**:

```bash
#!/usr/bin/env bash
EXT_DIR=".specify/extensions/my-ext"

# Load and merge config
config=$(yq eval '.' "$EXT_DIR/my-ext-config.yml" -o=json)

# Apply env overrides
if [ -n "${SPECKIT_MY_EXT_API_KEY:-}" ]; then
  config=$(echo "$config" | jq ".api.api_key = \"$SPECKIT_MY_EXT_API_KEY\"")
fi

echo "$config"
```

---

<a id="excluding-files-with-extensionignore"></a>

## Loại trừ file bằng `.extensionignore`

Tác giả extension có thể tạo file `.extensionignore` ở thư mục gốc extension để loại trừ file và thư mục khỏi việc sao chép khi người dùng cài extension bằng `specify extension add`. Điều này giúp giữ các file chỉ dành cho phát triển (test, cấu hình CI, nguồn tài liệu, v.v.) ngoài bản cài.

<a id="format"></a>

### Định dạng

File dùng các mẫu tương thích `.gitignore` (mỗi dòng một mẫu), dựa trên thư viện [`pathspec`](https://pypi.org/project/pathspec/):

- Dòng trống bị bỏ qua
- Dòng bắt đầu bằng `#` là comment
- `*` khớp mọi thứ **trừ** `/` (không vượt qua ranh giới thư mục)
- `**` khớp không hoặc nhiều thư mục (ví dụ `docs/**/*.draft.md`)
- `?` khớp một ký tự bất kỳ trừ `/`
- Dấu `/` ở cuối giới hạn mẫu chỉ áp dụng cho thư mục
- Mẫu chứa `/` (ngoài dấu gạch chéo ở cuối) được neo vào thư mục gốc extension
- Mẫu không có `/` khớp ở mọi độ sâu trong cây
- `!` phủ định một mẫu đã loại trừ trước đó (đưa file trở lại)
- Dấu gạch chéo ngược trong mẫu được chuẩn hóa thành gạch chéo xuôi để tương thích đa nền tảng
- Bản thân file `.extensionignore` luôn tự động bị loại trừ

<a id="example"></a>

### Ví dụ

```gitignore
# .extensionignore

# Development files
tests/
.github/
.gitignore

# Build artifacts
__pycache__/
*.pyc
dist/

# Documentation source (keep only the built README)
docs/
CONTRIBUTING.md
```

<a id="pattern-matching"></a>

### So khớp mẫu

| Mẫu | Khớp | KHÔNG khớp |
|---------|---------|----------------|
| `*.pyc` | Mọi file `.pyc` trong mọi thư mục | — |
| `tests/` | Thư mục `tests` (và toàn bộ nội dung) | File có tên `tests` |
| `docs/*.draft.md` | `docs/api.draft.md` (nằm trực tiếp trong `docs/`) | `docs/sub/api.draft.md` (lồng bên trong) |
| `.env` | File `.env` ở mọi cấp | — |
| `!README.md` | Đưa `README.md` trở lại kể cả khi nó khớp một mẫu trước đó | — |
| `docs/**/*.draft.md` | `docs/api.draft.md`, `docs/sub/api.draft.md` | — |

<a id="unsupported-features"></a>

### Tính năng không được hỗ trợ

Các tính năng sau của `.gitignore` **không áp dụng** trong ngữ cảnh này:

- **Nhiều file `.extensionignore`**: Chỉ hỗ trợ một file duy nhất ở thư mục gốc extension (`.gitignore` hỗ trợ file trong thư mục con)
- **`$GIT_DIR/info/exclude` và `core.excludesFile`**: Đây là các tính năng riêng của Git và không có tương đương ở đây
- **Phủ định bên trong thư mục đã bị loại trừ**: Vì việc sao chép file dùng `shutil.copytree`, loại trừ một thư mục sẽ ngăn hoàn toàn việc duyệt vào bên trong nó. Mẫu phủ định không thể đưa trở lại một file nằm trong thư mục mà bản thân thư mục đó đã bị loại trừ. Ví dụ, tổ hợp `tests/` rồi `!tests/important.py` sẽ **không** giữ lại `tests/important.py` — thư mục `tests/` bị bỏ qua ngay ở cấp gốc và nội dung của nó không bao giờ được xét. Để khắc phục, hãy loại trừ từng phần nội dung của thư mục thay vì chính thư mục đó (ví dụ `tests/*.pyc` và `tests/.cache/` thay vì `tests/`).

---

<a id="validation-rules"></a>

## Quy tắc kiểm tra hợp lệ

<a id="extension-id"></a>

### ID extension

- **Mẫu**: `^[a-z0-9-]+$`
- **Hợp lệ**: `my-ext`, `tool-123`, `awesome-plugin`
- **Không hợp lệ**: `MyExt` (chữ hoa), `my_ext` (gạch dưới), `my ext` (dấu cách)

<a id="extension-version"></a>

### Phiên bản extension

- **Định dạng**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Hợp lệ**: `1.0.0`, `0.1.0`, `2.5.3`
- **Không hợp lệ**: `1.0`, `v1.0.0`, `1.0.0-beta`

<a id="command-name"></a>

### Tên lệnh

- **Mẫu**: `^speckit\.[a-z0-9-]+\.[a-z0-9-]+$`
- **Hợp lệ**: `speckit.my-ext.hello`, `speckit.tool.cmd`
- **Không hợp lệ**: `my-ext.hello` (thiếu tiền tố), `speckit.hello` (không có namespace extension)

<a id="command-file-path"></a>

### Đường dẫn file lệnh

- **Bắt buộc** tương đối với thư mục gốc extension
- **Hợp lệ**: `commands/hello.md`, `commands/subdir/cmd.md`
- **Không hợp lệ**: `/absolute/path.md`, `../outside.md`

---

<a id="testing-extensions"></a>

## Kiểm thử extension

<a id="manual-testing"></a>

### Kiểm thử thủ công

1. **Tạo extension thử nghiệm** trong một dự án đã cấu hình [skill Copilot](../integrations/copilot.md#setup).
2. **Cài cục bộ**:

   ```bash
   specify extension add --dev /path/to/extension
   ```

3. **Xác minh cài đặt**:

   ```bash
   specify extension list
   ```

4. **Thử skill** trong khung chat Copilot, ví dụ `/speckit-my-ext-hello world`.
5. **Kiểm tra việc đăng ký skill**:

   ```bash
   ls .github/skills/speckit-my-ext-*/SKILL.md
   ```

6. **Gỡ extension**:

   ```bash
   specify extension remove my-ext
   ```

<a id="automated-testing"></a>

### Kiểm thử tự động

Tạo test cho extension của bạn:

```python
# tests/test_my_extension.py
import pytest
from pathlib import Path
from specify_cli.extensions import ExtensionManifest

def test_manifest_valid():
    """Test extension manifest is valid."""
    manifest = ExtensionManifest(Path("extension.yml"))
    assert manifest.id == "my-ext"
    assert len(manifest.commands) >= 1

def test_command_files_exist():
    """Test all command files exist."""
    manifest = ExtensionManifest(Path("extension.yml"))
    for cmd in manifest.commands:
        cmd_file = Path(cmd["file"])
        assert cmd_file.exists(), f"Command file not found: {cmd_file}"
```

---

<a id="distribution"></a>

## Phân phối

<a id="option-1-github-repository"></a>

### Lựa chọn 1: Repository GitHub

1. **Tạo repository**: `spec-kit-my-ext`
2. **Thêm file**:

   ```text
   spec-kit-my-ext/
   ├── extension.yml
   ├── commands/
   ├── scripts/
   ├── docs/
   ├── README.md
   ├── LICENSE
   └── CHANGELOG.md
   ```

3. **Tạo bản phát hành**: Gắn tag theo phiên bản (ví dụ `v1.0.0`)
4. **Cài từ repo**:

   ```bash
   git clone https://github.com/you/spec-kit-my-ext
   specify extension add --dev spec-kit-my-ext/
   ```

<a id="option-2-zip-archive-future"></a>

### Lựa chọn 2: Archive ZIP (tương lai)

Tạo archive ZIP và lưu trữ trên GitHub Releases:

```bash
zip -r spec-kit-my-ext-1.0.0.zip extension.yml commands/ scripts/ docs/
```

Người dùng cài bằng:

```bash
specify extension add <extension-name> --from https://github.com/.../spec-kit-my-ext-1.0.0.zip
```

<a id="option-3-community-reference-catalog"></a>

### Lựa chọn 3: Catalog tham khảo của cộng đồng

Gửi vào catalog cộng đồng để mọi người tìm thấy:

1. **Tạo GitHub release** cho extension của bạn
2. **Tạo issue** theo template [Extension Submission](https://github.com/github/spec-kit/issues/new?template=extension_submission.yml)
3. **Sau khi review**, người duy trì cập nhật catalog và extension của bạn trở nên khả dụng:
   - Người dùng có thể duyệt `catalog.community.json` để tìm extension của bạn
   - Người dùng sao chép mục đó vào `catalog.json` của họ
   - Người dùng cài bằng: `specify extension add my-ext` (từ catalog của họ)

Xem [Hướng dẫn phát hành extension](publishing.md) để có hướng dẫn gửi chi tiết.

---

<a id="best-practices"></a>

## Thực hành tốt

<a id="naming-conventions"></a>

### Quy ước đặt tên

- **ID extension**: Dùng tên mô tả rõ, có gạch nối (`jira-integration`, không phải `ji`)
- **Lệnh**: Dùng mẫu động từ-danh từ (`create-issue`, `sync-status`)
- **File cấu hình**: Khớp với ID extension (`jira-config.yml`)

<a id="documentation"></a>

### Tài liệu

- **README.md**: Tổng quan, cài đặt, cách dùng
- **CHANGELOG.md**: Lịch sử phiên bản
- **docs/**: Hướng dẫn chi tiết
- **Mô tả lệnh**: Rõ ràng, ngắn gọn

<a id="versioning"></a>

### Quản lý phiên bản

- **Tuân theo SemVer**: `MAJOR.MINOR.PATCH`
- **MAJOR**: Thay đổi phá vỡ tương thích
- **MINOR**: Tính năng mới
- **PATCH**: Sửa lỗi
- **Tăng phiên bản mỗi khi nội dung thay đổi**: đề xuất cập nhật của `specify extension update` dựa trên phiên bản, nên thay đổi nội dung được phát hành mà không tăng phiên bản sẽ không bao giờ tự động đến được các bản đã cài. Với các extension đi kèm trong repository này, việc tăng phiên bản được CI bắt buộc (`extension-version-guard.yml`): PR thay đổi file trong `extensions/<id>/` cũng phải tăng phiên bản trong `extension.yml` của extension đó và giữ `extensions/catalog.json` đồng bộ.

<a id="security"></a>

### Bảo mật

- **Không bao giờ commit bí mật**: Dùng biến môi trường
- **Kiểm tra đầu vào**: Làm sạch đối số của người dùng
- **Ghi rõ quyền truy cập**: Những file/API nào được truy cập

<a id="compatibility"></a>

### Tương thích

- **Chỉ định khoảng phiên bản**: Đừng yêu cầu một phiên bản chính xác
- **Kiểm thử với nhiều phiên bản**: Bảo đảm tương thích
- **Suy giảm nhẹ nhàng**: Xử lý trường hợp thiếu tính năng

---

<a id="example-extensions"></a>

## Extension ví dụ

<a id="minimal-extension"></a>

### Extension tối giản

Extension nhỏ nhất có thể:

```yaml
# extension.yml
schema_version: "1.0"
extension:
  id: "minimal"
  name: "Minimal Extension"
  version: "1.0.0"
  description: "Minimal example"
requires:
  speckit_version: ">=0.1.0"
provides:
  commands:
    - name: "speckit.minimal.hello"
      file: "commands/hello.md"
```

````markdown
<!-- commands/hello.md -->
---
description: "Hello command"
---

# Hello World

```bash
echo "Hello, $ARGUMENTS!"
```
````

<a id="extension-with-config"></a>

### Extension có cấu hình

Extension dùng cấu hình:

```yaml
# extension.yml
# ... metadata ...
provides:
  config:
    - name: "tool-config.yml"
      template: "tool-config.template.yml"
      required: true
```

```yaml
# tool-config.template.yml
api_endpoint: "https://api.example.com"
timeout: 30
```

````markdown
<!-- commands/use-config.md -->
# Use Config

Load config:
```bash
config_file=".specify/extensions/tool/tool-config.yml"
endpoint=$(yq eval '.api_endpoint' "$config_file")
echo "Using endpoint: $endpoint"
```
````

<a id="extension-with-hooks"></a>

### Extension có hook

Extension tự động chạy:

```yaml
# extension.yml
hooks:
  after_tasks:
    command: "speckit.auto.analyze"
    optional: false  # Always run
    description: "Analyze tasks after generation"
```

Nhiều lệnh trên một event, sắp xếp theo `priority` (nhỏ hơn chạy trước):

```yaml
# extension.yml
hooks:
  after_plan:
    - command: "speckit.my-ext.verify"
      priority: 5
      optional: false
      description: "Verify the plan"
    - command: "speckit.my-ext.report"
      priority: 10
      optional: true
      prompt: "Generate the report?"
      description: "Generate a report from the plan"
```

---

<a id="troubleshooting"></a>

## Xử lý sự cố

<a id="extension-wont-install"></a>

### Extension không cài được

**Lỗi**: `Invalid extension ID`

- **Cách sửa**: Chỉ dùng chữ thường, chữ và số + gạch nối

**Lỗi**: `Extension requires spec-kit >=0.2.0`

- **Cách sửa**: Nâng cấp Spec Kit theo [Hướng dẫn nâng cấp](../upgrade.md). `uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git` vẫn dùng được làm phương án dự phòng cài từ mã nguồn. Nếu bạn đã cài từ PyPI và muốn tiếp tục theo cách đó, hãy làm theo [hướng dẫn nâng cấp PyPI](../install/pypi.md#upgrade).

**Lỗi**: `Command file not found`

- **Cách sửa**: Bảo đảm file lệnh tồn tại tại các đường dẫn khai báo trong manifest

<a id="skills-not-registered"></a>

### Skill chưa được đăng ký

**Triệu chứng**: Skill không xuất hiện trong khung chat GitHub Copilot

**Kiểm tra**:

1. Skill được sinh ra tồn tại tại `.github/skills/speckit-my-ext-hello/SKILL.md`
2. Extension đã được cài thành công
3. Lệnh đã được đăng ký trong registry:

   ```bash
   cat .specify/extensions/.registry
   ```

**Cách sửa**: Xác nhận Copilot được cấu hình theo [bố cục skills](../integrations/copilot.md#default-skills-layout), rồi cài lại extension để kích hoạt việc đăng ký.

<a id="config-not-loading"></a>

### Cấu hình không được nạp

**Kiểm tra**:

1. File cấu hình tồn tại: `.specify/extensions/{ext-id}/{ext-id}-config.yml`
2. Cú pháp YAML hợp lệ: `yq eval '.' config.yml`
3. Biến môi trường được đặt đúng

---

<a id="getting-help"></a>

## Nhận trợ giúp

- **Issue**: Báo lỗi tại repository GitHub
- **Thảo luận**: Đặt câu hỏi trong GitHub Discussions
- **Ví dụ**: Xem `spec-kit-jira` để có ví dụ đầy đủ tính năng (Giai đoạn B)

---

<a id="next-steps"></a>

## Bước tiếp theo

1. **Tạo extension của bạn** theo hướng dẫn này
2. **Kiểm thử cục bộ** với cờ `--dev`
3. **Chia sẻ với cộng đồng** (GitHub, catalog)
4. **Cải tiến liên tục** dựa trên phản hồi

Chúc bạn mở rộng vui vẻ! 🚀

> Các ví dụ gọi agent trên trang này dùng cú pháp skills mặc định của GitHub Copilot (`/speckit-*`). Với các integration và chế độ khác, xem [Cách gọi lệnh](../integrations/cli.md#command-invocation).
