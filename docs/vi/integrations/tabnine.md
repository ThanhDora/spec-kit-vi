# Tabnine CLI

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/tabnine.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Tabnine CLI](https://docs.tabnine.com/main/getting-started/tabnine-cli) trước khi thiết lập. Khóa integration là `tabnine`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration tabnine
```

Với dự án Spec Kit đã có, dùng `specify integration install tabnine`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Lệnh TOML được cài tại `.tabnine/agent/commands/speckit.<command>.toml`. Gọi chúng trong khung chat của agent bằng ký pháp dấu chấm, ví dụ `/speckit.specify`, hoặc `/speckit.bug.assess` khi đã cài extension bug.

<a id="runtime-events-and-workflow-dispatch"></a>

## Runtime event và điều phối workflow

Event gốc dùng `.tabnine/agent/settings.json`, ánh xạ event gửi prompt và event dừng sang `BeforeAgent` và `AfterAgent`. Timeout của hook được đổi sang mili giây. `--integration-options="--events false"` tắt trình xử lý event của Spec Kit. Xem [runtime event](cli.md#runtime-events).

Workflow step dùng `tabnine -p <prompt>`, kèm `-m` khi đã cấu hình mô hình và `--output-format json` khi cần đầu ra có cấu trúc.
