# Command Code

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/command-code.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Command Code](https://commandcode.ai/docs) trước khi thiết lập. Khóa integration là `command-code`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration command-code
```

Với dự án Spec Kit đã có, dùng `specify integration install command-code`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.commandcode/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của the agent với tiền tố đô la, ví dụ `$speckit-specify`, hoặc `$speckit-bug-assess` khi đã cài extension bug.

<a id="options-and-workflow-dispatch"></a>

## Tùy chọn và điều phối workflow

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill.

Workflow step dùng `command-code -p <prompt>`, kèm `--model` khi đã cấu hình và `--output-format json` khi cần đầu ra có cấu trúc.
