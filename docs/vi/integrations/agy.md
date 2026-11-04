# Antigravity

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/agy.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Antigravity](https://antigravity.google/) trước khi thiết lập. Khóa integration là `agy`. Bố cục skills yêu cầu Antigravity CLI v1.0.0 trở lên, hoặc Antigravity IDE v2.0.0 trở lên.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration agy
```

Với dự án Spec Kit đã có, dùng `specify integration install agy`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.agents/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug. Thư mục này dùng chung với các integration khác, nên đừng cho rằng skill do chúng sinh ra có thể cùng tồn tại mà không chồng lấn.

<a id="headless-permissions"></a>

## Quyền khi chạy headless

Mặc định, việc tự động phê duyệt công cụ bị tắt. Trong các lần chạy headless không tương tác, chỉ bật rõ ràng `--dangerously-skip-permissions` bằng cách đặt `SPECKIT_AGY_ALLOW_ALL_TOOLS=1` hoặc `SPECKIT_INTEGRATION_AGY_ALLOW_ALL_TOOLS=1` nếu bạn thực sự muốn cho phép các thao tác công cụ mà không cần phê duyệt tương tác.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `agy --print <prompt>`. Spec Kit truyền `--add-dir` với thư mục gốc dự án để skill vẫn được tìm thấy, chuyển tiếp `--model` nếu đã cấu hình, và yêu cầu `--output-format json` để có đầu ra có cấu trúc. Integration này không có tùy chọn thiết lập riêng.
