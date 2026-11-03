# Oh My Pi

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/omp.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Oh My Pi](https://www.npmjs.com/package/@oh-my-pi/pi-coding-agent) trước khi thiết lập. Khóa integration là `omp`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration omp
```

Với dự án Spec Kit đã có, dùng `specify integration install omp`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-commands"></a>

## Lệnh được cài

Slash command Markdown được cài trong `.omp/commands/`. Gọi chúng trong khung chat của agent bằng ký pháp dấu chấm, ví dụ `/speckit.specify`, hoặc `/speckit.bug.assess` khi đã cài extension bug.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `omp --print <prompt>`; `--print` bật chế độ chạy một lần và prompt là đối số vị trí. Adapter chuyển tiếp `--model` đã cấu hình và dùng `--mode json`, không phải `--output-format`, cho đầu ra có cấu trúc. Integration này không có tùy chọn thiết lập riêng.
