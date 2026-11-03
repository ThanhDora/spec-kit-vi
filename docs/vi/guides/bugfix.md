<a id="bug-fixing-quickstart"></a>

# Hướng dẫn nhanh sửa lỗi

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../guides/bugfix.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Dùng quy trình này khi một hành vi hiện có bị hỏng và bạn cần chẩn đoán dựa trên
bằng chứng, một bản sửa có giới hạn phạm vi và việc xác minh dựa trên báo cáo ban đầu. Bạn
không cần chạy quy trình tính năng SDD trước.

Extension **bug** đi kèm (bundled), chỉ chạy khi bạn chủ động bật, chia công việc thành
**assess → fix → test** (đánh giá → sửa → kiểm thử). Mỗi lỗi có một thư mục trong
`.specify/bugs/<slug>/` chứa bản chẩn đoán, bản ghi thay đổi và kết quả kiểm thử.

<a id="set-up"></a>

## Thiết lập

Trước tiên hãy [cài Spec Kit](../installation.md) và khởi tạo repository
chứa lỗi. Nếu repository đã có code, hãy làm theo
[Áp dụng Spec Kit vào dự án có sẵn](existing-projects.md).

Trong terminal, tại thư mục gốc của dự án đã khởi tạo, cài extension:

```bash
specify extension add bug
```

Sau đó mở agent lập trình trong thư mục đó. Các ví dụ dưới đây dùng
chế độ skills mặc định của GitHub Copilot (`--integration copilot`). Các agent khác
cung cấp cùng các bước với
[cú pháp gọi lệnh](../integrations/cli.md#command-invocation) riêng.
Gọi từng skill `/speckit-bug-*` riêng biệt trong khung chat của agent và review
kết quả trước khi tiếp tục. Đây là skill của agent, không phải lệnh terminal;
lệnh terminal ở trên chỉ để cài extension.

<a id="1-assess-the-bug"></a>

## 1. Đánh giá lỗi

Cung cấp triệu chứng, các bước tái hiện và hành vi mong đợi. URL của một GitHub issue
hoặc stack trace cũng dùng được. Chọn một tên ngắn, dùng lại được cho lỗi:

```text
/speckit-bug-assess "Submitting the login form with an empty password crashes the app instead of showing a validation error." slug=login-crash
```

Agent điều tra code và ghi
`.specify/bugs/login-crash/assessment.md`. Bước này không thay đổi mã nguồn.
Hãy review bản chẩn đoán và hướng khắc phục được đề xuất trước khi yêu cầu sửa; đừng
tiếp tục với một chẩn đoán thiếu căn cứ hoặc một báo cáo không phải là lỗi.

<a id="2-fix-the-assessed-cause"></a>

## 2. Sửa nguyên nhân đã đánh giá

Dùng cùng slug:

```text
/speckit-bug-fix slug=login-crash
```

Agent áp dụng hướng khắc phục đã đánh giá và ghi lại các thay đổi trong
`.specify/bugs/login-crash/fix.md`. Đây là bước duy nhất sửa mã
nguồn. Nếu bằng chứng mới đòi hỏi phần việc nằm ngoài phạm vi đã đánh giá, agent phải
ghi lại sự sai lệch đó thay vì âm thầm mở rộng bản sửa.

<a id="3-test-the-fix"></a>

## 3. Kiểm thử bản sửa

```text
/speckit-bug-test slug=login-crash
```

Agent chạy lại các bước tái hiện và các test liên quan, rồi ghi
`.specify/bugs/login-crash/test.md`. Bước này ghi lại bằng chứng; nó không
sửa mã nguồn để làm cho test đang lỗi chạy qua.

| Kết luận | Ý nghĩa | Việc cần làm |
| --- | --- | --- |
| `verified` | Các yêu cầu xác minh đã được thực hiện thành công | Review bản vá và bằng chứng trước khi merge |
| `partial` | Một phần việc xác minh chưa thể hoàn tất | Bổ sung môi trường hoặc bằng chứng tái hiện còn thiếu rồi kiểm thử lại |
| `failed` | Việc xác minh phát hiện vấn đề còn tồn tại | Xem lại chẩn đoán hoặc bản sửa dựa trên bằng chứng đó, rồi kiểm thử lại |

Chỉ riêng bộ test chạy qua là chưa đủ nếu các bước tái hiện ban đầu chưa từng
được chạy. Hãy giữ bản đánh giá, bản ghi sửa lỗi và báo cáo kiểm thử cùng nhau để người review
có thể lần theo bản sửa từ triệu chứng đến bằng chứng.

<a id="learn-more"></a>

## Tìm hiểu thêm

- [Tài liệu tham khảo lệnh bug](../../reference/agentic-bugfix.md): đối số, cách xử lý slug và contract đầu ra.
- [Hướng dẫn nhanh SDD](../quickstart.md): dùng khi công việc là một tính năng mới chứ không phải sửa lỗi.
- [Hướng dẫn nhanh đánh giá ý tưởng](assessment.md): điều tra xem một thay đổi được đề xuất có đáng theo đuổi hay không.
