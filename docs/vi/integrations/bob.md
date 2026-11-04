# IBM Bob

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/bob.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [IBM Bob](https://www.ibm.com/products/bob) trước khi thiết lập. Khóa integration là `bob`; không cần CLI riêng.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration bob
```

Với dự án Spec Kit đã có, dùng `specify integration install bob`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="default-skills-layout"></a>

## Bố cục skills mặc định

Skill được cài tại `.bob/skills/speckit-<command>/SKILL.md`. Skill của Bob được kích hoạt theo ý định: hãy yêu cầu Bob dùng skill `speckit-specify`, hoặc `speckit-bug-assess` khi đã cài extension bug. Spec Kit hiển thị tham chiếu `/speckit-<command>` cho việc điều phối lệnh ở chế độ skills, nhưng điều đó không có nghĩa mỗi skill là một slash command riêng được đăng ký trong IDE.

<a id="legacy-commands-and-migration"></a>

## Lệnh kiểu cũ và chuyển đổi

Truyền `--integration-options="--legacy-commands"` để dựng bố cục Bob 1.x đã ngừng hỗ trợ (`.bob/commands/*.md`) thay thế. Cờ này sẽ bị gỡ bỏ trong một bản phát hành tương lai.

Các bản cài kiểu cũ hiện có có thể chuyển đổi bằng:

```bash
specify integration upgrade bob --integration-options="--skills"
```

Lệnh này chuyển bản cài sang bố cục skills và xóa các file lệnh cũ. Nếu đã cài preset ghi đè, việc chuyển đổi sẽ bị từ chối vì chưa thể đối soát artifact của preset qua một lần thay đổi bố cục. Hãy gỡ các preset, chuyển đổi, rồi cài lại chúng.

`--skills` và `--legacy-commands` loại trừ lẫn nhau. Khi không có lựa chọn rõ ràng, các file lệnh kiểu cũ được quản lý sẽ giữ bản cài hiện có ở chế độ kiểu cũ, trừ khi đã có skill Spec Kit được quản lý. Chỉ tạo một thư mục `.bob/skills/` không liên quan thì không chuyển đổi bản cài. Tham chiếu lệnh kiểu cũ giữ dạng dấu chấm `/speckit.<command>`.

<a id="workflow-permissions"></a>

## Quyền của workflow

Điều phối workflow còn cần thêm CLI `bob`, dù thiết lập IDE thì không cần. Nó dùng `bob run --trust --accept-license` với prompt ở dạng đối số vị trí, chọn `-f pretty` cho đầu ra dạng stream hoặc `-f json` cho đầu ra được thu lại. Các cờ trust và license áp dụng cho lần gọi không tương tác này.

Adapter không chuyển tiếp thiết lập `model` của workflow; Bob chọn mô hình qua `session.model` trong thiết lập riêng của nó.
