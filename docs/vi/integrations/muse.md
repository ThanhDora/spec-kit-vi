# Muse Code

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/muse.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Muse Code](https://dev.meta.ai/docs/muse-code) trước khi thiết lập. Khóa integration là `muse`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration muse
```

Với dự án Spec Kit đã có, dùng `specify integration install muse`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.agents/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug. Thư mục này dùng chung với các integration khác, nên đừng cho rằng skill do chúng sinh ra có thể cùng tồn tại mà không chồng lấn.

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `muse exec <prompt>`, kèm `--model` khi đã cấu hình và `--json` khi cần đầu ra có cấu trúc.
