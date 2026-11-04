<a id="agentic-bug-fix"></a>

# Sửa lỗi có agent

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/agentic-bugfix.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Extension **bug** bổ sung một quy trình phân loại lỗi ba bước — đánh giá, sửa và xác nhận — mà agent lập trình của bạn chạy song song với quy trình lõi [SDD có agent](agentic-sdd.md). Mỗi bug nằm trong thư mục riêng tại `.specify/bugs/<slug>/`, với một báo cáo Markdown cho mỗi giai đoạn.

Để xem ví dụ có hướng dẫn, hãy làm theo [Bắt đầu nhanh với sửa lỗi](../guides/bugfix.md). Sửa lỗi không cần chạy quy trình tính năng SDD trước. Để đánh giá một ý tưởng thay vì sửa hành vi bị hỏng, xem [Đánh giá ý tưởng](agentic-assessment.md).

> [!NOTE]
> Trang này viết các lệnh ở dạng `/speckit.bug.*`. Chế độ skills mặc định của GitHub Copilot dùng `/speckit-bug-*`; một số agent khác dùng `$speckit-bug-*` (ví dụ Codex, ZCode) hoặc `/skill:speckit-bug-*` (ví dụ Kimi). Xem [Cách gọi lệnh](../integrations/cli.md#command-invocation).

Extension bug là extension đi kèm, cần chủ động bật. Hãy cài nó trước khi dùng các lệnh này:

```bash
specify extension add bug
```

Ba lệnh dùng chung một định danh — **slug**, tên thư mục của từng bug trong `.specify/bugs/`. Truyền nó bằng `slug=<name>`; nếu bỏ qua, `/speckit.bug.assess` sẽ hỏi (hoặc sinh slug duy nhất ở chế độ tự động). Slug được chuẩn hóa thành kebab-case chữ thường. Nếu đã có bản đánh giá cho một slug, lần chạy tương tác sẽ hỏi trước khi ghi đè, còn lần chạy tự động sẽ từ chối và chọn một slug duy nhất mới.

```text
/speckit.bug.assess -> /speckit.bug.fix -> /speckit.bug.test
```

## `/speckit.bug.assess`

Phân loại một báo cáo lỗi — văn bản được dán (như stack trace) hoặc URL (như một GitHub issue) — dựa trên codebase: nó đánh giá báo cáo có phải lỗi thật không, xác định các đường code nghi vấn và đề xuất cách khắc phục. Lệnh này **chỉ đọc**: nó chỉ ghi `assessment.md` và không bao giờ sửa mã nguồn.

```text
/speckit.bug.assess "TypeError: cannot read properties of undefined (reading 'token') at /auth/callback"
```

```text
/speckit.bug.assess https://github.com/example/repo/issues/1234 slug=callback-token
```

Đầu ra: `.specify/bugs/<slug>/assessment.md`.

## `/speckit.bug.fix`

Áp dụng cách khắc phục được mô tả trong bản đánh giá và ghi lại chính xác những gì đã thay đổi. Đây là lệnh bug **duy nhất** sửa mã nguồn, và nó chỉ làm việc trong các file được liệt kê trong bản đánh giá, trừ khi bằng chứng mới đòi hỏi mở rộng phạm vi (được ghi trong mục **Deviations from Assessment**).

```text
/speckit.bug.fix slug=callback-token
```

Đầu ra: `.specify/bugs/<slug>/fix.md`.

## `/speckit.bug.test`

Xác nhận bản sửa bằng cách chạy lại bước tái hiện và mọi test được thêm, rồi ghi kết quả kiểm chứng — một trong `verified`, `partial` hoặc `failed`. Giống `assess`, nó **chỉ đọc** đối với mã nguồn. Kết luận không bao giờ bị phóng đại: nếu bản đánh giá có liệt kê bước tái hiện mà thực tế không được chạy, kết quả tổng thể bị hạ xuống `partial` thay vì báo là `verified`.

```text
/speckit.bug.test slug=callback-token
```

Đầu ra: `.specify/bugs/<slug>/test.md`.

<a id="extension-hooks"></a>

## Hook của extension

Mỗi lệnh bug cung cấp hook `before_bug_<command>` và `after_bug_<command>` cho các extension khác. Pre-hook chạy sau khi phân giải slug và kiểm tra điều kiện tiên quyết; bước đánh giá tạo thư mục bug trước. Post-hook chạy sau khi báo cáo được ghi và trước khi báo hoàn tất. Một báo cáo được dán không thể hiểu được sẽ dừng mà không ghi bản đánh giá hay chạy post-hook; before-hook có thể đã chạy. Hook là các prompt chạy trong cùng phiên; chúng dùng lại `BUG_SLUG` và `BUG_DIR` đã phân giải (và, với post-hook, cả báo cáo đã ghi) từ cuộc hội thoại, và không có biến nào được chèn vào. Khi không có hook nào được đăng ký, workflow vẫn chạy như trước. Xem [các event hook và ví dụ cấu hình của extension bug](https://github.com/github/spec-kit/blob/main/extensions/bug/README.md#hooks).
