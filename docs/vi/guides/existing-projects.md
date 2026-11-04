<a id="adopting-spec-kit-in-an-existing-project"></a>

# Áp dụng Spec Kit vào dự án có sẵn

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../guides/existing-projects.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Bạn không cần dựng lại hệ thống hiện có từ đặc tả trước khi dùng
Spec Kit. Hãy khởi tạo ngay trong repository, ghi lại những quy tắc quan trọng
và dùng quy trình cho thay đổi có giới hạn tiếp theo.

<a id="1-start-from-a-reviewable-baseline"></a>

## 1. Bắt đầu từ một mốc có thể review

Trước khi khởi tạo, hãy commit hoặc stash công việc đang dở và tạo một branch cho việc
áp dụng. Nhờ vậy mọi file được sinh ra đều hiện rõ trong một lần code review bình thường.

Chọn [khóa integration](../../integrations/index.md) cho agent lập trình
bạn đang dùng. Sau đó chạy lệnh từ thư mục gốc của repository:

```bash
specify init --here --force --integration <key>
```

`--here` nhắm tới thư mục hiện tại. `--force` cho phép khởi tạo trong
thư mục không rỗng và có thể thay thế file tại các đường dẫn được quản lý bị trùng, nên chỉ dùng
sau khi đã tạo mốc có thể review. Nó không xóa phần còn lại của
ứng dụng.

Hãy review diff kết quả trước khi tiếp tục. Việc khởi tạo thêm các file dự án dùng chung trong
`.specify/` cùng các file lệnh hoặc skill mà integration bạn chọn
cần đến. Nó không viết lại ứng dụng của bạn và cũng không tự suy ra
đặc tả cho các hành vi hiện có.

> [!NOTE]
> Khởi tạo Git và feature branch là tùy chọn, do extension
> **git** quản lý. Thêm nó bằng `specify extension add git` nếu bạn muốn dùng
> quy trình đó.

<a id="2-capture-project-guardrails"></a>

## 2. Ghi lại các rào chắn của dự án

Các bước còn lại minh họa việc áp dụng **SDD** cho một tính năng có giới hạn. Nếu
việc đầu tiên của bạn là sửa lỗi, bạn có thể làm theo
[hướng dẫn nhanh sửa lỗi](bugfix.md) sau khi khởi tạo; để đánh giá một đề xuất,
hãy dùng [hướng dẫn nhanh đánh giá ý tưởng](assessment.md). Cả hai quy trình đều không yêu cầu
hoàn tất các bước SDD bên dưới trước.

Chạy `/speckit.constitution` với những nguyên tắc vốn đã đúng với
repository hoặc đã được nhóm thống nhất rõ ràng là sẽ áp dụng:

```text
/speckit.constitution Preserve public API compatibility. Follow the existing
service boundaries. Every database migration must include a rollback plan.
Run the repository's established unit and integration test suites.
```

Hãy dùng README, các quyết định kiến trúc, hướng dẫn đóng góp và
cấu hình CI của repository làm bằng chứng. Đừng bịa ra tiêu chuẩn chỉ để lấp đầy
template hiến chương. Hiến chương chi phối việc lập kế hoạch và phân tích về sau,
nên những quy tắc phi thực tế chỉ tạo ra nhiễu thay vì ràng buộc hữu ích.

<a id="3-choose-a-bounded-first-change"></a>

## 3. Chọn một thay đổi đầu tiên có giới hạn

Bắt đầu với một tính năng hoặc một lát cắt hiện đại hóa có thể review
độc lập. Đừng lấy "viết tài liệu cho toàn bộ hệ thống hiện có" làm tính năng
đầu tiên, trừ khi bản kiểm kê đó chính là sản phẩm cần bàn giao.

Mô tả cả kết quả mong muốn lẫn các ranh giới tương thích phải
được giữ nguyên:

```text
/speckit.specify Add CSV export to the existing orders page. Preserve current
filters and authorization behavior. Export only the rows visible to the signed-in
user, and do not change the existing JSON API response.
```

Codebase vẫn là ngữ cảnh triển khai. `spec.md` mới xác định
thay đổi bạn định thực hiện, không phải bản đặc tả hồi tố cho mọi hành vi
hiện có.

<a id="4-plan-against-the-repository"></a>

## 4. Lập kế hoạch dựa trên repository

Tiếp tục với quy trình thông thường:

1. Chạy `/speckit.clarify` để giải quyết các hành vi chưa chắc chắn và các yêu cầu
   về tương thích.
2. Chạy `/speckit.plan` và kiểm tra thiết kế được đề xuất có tái sử dụng kiến trúc,
   thư viện phụ thuộc và quy ước kiểm thử hiện có.
3. Chạy `/speckit.tasks`, rồi `/speckit.analyze` để kiểm tra tính nhất quán trước khi
   triển khai.
4. Chạy `/speckit.implement` và review thay đổi về code lẫn artifact cùng lúc.
5. Chạy `/speckit.converge` để tìm những thiếu sót còn lại. Nếu lệnh bổ sung tác vụ, hãy lặp lại
   triển khai và hội tụ cho đến khi tính năng hoàn tất.

Để biết chi tiết các lệnh và các cổng kiểm soát chất lượng tùy chọn, xem
[Hướng dẫn nhanh](../quickstart.md) và
[tài liệu tham khảo Agentic SDD](../../reference/agentic-sdd.md).

<a id="5-decide-how-specs-will-age"></a>

## 5. Quyết định cách đặc tả "già đi"

Sau thay đổi đầu tiên, hãy thống nhất cách nhóm duy trì các artifact của tính năng
đã hoàn tất:

- Giữ mỗi thư mục tính năng như một bản ghi lịch sử bất biến.
- Duy trì `spec.md` như một contract sống và sinh lại các artifact phía sau.
- Cho phép các phát hiện từ code, tác vụ hoặc kế hoạch chảy ngược lên, rồi đối soát
  toàn bộ bộ artifact.

Trang [Các mô hình lưu giữ đặc tả](../concepts/spec-persistence.md) so sánh
các lựa chọn này. [Hướng dẫn phát triển đặc tả](evolving-specs.md) mô tả
vòng duy trì cho từng mô hình.

<a id="existing-project-examples"></a>

## Ví dụ với dự án có sẵn

[Các walkthrough của cộng đồng](../../community/walkthroughs.md) có các ví dụ brownfield
với codebase .NET, Java và Go/React. Các extension cộng đồng dùng để
khám phá kiến trúc và khởi động dự án brownfield được liệt kê trong
[catalog extension](../../community/extensions.md).
