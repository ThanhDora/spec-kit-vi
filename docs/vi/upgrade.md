<a id="upgrade-guide"></a>

# Hướng dẫn nâng cấp

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../upgrade.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

> Bạn đã cài Spec Kit và muốn nâng cấp lên phiên bản mới nhất để có tính năng mới, bản sửa lỗi hoặc slash command được cập nhật. Hướng dẫn này đề cập cả việc nâng cấp công cụ CLI lẫn cập nhật các file trong dự án của bạn.

---

<a id="quick-reference"></a>

## Tra cứu nhanh

| Cần nâng cấp | Lệnh | Khi nào dùng |
|----------------|---------|-------------|
| **Công cụ CLI (khuyến nghị)** | `specify self upgrade` | Nâng cấp tại chỗ lên bản ổn định mới nhất. Tự phát hiện bạn đã cài qua `uv tool` hay `pipx`. |
| **Công cụ CLI — ghim phiên bản** | `specify self upgrade --tag vX.Y.Z[suffix]` | Nâng cấp lên một tag phát hành cụ thể thay vì bản ổn định mới nhất. Hậu tố chỉ giới hạn ở dạng dev, alpha/beta/rc và/hoặc build metadata. |
| **Công cụ CLI — cách thủ công dự phòng** | `uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z` | Khi chưa có `specify self upgrade` (bản cài cũ) hoặc khi bạn muốn kiểm soát rõ ràng. |
| **Công cụ CLI — cách thủ công dự phòng (pipx)** | `pipx install --force git+https://github.com/github/spec-kit.git@vX.Y.Z` | Như trên, dành cho bản cài bằng pipx. |
| **File trong dự án** | Chạy `specify integration upgrade <key>`, rồi `specify extension update` | Làm mới các file integration và extension đã cài trong dự án |
| **Cả hai** | Nâng cấp CLI, rồi cập nhật dự án | Khuyến nghị khi cập nhật phiên bản lớn (major) |

---

<a id="part-1-upgrade-the-cli-tool"></a>

## Phần 1: Nâng cấp công cụ CLI

Công cụ CLI (`specify`) tách biệt với các file trong dự án. Hãy nâng cấp nó để có tính năng mới nhất và các bản sửa lỗi.

Nếu bạn đã cài từ PyPI và muốn tiếp tục dùng cách cài đó, hãy làm theo
[hướng dẫn nâng cấp từ PyPI](install/pypi.md#upgrade). Chạy lại
`uv tool install specify-cli` không nâng cấp bản cài hiện có.

<a id="recommended-specify-self-upgrade"></a>

### Khuyến nghị: `specify self upgrade`

CLI có sẵn hai lệnh tự quản lý, tự động xử lý trường hợp thông thường:

```bash
# Check whether a newer release is available (read-only — does not modify anything)
specify self check

# Preview what would run, without actually upgrading
specify self upgrade --dry-run

# Upgrade in place to the latest stable release (auto-detects uv tool vs pipx install)
specify self upgrade

# Or pin a specific release tag (replace vX.Y.Z[suffix] with the tag you want)
specify self upgrade --tag vX.Y.Z[suffix]
```

`specify self upgrade` không kèm tham số sẽ chạy ngay, giống hành vi không hỏi lại của các lệnh như `pip install -U` và `npm update`. CLI phân loại môi trường chạy của bạn thành một trong các loại: `uv tool`, `pipx`, `uvx (ephemeral)`, source checkout hoặc không được hỗ trợ. Chỉ `uv tool` và `pipx` được nâng cấp tự động; với bản cài bằng `uv tool`, lệnh sẽ chạy ngầm `uv tool install specify-cli --force --from <git ref>` để các tag phát hành được ghim vẫn hoạt động. Các trường hợp còn lại in hướng dẫn riêng cho từng trường hợp và thoát với mã 0 mà không động vào gì.

Tag được ghim phải bắt đầu bằng `vMAJOR.MINOR.PATCH`. Hậu tố tùy chọn chỉ giới hạn ở dạng dev, alpha/beta/rc và/hoặc build metadata như `v1.0.0-rc1`, `v0.8.0.dev0`, `v0.8.0+build.42`, hoặc kết hợp `v1.0.0-rc1+build.42`; tên branch, ref dạng hash, `latest` và phiên bản không có `v` đều bị từ chối.

Đặt `SPECIFY_UPGRADE_TIMEOUT_SECS` để giới hạn thời gian chạy tối đa của tiến trình con cài đặt (mặc định: không giới hạn — nhấn `Ctrl+C` để ngắt khi cần). Nếu hết thời gian chờ nội bộ này, `specify self upgrade` thoát với mã 124 và báo rằng đã hết thời gian khi chờ tiến trình con cài đặt, kèm thời gian chờ đã cấu hình và lệnh để thử lại thủ công. Nếu chính trình cài đặt thoát với mã 124 thì mã này được truyền ra kèm thông báo `Upgrade failed. Installer exit code: 124.`, vì vậy script nên coi mã thoát 124 là chưa rõ ràng và đọc thông báo khi cần phân biệt hai trường hợp.

Nếu CLI đã cài cũ hơn bản phát hành giới thiệu `specify self upgrade`, hãy dùng các lệnh thủ công tương đương bên dưới. Các lệnh này cũng hữu ích khi bạn muốn kiểm soát rõ lệnh cài đặt.

<a id="if-you-installed-with-uv-tool-install"></a>

### Nếu bạn đã cài bằng `uv tool install`

Nâng cấp lên một bản phát hành cụ thể (xem tag mới nhất trong [Releases](https://github.com/github/spec-kit/releases)):

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

<a id="if-you-use-one-shot-uvx-commands"></a>

### Nếu bạn dùng lệnh `uvx` chạy một lần

Chỉ định tag phát hành mong muốn:

```bash
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init --here --integration copilot
```

`uvx` chạy một bản Spec Kit tạm thời cho riêng lệnh đó. Nó không cập nhật bản `specify` cài lâu dài bằng `uv tool install`, `pipx` hay trình quản lý công cụ khác. Nếu một tính năng mới chạy được qua `uvx` nhưng `specify` cục bộ vẫn báo phiên bản cũ, hãy nâng cấp CLI cài lâu dài bằng lệnh tương ứng với cách bạn đã cài.

<a id="if-you-installed-with-pipx"></a>

### Nếu bạn đã cài bằng `pipx`

Nâng cấp lên một bản phát hành cụ thể:

```bash
pipx install --force git+https://github.com/github/spec-kit.git@vX.Y.Z
```

<a id="verify-the-upgrade"></a>

### Kiểm tra kết quả nâng cấp

```bash
# Confirms the CLI is working and shows installed tools
specify check

# Confirms the installed version against the latest GitHub release
specify self check
```

`specify check` cho biết môi trường công cụ xung quanh; `specify self check` chỉ đọc và cho biết bạn đã ở bản phát hành mới nhất chưa (`Up to date: X.Y.Z`) hay đã có bản mới hơn xuất hiện giữa các lần phát hành.

---

<a id="part-2-updating-project-files"></a>

## Phần 2: Cập nhật file trong dự án

Khi Spec Kit phát hành tính năng mới (như slash command mới, template được cập nhật hoặc thay đổi về extension), bạn cần làm mới các file Spec Kit đã được cài vào dự án.

<a id="what-gets-updated"></a>

### Những gì được cập nhật?

Với dự án Spec Kit có sẵn, hãy ưu tiên cách nâng cấp dựa trên manifest:

- ✅ **File lệnh/skill của integration** (`.claude/skills/`, `.github/skills/`, `.agents/skills/`...)
- ✅ **Script và template dùng chung được quản lý** (`.specify/scripts/`, `.specify/templates/`) khi chúng không thay đổi so với bản được quản lý trước đó
- ✅ **Extension đã cài** khi bạn chạy `specify extension update`

Lệnh nâng cấp integration dùng manifest cài đặt để phát hiện các chỉnh sửa cục bộ. Nếu một file integration được quản lý đã bị sửa sau khi cài, lệnh sẽ dừng lại và yêu cầu bạn xem lại thay đổi hoặc chạy lại với `--force`.

<a id="what-stays-safe"></a>

### Những gì vẫn an toàn?

Các file sau **không bao giờ bị động tới** khi nâng cấp integration/extension dựa trên manifest:

- ✅ **Đặc tả của bạn** (`specs/001-my-feature/spec.md`...) - **ĐÃ XÁC NHẬN AN TOÀN**
- ✅ **Kế hoạch triển khai của bạn** (`specs/001-my-feature/plan.md`, `tasks.md`...) - **ĐÃ XÁC NHẬN AN TOÀN**
- ✅ **Hiến chương của bạn** (`.specify/memory/constitution.md`) khi dùng `specify integration upgrade`
- ✅ **Mã nguồn của bạn** - **ĐÃ XÁC NHẬN AN TOÀN**
- ✅ **Lịch sử git của bạn** - **ĐÃ XÁC NHẬN AN TOÀN**

Thư mục `specs/` hoàn toàn bị loại khỏi các gói template và sẽ không bao giờ bị sửa khi nâng cấp.

<a id="1-check-installed-integrations"></a>

### 1. Kiểm tra các integration đã cài

Chạy lệnh sau trong thư mục dự án:

```bash
specify integration status
```

Lệnh này báo integration mặc định, mọi integration đã cài và các file được quản lý bị sửa hoặc bị thiếu. Bạn cũng có thể xem `.specify/integration.json`; các integration đã cài được liệt kê trong `installed_integrations`.

<a id="2-upgrade-each-installed-integration"></a>

### 2. Nâng cấp từng integration đã cài

Chạy lệnh sau trong thư mục dự án:

```bash
specify integration upgrade <key>
```

Thay `<key>` bằng khóa của một integration đã cài, như `copilot`, `claude` hoặc `codex`. Trong dự án cài nhiều integration, hãy chạy lệnh một lần cho mỗi khóa đã cài.

**Ví dụ:**

```bash
specify integration upgrade claude
specify integration upgrade codex
```

Xem [tài liệu tham khảo về integration](integrations/cli.md#upgrade-an-integration) để biết các tùy chọn như `--script`, `--integration-options` và `--force`.

<a id="3-update-installed-extensions"></a>

### 3. Cập nhật các extension đã cài

Chạy:

```bash
specify extension update
```

Khi không truyền tên extension, lệnh này cập nhật mọi extension đã cài. Dùng `specify extension update <extension-id-or-name>` để chỉ cập nhật một extension. Xem [tài liệu tham khảo về extension](reference/extensions.md#update-extensions) để biết chi tiết.

<a id="fallback-re-run-init"></a>

### Phương án dự phòng: chạy lại init

Nếu dự án được tạo trước khi có manifest, thiếu metadata của integration hoặc cần khôi phục ở phạm vi rộng hơn, bạn vẫn có thể chạy lại init:

```bash
specify init --here --force --integration <your-agent>
```

Hãy coi đây là lối thoát khẩn cấp, không phải cách mặc định để nâng cấp file trong dự án. Lệnh này làm mới integration được chọn và phần khung dùng chung của dự án, nhưng không áp dụng cùng các bước kiểm tra manifest theo từng integration trước khi ghi đè file.

<a id="-important-warnings"></a>

## ⚠️ Cảnh báo quan trọng

<a id="1-constitution-file-and-memory-customizations"></a>

### 1. File hiến chương và các tùy chỉnh trong memory

`specify integration upgrade <key>` không cập nhật `.specify/memory/constitution.md`.

Cách dự phòng `specify init --here --force --integration <your-agent>` cũng giữ nguyên `.specify/memory/constitution.md` đã có; nếu file chưa tồn tại, init sẽ tạo nó từ template hiến chương hiện tại. Bạn không cần bước sao lưu/khôi phục hiến chương khi nâng cấp dựa trên manifest.

Như với mọi lần làm mới diện rộng, hãy commit hoặc sao lưu các tùy chỉnh cục bộ trước khi dùng `init --here --force` để có thể review diff kết quả.

<a id="2-custom-integration-script-or-template-modifications"></a>

### 2. Chỉnh sửa tùy chỉnh trong integration, script hoặc template

`specify integration upgrade <key>` sẽ dừng lại khi các file integration được manifest theo dõi đã bị sửa cục bộ, trừ khi bạn truyền `--force`.

Script và template dùng chung được làm mới khi chúng vẫn khớp với bản được quản lý đã ghi nhận trước đó. Các tùy chỉnh cục bộ được giữ nguyên, trừ khi bạn chủ động dùng tùy chọn force/refresh để ghi đè. Nếu bạn đã tùy chỉnh file trong `.specify/scripts/` hoặc `.specify/templates/`, hãy commit hoặc sao lưu chúng trước:

```bash
# Back up custom templates and scripts
cp -r .specify/templates .specify/templates-backup
cp -r .specify/scripts .specify/scripts-backup

# After upgrade, merge your changes back manually
```

<a id="3-duplicate-slash-commands-ide-based-agents"></a>

### 3. Slash command bị trùng (agent chạy trong IDE)

Một số agent chạy trong IDE (như Kilo Code, Cline) có thể hiển thị **slash command bị trùng** sau khi nâng cấp — cả bản cũ lẫn bản mới cùng xuất hiện.

**Cách xử lý:** Xóa thủ công các file lệnh cũ trong thư mục của agent.

**Ví dụ với Kilo Code:**

```bash
# List current and legacy Kilo command folders
ls -la .kilo/commands/
ls -la .kilocode/workflows/

# Delete old versions (example filenames - yours may differ)
rm .kilocode/workflows/speckit.specify-old.md
rm .kilocode/workflows/speckit.plan-v1.md
```

Khởi động lại IDE để làm mới danh sách lệnh.

---

<a id="behavior-change-constitution-no-longer-propagates-into-templates"></a>

## Thay đổi hành vi: `/constitution` không còn lan truyền vào template

Lệnh `/constitution` ([#3790](https://github.com/github/spec-kit/pull/3790)) giờ chỉ làm việc với
artifact của chính nó. Lệnh cập nhật
`.specify/memory/constitution.md` và ghi một Sync Impact Report, và **không còn sửa**
`plan-template.md`, `spec-template.md`, `tasks-template.md`, các file lệnh đã cài hay
tài liệu hướng dẫn.

<a id="why"></a>

### Lý do

Spec Kit dùng **phân giải lúc chạy**: `plan`, `tasks` và `analyze` đọc trực tiếp
`.specify/memory/constitution.md` ở mỗi lần chạy, còn `analyze` là công cụ chuyên kiểm tra
độ lệch. Các template chịu sự chi phối chỉ chứa một con trỏ, không chứa bản sao — `plan-template.md` có sẵn
`[Gates determined based on constitution file]`, và `/plan` điền mục đó từ hiến chương
hiện hành ở mỗi lần chạy. Việc lan truyền tạo ra bản sao của nguồn sự thật duy nhất và xung đột với
hệ thống kết hợp preset/override (một preset `replace` sẽ che mất template lõi đã bị sửa).

Rộng hơn, giờ đây Spec Kit quản trị các tài nguyên dùng chung bằng preset và extension — chứ không
phải sửa file tại chỗ. Kết hợp chính sách qua chồng phân giải giúp chính sách được sở hữu tập trung, có phiên bản
và kiểm toán được trên nhiều repository, thay vì bị đóng băng trong các bản sao riêng của từng repo mà nhóm lõi không thể thấy.

<a id="is-this-a-breaking-change-for-existing-projects"></a>

### Đây có phải thay đổi phá vỡ tương thích với dự án hiện có không?

**Không — quy trình của bạn vẫn hoạt động.** Bạn chỉ thấy khác biệt nếu đã dựa vào việc
`/constitution` sửa trực tiếp những file đó. Template chỉ là khung sườn, không phải nguồn quyết định. Khi bạn
chạy `/plan`, lệnh sao chép template vào `plan.md` riêng của từng tính năng và dựng lại phần Constitution
Check từ hiến chương hiện hành; `/analyze` kiểm định dựa trên hiến chương đó. Ngay cả khi một lần chạy
`/constitution` trước đây đã ghi cụ thể nội dung cổng kiểm soát vào `.specify/templates/plan-template.md`,
hiến chương hiện hành vẫn là nguồn sự thật lúc chạy.

Khi **nâng cấp không dùng force**, template đã được ghi cụ thể sẽ được *giữ nguyên* (hash của nó khác với
bản được quản lý đã ghi nhận, nên bước làm mới coi đó là tùy chỉnh và không ghi đè).
Không có gì bị thoái lui.

<a id="optional-cleanup--return-to-the-runtime-pointer"></a>

### Dọn dẹp tùy chọn — quay về con trỏ lúc chạy

Một phần Constitution Check bị đóng băng, điền sẵn là khung sườn hơi gây hiểu nhầm và có thể làm lệch lần chạy
`/plan` đầu tiên. Để quay hẳn về phân giải lúc chạy, hãy đặt lại nội dung mục đó trong
`.specify/templates/plan-template.md` về con trỏ:

```text
## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

[Gates determined based on constitution file]
```

Giữ nguyên phần còn lại của file. Đây là việc dọn dẹp, không phải bước chuyển đổi bắt buộc.

<a id="keeping-the-old-behavior-opt-in"></a>

### Giữ hành vi cũ (bật khi cần)

Nếu nhóm của bạn coi các template đã được ghi cụ thể là **artifact đã review và commit**, và muốn
`/constitution` tiếp tục lan truyền, hãy cài preset đi kèm **`constitution-sync`**:

```bash
specify preset add constitution-sync
```

Preset này bao bọc lệnh `/constitution` lõi và bổ sung lại bước lan truyền. Nó **không** sửa
template hay file lệnh có phiên bản do preset hoặc extension cung cấp (những file đó thuộc về
package của chúng và được kết hợp lại khi đồng bộ). Lưu ý rằng mô hình lan truyền bằng cách sửa tại chỗ này
xung đột với mô hình kết hợp mà các lệnh SDD còn lại sử dụng khi chúng được
preset/extension quản lý — xem mục "Interaction with the resolution stack" trong
`presets/constitution-sync/README.md` để hiểu các đánh đổi và khi nào nên dùng mặc định.

---

<a id="common-scenarios"></a>

## Các tình huống thường gặp

<a id="scenario-1-i-just-want-new-slash-commands"></a>

### Tình huống 1: "Tôi chỉ muốn có slash command mới"

```bash
# Upgrade CLI (auto-detects uv tool vs pipx install)
specify self upgrade

# Inspect installed integrations
specify integration status

# Update project files to get new commands
specify integration upgrade <key>
specify extension update
```

<a id="scenario-2-i-customized-templates-and-constitution"></a>

### Tình huống 2: "Tôi đã tùy chỉnh template và hiến chương"

```bash
# 1. Commit or back up customizations
git status
cp -r .specify/templates /tmp/templates-backup

# 2. Upgrade CLI
specify self upgrade

# 3. Use the manifest-aware project update first
specify integration upgrade <key>
specify extension update

# 4. If the upgrade reports modified managed files, inspect the diff before using --force
```

<a id="scenario-3-i-see-duplicate-slash-commands-in-my-ide"></a>

### Tình huống 3: "Tôi thấy slash command bị trùng trong IDE"

Điều này xảy ra với các agent chạy trong IDE (Kilo Code, Cline...).

```bash
# For Kilo Code, inspect both current and legacy command folders
ls -la .kilo/commands/
ls -la .kilocode/workflows/

# Delete old command files
rm .kilocode/workflows/speckit.old-command-name.md

# Restart your IDE
```

<a id="scenario-4-i-dont-want-the-git-extension"></a>

### Tình huống 4: "Tôi không muốn dùng extension git"

Extension git giờ chỉ được cài khi bạn chủ động bật, nên khi nâng cấp nó sẽ không được cài trừ khi bạn thêm rõ ràng.

```bash
# Upgrade CLI
specify self upgrade

# Refresh integration files and installed extensions
specify integration upgrade <key>
specify extension update

# The git extension is not added unless you run `specify extension add git`
```

Nếu sau này bạn muốn dùng các lệnh và hook của extension git, hãy cài rõ ràng:

```bash
specify extension add git
```

Dự án không dùng Git vẫn làm việc được với Spec Kit bằng cách đặt `SPECIFY_FEATURE_DIRECTORY` thành đường dẫn thư mục tính năng trước khi chạy các lệnh lập kế hoạch:

```bash
# Bash/Zsh
export SPECIFY_FEATURE_DIRECTORY="specs/001-my-feature"

# PowerShell
$env:SPECIFY_FEATURE_DIRECTORY = "specs/001-my-feature"
```

Hoặc chạy lệnh `/speckit.specify`, lệnh này tự động tạo `.specify/feature.json`.

---

<a id="troubleshooting"></a>

## Xử lý sự cố

<a id="slash-commands-not-showing-up-after-upgrade"></a>

### "Slash command không hiện ra sau khi nâng cấp"

**Nguyên nhân:** Agent chưa tải lại các file lệnh.

**Cách xử lý:**

1. **Khởi động lại hoàn toàn IDE/trình soạn thảo** (không chỉ reload cửa sổ)
2. **Với agent chạy qua CLI**, kiểm tra các file có tồn tại:

   ```bash
   ls -la .claude/skills/        # Claude Code
   ls -la .gemini/commands/      # Gemini
   ls -la .cursor/skills/      # Cursor
   ls -la .pi/prompts/           # Pi Coding Agent
   ls -la .omp/commands/         # Oh My Pi
   ```

3. **Kiểm tra thiết lập riêng của từng agent:**
   - Codex cần biến môi trường `CODEX_HOME`
   - Một số agent cần khởi động lại workspace hoặc xóa cache

<a id="will-init-overwrite-my-constitution-customizations"></a>

### "init có ghi đè các tùy chỉnh hiến chương của tôi không?"

Bản `specify init --here --force` hiện tại giữ nguyên `.specify/memory/constitution.md` đã có; nó chỉ tạo file từ template khi file chưa tồn tại.

Nếu trước đây bạn từng mất thay đổi trong hiến chương do một quy trình cũ hoặc do thay thế thủ công, hãy khôi phục từ git hoặc bản sao lưu:

```bash
# If you committed the customized constitution
git restore .specify/memory/constitution.md

# If you backed up manually
cp /tmp/constitution-backup.md .specify/memory/constitution.md
```

**Phòng ngừa:** Dùng `specify integration upgrade <key>` cho các lần cập nhật file dự án thường lệ. Nếu cần dùng cách dự phòng `specify init --here --force`, hãy commit trước để có thể review toàn bộ diff sau đó.

### "Warning: Current directory is not empty"

**Toàn văn cảnh báo:**

```text
Warning: Current directory is not empty (25 items)
Template files will be merged with existing content and may overwrite existing files
Do you want to continue? [y/N]
```

**Ý nghĩa:**

Cảnh báo này xuất hiện khi bạn chạy `specify init --here` (hoặc `specify init .`) trong thư mục đã có file. Nó cho bạn biết:

1. **Thư mục đã có nội dung** - Trong ví dụ là 25 file/thư mục
2. **Các file sẽ được gộp** - File template mới sẽ được thêm vào cạnh các file hiện có
3. **Một số file có thể bị ghi đè** - Nếu bạn đã có file Spec Kit (`.claude/`, `.specify/`...), chúng sẽ được thay bằng phiên bản mới

**Những gì bị ghi đè:**

Chỉ các file hạ tầng của Spec Kit:

- File lệnh/skill của agent (`.claude/skills/`, `.github/skills/`...)
- Script trong `.specify/scripts/`
- Template trong `.specify/templates/`
- Các file memory còn thiếu như `.specify/memory/constitution.md` có thể được tạo từ template; hiến chương đã có được giữ nguyên

**Những gì không bị động tới:**

- Thư mục `specs/` của bạn (đặc tả, kế hoạch, tác vụ)
- Các file mã nguồn của bạn
- Thư mục `.git/` và lịch sử git
- Mọi file khác không thuộc template của Spec Kit

**Cách phản hồi:**

- **Gõ `y` rồi nhấn Enter** - Tiếp tục gộp khi dùng cách dự phòng bằng init
- **Gõ `n` rồi nhấn Enter** - Hủy thao tác
- **Dùng cờ `--force`** - Bỏ qua hoàn toàn bước xác nhận này:

  ```bash
  specify init --here --force --integration copilot
  ```

**Khi bạn thấy cảnh báo này:**

- ✅ **Bình thường** khi dùng cách dự phòng bằng init trong một dự án Spec Kit có sẵn
- ✅ **Bình thường** khi thêm Spec Kit vào một codebase có sẵn
- ⚠️ **Bất thường** nếu bạn nghĩ mình đang tạo dự án mới trong thư mục rỗng

**Mẹo phòng ngừa:** Trước khi dùng cách dự phòng bằng init, hãy commit công việc hiện tại để dễ review hoặc khôi phục các file được làm mới.

<a id="cli-upgrade-doesnt-seem-to-work"></a>

### "Nâng cấp CLI có vẻ không có tác dụng"

Nếu một lệnh hoạt động như phiên bản Spec Kit cũ, trước hết hãy hỏi chính CLI:

```bash
# Read-only — prints "Up to date: X.Y.Z" or "Update available: X.Y.Z → vY.Z.W"
specify self check

# Preview the install method, current version, and target tag the upgrade would use
specify self upgrade --dry-run
```

`specify check` là bước quét môi trường offline; `specify self check` là bước tra cứu phiên bản CLI.

Nếu `self check` hiển thị sai phiên bản, hãy kiểm tra bản cài:

```bash
# Check installed tools
uv tool list

# Should show specify-cli

# Verify path
which specify

# Should point to the uv tool installation directory
```

Nếu không tìm thấy, hãy cài lại:

```bash
uv tool uninstall specify-cli
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

<a id="do-i-need-to-run-specify-every-time-i-open-my-project"></a>

### "Có phải chạy specify mỗi lần mở dự án không?"

**Trả lời ngắn:** Không, bạn chỉ chạy `specify init` một lần cho mỗi dự án, hoặc về sau như một cách khôi phục dự phòng.

**Giải thích:**

Công cụ CLI `specify` được dùng để:

- **Thiết lập ban đầu:** `specify init` để khởi tạo Spec Kit trong dự án
- **Nâng cấp file dự án thường lệ:** `specify integration upgrade <key>` và `specify extension update`
- **Khôi phục dự phòng:** `specify init --here --force` khi thiếu metadata của integration hoặc không dùng được cách dựa trên manifest
- **Chẩn đoán:** `specify check` để kiểm tra các công cụ đã cài

Sau khi đã chạy `specify init`, các slash command (như `/speckit.specify`, `/speckit.plan`...) được **cài cố định** trong thư mục agent của dự án (`.claude/`, `.github/skills/`, `.pi/prompts/`, `.omp/commands/`...). Agent lập trình AI đọc trực tiếp các file lệnh này — không cần chạy lại `specify`.

**Nếu agent không nhận ra slash command:**

1. **Kiểm tra các file lệnh có tồn tại:**

   ```bash
   # For GitHub Copilot (default skills layout)
   ls -la .github/skills/

   # For GitHub Copilot with the commands layout (--integration-options="--commands",
   # or a project created before skills became the default and upgraded since)
   ls -la .github/agents/ .github/prompts/

   # For Claude
   ls -la .claude/skills/

   # For Pi
   ls -la .pi/prompts/

   # For Oh My Pi
   ls -la .omp/commands/
   ```

2. **Khởi động lại hoàn toàn IDE/trình soạn thảo** (không chỉ reload cửa sổ)

3. **Kiểm tra bạn đang ở đúng thư mục** đã chạy `specify init`

4. **Với một số agent**, bạn có thể cần tải lại workspace hoặc xóa cache

**Vấn đề liên quan:** Nếu Copilot không mở được file cục bộ hoặc dùng lệnh PowerShell ngoài ý muốn, đó thường là vấn đề ngữ cảnh của IDE, không liên quan đến `specify`. Hãy thử:

- Khởi động lại VS Code
- Kiểm tra quyền truy cập file
- Đảm bảo thư mục workspace được mở đúng cách

---

<a id="version-compatibility"></a>

## Tương thích phiên bản

Spec Kit tuân theo semantic versioning cho các bản phát hành lớn. CLI và file dự án được thiết kế để tương thích với nhau trong cùng một phiên bản major.

**Best practice:** Giữ CLI và file dự án đồng bộ bằng cách nâng cấp cả hai cùng lúc khi chuyển phiên bản major.

---

<a id="next-steps"></a>

## Bước tiếp theo

Sau khi nâng cấp:

- **Thử các slash command mới:** Chạy `/speckit.constitution` hoặc một lệnh khác để kiểm tra mọi thứ hoạt động
- **Đọc ghi chú phát hành:** Xem [GitHub Releases](https://github.com/github/spec-kit/releases) để biết tính năng mới và các thay đổi phá vỡ tương thích
- **Cập nhật quy trình làm việc:** Nếu có lệnh mới, hãy cập nhật quy trình phát triển của nhóm
- **Xem tài liệu:** Truy cập [github.io/spec-kit](https://github.github.io/spec-kit/) để đọc các hướng dẫn mới nhất
