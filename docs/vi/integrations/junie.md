# Junie

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/junie.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Junie](https://junie.jetbrains.com/) trước khi thiết lập. Khóa integration là `junie`; Specify kiểm tra CLI của nó.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration junie
```

Với dự án Spec Kit đã có, dùng `specify integration install junie`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Lệnh Markdown được cài trong `.junie/commands/`, dùng tên file có gạch nối như `speckit-specify.md`. Gọi chúng trong khung chat của Junie bằng `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug, chứ không dùng lệnh dấu chấm.

Tham chiếu handoff và nội dung lệnh của extension/preset cũng được chuẩn hóa thành tên có gạch nối.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `junie --task <prompt>`, kèm `--model` khi đã cấu hình và `--output-format json` khi cần đầu ra có cấu trúc. Integration này không có tùy chọn thiết lập riêng.
