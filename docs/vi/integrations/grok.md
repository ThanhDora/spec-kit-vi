# Grok Build

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/grok.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Grok Build](https://docs.x.ai/build/overview) trước khi thiết lập. Khóa integration là `grok`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration grok
```

Với dự án Spec Kit đã có, dùng `specify integration install grok`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.grok/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

<a id="workflow-permissions"></a>

## Quyền của workflow

Workflow step dùng `grok -p <prompt> --always-approve`, tự động phê duyệt việc thực thi công cụ. Chỉ chạy workflow ở nơi bạn thực sự muốn cấp quyền đó. `--model` đã cấu hình và `--output-format json` khi được yêu cầu đều được chuyển tiếp. Integration này không có tùy chọn thiết lập riêng.
