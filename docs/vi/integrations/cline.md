# Cline

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/cline.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Cline](https://github.com/cline/cline) trong IDE của bạn trước khi thiết lập. Khóa integration là `cline`; không cần CLI riêng.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration cline
```

Với dự án Spec Kit đã có, dùng `specify integration install cline`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Các workflow Markdown được cài trong `.clinerules/workflows/`, dùng tên file có gạch nối như `speckit-specify.md`. Gọi chúng trong khung chat của Cline bằng `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug, chứ không dùng lệnh dấu chấm.

Tham chiếu handoff và nội dung lệnh của extension/preset cũng được chuẩn hóa thành tên lệnh có gạch nối, nên `/speckit.git.commit` trong một lệnh extension trở thành `/speckit-git-commit`. Tên file `speckit.*.md` nằm trong một đường dẫn, như `.specify/extensions/git/commands/speckit.git.commit.md`, `C:\speckit.foo.md`, `C:\Program Files (x86)\speckit.foo.md`, `%TEMP%\speckit.foo.md` hoặc `./commands[old]/speckit.foo.md`, vẫn giữ dấu chấm và phần mở rộng `.md`. Một token đứng riêng hoặc có tiền tố gạch chéo như `/speckit.foo.md` được coi là tham chiếu lệnh và chuyển sang gạch nối. Nội dung lệnh lõi không bị viết lại theo cách này.

<a id="workflow-limitation"></a>

## Giới hạn của workflow

Integration này không hỗ trợ điều phối qua CLI cho các workflow step loại command hoặc prompt. Nó chỉ cài workflow cho IDE và không có tùy chọn thiết lập riêng.
