# Qoder CLI

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/qodercli.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Qoder CLI](https://qoder.com/cli) trước khi thiết lập. Khóa integration là `qodercli`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration qodercli
```

Với dự án Spec Kit đã có, dùng `specify integration install qodercli`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.qoder/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Bố cục skills thay thế việc quét `.qoder/commands/` kiểu cũ. Khi các extension đang bật được đăng ký lại, file lệnh extension phẳng kiểu cũ chỉ bị loại bỏ sau khi đã có file skill thay thế. Hãy sao lưu các chỉnh sửa trên những lệnh extension kiểu cũ đó trước khi đăng ký lại: việc loại bỏ này không so sánh hash nội dung của chúng.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `qodercli -p <prompt>`, kèm `--model` khi đã cấu hình và `--output-format json` khi cần đầu ra có cấu trúc. Integration này không có tùy chọn thiết lập riêng; chế độ skills luôn được dùng.
