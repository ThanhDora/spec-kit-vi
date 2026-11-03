# Codex CLI

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/codex.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Codex CLI](https://github.com/openai/codex) trước khi thiết lập. Khóa integration là `codex`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration codex
```

Với dự án Spec Kit đã có, dùng `specify integration install codex`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.agents/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của Codex với tiền tố đô la, ví dụ `$speckit-specify`, hoặc `$speckit-bug-assess` khi đã cài extension bug. Các integration khác cũng nhắm tới `.agents/skills/`; hãy xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project) trước khi cài agent khác dùng chung thư mục này.

<a id="options-and-workflow-dispatch"></a>

## Tùy chọn và điều phối workflow

`--integration-options="--skills"` chọn rõ bố cục skills, vốn đã là bố cục duy nhất được hỗ trợ cho integration này. Event gốc dùng `.codex/config.toml`; `--events false` tắt trình xử lý event của Spec Kit. Xem [runtime event](cli.md#runtime-events).

Workflow step dùng `codex exec <prompt>`, kèm `--model` khi đã cấu hình và `--json` khi cần đầu ra có cấu trúc. Khi đăng ký ở chế độ dev, Codex ghi file skill thay vì tạo symlink.
