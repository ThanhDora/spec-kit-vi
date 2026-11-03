# Lingma

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/lingma.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Lingma](https://lingma.aliyun.com/) trong your IDE trước khi thiết lập. Khóa integration là `lingma`; không cần CLI riêng.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration lingma
```

Với dự án Spec Kit đã có, dùng `specify integration install lingma`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được tự động cài tại `.lingma/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill.

<a id="workflow-limitation"></a>

## Giới hạn của workflow

Integration này không hỗ trợ điều phối qua CLI cho các workflow step loại command hoặc prompt; cách được hỗ trợ là giao diện skills trong IDE.
