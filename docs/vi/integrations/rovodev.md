# RovoDev

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/rovodev.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [RovoDev](https://www.atlassian.com/software/rovo-dev) trước khi thiết lập. Khóa integration là `rovodev`; điều phối lúc chạy dùng `acli rovodev`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration rovodev
```

Với dự án Spec Kit đã có, dùng `specify integration install rovodev`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills-and-prompts"></a>

## Skill và prompt được cài

Integration sinh `.rovodev/skills/`, các prompt bao bọc trong `.rovodev/prompts/` và `.rovodev/prompts.yml`. Skill dùng bố cục `speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent bằng `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Prompt bao bọc chứa `use skill <name> $ARGUMENTS`. Thiết lập gộp các mục manifest theo tên: mục được sinh ra thay thế mục trùng tên, còn các mục không trùng của người dùng giữ nguyên thứ tự. `prompts.yml` đã gộp được theo dõi như một file nguyên vẹn: nếu không đổi kể từ lúc thiết lập, nó bị xóa khi gỡ cài đặt, kể cả khi chứa các mục người dùng đã được gộp trước đó. Hãy sao lưu manifest đó nếu cần.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `acli rovodev run <prompt>`. Biến ghi đè file thực thi `SPECKIT_INTEGRATION_ROVODEV_EXECUTABLE` thay thế `acli`, không phải lệnh con `rovodev`. Yêu cầu đầu ra có cấu trúc thêm `--output-schema` với schema đối tượng kết quả. Thiết lập `model` của workflow không được chuyển tiếp. Integration này không có tùy chọn thiết lập riêng; chế độ skills luôn được dùng.
