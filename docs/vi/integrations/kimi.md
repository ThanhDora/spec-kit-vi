# Kimi Code

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/kimi.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Kimi Code](https://code.kimi.com/) trước khi thiết lập. Khóa integration là `kimi`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration kimi
```

Với dự án Spec Kit đã có, dùng `specify integration install kimi`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.kimi-code/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của Kimi với tiền tố skill và dấu hai chấm, ví dụ `/skill:speckit-specify`, hoặc `/skill:speckit-bug-assess` khi đã cài extension bug.

Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill.

<a id="legacy-migration"></a>

## Chuyển đổi từ kiểu cũ

Truyền `--integration-options="--migrate-legacy"` khi nâng cấp bản cài cũ để chuyển skill từ `.kimi/skills/` sang `.kimi-code/skills/`. Việc chuyển đổi cũng đổi tên skill dấu chấm như `speckit.xxx` thành tên có gạch nối như `speckit-xxx`:

```bash
specify integration upgrade kimi --integration-options="--migrate-legacy"
```

Thiết lập ghi các skill mới trước. Thư mục kiểu cũ chỉ được di chuyển nếu đích mới của nó chưa tồn tại. Nếu đích đã tồn tại, thư mục cũ chỉ bị xóa khi cả hai file `SKILL.md` giống hệt nhau từng byte và thư mục kiểu cũ không có file nào khác. Nội dung kiểu cũ khác biệt và các file bổ sung của người dùng được giữ lại để đối soát thủ công. Đường dẫn kiểu cũ là symlink sẽ bị bỏ qua; thành phần đích là symlink sẽ bị từ chối.

<a id="legacy-cleanup-on-uninstall"></a>

## Dọn dẹp kiểu cũ khi gỡ cài đặt

Các file thông thường được theo dõi bằng manifest dùng cơ chế bảo vệ file đã sửa dùng chung. Ngoài ra, bước gỡ bỏ còn xóa các thư mục `.kimi/skills/speckit-*` và `speckit.*` kiểu cũ được nhận diện qua `metadata.author` và `metadata.source` được sinh ra. Việc dọn dẹp kiểu cũ đó không so sánh hash đã ghi và không cần `--force`; hãy sao lưu các skill kiểu cũ đã sửa và file bổ sung trong các thư mục đó trước khi gỡ cài đặt.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `kimi -p <prompt>` với lời gọi `/skill:speckit-<command>` và chuyển tiếp `--model` đã cấu hình. Yêu cầu đầu ra có cấu trúc dùng `--output-format stream-json` (event JSONL), không phải giá trị `json` không được hỗ trợ.
