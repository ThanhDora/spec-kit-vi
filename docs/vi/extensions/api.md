<a id="extension-api-reference"></a>

# Tài liệu tham khảo API extension

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../extensions/api.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Tài liệu kỹ thuật về các API và schema manifest của hệ thống extension trong Spec Kit.

<a id="table-of-contents"></a>

## Mục lục

1. [Manifest extension](#extension-manifest)
2. [Python API](#python-api)
3. [Định dạng file lệnh](#command-file-format)
4. [Schema cấu hình](#configuration-schema)
5. [Hệ thống hook](#hook-system)
6. [Lệnh CLI](#cli-commands)

---

<a id="extension-manifest"></a>

## Manifest extension

<a id="schema-version-10"></a>

### Schema phiên bản 1.0

File: `extension.yml`

```yaml
schema_version: "1.0"  # Required

extension:
  id: string           # Required, pattern: ^[a-z0-9-]+$
  name: string         # Required, human-readable name
  version: string      # Required, semantic version (X.Y.Z)
  description: string  # Required, brief description (<200 chars)
  author: string       # Required
  repository: string   # Required, valid URL
  license: string      # Required (e.g., "MIT", "Apache-2.0")
  homepage: string     # Optional, valid URL

requires:
  speckit_version: string  # Required, version specifier (>=X.Y.Z)
  tools:                   # Optional, array of tool requirements
    - name: string         # Tool name
      version: string      # Optional, version specifier
      required: boolean    # Optional, default: false

provides:
  commands:              # At least one of commands/templates/scripts/hooks/events required
    - name: string       # Required, pattern: ^speckit\.[a-z0-9-]+\.[a-z0-9-]+$
      file: string       # Required, relative path to command file
      description: string # Required

  templates:             # Optional, array of declared templates. Always resolve
                          # as "replace" -- 'strategy' is not an authorable field here.
    - name: string       # Required, pattern: ^[a-z0-9-]+$
      file: string       # Required, relative path to template file
      description: string # Optional

  scripts:               # Optional, array of declared scripts. Always resolve
                          # as "replace" -- 'strategy' is not an authorable field here.
    - name: string       # Required, pattern: ^[a-z0-9-]+$
      file: string       # Required, relative path to script file
      description: string # Optional
      runtimes: [string] # Optional, subset of: bash, powershell, python

  config:                # Optional, array of config files
    - name: string       # Config file name
      template: string   # Template file path
      description: string
      required: boolean  # Default: false

hooks:                   # Optional, event hooks. Each event accepts either form below.
  event_name:            # e.g., "after_specify", "after_plan", "after_tasks", "after_implement"
    command: string      # Command to execute
    priority: integer    # Optional, >= 1, default 10 (lower runs first)
    optional: boolean    # Default: true
    prompt: string       # Prompt text for optional hooks
    description: string  # Hook description
    condition: string    # Optional, condition expression
  another_event:         # Any event may instead use a list of mappings (multiple commands)
    - command: string    # Same fields as the single mapping, per entry
      priority: integer
    - command: string
      priority: integer

tags:                    # Optional, array of tags (2-10 recommended)
  - string

defaults:                # Optional, default configuration values
  key: value             # Any YAML structure
```

<a id="field-specifications"></a>

### Đặc tả các trường

#### `extension.id`

- **Kiểu**: string
- **Mẫu**: `^[a-z0-9-]+$`
- **Mô tả**: Định danh duy nhất của extension
- **Ví dụ**: `jira`, `linear`, `azure-devops`
- **Không hợp lệ**: `Jira`, `my_extension`, `extension.id`

#### `extension.version`

- **Kiểu**: string
- **Định dạng**: Semantic versioning (X.Y.Z)
- **Mô tả**: Phiên bản extension
- **Ví dụ**: `1.0.0`, `0.9.5`, `2.1.3`
- **Không hợp lệ**: `v1.0`, `1.0`, `1.0.0-beta`

#### `requires.speckit_version`

- **Kiểu**: string
- **Định dạng**: Đặc tả phiên bản
- **Mô tả**: Khoảng phiên bản spec-kit yêu cầu
- **Ví dụ**:
  - `>=0.1.0` - Mọi phiên bản từ 0.1.0 trở lên
  - `>=0.1.0,<2.0.0` - Phiên bản 0.1.x hoặc 1.x
  - `==0.1.0` - Đúng phiên bản 0.1.0
- **Không hợp lệ**: `0.1.0`, `>= 0.1.0` (có dấu cách), `latest`

#### `provides.commands[].name`

- **Kiểu**: string
- **Mẫu**: `^speckit\.[a-z0-9-]+\.[a-z0-9-]+$`
- **Mô tả**: Tên lệnh có namespace
- **Định dạng**: `speckit.{extension-id}.{command-name}`
- **Ví dụ**: `speckit.jira.specstoissues`, `speckit.linear.sync`
- **Không hợp lệ**: `jira.specstoissues`, `speckit.command`, `speckit.jira.CreateIssues`

#### `provides.templates[].name` / `provides.scripts[].name`

- **Kiểu**: string
- **Mẫu**: `^[a-z0-9-]+$`
- **Mô tả**: Khác với lệnh, template và script không được gọi theo tên, nên chúng dùng cùng mẫu slug đơn giản như `extension.id` thay vì mẫu lệnh có namespace.
- **Ví dụ**: `myext-template`, `myext-collect`

#### `provides.templates[].strategy` / `provides.scripts[].strategy`

- Không phải trường do tác giả khai báo. Template và script do extension đóng góp luôn được phân giải theo `replace`; manifest có khóa `strategy` trên một trong các mục này sẽ bị từ chối với `ValidationError`. Các strategy kết hợp (`wrap`/`prepend`/`append`) chỉ dành cho preset.

#### `provides.scripts[].runtimes`

- **Kiểu**: array of strings
- **Giá trị**: `bash`, `powershell`, `python`
- **Mô tả**: Khai báo các runtime mà script hỗ trợ. Chỉ là metadata mang tính thông tin — không được dùng để chọn hay gọi script.

#### `hooks`

- **Kiểu**: object
- **Khóa**: Tên event (ví dụ `after_specify`, `after_plan`, `after_tasks`, `after_implement`, `before_analyze`)
- **Giá trị**: Một mapping hook, hoặc một danh sách mapping hook để đăng ký nhiều lệnh trên một event
- **Mô tả**: Các hook thực thi tại các event trong vòng đời
- **Event**: Do các lệnh lõi của spec-kit định nghĩa
- **Thứ tự**: Trong một event, hook chạy theo `priority` tăng dần (số nguyên ≥ 1, mặc định 10; nhỏ hơn chạy trước; priority bằng nhau giữ thứ tự khai báo nhờ sắp xếp ổn định)

---

## Python API

### ExtensionManifest

**Module**: `specify_cli.extensions`

```python
from specify_cli.extensions import ExtensionManifest

manifest = ExtensionManifest(Path("extension.yml"))
```

**Thuộc tính**:

```python
manifest.id                        # str: Extension ID
manifest.name                      # str: Extension name
manifest.version                   # str: Version
manifest.description               # str: Description
manifest.requires_speckit_version  # str: Required spec-kit version
manifest.commands                  # List[Dict]: Command definitions
manifest.templates                 # List[Dict]: Declared template definitions
manifest.scripts                   # List[Dict]: Declared script definitions
manifest.hooks                     # Dict: Hook definitions
```

**Phương thức**:

```python
manifest.get_hash()  # str: SHA256 hash of manifest file
```

**Ngoại lệ**:

```python
ValidationError       # Invalid manifest structure
CompatibilityError    # Incompatible with current spec-kit version
```

### ExtensionRegistry

**Module**: `specify_cli.extensions`

```python
from specify_cli.extensions import ExtensionRegistry

registry = ExtensionRegistry(extensions_dir)
```

**Phương thức**:

```python
# Add extension to registry
registry.add(extension_id: str, metadata: dict)

# Remove extension from registry
registry.remove(extension_id: str)

# Get extension metadata
metadata = registry.get(extension_id: str)  # Optional[dict]

# List all extensions
extensions = registry.list()  # Dict[str, dict]

# Check if installed
is_installed = registry.is_installed(extension_id: str)  # bool
```

**Định dạng registry**:

```json
{
  "schema_version": "1.0",
  "extensions": {
    "jira": {
      "version": "1.0.0",
      "source": "catalog",
      "manifest_hash": "sha256...",
      "enabled": true,
      "registered_commands": ["speckit.jira.specstoissues", ...],
      "installed_at": "2026-01-28T..."
    }
  }
}
```

### ExtensionManager

**Module**: `specify_cli.extensions`

```python
from specify_cli.extensions import ExtensionManager

manager = ExtensionManager(project_root)
```

**Phương thức**:

```python
# Install from directory
manifest = manager.install_from_directory(
    source_dir: Path,
    speckit_version: str,
    register_commands: bool = True
)  # Returns: ExtensionManifest

# Install from ZIP
manifest = manager.install_from_zip(
    zip_path: Path,
    speckit_version: str
)  # Returns: ExtensionManifest

# Remove extension
success = manager.remove(
    extension_id: str,
    keep_config: bool = False
)  # Returns: bool

# List installed extensions
extensions = manager.list_installed()  # List[Dict]

# Get extension manifest
manifest = manager.get_extension(extension_id: str)  # Optional[ExtensionManifest]

# Check compatibility
manager.check_compatibility(
    manifest: ExtensionManifest,
    speckit_version: str
)  # Raises: CompatibilityError if incompatible
```

### CatalogEntry

**Module**: `specify_cli.extensions`

Đại diện cho một catalog trong chồng catalog đang hoạt động.

```python
from specify_cli.extensions import CatalogEntry

entry = CatalogEntry(
    url="https://example.com/catalog.json",
    name="default",
    priority=1,
    install_allowed=True,
    description="Built-in catalog of installable extensions",
)
```

**Trường**:

| Trường | Kiểu | Mô tả |
|-------|------|-------------|
| `url` | `str` | URL catalog (phải dùng HTTPS, hoặc HTTP cho localhost) |
| `name` | `str` | Tên catalog dễ đọc |
| `priority` | `int` | Thứ tự sắp xếp (nhỏ hơn = ưu tiên cao hơn, thắng khi xung đột) |
| `install_allowed` | `bool` | Có cho phép cài extension từ catalog này hay không |
| `description` | `str` | Mô tả dễ đọc tùy chọn của catalog (mặc định: rỗng) |

### ExtensionCatalog

**Module**: `specify_cli.extensions`

```python
from specify_cli.extensions import ExtensionCatalog

catalog = ExtensionCatalog(project_root)
```

**Thuộc tính lớp**:

```python
ExtensionCatalog.DEFAULT_CATALOG_URL    # default catalog URL
ExtensionCatalog.COMMUNITY_CATALOG_URL  # community catalog URL
```

**Phương thức**:

```python
# Get the ordered list of active catalogs
entries = catalog.get_active_catalogs()  # List[CatalogEntry]

# Fetch catalog (primary catalog, backward compat)
catalog_data = catalog.fetch_catalog(force_refresh: bool = False)  # Dict

# Search extensions across all active catalogs
# Each result includes _catalog_name and _install_allowed
results = catalog.search(
    query: Optional[str] = None,
    tag: Optional[str] = None,
    author: Optional[str] = None,
    verified_only: bool = False
)  # Returns: List[Dict]  — each dict includes _catalog_name, _install_allowed

# Get extension info (searches all active catalogs)
# Returns None if not found; includes _catalog_name and _install_allowed
ext_info = catalog.get_extension_info(extension_id: str)  # Optional[Dict]

# Check cache validity (primary catalog)
is_valid = catalog.is_cache_valid()  # bool

# Clear all catalog caches
catalog.clear_cache()
```

**Các trường chú thích kết quả**:

Mỗi dict extension do `search()` và `get_extension_info()` trả về đều có:

| Trường | Kiểu | Mô tả |
|-------|------|-------------|
| `_catalog_name` | `str` | Tên catalog nguồn |
| `_install_allowed` | `bool` | Có cho phép cài đặt từ catalog này hay không |

**File cấu hình catalog** (`.specify/extension-catalogs.yml`):

```yaml
catalogs:
  - name: "default"
    url: "https://raw.githubusercontent.com/github/spec-kit/main/extensions/catalog.json"
    priority: 1
    install_allowed: true
    description: "Built-in catalog of installable extensions"
  - name: "community"
    url: "https://raw.githubusercontent.com/github/spec-kit/main/extensions/catalog.community.json"
    priority: 2
    install_allowed: false
    description: "Community-contributed extensions (discovery only)"
```

### HookExecutor

**Module**: `specify_cli.extensions`

```python
from specify_cli.extensions import HookExecutor

hook_executor = HookExecutor(project_root)
```

**Phương thức**:

```python
# Get project config
config = hook_executor.get_project_config()  # Dict

# Save project config
hook_executor.save_project_config(config: Dict)

# Register hooks
hook_executor.register_hooks(manifest: ExtensionManifest)

# Unregister hooks
hook_executor.unregister_hooks(extension_id: str)

# Get hooks for event
hooks = hook_executor.get_hooks_for_event(event_name: str)  # List[Dict]

# Check if hook should execute
should_run = hook_executor.should_execute_hook(hook: Dict)  # bool

# Format hook message
message = hook_executor.format_hook_message(
    event_name: str,
    hooks: List[Dict]
)  # str
```

### CommandRegistrar

**Module**: `specify_cli.extensions`

```python
from specify_cli.extensions import CommandRegistrar

registrar = CommandRegistrar()
```

**Phương thức**:

```python
# Register commands for Claude Code
registered = registrar.register_commands_for_claude(
    manifest: ExtensionManifest,
    extension_dir: Path,
    project_root: Path
)  # Returns: List[str] (command names)

# Parse frontmatter
frontmatter, body = registrar.parse_frontmatter(content: str)

# Render frontmatter
yaml_text = registrar.render_frontmatter(frontmatter: Dict)  # str
```

---

<a id="command-file-format"></a>

## Định dạng file lệnh

<a id="universal-command-format"></a>

### Định dạng lệnh chung

**File**: `commands/{command-name}.md`

```markdown
---
description: "Command description"
tools:
  - 'mcp-server/tool_name'
  - 'other-mcp-server/other_tool'
---

# Command Title

Command documentation in Markdown.

## Prerequisites

1. Requirement 1
2. Requirement 2

## User Input

$ARGUMENTS

## Steps

### Step 1: Description

Instruction text...

\`\`\`bash
# Shell commands
\`\`\`

### Step 2: Another Step

More instructions...

## Configuration Reference

Information about configuration options.

## Notes

Additional notes and tips.
```

<a id="frontmatter-fields"></a>

### Các trường frontmatter

```yaml
description: string   # Required, brief command description
tools: [string]       # Optional, MCP tools required
```

<a id="special-variables"></a>

### Biến đặc biệt

- `$ARGUMENTS` - Placeholder cho đối số do người dùng cung cấp
- Ngữ cảnh extension được tự động chèn vào:

  ```markdown
  <!-- Extension: {extension-id} -->
  <!-- Config: .specify/extensions/{extension-id}/ -->
  ```

---

<a id="configuration-schema"></a>

## Schema cấu hình

<a id="extension-config-file"></a>

### File cấu hình extension

**File**: `.specify/extensions/{extension-id}/{extension-id}-config.yml`

Extension tự định nghĩa schema cấu hình của mình. Các mẫu thường gặp:

```yaml
# Connection settings
connection:
  url: string
  api_key: string

# Project settings
project:
  key: string
  workspace: string

# Feature flags
features:
  enabled: boolean
  auto_sync: boolean

# Defaults
defaults:
  labels: [string]
  assignee: string

# Custom fields
field_mappings:
  internal_name: "external_field_id"
```

<a id="config-layers"></a>

### Các lớp cấu hình

1. **Mặc định của extension** (từ phần `defaults` trong `extension.yml`)
2. **Cấu hình dự án** (`{extension-id}-config.yml`)
3. **Ghi đè cục bộ** (`{extension-id}-config.local.yml`, được gitignore)
4. **Biến môi trường** (`SPECKIT_{EXTENSION}_*`)

<a id="environment-variable-pattern"></a>

### Mẫu biến môi trường

Định dạng: `SPECKIT_{EXTENSION}_{KEY}`

Ví dụ:

- `SPECKIT_JIRA_PROJECT_KEY`
- `SPECKIT_LINEAR_API_KEY`
- `SPECKIT_GITHUB_TOKEN`

---

<a id="hook-system"></a>

## Hệ thống hook

<a id="hook-definition"></a>

### Định nghĩa hook

Mỗi event nhận một mapping hook hoặc một danh sách mapping. Danh sách cho phép đăng ký nhiều lệnh trên cùng một event.

**Một mapping (trong extension.yml)**:

```yaml
hooks:
  after_tasks:
    command: "speckit.jira.specstoissues"
    optional: true
    prompt: "Create Jira issues from tasks?"
    description: "Automatically create Jira hierarchy"
    condition: null
```

**Danh sách mapping có priority**:

```yaml
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

Trong cùng một danh sách manifest, `command` bị lặp được khử trùng theo kiểu "cái sau thắng" và được chuyển xuống cuối, nên nó cũng phân định các trường hợp priority bằng nhau theo thứ tự khai báo.

<a id="hook-events"></a>

### Các event hook

Event chuẩn (do lõi định nghĩa):

- `before_specify` - Trước khi sinh đặc tả
- `after_specify` - Sau khi sinh đặc tả
- `before_plan` - Trước khi lập kế hoạch triển khai
- `after_plan` - Sau khi lập kế hoạch triển khai
- `before_tasks` - Trước khi sinh task
- `after_tasks` - Sau khi sinh task
- `before_implement` - Trước khi triển khai
- `after_implement` - Sau khi triển khai
- `before_analyze` - Trước khi phân tích chéo các artifact
- `after_analyze` - Sau khi phân tích chéo các artifact
- `before_checklist` - Trước khi sinh checklist
- `after_checklist` - Sau khi sinh checklist
- `before_clarify` - Trước khi làm rõ đặc tả
- `after_clarify` - Sau khi làm rõ đặc tả
- `before_constitution` - Trước khi cập nhật constitution
- `after_constitution` - Sau khi cập nhật constitution

<a id="bundled-bug-extension-events-available-when-the-extension-is-installed"></a>

#### Event của extension `bug` đi kèm (có khi extension đã được cài)

Hook là các prompt chạy trong cùng phiên; chúng dùng lại `BUG_SLUG` và `BUG_DIR` đã phân giải (và, với post-hook, cả báo cáo đã ghi) từ cuộc hội thoại, và không có biến nào được chèn vào. Pre-hook chạy sau khi phân giải slug và kiểm tra điều kiện tiên quyết; post-hook chạy sau khi báo cáo được ghi và trước khi báo hoàn tất.

- `before_bug_assess` - Sau khi thư mục bug đã tồn tại, trước khi tiếp nhận báo cáo
- `after_bug_assess` - Sau khi ghi `assessment.md`; không chạy tới khi một báo cáo không thể hiểu được khiến quy trình dừng sớm
- `before_bug_fix` - Trước khi áp dụng bản sửa
- `after_bug_fix` - Sau khi ghi `fix.md`
- `before_bug_test` - Trước khi chạy kiểm chứng
- `after_bug_test` - Sau khi ghi `test.md`

<a id="hook-configuration"></a>

### Cấu hình hook

**Trong `.specify/extensions.yml`**:

```yaml
hooks:
  after_tasks:
    - extension: jira
      command: speckit.jira.specstoissues
      enabled: true
      optional: true
      prompt: "Create Jira issues from tasks?"
      description: "..."
      condition: null
```

<a id="hook-message-format"></a>

### Định dạng thông điệp hook

```markdown
## Extension Hooks

**Optional Hook**: {extension}
Command: `/{command}`
Description: {description}

Prompt: {prompt}
To execute: `/{command}`
```

Hoặc với hook bắt buộc:

```markdown
**Automatic Hook**: {extension}
Executing: `/{command}`
EXECUTE_COMMAND: {command}
```

---

<a id="cli-commands"></a>

## Lệnh CLI

### extension list

**Cách dùng**: `specify extension list [OPTIONS]`

**Tùy chọn**:

- `--available` - Hiển thị extension có sẵn trong catalog
- `--all` - Hiển thị cả extension đã cài và có sẵn

**Đầu ra**: Danh sách extension đã cài kèm metadata

### extension catalog list

**Cách dùng**: `specify extension catalog list`

Liệt kê mọi catalog đang hoạt động trong chồng catalog hiện tại, hiển thị tên, mô tả, URL, priority và trạng thái `install_allowed`.

### extension catalog add

**Cách dùng**: `specify extension catalog add URL [OPTIONS]`

**Tùy chọn**:

- `--name NAME` - Tên catalog (bắt buộc)
- `--priority INT` - Priority (nhỏ hơn = ưu tiên cao hơn, mặc định: 10)
- `--install-allowed / --no-install-allowed` - Cho phép cài từ catalog này (mặc định: false)
- `--description TEXT` - Mô tả tùy chọn của catalog

**Đối số**:

- `URL` - URL catalog (phải dùng HTTPS)

Thêm một mục catalog vào `.specify/extension-catalogs.yml`.

### extension catalog remove

**Cách dùng**: `specify extension catalog remove NAME`

**Đối số**:

- `NAME` - Tên catalog cần gỡ

Gỡ một mục catalog khỏi `.specify/extension-catalogs.yml`.

### extension add

**Cách dùng**: `specify extension add EXTENSION [OPTIONS]`

**Tùy chọn**:

- `--from URL` - Cài từ URL tùy chỉnh
- `--dev PATH` - Cài từ thư mục cục bộ

**Đối số**:

- `EXTENSION` - Tên hoặc URL của extension

**Lưu ý**: Không thể cài bằng lệnh này các extension từ catalog có `install_allowed: false`.

### extension remove

**Cách dùng**: `specify extension remove EXTENSION [OPTIONS]`

**Tùy chọn**:

- `--keep-config` - Giữ lại file cấu hình
- `--force` - Bỏ qua bước xác nhận

**Đối số**:

- `EXTENSION` - ID extension

### extension search

**Cách dùng**: `specify extension search [QUERY] [OPTIONS]`

Tìm đồng thời trong mọi catalog đang hoạt động. Kết quả gồm tên catalog nguồn và trạng thái install_allowed.

**Tùy chọn**:

- `--tag TAG` - Lọc theo tag
- `--author AUTHOR` - Lọc theo tác giả
- `--verified` - Chỉ hiển thị extension đã xác minh

**Đối số**:

- `QUERY` - Từ khóa tìm kiếm tùy chọn

### extension info

**Cách dùng**: `specify extension info EXTENSION`

Hiển thị catalog nguồn và trạng thái install_allowed.

**Đối số**:

- `EXTENSION` - ID extension

### extension update

**Cách dùng**: `specify extension update [EXTENSION]`

**Đối số**:

- `EXTENSION` - Tùy chọn, ID extension (mặc định: tất cả)

### extension enable

**Cách dùng**: `specify extension enable EXTENSION`

**Đối số**:

- `EXTENSION` - ID extension

### extension disable

**Cách dùng**: `specify extension disable EXTENSION`

**Đối số**:

- `EXTENSION` - ID extension

---

<a id="exceptions"></a>

## Ngoại lệ

### ValidationError

Phát sinh khi manifest extension không qua kiểm tra hợp lệ.

```python
from specify_cli.extensions import ValidationError

try:
    manifest = ExtensionManifest(path)
except ValidationError as e:
    print(f"Invalid manifest: {e}")
```

### CompatibilityError

Phát sinh khi extension không tương thích với phiên bản spec-kit hiện tại.

```python
from specify_cli.extensions import CompatibilityError

try:
    manager.check_compatibility(manifest, "0.1.0")
except CompatibilityError as e:
    print(f"Incompatible: {e}")
```

### ExtensionError

Ngoại lệ cơ sở cho mọi lỗi liên quan đến extension.

```python
from specify_cli.extensions import ExtensionError

try:
    manager.install_from_directory(path, "0.1.0")
except ExtensionError as e:
    print(f"Extension error: {e}")
```

---

<a id="version-functions"></a>

## Hàm phiên bản

### version_satisfies

Kiểm tra một phiên bản có thỏa mãn đặc tả phiên bản hay không.

```python
from specify_cli.extensions import version_satisfies

# True if 1.2.3 satisfies >=1.0.0,<2.0.0
satisfied = version_satisfies("1.2.3", ">=1.0.0,<2.0.0")  # bool
```

---

<a id="file-system-layout"></a>

## Bố cục hệ thống file

```text
.specify/
├── extensions/
│   ├── .registry               # Extension registry (JSON)
│   ├── .cache/                 # Catalog cache
│   │   ├── catalog.json
│   │   └── catalog-metadata.json
│   ├── .backup/                # Config backups
│   │   └── {ext}-{config}.yml
│   ├── {extension-id}/         # Extension directory
│   │   ├── extension.yml       # Manifest
│   │   ├── {ext}-config.yml    # User config
│   │   ├── {ext}-config.local.yml  # Local overrides (gitignored)
│   │   ├── {ext}-config.template.yml  # Template
│   │   ├── commands/           # Command files
│   │   │   └── *.md
│   │   ├── scripts/            # Helper scripts
│   │   │   └── *.sh
│   │   ├── docs/               # Documentation
│   │   └── README.md
│   └── extensions.yml          # Project extension config
└── scripts/                    # (existing spec-kit)

.claude/
└── commands/
    └── speckit.{ext}.{cmd}.md  # Registered commands
```

---

*Cập nhật lần cuối: 2026-01-28* *Phiên bản API: 1.0* *Phiên bản Spec Kit: 0.1.0*
