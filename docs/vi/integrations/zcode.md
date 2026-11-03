# ZCode

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/zcode.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [ZCode](https://zcode.z.ai/) trước khi thiết lập. Khóa integration là `zcode`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration zcode
```

Với dự án Spec Kit đã có, dùng `specify integration install zcode`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.zcode/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của the agent với tiền tố đô la, ví dụ `$speckit-specify`, hoặc `$speckit-bug-assess` khi đã cài extension bug.

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `zcode -p <prompt>` và yêu cầu `--output-format json` để có đầu ra có cấu trúc. Adapter bỏ qua thiết lập `model` của workflow vì ZCode không có cờ chọn mô hình cho từng lần gọi; hãy chọn mô hình trong phiên bằng `/model`.
