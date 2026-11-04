<a id="artifacts"></a>

# Artifact

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/artifacts.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

**Artifact** là bất kỳ command, template, script hay hook nào mà Spec Kit cung cấp trong dự án, bất kể lớp nào đóng góp nó — tài nguyên có sẵn, preset đã cài, extension đã cài hay ghi đè cục bộ của dự án trong `.specify/templates/overrides/`.

Nhóm lệnh `specify artifact` là bề mặt chỉ đọc để tra cứu danh mục đó. `specify preset resolve <name>` trả lời "file nào thắng cho tên do preset quản lý này?"; `specify artifact` trả lời "những gì tồn tại, và toàn bộ chồng kết hợp phía sau nó là gì?" — kể cả các artifact có sẵn mà không preset nào động tới.

Hiện mọi lệnh con đều yêu cầu `--json`. Bỏ nó sẽ thoát với mã `2` và in thông báo cách dùng ra stderr; không có gì được ghi ra stdout. Việc hiển thị dạng văn bản được cố ý hoãn lại để các dạng JSON bên dưới là hợp đồng duy nhất, và việc thêm trình hiển thị văn bản mặc định sau này vẫn là một thay đổi bổ sung, không phá vỡ tương thích.

<a id="list-artifacts"></a>

## Liệt kê artifact

```bash
specify artifact list --json
```

| Tùy chọn | Mô tả |
| -------- | -------------------------------------------------------- |
| `--json` | Bắt buộc. Xuất danh mục dưới dạng mảng JSON ra stdout. |

In toàn bộ danh mục của mọi artifact hiển thị — mỗi cặp `(kind, name)` một dòng, kèm `stack` kết hợp của nó. Các artifact có tên được sắp theo kind (`command`, rồi `template`, rồi `script`) và theo tên. Các dòng hook đứng sau, sắp theo event rồi theo priority của khai báo đầu tiên.

```json
[
  {
    "id": "command:speckit.specify",
    "name": "speckit.specify",
    "kind": "command",
    "description": "Create or update the feature specification.",
    "stack": [
      {
        "id": "command:speckit.specify",
        "layer": null,
        "sourceId": null,
        "presetId": null,
        "presetName": null,
        "strategy": "replace",
        "active": true,
        "hidden": false,
        "manifestPath": null,
        "lookupId": null,
        "sourcePath": null
      }
    ]
  },
  {
    "id": "script:setup-plan",
    "name": "setup-plan",
    "kind": "script",
    "description": "Setup implementation plan for a feature.",
    "stack": [
      {
        "id": "script:setup-plan",
        "layer": null,
        "sourceId": null,
        "presetId": null,
        "presetName": null,
        "strategy": "replace",
        "active": true,
        "hidden": false,
        "manifestPath": null,
        "lookupId": null,
        "sourcePath": null
      }
    ]
  }
]
```

| Trường | Mô tả |
| ------------- | ------------------------------------------------------------------------- |
| `id` | `{kind}:{name}` — dạng viết tắt mà `artifact info` chấp nhận làm đối số |
| `name` | Tên logic của artifact (command dùng namespace `speckit.<stem>`) |
| `kind` | Một trong `command`, `template`, `script`, `hook` |
| `description` | Mô tả từ lớp có độ ưu tiên cao nhất có khai báo mô tả, nếu không thì `""` |
| `stack` | Chồng kết hợp của artifact này, dùng cùng dạng dòng như `artifact info` |

Artifact có sẵn luôn xuất hiện, kể cả khi không có gì ghi đè chúng. Mô tả lấy từ lớp có độ ưu tiên cao nhất có mô tả — preset hoặc ghi đè dự án che một lệnh có sẵn sẽ báo mô tả của chính nó, không phải văn bản của lệnh có sẵn bị che. Skill (`.github/skills/**/SKILL.md`) bị loại trừ: chúng là đầu ra riêng của integration, không phải một nhóm tài nguyên được phát hành kèm.

<a id="artifact-info"></a>

## Thông tin artifact

```bash
specify artifact info <name> --json
```

| Tùy chọn | Mô tả |
| ---------------- | ------------------------------------------------------------------- |
| `--json` | Bắt buộc. Xuất chồng kết hợp dưới dạng đối tượng JSON ra stdout. |
| `--kind <kind>` | Thu hẹp phạm vi tra cứu về `command`, `template`, `script` hoặc `hook` |

`<name>` nhận tên trần (`speckit.specify`) hoặc dạng viết tắt `kind:name` (`command:speckit.specify`). Khi truyền cả dạng viết tắt lẫn `--kind`, hai giá trị phải khớp nhau.

```json
{
  "id": "command:speckit.specify",
  "name": "speckit.specify",
  "kind": "command",
  "description": "Create or update the feature specification.",
  "stack": [
    {
      "id": "command:speckit.specify",
      "layer": "preset",
      "sourceId": "compliance",
      "presetId": "compliance",
      "presetName": "Compliance Preset",
      "strategy": "replace",
      "active": true,
      "hidden": false,
      "manifestPath": ".specify/presets/compliance/preset.yml",
      "lookupId": "preset:compliance:command:speckit.specify",
      "sourcePath": ".github/skills/speckit-specify/SKILL.md"
    },
    {
      "id": "command:speckit.specify",
      "layer": null,
      "sourceId": null,
      "presetId": null,
      "presetName": null,
      "strategy": "replace",
      "active": false,
      "hidden": true,
      "manifestPath": null,
      "lookupId": null,
      "sourcePath": null
    }
  ]
}
```

Các trường cấp cao nhất `id`, `name`, `kind`, `description` và `stack` khớp với dòng tương ứng trong `artifact list --json`.

<a id="stack-semantics"></a>

### Ngữ nghĩa của stack

Với artifact command, template và script, `stack` được sắp theo thứ tự ưu tiên phân giải: chỉ số `0` là lớp thắng. Stack của hook mang tính cộng dồn thay vì chọn lớp thắng: nhiều mục có thể cùng hoạt động, và thứ tự khai báo của chúng được mô tả trong [Artifact hook](#hook-artifacts). Mỗi dòng mô tả một lớp đóng góp:

| Trường | Mô tả |
| -------------- | -------------------------------------------------------------------------------- |
| `id` | `{kind}:{name}` — khóa khứ hồi không phụ thuộc nguồn, giống hệt nhau trên mọi dòng trong stack của cùng một artifact |
| `layer` | `project`, `preset` hoặc `extension`; `null` với lớp có sẵn |
| `sourceId` | ID preset hoặc extension đã cài mà resolver dùng, hoặc `null` khi lớp không có nguồn gốc |
| `presetId` | ID thư mục gói preset; `null` trên các dòng có sẵn, `project` và `extension` |
| `presetName` | Tên hiển thị của preset nếu manifest có khai báo, nếu không thì là ID gói; `null` khi `presetId` là `null` |
| `strategy` | `replace`, `wrap`, `prepend`, `append` hoặc `additive` |
| `active` | Lớp có đang hoạt động hay không; với artifact có tên, giá trị này chỉ là `true` tại chỉ số `0` |
| `hidden` | `true` khi một lớp `replace` có chỉ số nhỏ hơn loại lớp này khỏi kết quả kết hợp |
| `manifestPath` | Đường dẫn tương đối trong dự án tới manifest khai báo, hoặc `null` khi không áp dụng |
| `lookupId` | Định danh tất định `{layer}:{sourceId}:{kind}:{name}`, hoặc `null` với lớp có sẵn |
| `sourcePath` | Đường dẫn POSIX tương đối trong dự án tới file cụ thể đứng sau lớp, hoặc `null` với lớp có sẵn/tổng hợp |

`active` và `hidden` là hai nhãn độc lập, không phải hai mặt đối lập. Với artifact command, template và script, `active` xác định lớp có độ ưu tiên cao nhất được chọn theo thứ tự phân giải lớp hiện có của Spec Kit; nó không kiểm tra nội dung của lớp có đọc hay kết hợp được hay không. Điều này giữ nguyên hành vi chẩn đoán của `specify preset resolve`, vốn báo chuỗi lớp đã phát hiện kể cả khi việc kết hợp nội dung sau đó sinh cảnh báo. Các strategy kết hợp (`wrap`, `prepend`, `append`) giữ các lớp thấp hơn trong đầu ra kết hợp, nên một lớp không hoạt động chưa chắc đã bị che: chỉ các lớp nằm dưới lớp `replace` đầu tiên mới được đánh dấu `hidden`. Dòng có sẵn không có nguồn gốc: `layer`, `sourceId` và `lookupId` là `null` — nhưng `id` luôn có giá trị, kể cả trên dòng có sẵn. `id` là khóa khứ hồi: `specify artifact info` nhận nó làm đầu vào (ví dụ `specify artifact info command:speckit.specify --json`), và nó phân giải ra cùng một artifact dù bên gọi truyền tên trần hay `id`.

Ở đây, **nguồn gốc** (provenance) nghĩa là xuất xứ của một lớp artifact: preset hoặc extension đã cài cung cấp nó, manifest khai báo nó và file cụ thể đứng sau nó. ID tra cứu dùng ID của preset hoặc extension đã cài, khớp với định danh và thứ tự mà resolver hiện có sử dụng. ID đã cài là tên trong registry/thư mục và có thể khác với `id` logic được khai báo trong manifest. Dùng ID đã cài giúp các thư mục đã cài riêng biệt vẫn phân biệt được, kể cả khi manifest của chúng khai báo cùng một ID logic.

Ghi đè cục bộ của dự án mang ID tổng hợp `project:_:{kind}:{name}`, còn lớp có sẵn không có `lookupId`. Các giá trị này xác định nguồn gốc trong stack artifact; chúng không phải khóa khứ hồi của artifact — hãy dùng `id` với `artifact info` cho việc đó. `manifestPath` xác định manifest khai báo, và `sourcePath` xác định file cụ thể đứng sau lớp khi có. Dòng lõi, dòng ghi đè dự án và các dòng tổng hợp khác có thể báo `sourcePath: null`.

<a id="contribution-lookup"></a>

## Tra cứu đóng góp

```bash
specify artifact lookup <lookupId> --json
```

Phân giải một `lookupId` của stack có manifest đứng sau thành khai báo preset hoặc extension đã được kiểm tra hợp lệ mà Spec Kit sử dụng. Khai báo trả về phản ánh quá trình xử lý manifest thông thường, gồm tên lệnh extension chuẩn hóa, các giá trị mặc định được chèn như danh sách alias rỗng, và strategy preset viết thường. Nó không phải bản sao nguyên văn của YAML đã viết.

Điều này giữ hành vi tham chiếu chéo bên trong lệnh artifact: lệnh preset và extension, manifest và dạng dữ liệu trả về của resolver đều không thay đổi.

Phản hồi gồm ID tra cứu ổn định, tọa độ của provider, đường dẫn manifest và nguồn, và khai báo hiệu lực trong `contribution`. Đóng góp chỉ dựa trên quy ước và ghi đè dự án không có khai báo manifest gốc, nên tra cứu trả về `{"error": "unknown contribution <lookupId>"}` với mã thoát `1`. Dòng có sẵn không bao giờ có `lookupId`.

<a id="hook-artifacts"></a>

### Artifact hook

Các dòng hook thể hiện khai báo hook từ các extension được resolver preset và extension chuẩn đưa vào. Dạng viết tắt khứ hồi là:

```text
hook:{encodedEventName}:{encodedTargetCommand}
```

Ví dụ, cả hai cách sau đều chọn cùng một artifact hook:

```bash
specify artifact info hook:before_specify:speckit.compliance.pre-check --json
specify artifact info before_specify:speckit.compliance.pre-check --kind hook --json
```

Thành phần event và lệnh đích của hook được mã hóa phần trăm UTF-8 theo quy tắc URL quoting: Chữ cái ASCII, chữ số, `-`, `.`, `_` và `~` giữ nguyên, còn mọi byte khác đều được mã hóa. Cách mã hóa này chỉ áp dụng cho thành phần hook trong `id`, `name` và `lookupId` của artifact; manifest hook, binding lúc chạy, `eventName` và `targetCommand` không thay đổi. Ví dụ, một event tên `custom:after` nhắm tới `/skill:speckit-test-ext-hello` có ID artifact là:

```text
hook:custom%3Aafter:%2Fskill%3Aspeckit-test-ext-hello
```

Dòng hook thêm ba trường cấp cao nhất:

| Trường | Mô tả |
| --------------- | ------------------------------------------------------------------------------ |
| `eventName` | Event hook kích hoạt khai báo |
| `targetCommand` | Lệnh được khai báo hook gọi |
| `registered` | `true` khi ít nhất một mục stack khai báo có binding lúc chạy đang bật |

Mỗi mục stack của hook cũng chứa giá trị `priority` và `optional` đã chuẩn hóa của khai báo. Mục hook luôn dùng `strategy: "additive"` và `hidden: false`: nhiều extension có thể khai báo và đăng ký cùng một cặp event-lệnh, và mọi khai báo đang bật đều hoạt động. Các mục stack được sắp theo priority của hook, dùng thứ tự khai báo tất định của resolver để phân định khi bằng nhau. Thứ tự này mô tả danh mục khai báo; nó không cam kết rằng các hook cùng priority sẽ chạy theo cùng thứ tự lúc chạy.

Với hook, `active` báo trạng thái đăng ký trong `.specify/extensions.yml`, không phải kết quả đánh giá điều kiện. Một khai báo chỉ hoạt động khi cấu hình lúc chạy có một binding đang bật với cùng ID extension, event và lệnh. Điều kiện được đánh giá sau, khi hook thực thi. Vì vậy, cấu hình lúc chạy bị thiếu, sai định dạng hoặc không đọc được sẽ khiến các khai báo vẫn hiển thị với `registered: false` và `active: false`.

Hook được khai báo nhưng chưa đăng ký vẫn hiển thị khi extension của chúng được resolver thông thường đưa vào. Extension bị tắt trong registry bị loại trừ hoàn toàn, nhất quán với các đóng góp khác của chúng. Manifest extension riêng lẻ không hợp lệ cũng bị resolver hiện có bỏ qua và vẫn chẩn đoán được qua các lệnh kiểm tra và xác thực extension.

ID tra cứu hook dùng ngữ pháp riêng của artifact `{layer}:{sourceId}:hook:{encodedEventName}:{encodedTargetCommand}`, trong đó `sourceId` là ID provider đã cài. Nguồn gốc của hook chỉ giới hạn ở lớp `preset` và `extension`; hook không bao giờ có lớp có sẵn/lõi. API manifest hiện tại cung cấp khai báo hook của extension, nên các dòng hiện tại dùng lớp `extension`. Lớp `preset` vẫn được ngữ pháp định danh hook dành riêng cho hook do preset cung cấp, mà không cần thêm ID artifact vào API manifest của preset hay extension.

<a id="json-errors"></a>

## Lỗi JSON

Khi thất bại, không có gì được ghi ra stdout. Một phong bì JSON một khóa được ghi ra stderr và tiến trình thoát với mã `1`:

```json
{ "error": "unknown artifact command:nope" }
```

| Thông điệp | Nguyên nhân |
| --------------------------------------------------- | ---------------------------------------------------------------- |
| `not a Spec Kit project: no .specify/ directory found` | Chạy bên ngoài một dự án đã khởi tạo |
| `unknown artifact <name>` | Không có artifact nào khớp tên được yêu cầu (và kind, nếu có) |
| `ambiguous artifact <name>: matches kinds [...]` | Tên trần khớp nhiều hơn một kind — hãy chạy lại với `--kind` |
| `artifact resolution failed` | Không đọc được registry extension, hoặc một lỗi đã ngăn việc thu thập stack lớp artifact |

Mã thoát `2` dành cho lỗi cách dùng — thiếu cờ `--json` hoặc giá trị `--kind` không hợp lệ — và in thông báo văn bản thuần ra stderr thay vì phong bì JSON.
