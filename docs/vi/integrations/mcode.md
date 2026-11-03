# MiniMax Code

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/mcode.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [MiniMax Code](https://github.com/MiniMax-AI/minimax-code) trước khi thiết lập. Khóa integration là `mcode`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration mcode
```

Với dự án Spec Kit đã có, dùng `specify integration install mcode`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.minimax/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill.

<a id="headless-permissions"></a>

## Quyền khi chạy headless

Điều phối workflow headless dùng `--permission full` để thao tác công cụ không bị chặn bởi cơ chế kiểm soát quyền khi chạy headless. Đặt `SPECKIT_INTEGRATION_MCODE_EXTRA_ARGS="--permission smart"` để dùng chính sách chặt chẽ hơn của MiniMax Code.

Việc điều phối dùng `mcode exec <prompt>`. `--model` đã cấu hình và `--output-format json` khi được yêu cầu đều được chuyển tiếp.
