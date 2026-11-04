# opencode

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/opencode.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [opencode](https://opencode.ai/) trước khi thiết lập. Khóa integration là `opencode`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration opencode
```

Với dự án Spec Kit đã có, dùng `specify integration install opencode`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Lệnh Markdown được cài trong `.opencode/commands/`. Gọi chúng trong khung chat của agent bằng ký pháp dấu chấm, ví dụ `/speckit.specify`, hoặc `/speckit.bug.assess` khi đã cài extension bug.

Các bản cài `.opencode/command/` kiểu cũ vẫn là phương án dự phòng khi đăng ký nếu thư mục chuẩn chưa tồn tại.

<a id="runtime-events-and-workflow-dispatch"></a>

## Runtime event và điều phối workflow

Event gốc dùng `.opencode/plugin/speckit-events.ts` thay vì map hook JSON; Spec Kit gộp tham chiếu plugin của nó vào `opencode.json`. `--integration-options="--events false"` tắt trình xử lý event của Spec Kit. Xem [runtime event](cli.md#runtime-events).

Workflow step dùng `opencode run`. Prompt có tiền tố gạch chéo trở thành `--command <name>` với phần văn bản còn lại làm message; các prompt khác được truyền làm văn bản message. Adapter chuyển tiếp mô hình đã cấu hình bằng `-m` và yêu cầu `--format json` để có đầu ra có cấu trúc.
