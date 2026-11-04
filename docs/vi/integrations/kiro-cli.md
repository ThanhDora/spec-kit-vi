# Kiro CLI

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/kiro-cli.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Kiro CLI](https://kiro.dev/docs/cli/) trước khi thiết lập. Khóa integration là `kiro-cli`. Phép kiểm tra tương thích file thực thi cũng chấp nhận `kiro`, nhưng `kiro` không phải là khóa integration đã đăng ký.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration kiro-cli
```

Với dự án Spec Kit đã có, dùng `specify integration install kiro-cli`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-prompts"></a>

## Prompt được cài

Prompt Markdown được cài trong `.kiro/prompts/`. Spec Kit dùng tên dấu chấm như `speckit.specify`; hãy dùng [giao diện prompt](https://kiro.dev/docs/cli/chat/manage-prompts/) của Kiro để chọn chúng.

Kiro CLI không thay thế `$ARGUMENTS` trong prompt dạng file. Vì vậy Spec Kit hiển thị một đoạn văn dự phòng hướng dẫn mô hình lấy đối số từ cuộc hội thoại. Xem [github/spec-kit#1926](https://github.com/github/spec-kit/issues/1926).

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng file thực thi `kiro-cli` với `-p <prompt>`, chuyển tiếp `--model` và yêu cầu `--output-format json` khi phù hợp. Việc phát hiện công cụ cũng nhận ra file thực thi `kiro`, nhưng file thực thi điều phối mặc định của adapter vẫn là `kiro-cli`. Nếu chỉ có `kiro`, hãy đặt `SPECKIT_INTEGRATION_KIRO_CLI_EXECUTABLE` thành đường dẫn của nó để điều phối workflow. Integration này không có tùy chọn thiết lập riêng.
