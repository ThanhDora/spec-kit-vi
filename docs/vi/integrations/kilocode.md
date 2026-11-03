# Kilo Code

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/kilocode.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Kilo Code](https://github.com/Kilo-Org/kilocode) trong your IDE trước khi thiết lập. Khóa integration là `kilocode`; không cần CLI riêng.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration kilocode
```

Với dự án Spec Kit đã có, dùng `specify integration install kilocode`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Lệnh Markdown được cài trong `.kilo/commands/`. Gọi chúng trong khung chat của agent bằng ký pháp dấu chấm, ví dụ `/speckit.specify`, hoặc `/speckit.bug.assess` khi đã cài extension bug.

Các bản cài `.kilocode/workflows/` kiểu cũ vẫn được hỗ trợ làm phương án dự phòng khi đăng ký.

Upgrade chuyển các lệnh lõi được theo dõi bằng manifest sang `.kilo/commands/`. Nếu ghi đè lệnh của preset ảnh hưởng đến thư mục kiểu cũ, việc nâng cấp bị từ chối trước khi thay đổi file; hãy gỡ các preset, nâng cấp, rồi cài lại chúng. Registry preset không đọc được cũng chặn việc chuyển đổi đó.

<a id="workflow-limitation"></a>

## Giới hạn của workflow

Integration này không hỗ trợ điều phối qua CLI cho các workflow step loại command hoặc prompt. Nó chỉ cài lệnh cho IDE và không có tùy chọn thiết lập riêng.
