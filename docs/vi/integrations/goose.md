# Goose

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/goose.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Goose](https://goose-docs.ai/) trước khi thiết lập. Khóa integration là `goose`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration goose
```

Với dự án Spec Kit đã có, dùng `specify integration install goose`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-recipes"></a>

## Recipe được cài

Goose dùng recipe YAML được cài tại `.goose/recipes/speckit.<command>.yaml`. Điều phối workflow của Spec Kit chuyển các lời gọi `/speckit.<command>` thành việc thực thi recipe, truyền các đối số phía sau làm tham số `args` của recipe. Hãy dùng giao diện recipe của Goose để chạy tương tác, thay vì cho rằng recipe là skill.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Việc điều phối dùng `goose run --recipe <path>` cho prompt `/speckit.<command>`, và `goose run -t <prompt>` cho văn bản prompt khác, kể cả slash command không thuộc Spec Kit. `--model` đã cấu hình và `--output-format json` khi được yêu cầu đều được chuyển tiếp.

Tránh lặp lại các cờ một giá trị như `--model`, `--recipe` hoặc `--output-format` trong `SPECKIT_INTEGRATION_GOOSE_EXTRA_ARGS`; Goose từ chối cờ xuất hiện trùng lặp thay vì dùng giá trị cuối. Integration này không có tùy chọn thiết lập riêng.
