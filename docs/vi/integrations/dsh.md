# DeepSeek Harness

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/dsh.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) trước khi thiết lập. Khóa integration là `dsh`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration dsh
```

Với dự án Spec Kit đã có, dùng `specify integration install dsh`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.dsh/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `dsh --profile headless <prompt>`. Adapter bỏ qua `model` của workflow và yêu cầu đầu ra có cấu trúc: profile headless trả về tin nhắn cuối của assistant dưới dạng văn bản thuần. Integration này không có tùy chọn thiết lập riêng.
