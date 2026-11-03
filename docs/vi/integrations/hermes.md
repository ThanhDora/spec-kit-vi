# Hermes

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/hermes.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Hermes Agent](https://github.com/NousResearch/hermes-agent) trước khi thiết lập. Khóa integration là `hermes`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Skill của nó được dùng chung giữa các dự án trong thư mục home của cùng người dùng. Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration hermes
```

Với dự án Spec Kit đã có, dùng `specify integration install hermes`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Khác với các integration skills cục bộ theo dự án, Hermes cài skill ở phạm vi toàn cục tại `~/.hermes/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của Hermes, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Một marker `.hermes/skills/` rỗng cục bộ trong dự án giúp nhận diện integration; bản thân các file skill lõi được sinh ra không được sao chép vào dự án. Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định.

<a id="global-ownership-and-removal"></a>

## Quyền sở hữu toàn cục và việc gỡ bỏ

Thiết lập có thể thay thế các file skill Spec Kit toàn cục của dự án khác.

**Uninstall xóa mọi thư mục skill `speckit-*` toàn cục, kể cả khi đã chỉnh sửa và kể cả khi không có `--force`.** Các file toàn cục này không được bảo vệ bởi các kiểm tra file đã sửa của manifest cục bộ trong dự án. Hãy sao lưu các tùy biến trước khi gỡ hoặc chuyển khỏi Hermes. Marker rỗng cục bộ trong dự án cũng bị xóa; skill toàn cục không thuộc Spec Kit vẫn được giữ.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `hermes chat -Q`. Prompt có tiền tố gạch chéo chọn skill bằng `-s`; phần văn bản còn lại được truyền bằng `-q`. Các prompt khác dùng trực tiếp `-q`. Adapter chuyển tiếp mô hình đã cấu hình bằng `-m` và yêu cầu `--json` để có đầu ra có cấu trúc.
