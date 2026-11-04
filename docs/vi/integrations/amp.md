# Amp

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/amp.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Amp CLI](https://ampcode.com/) trước khi thiết lập. Khóa integration là `amp`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration amp
```

Với dự án Spec Kit đã có, dùng `specify integration install amp`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Lệnh Markdown được cài trong `.agents/commands/`. Gọi chúng trong khung chat của agent bằng ký pháp dấu chấm, ví dụ `/speckit.specify`, hoặc `/speckit.bug.assess` khi đã cài extension bug.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `amp --execute <prompt>`, thêm `--stream-json` khi cần đầu ra có cấu trúc. Integration không chuyển tiếp thiết lập `model` của workflow: `--mode` của Amp chọn chế độ agent, không phải mô hình. Integration này không có tùy chọn thiết lập riêng.
