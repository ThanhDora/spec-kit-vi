<a id="extensions"></a>

# Extension

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/extensions.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Extension bổ sung khả năng mới cho Spec Kit — lệnh chuyên biệt theo lĩnh vực, tích hợp công cụ bên ngoài, cổng chất lượng và nhiều hơn nữa. Chúng đưa vào các lệnh và template mới vượt ra ngoài workflow Phát triển hướng đặc tả có sẵn.

Một extension có thể định nghĩa lệnh hoặc hook để đối soát `spec.md`, `plan.md` và `tasks.md` trong hoặc sau khi bàn giao tính năng. Mọi chỉnh sửa như vậy tuân theo hành vi được mô tả của extension và quy tắc quản trị của dự án; chúng không do các lệnh lõi của Spec Kit thực hiện, cũng không được thêm vào trách nhiệm của các lệnh đó. Mô hình lưu giữ của nhóm quyết định riêng cách duy trì artifact sau khi bàn giao.

<a id="search-available-extensions"></a>

## Tìm extension có sẵn

```bash
specify extension search [query]
```

| Tùy chọn | Mô tả |
| ------------ | ------------------------------------ |
| `--tag` | Lọc theo tag |
| `--author` | Lọc theo tác giả |
| `--verified` | Chỉ hiển thị extension đã xác minh |

Tìm trong mọi catalog đang hoạt động các extension khớp từ khóa. Khi không có từ khóa, liệt kê mọi extension có sẵn.

<a id="install-an-extension"></a>

## Cài một extension

```bash
specify extension add <name>
```

| Tùy chọn | Mô tả |
| --------------- | -------------------------------------------------------- |
| `--dev` | Cài từ thư mục cục bộ (để phát triển) |
| `--from <url>` | Cài từ URL tùy chỉnh thay vì từ catalog |
| `--version <v>` | Cài đúng một phiên bản được catalog công bố |
| `--force` | Ghi đè nếu extension đã được cài |
| `--priority <N>` | Độ ưu tiên phân giải (mặc định: 10; nhỏ hơn = ưu tiên cao hơn) |

Cài một extension từ catalog, URL hoặc thư mục cục bộ. Lệnh của extension được đăng ký với integration agent lập trình AI đang hoạt động. Với `generic`, lời gọi dùng `--commands-dir` đã cấu hình: mặc định là các file lệnh phẳng, hoặc `speckit-<name>/SKILL.md` khi có `--skills`.

Nếu một lần làm mới integration generic không thể tạo đủ mọi lời gọi extension (ví dụ vì một lệnh hoặc skill đã bị người dùng sửa hoặc thiếu nguồn), nó sẽ cảnh báo và khôi phục các artifact đã đăng ký trước đó của extension đó. Các extension khác vẫn có thể làm mới.

Cài từ catalog mà không chỉ định phiên bản vẫn chọn phiên bản hiện tại được công bố. `--version` chỉ dùng nguồn catalog thắng cho ID extension đó; nó không quay về nguồn ưu tiên thấp hơn khi không có phiên bản được yêu cầu. Catalog chỉ dùng để tìm kiếm vẫn không cài được. Không thể kết hợp `--version` với `--dev` hoặc tùy chọn URL trực tiếp `--from`. ID và phiên bản extension trong archive đã tải được kiểm tra trước khi cài.

> **Lưu ý:** Mọi lệnh extension đều yêu cầu dự án đã được khởi tạo bằng `specify init`.

<a id="remove-an-extension"></a>

## Gỡ một extension

```bash
specify extension remove <name>
```

| Tùy chọn | Mô tả |
| --------------- | ---------------------------------------------- |
| `--keep-config` | Giữ lại file cấu hình khi gỡ |
| `--force` | Bỏ qua lời nhắc xác nhận |

Gỡ một extension đã cài. File cấu hình được sao lưu mặc định; dùng `--keep-config` để giữ nguyên chúng hoặc `--force` để bỏ qua xác nhận.

<a id="list-installed-extensions"></a>

## Liệt kê extension đã cài

```bash
specify extension list
specify extension list --json
```

| Tùy chọn | Mô tả |
| ------------- | -------------------------------------------------- |
| `--available` | Hiển thị extension có sẵn (chưa cài) |
| `--all` | Hiển thị cả extension đã cài và có sẵn |
| `--json` | Ghi danh sách extension đã cài dưới dạng JSON |

Liệt kê extension đã cài kèm trạng thái, phiên bản và số lượng lệnh.

`--json` ghi một mảng JSON ra stdout. Mỗi phần tử có các khóa `id`, `name`, `description`, `version`, `author`, `priority`, `enabled`, `source` và `provides`. `author` là `null` khi không có; `source` là `{"kind":"local"}` với nguồn gốc cục bộ, kiểu cũ hoặc sai định dạng, hoặc `{"kind":"catalog","catalog":"<catalog-name>"}` với nguồn catalog hợp lệ. `provides` của extension chứa số lượng `commands`, `templates`, `scripts` và `hooks`. `--available` và `--all` không mở rộng đầu ra JSON ra ngoài các extension đã cài. Khi thành công, `--json` ghi đúng một mảng ra stdout và thoát với mã
0. Lỗi lúc chạy sau khi phân tích tùy chọn sẽ ghi đúng một
đối tượng `{"error":"..."}` ra stderr và thoát với mã 1. Nếu việc phân tích phát sinh lỗi cách dùng và có token `--json` nguyên văn, nó ghi đối tượng lỗi JSON đó ra stderr và giữ nguyên mã thoát của lỗi cách dùng (thường là 2). Khi không có `--json`, kể cả với help, hành vi hiển thị cho người đọc hiện có không thay đổi.

<a id="extension-info"></a>

## Thông tin extension

```bash
specify extension info <name>
specify extension info <name> --versions
specify extension info <name> --json
```

Hiển thị thông tin chi tiết về một extension đã cài hoặc có sẵn, gồm mô tả, phiên bản, lệnh và cấu hình. `--versions` liệt kê các phiên bản hiện tại và lịch sử được nguồn catalog thắng công bố; nó gắn nhãn không cài được cho nguồn chỉ dùng để tìm kiếm. Các cách viết phiên bản tương đương theo PEP 440 (ví dụ `v1.0` và `1.0`) chọn cùng một bản phát hành; cách viết được catalog công bố vẫn hiển thị.

Catalog có thể giữ bản phát hành hiện tại trong các trường cấp cao nhất hiện có và thêm các bản phát hành lịch sử trong mapping `releases`. Catalog cũ chỉ có một phiên bản vẫn hoạt động như trước. Mỗi bản phát hành lịch sử cần URL tải về và digest SHA-256 riêng; yêu cầu hoặc khả năng cung cấp riêng của bản phát hành phải đặt trong bản ghi của bản đó thay vì kế thừa từ bản hiện tại. Giống bản hiện tại, digest có thể dùng tiền tố `sha256:` không phân biệt hoa thường và khoảng trắng bao quanh.

```json
{
  "extensions": {
    "my-extension": {
      "name": "My Extension",
      "version": "0.5.1",
      "download_url": "https://example.com/my-extension-0.5.1.zip",
      "sha256": "<64-character SHA-256 for 0.5.1>",
      "releases": {
        "0.4.12": {
          "download_url": "https://example.com/my-extension-0.4.12.zip",
          "sha256": "<64-character SHA-256 for 0.4.12>"
        }
      }
    }
  }
}
```

Ví dụ lược bỏ các metadata catalog khác cho ngắn gọn. Không được lặp lại phiên bản hiện tại trong `releases`; bản ghi phát hành sai định dạng hoặc trùng lặp sẽ bị từ chối. Phiên bản ghim của bundle vẫn dùng đường phân giải catalog hiện tại cho đến khi phần việc riêng về bundle mô tả trong [#4719](https://github.com/github/spec-kit/issues/4719) bổ sung khả năng tra cứu thành phần theo phiên bản chính xác.

`--json` mô tả một extension đã cài và ghi một đối tượng JSON duy nhất ra stdout. `<name>` được so khớp như khi không có `--json`: trước hết là ID extension, rồi đến tên hiển thị duy nhất, không phân biệt hoa thường. Đối tượng có cùng các khóa `id`, `name`, `description`, `version`, `author`, `priority`, `enabled` và `source` như phần tử tương ứng của `specify extension list --json`. Thay cho số lượng trong `provides`, nó có các mảng `commands`, `templates`, `scripts` và `hooks`. Các mục command, template và script có `name`, `description` (`""` khi không có), `source` (`{"layer": "extension", "extensionId": "<id>"}`, extension cung cấp nó; `source` cấp cao nhất là nơi nó được cài từ đó), và `sourcePath` (`file` trong manifest, tương đối với thư mục extension); mục script còn có `runtimes` khi manifest khai báo. Mục của extension không có `strategy`, vì file do extension cung cấp luôn thay thế. Mỗi mục hook có `trigger` (event hook, như `after_tasks`), `targetCommand`, `optional` (mặc định `true`) và `priority` (mặc định `10`). Khi một event khai báo cùng một lệnh nhiều lần, khai báo cuối cùng thắng, giống như khi đăng ký hook. Không thể kết hợp `--json` với `--versions` (lỗi cách dùng, mã thoát 2). Extension chưa được cài, tên mơ hồ hoặc thiếu dự án sẽ ghi một đối tượng `{"error":"..."}` ra stderr và thoát với mã 1; lỗi cách dùng giữ mã thoát của chúng (thường là 2), giống `list --json`.

<a id="update-extensions"></a>

## Cập nhật extension

```bash
specify extension update [<name>]
```

Cập nhật một extension cụ thể, hoặc mọi extension đã cài nếu không truyền tên.

Extension đóng gói sẵn (như `agent-context` và `git`) không có URL tải về; bản cập nhật của chúng được cài từ bản đi kèm phiên bản spec-kit đang chạy. Khi catalog công bố phiên bản mới hơn bản đi kèm phiên bản spec-kit của bạn, bản cập nhật được báo là cần nâng cấp spec-kit trước.

Với `generic`, một lần cập nhật thất bại sẽ khôi phục các lời gọi thuộc sở hữu theo hash từ các vị trí `--commands-dir` đã cấu hình trước đó cũng như vị trí hiện tại, kể cả khi integration khác đang hoạt động.

<a id="enable--disable-an-extension"></a>

## Bật / tắt extension

```bash
specify extension enable <name>
specify extension disable <name>
```

Tắt một extension mà không gỡ nó. Extension bị tắt không được nạp và lệnh của chúng không khả dụng. Extension chỉ có hook có thể được cài, bật và tắt kể cả khi thiết lập đầu ra lệnh generic bị thiếu hoặc không hợp lệ; extension có lệnh vẫn cần thiết lập hợp lệ. Bật lại bằng `enable`.

Với `generic`, việc tắt sẽ gỡ các lời gọi thuộc sở hữu theo hash kể cả sau khi thư mục đầu ra bị di chuyển, nhưng giữ lại các file trùng tên không liên quan trong thư mục mới.

<a id="set-extension-priority"></a>

## Đặt độ ưu tiên extension

```bash
specify extension set-priority <name> <priority>
```

Thay đổi độ ưu tiên phân giải của một extension. Khi nhiều extension cung cấp lệnh trùng tên, extension có số priority nhỏ nhất được ưu tiên.

<a id="catalog-management"></a>

## Quản lý catalog

Catalog extension quyết định nơi `search` và `add` tìm extension. Catalog được kiểm tra theo thứ tự ưu tiên (số nhỏ hơn = ưu tiên cao hơn).

<a id="trust-model-discovery-only-vs-install-sources"></a>

### Mô hình tin cậy: nguồn chỉ tìm kiếm và nguồn cài đặt

Catalog có hai loại, và sự phân biệt này là một **ranh giới bảo mật**, không phải một giới hạn:

- **Nguồn cài đặt** (`install_allowed: true`) — các catalog bạn tin cậy để cài đặt từ đó. Catalog `default` (chính thức) có sẵn là một nguồn như vậy, cũng như bất kỳ catalog nào bạn tự viết và tự thẩm định.
- Catalog **chỉ tìm kiếm** (`install_allowed: false`) — bề mặt tìm kiếm để *tìm* extension, nhưng không cài được. Catalog `community` có sẵn là catalog chỉ tìm kiếm và đã hoạt động cho `search` ngay từ đầu; bạn không cần thêm nó.

`community` được cố ý để ở chế độ chỉ tìm kiếm vì đó là một danh sách mở, chưa được thẩm định. Cho phép cài mọi thứ trong đó chỉ bằng một lệnh đồng nghĩa với việc kéo code bất kỳ của bên thứ ba vào mà không review.

> **Đừng chuyển catalog chỉ tìm kiếm sang `install_allowed`.** Làm vậy sẽ phá hỏng toàn bộ ý nghĩa của việc tách tìm kiếm khỏi cài đặt. Có hai cách đúng để cài thứ bạn tìm thấy qua `community`:
>
> 1. **Cài trực tiếp một extension đã thẩm định** bằng `--from` (không cần viết catalog). Lấy URL archive ứng viên từ `specify extension info <name>` — với mục chỉ tìm kiếm, lệnh này in URL "Candidate archive". Review archive phát hành đó, rồi cài nó:
>
>    ```bash
>    specify extension info <name>          # shows the candidate archive URL
>    specify extension add <name> --from <archive-url>
>    ```
>
> Hãy coi URL là không đáng tin cậy cho đến khi bạn thẩm định nó — nó đến từ một catalog chưa được thẩm định.
> 2. **Tự tuyển chọn catalog của riêng bạn**, do bạn kiểm soát và thẩm định, và đánh dấu *catalog đó* là `install_allowed: true` — khi bạn muốn một nguồn cài đặt có quản trị, dùng lại được (ví dụ cho một tổ chức).

<a id="list-catalogs"></a>

### Liệt kê catalog

```bash
specify extension catalog list
```

Hiển thị mọi catalog đang hoạt động trong chồng cùng độ ưu tiên và quyền cài đặt.

<a id="add-a-catalog"></a>

### Thêm catalog

```bash
specify extension catalog add <url>
```

| Tùy chọn | Mô tả |
| ------------------------------------ | -------------------------------------------------- |
| `--name <name>` | Bắt buộc. Tên duy nhất cho catalog |
| `--priority <N>` | Độ ưu tiên (mặc định: 10; nhỏ hơn = ưu tiên cao hơn) |
| `--install-allowed / --no-install-allowed` | Đánh dấu catalog là nguồn cài đặt đáng tin cậy. Chỉ bật cho catalog bạn sở hữu và thẩm định; để tắt (mặc định) với nguồn chỉ tìm kiếm. Không bao giờ bật nó cho một catalog công khai chưa thẩm định. |
| `--description <text>` | Mô tả tùy chọn |

Thêm một catalog vào `.specify/extension-catalogs.yml` của dự án.

Thêm lại catalog cùng tên với thiết lập giống hệt sẽ thành công mà không đổi cấu hình; thiết lập khác sẽ bị từ chối.

<a id="remove-a-catalog"></a>

### Gỡ catalog

```bash
specify extension catalog remove <name>
```

Gỡ một catalog khỏi cấu hình dự án.

<a id="catalog-resolution-order"></a>

### Thứ tự phân giải catalog

Catalog được phân giải theo thứ tự sau (mục khớp đầu tiên thắng):

1. **Biến môi trường** — `SPECKIT_CATALOG_URL` ghi đè mọi catalog
2. **Cấu hình dự án** — `.specify/extension-catalogs.yml`
3. **Cấu hình người dùng** — `~/.specify/extension-catalogs.yml`
4. **Mặc định có sẵn** — catalog `default` chính thức (cho phép cài đặt) + catalog `community` (chỉ tìm kiếm)

Ví dụ `.specify/extension-catalogs.yml` cho một catalog bạn sở hữu và thẩm định:

```yaml
catalogs:
  - name: "my-org-catalog"
    url: "https://example.com/catalog.json"
    priority: 5
    install_allowed: true
    description: "Our approved extensions"
```

<a id="extension-configuration"></a>

## Cấu hình extension

Hầu hết extension có file cấu hình trong thư mục cài đặt:

```text
.specify/extensions/<ext>/
├── <ext>-config.yml           # Project config (version controlled)
├── <ext>-config.local.yml     # Local overrides (gitignored)
└── <ext>-config.template.yml  # Template reference
```

Cấu hình được gộp theo thứ tự sau (ưu tiên cao nhất ở cuối):

1. **Mặc định của extension** (từ `extension.yml`)
2. **Cấu hình dự án** (`<ext>-config.yml`)
3. **Ghi đè cục bộ** (`<ext>-config.local.yml`)
4. **Biến môi trường** (`SPECKIT_<EXT>_*`)

Để thiết lập cấu hình cho extension mới cài, hãy sao chép template:

```bash
cp .specify/extensions/<ext>/<ext>-config.template.yml \
   .specify/extensions/<ext>/<ext>-config.yml
```

<a id="extension-runtime-events"></a>

## Runtime event của extension

Extension có thể phản ứng với các event trong vòng đời của agent lập trình bằng cách khai báo mapping `events` cấp cao nhất trong `extension.yml`:

```yaml
events:
  session_start:
    command: speckit.my-extension.initialize
  pre_tool_use:
    command: speckit.my-extension.validate
```

Khai báo event không phụ thuộc integration. Spec Kit làm mới mọi integration hỗ trợ event đã cài, và mỗi integration dịch tên event chuẩn sang cấu hình event gốc của agent lập trình tương ứng. Các event chuẩn được hỗ trợ là `session_start`, `pre_tool_use`, `post_tool_use`, `user_prompt_submit`, `stop` và `session_end`; mỗi integration có thể chỉ hỗ trợ một phần.

Runtime event khác với hook của extension. Event phản ứng với vòng đời của agent lập trình và trực tiếp thực thi mục `scripts` của template lệnh được tham chiếu. Vì vậy lệnh được tham chiếu phải cung cấp một script chạy được; chỉ dẫn Markdown của nó không được gửi tới agent lập trình. Ngược lại, hook đưa lệnh của extension ra trước hoặc sau các lệnh Spec Kit như `plan`, `tasks` và `implement`.

<a id="project-extension-and-hook-configuration"></a>

## Cấu hình extension và hook của dự án

Spec Kit lưu việc đăng ký extension và cấu hình hook ở cấp dự án trong:

```text
.specify/extensions.yml
```

File chứa các extension đã cài, thiết lập chung và các hook được đưa ra trước hoặc sau các lệnh Spec Kit.

```yaml
installed:
  - git
  - my-extension

settings:
  auto_execute_hooks: true

hooks:
  before_implement:
    - extension: git
      command: speckit.git.commit
      enabled: true
      optional: true
      priority: 10
      prompt: "Commit outstanding changes before implementation?"
      description: "Auto-commit before implementation"

  after_implement:
    - extension: my-extension
      command: speckit.my-extension.verify
      enabled: true
      optional: false
      priority: 5
      description: "Run verification after implementation"
```

<a id="configuration-fields"></a>

### Các trường cấu hình

Danh sách `installed` cấp cao nhất ghi các extension đã cài trong dự án. Mapping `settings` lưu thiết lập extension cho toàn dự án, và `hooks` nhóm các đăng ký hook theo event.

`auto_execute_hooks` mặc định là `true`, nhưng hiện được dành riêng và không được tra cứu khi hook được đưa ra hoặc được gọi.

Mỗi mục hook hỗ trợ các trường sau:

| Trường | Mô tả |
| --- | --- |
| `extension` | ID của extension đã đăng ký hook. |
| `command` | Lệnh extension gắn với hook. |
| `enabled` | Hook có đang hoạt động hay không. Hook có `enabled: false` sẽ bị bỏ qua. |
| `optional` | Hook có phải tùy chọn hay không. Nếu là `true`, hook được trình bày kèm `prompt` và có thể bỏ qua; nếu là `false`, hook được phát ra như hook tự động (có marker `EXECUTE_COMMAND`). |
| `priority` | Metadata về độ ưu tiên của hook. Mục hook đã đăng ký dùng giá trị số nguyên >= 1; mục được cài từ manifest mặc định là `10` khi không khai báo priority. Template lệnh hiện tại đưa ra hook theo thứ tự YAML đã cấu hình và không sắp theo `priority`. |
| `prompt` | Thông điệp hiển thị khi hỏi có chạy một hook tùy chọn hay không. |
| `description` | Giải thích dễ đọc về việc hook làm. |
| `condition` | Biểu thức tùy chọn do `HookExecutor` đánh giá (dùng `config.<path>` hoặc `env.<VAR>` với `is set`, `==` hoặc `!=`). Template lệnh hiện tại không đánh giá điều kiện và bỏ qua hook có điều kiện không rỗng. |

Tên event hook xác định thời điểm hook được gọi. Chúng thường dùng `before_<command>` hoặc `after_<command>`, như `before_implement`, `after_implement`, `before_tasks` và `after_tasks`.

Manifest extension từ chối priority hook không hợp lệ khi cài đặt. Với các mục `.specify/extensions.yml` hiện có, `HookExecutor.get_hooks_for_event()` sắp xếp bằng `normalize_priority()`: giá trị bị thiếu, boolean, giá trị không phải số bị `int()` từ chối và giá trị nhỏ hơn `1` đều quay về `10`; chuỗi số và số thực hữu hạn được ép kiểu bằng `int()`, còn số thực không hữu hạn không được hỗ trợ và có thể gây lỗi thay vì quay về giá trị mặc định.

`HookExecutor.get_hooks_for_event()` trả về hook theo thứ tự `priority`, giá trị nhỏ hơn đứng trước. Tuy nhiên, template lệnh hiện tại đọc trực tiếp danh sách hook và đưa chúng ra theo thứ tự YAML đã cấu hình thay vì sắp theo priority.

<a id="faq"></a>

## Câu hỏi thường gặp

<a id="why-cant-i-find-an-extension-with-search"></a>

### Vì sao tôi không tìm thấy extension bằng `search`?

Kiểm tra chính tả tên extension. Có thể extension chưa được phát hành, hoặc nằm trong một catalog bạn chưa thêm. Dùng `specify extension catalog list` để xem catalog nào đang hoạt động.

<a id="why-doesnt-the-extension-command-appear-in-my-ai-coding-agent"></a>

### Vì sao lệnh của extension không xuất hiện trong agent lập trình AI của tôi?

Xác nhận extension đã được cài và đang bật bằng `specify extension list`. Nếu nó hiển thị là đã cài, hãy khởi động lại agent lập trình AI — có thể agent cần nạp lại để thay đổi có hiệu lực.

<a id="how-do-i-set-up-extension-configuration"></a>

### Làm sao để thiết lập cấu hình extension?

Sao chép template cấu hình đi kèm extension:

```bash
cp .specify/extensions/<ext>/<ext>-config.template.yml \
   .specify/extensions/<ext>/<ext>-config.yml
```

Xem [Cấu hình extension](#extension-configuration) để biết chi tiết về các lớp cấu hình và ghi đè.

<a id="how-do-i-resolve-an-incompatible-version-error"></a>

### Làm sao xử lý lỗi phiên bản không tương thích?

Cập nhật Spec Kit lên phiên bản mà extension yêu cầu.

<a id="who-maintains-extensions"></a>

### Ai duy trì các extension?

Hầu hết extension được tạo và duy trì độc lập bởi tác giả của chúng. Các maintainer của Spec Kit không review, kiểm định, bảo chứng hay hỗ trợ code của extension. Hãy review mã nguồn của extension trước khi cài và tự cân nhắc khi sử dụng. Với vấn đề của một extension cụ thể, hãy liên hệ tác giả hoặc tạo issue trên repository của extension đó.
