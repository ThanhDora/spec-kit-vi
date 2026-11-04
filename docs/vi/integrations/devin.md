# Devin for Terminal

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/devin.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Devin for Terminal](https://cli.devin.ai/docs) trước khi thiết lập. Khóa integration là `devin`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration devin
```

Với dự án Spec Kit đã có, dùng `specify integration install devin`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.devin/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

<a id="options-and-workflow-dispatch"></a>

## Tùy chọn và điều phối workflow

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill. Event gốc dùng `.devin/hooks.v1.json`; `--events false` tắt trình xử lý event của Spec Kit. Xem [runtime event](cli.md#runtime-events).

Workflow step dùng `devin -p <prompt>` và chuyển tiếp `--model` đã cấu hình. Adapter của Devin trả về stdout dạng văn bản thuần kể cả khi yêu cầu đầu ra có cấu trúc; nó không thêm cờ đầu ra JSON.
