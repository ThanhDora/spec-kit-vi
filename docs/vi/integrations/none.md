<a id="none-shared-scaffolding-only"></a>

# None: Chỉ phần khung dùng chung

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/none.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Dùng integration `none` cho dự án trung lập với agent. Nó cài phần khung `.specify/` dùng chung mà không có lệnh, skill, thiết lập hay hook riêng của agent nào. Không cần agent lập trình nào.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài nhiều integration vì nó không sinh file riêng cho agent nào. Các integration đã cài khác cũng phải được khai báo an toàn thì mới cùng tồn tại được mà không cần `--force`. Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration none
```

Để thay integration mặc định hiện tại trong một dự án đã có:

```bash
specify integration switch none
```

Nếu `none` đã được cài, `switch` chỉ chọn nó làm mặc định; lệnh này không gỡ các integration khác. Xem [quản lý integration](cli.md) để biết cách cài đặt, kích hoạt và dọn dẹp.

<a id="shared-files-and-removal"></a>

## File dùng chung và việc gỡ bỏ

Template, script, constitution, workflow đi kèm và metadata dự án vẫn có trong `.specify/`. Manifest file được sinh ra của integration này rỗng; gỡ `none` không xóa phần khung dùng chung hay các file không thuộc quyền sở hữu của nó.

Về cách làm tùy chọn cho nhóm dùng nhiều agent, xem [Làm việc theo nhóm](index.md#working-in-a-team).

<a id="workflow-limitation"></a>

## Giới hạn của workflow

Integration này không thể điều phối workflow step loại command hoặc prompt. Hãy chuyển sang một integration agent hỗ trợ điều phối qua CLI để chạy các step đó. Integration này không có tùy chọn thiết lập riêng.
