# Alquimia AI

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/alquimia.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Alquimia AI CLI](https://docs.alquimia.ai) trước khi thiết lập. Khóa integration là `alquimia`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration alquimia
```

Với dự án Spec Kit đã có, dùng `specify integration install alquimia`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.alquimia/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Skill được sinh ra vừa do người dùng gọi được vừa do mô hình gọi được; các skill lõi được hỗ trợ còn nhận gợi ý đối số ngay trong dòng.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Các workflow step loại command và prompt dùng `alquimia -p <prompt>`, kèm `--model` khi đã cấu hình và `--output-format json` khi cần đầu ra có cấu trúc. Integration này không có tùy chọn thiết lập riêng.
