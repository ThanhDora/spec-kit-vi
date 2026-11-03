# Cursor

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/cursor-agent.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Cursor](https://cursor.sh/) trước khi thiết lập. Khóa integration là `cursor-agent`; thiết lập IDE không cần CLI riêng.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration cursor-agent
```

Với dự án Spec Kit đã có, dùng `specify integration install cursor-agent`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.cursor/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của Cursor, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

<a id="options-and-workflow-permissions"></a>

## Tùy chọn và quyền của workflow

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill. Event gốc dùng `.cursor/hooks.json`; `--events false` tắt trình xử lý event của Spec Kit. Xem [runtime event](cli.md#runtime-events).

Các workflow step loại command và prompt còn cần thêm CLI `cursor-agent`. Việc điều phối dùng `-p --trust --approve-mcps --force`: các cờ này bỏ qua lời nhắc tin cậy workspace và phê duyệt việc nạp MCP cùng các thao tác công cụ. Chỉ chạy workflow trong dự án mà bạn thực sự muốn cấp các quyền đó. `--model` đã cấu hình và `--output-format json` khi được yêu cầu đều được chuyển tiếp.
