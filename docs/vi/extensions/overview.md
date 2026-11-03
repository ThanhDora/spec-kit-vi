<a id="extensions-overview"></a>

# Tổng quan về extension

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../extensions/overview.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hướng dẫn đầy đủ về cách dùng extension của Spec Kit để nâng cao quy trình làm việc.

<a id="table-of-contents"></a>

## Mục lục

1. [Giới thiệu](#introduction)
2. [Bắt đầu](#getting-started)
3. [Tìm extension](#finding-extensions)
4. [Cài extension](#installing-extensions)
5. [Dùng extension](#using-extensions)
6. [Quản lý extension](#managing-extensions)
7. [Cấu hình](#configuration)
8. [Xử lý sự cố](#troubleshooting)
9. [Thực hành tốt](#best-practices)

---

<a id="introduction"></a>

## Giới thiệu

<a id="what-are-extensions"></a>

### Extension là gì?

Extension là các package dạng mô-đun bổ sung lệnh và chức năng mới cho Spec Kit mà không làm phình framework lõi. Chúng cho phép bạn:

- **Tích hợp** với công cụ bên ngoài (Jira, Linear, GitHub, v.v.)
- **Tự động hóa** các tác vụ lặp lại bằng hook
- **Tùy biến** quy trình cho nhóm của bạn
- **Chia sẻ** giải pháp giữa các dự án

<a id="why-use-extensions"></a>

### Vì sao nên dùng extension?

- **Lõi gọn gàng**: Giữ spec-kit nhẹ và tập trung
- **Tính năng tùy chọn**: Chỉ cài những gì bạn cần
- **Do cộng đồng thúc đẩy**: Ai cũng có thể tạo và chia sẻ extension
- **Quản lý phiên bản**: Extension được đánh phiên bản độc lập

---

<a id="getting-started"></a>

## Bắt đầu

<a id="prerequisites"></a>

### Điều kiện tiên quyết

- Spec Kit phiên bản 0.1.0 trở lên
- Một dự án spec-kit (thư mục có thư mục `.specify/`)

<a id="check-your-version"></a>

### Kiểm tra phiên bản

```bash
specify version
# Should show 0.1.0 or higher
```

<a id="first-extension"></a>

### Extension đầu tiên

Hãy cài extension Jira làm ví dụ:

```bash
# 1. Search for the extension
specify extension search jira

# 2. Get detailed information
specify extension info jira

# 3. Install it
specify extension add jira

# 4. Configure it
vim .specify/extensions/jira/jira-config.yml

# 5. Use it
# (Skills are now available in GitHub Copilot)
/speckit-jira-specstoissues
```

---

<a id="finding-extensions"></a>

## Tìm extension

`specify extension search` tìm đồng thời trong **mọi catalog đang hoạt động**, mặc định bao gồm cả catalog cộng đồng. Kết quả được chú thích catalog nguồn và trạng thái cài đặt.

<a id="browse-all-extensions"></a>

### Duyệt mọi extension

```bash
specify extension search
```

Hiển thị mọi extension trong mọi catalog đang hoạt động (mặc định là catalog mặc định và catalog cộng đồng).

<a id="search-by-keyword"></a>

### Tìm theo từ khóa

```bash
# Search for "jira"
specify extension search jira

# Search for "issue tracking"
specify extension search issue
```

<a id="filter-by-tag"></a>

### Lọc theo tag

```bash
# Find all issue-tracking extensions
specify extension search --tag issue-tracking

# Find all Atlassian tools
specify extension search --tag atlassian
```

<a id="filter-by-author"></a>

### Lọc theo tác giả

```bash
# Extensions by Stats Perform
specify extension search --author "Stats Perform"
```

<a id="show-verified-only"></a>

### Chỉ hiển thị extension đã xác minh

```bash
# Only show verified extensions
specify extension search --verified
```

<a id="get-extension-details"></a>

### Xem chi tiết extension

```bash
# Detailed information
specify extension info jira
```

Hiển thị:

- Mô tả
- Yêu cầu
- Các lệnh được cung cấp
- Các hook có sẵn
- Liên kết (tài liệu, repository, changelog)
- Trạng thái cài đặt

---

<a id="installing-extensions"></a>

## Cài extension

<a id="install-from-catalog"></a>

### Cài từ catalog

```bash
# By name (from catalog)
specify extension add jira
```

Lệnh này sẽ:

1. Tải extension từ GitHub
2. Kiểm tra hợp lệ manifest
3. Kiểm tra tương thích với phiên bản spec-kit của bạn
4. Cài vào `.specify/extensions/jira/`
5. Đăng ký lệnh với agent lập trình của bạn
6. Tạo template cấu hình

<a id="install-from-url"></a>

### Cài từ URL

```bash
# From GitHub release
specify extension add <extension-name> --from https://github.com/org/spec-kit-ext/archive/refs/tags/v1.0.0.zip
```

<a id="install-from-local-directory-development"></a>

### Cài từ thư mục cục bộ (phát triển)

```bash
# For testing or development
specify extension add --dev /path/to/extension
```

<a id="installation-output"></a>

### Đầu ra khi cài đặt

```text
✓ Extension installed successfully!

Jira Integration (v1.0.0)
  Create Jira Epics, Stories, and Issues from spec-kit artifacts

Provided commands:
  • speckit-jira-specstoissues - Create Jira hierarchy from spec and tasks
  • speckit-jira-discover-fields - Discover Jira custom fields for configuration
  • speckit-jira-sync-status - Sync task completion status to Jira

⚠  Configuration may be required
   Check: .specify/extensions/jira/
```

---

<a id="using-extensions"></a>

## Dùng extension

<a id="using-extension-commands"></a>

### Dùng lệnh của extension

Extension bổ sung các skill xuất hiện trong GitHub Copilot:

```text
# In GitHub Copilot
> /speckit-jira-specstoissues
```

<a id="extension-configuration"></a>

### Cấu hình extension

Hầu hết extension cần được cấu hình:

```bash
# 1. Find the config file
ls .specify/extensions/jira/

# 2. Copy template to config
cp .specify/extensions/jira/jira-config.template.yml \
   .specify/extensions/jira/jira-config.yml

# 3. Edit configuration
vim .specify/extensions/jira/jira-config.yml

# 4. Use the extension
# (Commands will now work with your config)
```

<a id="extension-hooks"></a>

### Hook của extension

Một số extension cung cấp hook chạy sau các lệnh lõi:

**Ví dụ**: Extension Jira gắn hook vào `/speckit-tasks`

```text
# Run core command
> /speckit-tasks

# Output includes:
## Extension Hooks

**Optional Hook**: jira
Command: `/speckit-jira-specstoissues`
Description: Automatically create Jira hierarchy after task generation

Prompt: Create Jira issues from tasks?
To execute: `/speckit-jira-specstoissues`
```

Sau đó bạn có thể chọn chạy hook hoặc bỏ qua.

---

<a id="managing-extensions"></a>

## Quản lý extension

<a id="list-installed-extensions"></a>

### Liệt kê extension đã cài

```bash
specify extension list
```

Đầu ra:

```text
Installed Extensions:

  ✓ Jira Integration (v1.0.0)
     Create Jira Epics, Stories, and Issues from spec-kit artifacts
     Commands: 3 | Hooks: 1 | Status: Enabled
```

<a id="update-extensions"></a>

### Cập nhật extension

```bash
# Check for updates (all extensions)
specify extension update

# Update specific extension
specify extension update jira
```

Đầu ra:

```text
🔄 Checking for updates...

Updates available:

  • jira: 1.0.0 → 1.1.0

Update these extensions? [y/N]:
```

<a id="disable-extension-temporarily"></a>

### Tạm thời tắt extension

```bash
# Disable without removing
specify extension disable jira

✓ Extension 'jira' disabled

Commands will no longer be available. Hooks will not execute.
To re-enable: specify extension enable jira
```

<a id="re-enable-extension"></a>

### Bật lại extension

```bash
specify extension enable jira

✓ Extension 'jira' enabled
```

<a id="remove-extension"></a>

### Gỡ extension

```bash
# Remove extension (with confirmation)
specify extension remove jira

# Keep configuration when removing
specify extension remove jira --keep-config

# Force removal (no confirmation)
specify extension remove jira --force
```

---

<a id="configuration"></a>

## Cấu hình

<a id="configuration-files"></a>

### File cấu hình

Extension có thể có nhiều file cấu hình:

```text
.specify/extensions/jira/
├── jira-config.yml           # Main config (version controlled)
├── local-config.yml         # Local overrides (gitignored)
└── jira-config.template.yml  # Template (reference)
```

<a id="configuration-layers"></a>

### Các lớp cấu hình

Cấu hình được gộp theo thứ tự sau (ưu tiên cao nhất ở cuối):

1. **Mặc định của extension** (từ `extension.yml`)
2. **Cấu hình dự án** (`jira-config.yml`)
3. **Ghi đè cục bộ** (`local-config.yml`)
4. **Biến môi trường** (`SPECKIT_JIRA_*`)

<a id="example-jira-configuration"></a>

### Ví dụ: Cấu hình Jira

**Cấu hình dự án** (`.specify/extensions/jira/jira-config.yml`):

```yaml
project:
  key: "MSATS"

defaults:
  epic:
    labels: ["spec-driven"]
```

**Ghi đè cục bộ** (`.specify/extensions/jira/local-config.yml`):

```yaml
project:
  key: "MYTEST"  # Override for local development
```

**Biến môi trường**:

```bash
export SPECKIT_JIRA_PROJECT_KEY="DEVTEST"
```

Cấu hình cuối cùng sau khi phân giải dùng `DEVTEST` từ biến môi trường.

<a id="project-wide-extension-settings"></a>

### Thiết lập extension cho toàn dự án

File: `.specify/extensions.yml`

```yaml
# Extensions installed in this project
installed:
  - jira
  - linear

# Global settings
settings:
  auto_execute_hooks: true

# Hook configuration
# Available events: before_specify, after_specify, before_plan, after_plan,
#                   before_tasks, after_tasks, before_implement, after_implement,
#                   before_analyze, after_analyze, before_checklist, after_checklist,
#                   before_clarify, after_clarify, before_constitution, after_constitution,
# Bundled bug extension events (when installed):
#                   before_bug_assess, after_bug_assess, before_bug_fix, after_bug_fix,
#                   before_bug_test, after_bug_test
hooks:
  after_tasks:
    - extension: jira
      command: speckit.jira.specstoissues
      enabled: true
      optional: true
      prompt: "Create Jira issues from tasks?"
```

<a id="core-environment-variables"></a>

### Biến môi trường lõi

Ngoài các biến môi trường riêng của extension (`SPECKIT_{EXT_ID}_*`), spec-kit hỗ trợ các biến môi trường lõi:

| Biến | Mô tả | Mặc định |
|----------|-------------|---------|
| `SPECKIT_CATALOG_URL` | Ghi đè toàn bộ chồng catalog bằng một URL duy nhất (tương thích ngược) | Chồng mặc định có sẵn |
| `GH_TOKEN` / `GITHUB_TOKEN` | Token GitHub cho các request có xác thực tới URL lưu trữ trên GitHub (`raw.githubusercontent.com`, `github.com`, `api.github.com`, `codeload.github.com`). Bắt buộc khi JSON catalog hoặc file ZIP extension được lưu trong repository GitHub riêng tư. | Không có |

<a id="example-using-a-custom-catalog-for-testing"></a>

#### Ví dụ: Dùng catalog tùy chỉnh để kiểm thử

```bash
# Point to a local or alternative catalog (replaces the full stack)
export SPECKIT_CATALOG_URL="http://localhost:8000/catalog.json"

# Or use a staging catalog
export SPECKIT_CATALOG_URL="https://example.com/staging/catalog.json"
```

<a id="example-using-a-private-github-hosted-catalog"></a>

#### Ví dụ: Dùng catalog lưu trên GitHub riêng tư

```bash
# Authenticate with a token (gh CLI, PAT, or GITHUB_TOKEN in CI)
export GITHUB_TOKEN=$(gh auth token)

# Search a private catalog added via `specify extension catalog add`
specify extension search jira

# Install from a private catalog
specify extension add jira-sync
```

Token được tự động đính kèm vào các request tới domain GitHub. URL catalog không thuộc GitHub luôn được tải mà không kèm thông tin xác thực.

---

<a id="extension-catalogs"></a>

## Catalog extension

Spec Kit dùng một **chồng catalog** — danh sách catalog có thứ tự được tìm đồng thời. Mặc định có hai catalog hoạt động:

| Priority | Catalog | Cho phép cài | Mục đích |
|----------|---------|-----------------|---------|
| 1 | `catalog.json` (mặc định) | ✅ Có | Extension được tuyển chọn, cài được |
| 2 | `catalog.community.json` (cộng đồng) | ❌ Không (chỉ để tìm kiếm) | Duyệt extension của cộng đồng |

<a id="listing-active-catalogs"></a>

### Liệt kê catalog đang hoạt động

```bash
specify extension catalog list
```

<a id="managing-catalogs-via-cli"></a>

### Quản lý catalog qua CLI

Bạn có thể xem các lệnh quản lý catalog chính bằng `--help`:

```text
specify extension catalog --help

 Usage: specify extension catalog [OPTIONS] COMMAND [ARGS]...

 Manage extension catalogs
╭─ Options ────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                      │
╰──────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────╮
│ list     List all active extension catalogs.                                     │
│ add      Add a catalog to .specify/extension-catalogs.yml.                       │
│ remove   Remove a catalog from .specify/extension-catalogs.yml.                  │
╰──────────────────────────────────────────────────────────────────────────────────╯
```

<a id="adding-a-catalog-project-scoped"></a>

### Thêm catalog (phạm vi dự án)

```bash
# Add an internal catalog that allows installs
specify extension catalog add \
  --name "internal" \
  --priority 2 \
  --install-allowed \
  https://internal.company.com/spec-kit/catalog.json

# Add a discovery-only catalog
specify extension catalog add \
  --name "partner" \
  --priority 5 \
  https://partner.example.com/spec-kit/catalog.json
```

Lệnh này tạo hoặc cập nhật `.specify/extension-catalogs.yml`.

<a id="removing-a-catalog"></a>

### Gỡ catalog

```bash
specify extension catalog remove internal
```

<a id="manual-config-file"></a>

### Sửa file cấu hình thủ công

Bạn cũng có thể sửa trực tiếp `.specify/extension-catalogs.yml`:

```yaml
catalogs:
  - name: "default"
    url: "https://raw.githubusercontent.com/github/spec-kit/main/extensions/catalog.json"
    priority: 1
    install_allowed: true
    description: "Built-in catalog of installable extensions"

  - name: "internal"
    url: "https://internal.company.com/spec-kit/catalog.json"
    priority: 2
    install_allowed: true
    description: "Internal company extensions"

  - name: "community"
    url: "https://raw.githubusercontent.com/github/spec-kit/main/extensions/catalog.community.json"
    priority: 3
    install_allowed: false
    description: "Community-contributed extensions (discovery only)"
```

Bản tương đương ở cấp người dùng nằm tại `~/.specify/extension-catalogs.yml`. Cấu hình cấp dự án được ưu tiên hoàn toàn khi có một hoặc nhiều mục catalog. Danh sách rỗng `catalogs: []` sẽ quay về mặc định có sẵn.

<a id="organization-catalog-customization"></a>

## Tùy biến catalog cho tổ chức

<a id="why-customize-your-catalog"></a>

### Vì sao nên tùy biến catalog

Các tổ chức tùy biến catalog để:

- **Kiểm soát extension khả dụng** - Tuyển chọn những extension nhóm của bạn được cài
- **Lưu trữ extension riêng tư** - Các công cụ nội bộ không nên công khai
- **Tùy biến để tuân thủ** - Đáp ứng yêu cầu bảo mật/kiểm toán
- **Hỗ trợ môi trường air-gapped** - Làm việc không cần Internet

<a id="setting-up-a-custom-catalog"></a>

### Thiết lập catalog tùy chỉnh

<a id="1-create-your-catalog-file"></a>

#### 1. Tạo file catalog

Tạo file `catalog.json` chứa các extension của bạn:

```json
{
  "schema_version": "1.0",
  "updated_at": "2026-02-03T00:00:00Z",
  "catalog_url": "https://your-org.com/spec-kit/catalog.json",
  "extensions": {
    "jira": {
      "name": "Jira Integration",
      "id": "jira",
      "description": "Create Jira issues from spec-kit artifacts",
      "author": "Your Organization",
      "version": "2.1.0",
      "download_url": "https://github.com/your-org/spec-kit-jira/archive/refs/tags/v2.1.0.zip",
      "repository": "https://github.com/your-org/spec-kit-jira",
      "license": "MIT",
      "requires": {
        "speckit_version": ">=0.1.0",
        "tools": [
          {"name": "atlassian-mcp-server", "required": true}
        ]
      },
      "provides": {
        "commands": 3,
        "hooks": 1
      },
      "tags": ["jira", "atlassian", "issue-tracking"],
      "verified": true
    },
    "internal-tool": {
      "name": "Internal Tool Integration",
      "id": "internal-tool",
      "description": "Connect to internal company systems",
      "author": "Your Organization",
      "version": "1.0.0",
      "download_url": "https://internal.your-org.com/extensions/internal-tool-1.0.0.zip",
      "repository": "https://github.internal.your-org.com/spec-kit-internal",
      "license": "Proprietary",
      "requires": {
        "speckit_version": ">=0.1.0"
      },
      "provides": {
        "commands": 2
      },
      "tags": ["internal", "proprietary"],
      "verified": true
    }
  }
}
```

<a id="2-host-the-catalog"></a>

#### 2. Lưu trữ catalog

Các cách lưu trữ catalog:

| Cách | Ví dụ URL | Trường hợp sử dụng |
| ------ | ----------- | -------- |
| GitHub Pages | `https://your-org.github.io/spec-kit-catalog/catalog.json` | Công khai hoặc hiển thị trong tổ chức |
| Web server nội bộ | `https://internal.company.com/spec-kit/catalog.json` | Mạng doanh nghiệp |
| S3/lưu trữ đám mây | `https://s3.amazonaws.com/your-bucket/catalog.json` | Nhóm dùng hạ tầng đám mây |
| File server cục bộ | `http://localhost:8000/catalog.json` | Phát triển/kiểm thử |

**Yêu cầu bảo mật**: URL phải dùng HTTPS (trừ `localhost` để kiểm thử).

<a id="3-configure-your-environment"></a>

#### 3. Cấu hình môi trường

<a id="option-a-catalog-stack-config-file-recommended"></a>

##### Lựa chọn A: File cấu hình chồng catalog (khuyến nghị)

Thêm vào `.specify/extension-catalogs.yml` trong dự án của bạn:

```yaml
catalogs:
  - name: "my-org"
    url: "https://your-org.com/spec-kit/catalog.json"
    priority: 1
    install_allowed: true
```

Hoặc dùng CLI:

```bash
specify extension catalog add \
  --name "my-org" \
  --install-allowed \
  https://your-org.com/spec-kit/catalog.json
```

<a id="option-b-environment-variable-recommended-for-cicd-single-catalog"></a>

##### Lựa chọn B: Biến môi trường (khuyến nghị cho CI/CD, một catalog)

```bash
# In ~/.bashrc, ~/.zshrc, or CI pipeline
export SPECKIT_CATALOG_URL="https://your-org.com/spec-kit/catalog.json"
```

<a id="4-verify-configuration"></a>

#### 4. Xác minh cấu hình

```bash
# List active catalogs
specify extension catalog list

# Search should now show your catalog's extensions
specify extension search

# Install from your catalog
specify extension add jira
```

<a id="catalog-json-schema"></a>

### JSON schema của catalog

Các trường bắt buộc cho mỗi mục extension:

| Trường | Kiểu | Bắt buộc | Mô tả |
| ----- | ---- | -------- | ----------- |
| `name` | string | Có | Tên dễ đọc |
| `id` | string | Có | Định danh duy nhất (chữ thường, gạch nối) |
| `version` | string | Có | Phiên bản ngữ nghĩa (X.Y.Z) |
| `download_url` | string | Có | URL tới archive ZIP |
| `repository` | string | Có | URL mã nguồn |
| `description` | string | Không | Mô tả ngắn |
| `author` | string | Không | Tác giả/tổ chức |
| `license` | string | Không | Định danh giấy phép SPDX |
| `requires.speckit_version` | string | Không | Ràng buộc phiên bản |
| `requires.tools` | array | Không | Công cụ bên ngoài cần có |
| `provides.commands` | number | Không | Số lượng lệnh |
| `provides.hooks` | number | Không | Số lượng hook |
| `tags` | array | Không | Tag tìm kiếm |
| `verified` | boolean | Không | Trạng thái xác minh |

<a id="use-cases"></a>

### Trường hợp sử dụng

<a id="privateinternal-extensions"></a>

#### Extension riêng tư/nội bộ

Lưu trữ extension độc quyền tích hợp với hệ thống nội bộ:

```json
{
  "internal-auth": {
    "name": "Internal SSO Integration",
    "download_url": "https://artifactory.company.com/spec-kit/internal-auth-1.0.0.zip",
    "verified": true
  }
}
```

<a id="curated-team-catalog"></a>

#### Catalog tuyển chọn cho nhóm

Giới hạn những extension nhóm của bạn được cài:

```json
{
  "extensions": {
    "jira": { "..." },
    "github": { "..." }
  }
}
```

Chỉ `jira` và `github` xuất hiện trong `specify extension search`.

<a id="air-gapped-environments"></a>

#### Môi trường air-gapped

Với mạng không có Internet:

1. Tải file ZIP extension về file server nội bộ
2. Tạo catalog trỏ tới URL nội bộ
3. Lưu trữ catalog trên web server nội bộ

```json
{
  "jira": {
    "download_url": "https://files.internal/spec-kit/jira-2.1.0.zip"
  }
}
```

<a id="developmenttesting"></a>

#### Phát triển/kiểm thử

Kiểm thử extension mới trước khi phát hành:

```bash
# Start local server
python -m http.server 8000 --directory ./my-catalog/

# Point spec-kit to local catalog
export SPECKIT_CATALOG_URL="http://localhost:8000/catalog.json"

# Test installation
specify extension add my-new-extension
```

<a id="combining-with-direct-installation"></a>

### Kết hợp với cài đặt trực tiếp

Bạn vẫn có thể cài extension không có trong catalog bằng `--from`:

```bash
# From catalog
specify extension add jira

# Direct URL (bypasses catalog)
specify extension add <extension-name> --from https://github.com/someone/spec-kit-ext/archive/v1.0.0.zip

# Local development
specify extension add --dev /path/to/extension
```

**Lưu ý**: Cài trực tiếp từ URL sẽ hiện cảnh báo bảo mật vì extension không đến từ catalog bạn đã cấu hình.

---

<a id="troubleshooting"></a>

## Xử lý sự cố

<a id="extension-not-found"></a>

### Không tìm thấy extension

**Lỗi**: `Extension 'jira' not found in catalog

**Giải pháp**:

1. Kiểm tra chính tả: `specify extension search jira`
2. Làm mới catalog: `specify extension search --help`
3. Kiểm tra kết nối Internet
4. Có thể extension chưa được phát hành

<a id="configuration-not-found"></a>

### Không tìm thấy cấu hình

**Lỗi**: `Jira configuration not found`

**Giải pháp**:

1. Kiểm tra extension đã được cài chưa: `specify extension list`
2. Tạo cấu hình từ template:

   ```bash
   cp .specify/extensions/jira/jira-config.template.yml \
      .specify/extensions/jira/jira-config.yml
   ```

3. Cài lại extension: `specify extension remove jira && specify extension add jira`

<a id="command-not-available"></a>

### Lệnh không khả dụng

**Vấn đề**: Lệnh của extension không xuất hiện trong agent lập trình

**Giải pháp**:

1. Kiểm tra extension đang được bật: `specify extension list`
2. Khởi động lại GitHub Copilot
3. Kiểm tra file skill tồn tại:

   ```bash
   ls .github/skills/speckit-jira-*/SKILL.md
   ```

4. Cài lại extension

<a id="incompatible-version"></a>

### Phiên bản không tương thích

**Lỗi**: `Extension requires spec-kit >=0.2.0, but you have 0.1.0`

**Giải pháp**:

1. Nâng cấp spec-kit:

   ```bash
   uv tool upgrade specify-cli
   ```

2. Cài phiên bản cũ hơn của extension:

   ```bash
   specify extension add <extension-name> --from https://github.com/org/ext/archive/v1.0.0.zip
   ```

<a id="mcp-tool-not-available"></a>

### Công cụ MCP không khả dụng

**Lỗi**: `Tool 'jira-mcp-server/epic_create' not found`

**Giải pháp**:

1. Kiểm tra MCP server đã được cài
2. Kiểm tra cấu hình MCP của agent lập trình
3. Khởi động lại agent lập trình
4. Kiểm tra yêu cầu của extension: `specify extension info jira`

<a id="permission-denied"></a>

### Bị từ chối quyền truy cập

**Lỗi**: `Permission denied` khi truy cập Jira

**Giải pháp**:

1. Kiểm tra thông tin xác thực Jira trong cấu hình MCP server
2. Xác minh quyền trên dự án trong Jira
3. Kiểm tra kết nối MCP server một cách độc lập

---

<a id="best-practices"></a>

## Thực hành tốt

<a id="1-version-control"></a>

### 1. Quản lý phiên bản mã nguồn

**Nên commit**:

- `.specify/extensions.yml` (cấu hình extension của dự án)
- `.specify/extensions/*/jira-config.yml` (cấu hình dự án)

**Không commit**:

- `.specify/extensions/.cache/` (cache catalog)
- `.specify/extensions/.backup/` (bản sao lưu cấu hình)
- `.specify/extensions/*/local-config.yml` (ghi đè cục bộ)
- `.specify/extensions/.registry` (trạng thái cài đặt)

Thêm vào `.gitignore`:

```gitignore
.specify/extensions/.cache/
.specify/extensions/.backup/
.specify/extensions/*/local-config.yml
.specify/extensions/.registry
```

<a id="2-team-workflows"></a>

### 2. Quy trình làm việc nhóm

**Với nhóm**:

1. Thống nhất các extension sẽ dùng
2. Commit cấu hình extension
3. Ghi lại cách dùng extension trong README
4. Cập nhật extension cùng lúc

**Ví dụ phần README**:

```markdown
## Extensions

This project uses:
- **jira** (v1.0.0) - Jira integration
  - Config: `.specify/extensions/jira/jira-config.yml`
  - Requires: jira-mcp-server

To install: `specify extension add jira`
```

<a id="3-local-development"></a>

### 3. Phát triển cục bộ

Dùng cấu hình cục bộ khi phát triển:

```yaml
# .specify/extensions/jira/local-config.yml
project:
  key: "DEVTEST"  # Your test project

defaults:
  task:
    custom_fields:
      customfield_10002: 1  # Lower story points for testing
```

<a id="4-environment-specific-config"></a>

### 4. Cấu hình theo môi trường

Dùng biến môi trường cho CI/CD:

```bash
# .github/workflows/deploy.yml
env:
  SPECKIT_JIRA_PROJECT_KEY: ${{ secrets.JIRA_PROJECT }}

- name: Create Jira Issues
  run: specify extension add jira && ...
```

<a id="5-extension-updates"></a>

### 5. Cập nhật extension

**Kiểm tra cập nhật thường xuyên**:

```bash
# Weekly or before major releases
specify extension update
```

**Ghim phiên bản để ổn định**:

```yaml
# .specify/extensions.yml
installed:
  - id: jira
    version: "1.0.0"  # Pin to specific version
```

<a id="6-minimal-extensions"></a>

### 6. Tối giản extension

Chỉ cài những extension bạn thực sự dùng:

- Giảm độ phức tạp
- Nạp lệnh nhanh hơn
- Ít cấu hình hơn

<a id="7-documentation"></a>

### 7. Tài liệu

Ghi lại cách dùng extension trong dự án của bạn:

```markdown
# PROJECT.md

## Working with Jira

After creating tasks, sync to Jira:
1. Run `/speckit-tasks` to generate tasks
2. Run `/speckit-jira-specstoissues` to create Jira issues
3. Run `/speckit-jira-sync-status` to update status
```

---

<a id="faq"></a>

## Câu hỏi thường gặp

<a id="q-can-i-use-multiple-extensions-at-once"></a>

### H: Tôi có thể dùng nhiều extension cùng lúc không?

**Đ**: Có! Extension được thiết kế để hoạt động cùng nhau. Cài bao nhiêu tùy bạn cần.

<a id="q-do-extensions-slow-down-spec-kit"></a>

### H: Extension có làm chậm spec-kit không?

**Đ**: Không. Extension chỉ được nạp khi cần và chỉ khi lệnh của chúng được dùng.

<a id="q-can-i-create-private-extensions"></a>

### H: Tôi có thể tạo extension riêng tư không?

**Đ**: Có. Cài bằng `--dev` hoặc `--from` và giữ riêng tư. Gửi vào catalog công khai là tùy chọn.

<a id="q-how-do-i-know-if-an-extension-is-safe"></a>

### H: Làm sao biết một extension có an toàn không?

**Đ**: Tìm huy hiệu ✓ Verified. Extension đã xác minh được người duy trì review. Luôn review code của extension trước khi cài.

<a id="q-can-extensions-modify-spec-kit-core"></a>

### H: Extension có thể sửa lõi spec-kit không?

**Đ**: Không. Extension chỉ có thể thêm lệnh và hook. Chúng không thể sửa chức năng lõi.

<a id="q-what-happens-if-two-extensions-have-the-same-command-name"></a>

### H: Điều gì xảy ra nếu hai extension có cùng tên lệnh?

**Đ**: Extension dùng lệnh có namespace (`speckit.{extension}.{command}`), nên xung đột rất hiếm. Hệ thống extension sẽ cảnh báo bạn nếu xảy ra xung đột.

<a id="q-can-i-contribute-to-existing-extensions"></a>

### H: Tôi có thể đóng góp cho extension hiện có không?

**Đ**: Có! Hầu hết extension là mã nguồn mở. Xem liên kết repository trong `specify extension info {extension}`.

<a id="q-how-do-i-report-extension-bugs"></a>

### H: Làm sao để báo lỗi extension?

**Đ**: Vào repository của extension (hiển thị trong `specify extension info`) và tạo issue.

<a id="q-can-extensions-work-offline"></a>

### H: Extension có hoạt động offline được không?

**Đ**: Sau khi cài, extension hoạt động offline. Tuy nhiên, một số extension có thể cần Internet cho chức năng của chúng (ví dụ Jira cần truy cập Jira API).

<a id="q-how-do-i-backup-my-extension-configuration"></a>

### H: Làm sao sao lưu cấu hình extension?

**Đ**: Cấu hình extension nằm trong `.specify/extensions/{extension}/`. Hãy sao lưu thư mục này hoặc commit cấu hình vào git.

---

<a id="support"></a>

## Hỗ trợ

- **Vấn đề về extension**: Báo cho repository của extension (xem `specify extension info`)
- **Vấn đề về Spec Kit**: <https://github.com/github/spec-kit/issues>
- **Catalog extension**: <https://github.com/github/spec-kit/tree/main/extensions>
- **Tài liệu**: Xem [Phát triển extension](developing.md) và [Hướng dẫn phát hành extension](publishing.md)

---

*Cập nhật lần cuối: 2026-01-28* *Phiên bản Spec Kit: 0.1.0*

> Các ví dụ gọi agent trên trang này dùng cú pháp skills mặc định của GitHub Copilot (`/speckit-*`). Với các integration và chế độ khác, xem [Cách gọi lệnh](../integrations/cli.md#command-invocation).
