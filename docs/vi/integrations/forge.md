# Forge

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/forge.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Forge](https://forgecode.dev/) trước khi thiết lập. Khóa integration là `forge`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration forge
```

Với dự án Spec Kit đã có, dùng `specify integration install forge`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Lệnh Markdown được cài trong `.forge/commands/`, dùng tên file có dấu chấm như `speckit.specify.md`. Tên lệnh trong frontmatter của chúng có gạch nối, như `speckit-specify`; tên file và tên gọi khác nhau. Gọi chúng trong khung chat của agent bằng `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug, chứ không dùng lệnh dấu chấm.

Template của Forge dùng `{{parameters}}` cho đối số. Spec Kit loại bỏ frontmatter `handoffs` không tương thích khi thiết lập lõi.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `forge -p <prompt>`. Adapter không chuyển tiếp `model` đã cấu hình và không thêm cờ đầu ra có cấu trúc. Hãy chọn mô hình trong cấu hình riêng của Forge, ví dụ bằng `forge config set model`. Integration này không có tùy chọn thiết lập riêng.
