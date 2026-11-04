<a id="generic-bring-your-own-agent"></a>

# Generic: Dùng agent của riêng bạn

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/generic.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Dùng integration `generic` cho agent lập trình AI chưa có integration có sẵn. Cung cấp thư mục đầu ra cục bộ trong dự án bằng `--commands-dir`. Integration này không yêu cầu CLI agent cụ thể nào.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài nhiều integration vì nó dùng đường dẫn đầu ra động. Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration generic --integration-options="--commands-dir .myagent/cmds"
```

Với dự án Spec Kit đã có:

```bash
specify integration install generic --integration-options="--commands-dir .myagent/cmds"
```

Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="output-options-and-invocation"></a>

## Tùy chọn đầu ra và cách gọi

| Tùy chọn | Mô tả |
| --- | --- |
| `--commands-dir <path>` | Bắt buộc. Thư mục đầu ra cục bộ trong dự án cho lệnh hoặc skill. |
| `--skills` | Ghi các thư mục `speckit-<command>/SKILL.md` thay vì các file phẳng `speckit.<command>.md`. |

Tham chiếu lệnh mặc định dùng `/speckit.specify` và `/speckit.bug.assess`. Chế độ skills đổi tham chiếu lệnh và hướng dẫn bước tiếp theo thành `/speckit-specify` và `/speckit-bug-assess`:

```bash
specify integration install generic --integration-options="--commands-dir .myagent/skills --skills"
```

Agent của bạn phải hỗ trợ bố cục file và kiểu gọi đã chọn; Spec Kit không bổ sung khả năng tự phát hiện lệnh gốc cho agent.

<a id="extensions"></a>

## Extension

Khi `generic` là integration đang hoạt động, `specify extension add` đăng ký lệnh của extension trong `--commands-dir` đã cấu hình, ở dạng file lệnh hoặc skill tùy theo `--skills`. `specify extension remove` gỡ các artifact chưa sửa thuộc extension, giữ nguyên lệnh lõi, file của người dùng và file extension đã chỉnh sửa.

<a id="workflow-limitation"></a>

## Giới hạn của workflow

Integration generic không hỗ trợ điều phối qua CLI cho các workflow step loại command hoặc prompt. Chọn thư mục đầu ra không cấu hình file thực thi, cũng không dạy Spec Kit cách gọi một CLI agent bất kỳ.
