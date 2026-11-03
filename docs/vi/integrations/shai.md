# SHAI (OVHcloud)

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/shai.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [SHAI](https://github.com/ovh/shai) trước khi thiết lập. Khóa integration là `shai`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration shai
```

Với dự án Spec Kit đã có, dùng `specify integration install shai`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Lệnh Markdown được cài trong `.shai/commands/`, dùng tên dấu chấm như `speckit.specify.md`.

<a id="workflow-limitation"></a>

## Giới hạn của workflow

Workflow step loại `command` và `prompt` không thể chạy qua SHAI. CLI của nó nhận văn bản prompt qua đối số, stdin hoặc `shai agent`, nhưng chuyển cho agent tự sửa lỗi của nó và không bao giờ nạp `.shai/commands/`, nên các step đó thất bại.

Adapter chủ động từ chối điều phối qua CLI thay vì báo thành công mà không chạy lệnh đã cài. Integration này không có tùy chọn thiết lập riêng.
