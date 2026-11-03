# Pi Coding Agent

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/pi.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Pi Coding Agent](https://pi.dev) trước khi thiết lập. Khóa integration là `pi`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration pi
```

Với dự án Spec Kit đã có, dùng `specify integration install pi`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-prompts"></a>

## Prompt được cài

Prompt Markdown được cài trong `.pi/prompts/`. Gọi chúng trong khung chat của agent bằng ký pháp dấu chấm, ví dụ `/speckit.specify`, hoặc `/speckit.bug.assess` khi đã cài extension bug.

<a id="workflow-dispatch-and-tooling"></a>

## Điều phối workflow và công cụ

Workflow step dùng `pi -p <prompt>`, kèm `--model` khi đã cấu hình và `--mode json` (event JSONL), không phải `--output-format`, khi cần đầu ra có cấu trúc. Integration này không có tùy chọn thiết lập riêng.

Integration này dựng các file prompt; nó không cài hay cấu hình MCP server. Các lệnh cần công cụ GitHub đòi hỏi công cụ đó được cấu hình riêng trong Pi. Xem [extension của Pi](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent#extensions).
