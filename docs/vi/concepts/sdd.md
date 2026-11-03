<a id="what-is-spec-driven-development"></a>

# Phát triển hướng đặc tả là gì?

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../concepts/sdd.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Phát triển hướng đặc tả (Spec-Driven Development) **đảo ngược cách làm** của phát triển phần mềm truyền thống. Suốt nhiều thập kỷ, code là trung tâm — đặc tả chỉ là giàn giáo dựng lên rồi bỏ đi khi "phần việc thật sự" là viết code bắt đầu. Phát triển hướng đặc tả thay đổi điều đó: **đặc tả trở nên thực thi được**, trực tiếp sinh ra phần triển khai chạy được thay vì chỉ dẫn đường cho nó.

<a id="core-philosophy"></a>

## Triết lý cốt lõi

Phát triển hướng đặc tả là một quy trình có cấu trúc, nhấn mạnh vào:

- **Phát triển theo ý định**, trong đó đặc tả xác định "*cái gì*" trước "*làm thế nào*"
- **Tạo đặc tả chi tiết** với các rào chắn (guardrail) và nguyên tắc của tổ chức
- **Tinh chỉnh qua nhiều bước** thay vì sinh code một lần duy nhất từ prompt
- **Dựa nhiều** vào năng lực của các mô hình AI tiên tiến trong việc diễn giải đặc tả

Spec Kit không quy định cách nhóm giữ nguyên hay thay đổi `spec.md`, `plan.md`
và `tasks.md` sau khi yêu cầu thay đổi. Xem
[Các mô hình lưu giữ đặc tả](spec-persistence.md) để hiểu các khái niệm và
[Phát triển đặc tả trong dự án có sẵn](../guides/evolving-specs.md) để biết
các quy trình cập nhật đặc tả cho dự án có sẵn.

Khi các thành phần cung cấp giao diện cho bên sử dụng bên ngoài, hãy dùng
[Phát triển hướng contract](../guides/contract-driven-development.md) để
thống nhất các nghĩa vụ quan sát được của chúng trước khi triển khai từng phía. Điều này
áp dụng bất kể kiến trúc hay cách tổ chức repository.

<a id="development-phases"></a>

## Các giai đoạn phát triển

| Giai đoạn | Trọng tâm | Hoạt động chính |
|-------|-------|----------------|
| **Phát triển từ 0 đến 1** ("Greenfield") | Sinh từ đầu | <ul><li>Bắt đầu với các yêu cầu tổng quát</li><li>Sinh đặc tả</li><li>Lập kế hoạch các bước triển khai</li><li>Xây dựng ứng dụng sẵn sàng cho production</li></ul> |
| **Khám phá sáng tạo** | Nhiều phần triển khai song song | <ul><li>Khám phá các giải pháp đa dạng</li><li>Hỗ trợ nhiều tech stack và kiến trúc</li><li>Thử nghiệm các mẫu UX</li></ul> |
| **Cải tiến lặp** ("Brownfield") | Hiện đại hóa hệ thống có sẵn | <ul><li>Bổ sung tính năng theo từng vòng lặp</li><li>Hiện đại hóa hệ thống cũ</li><li>Điều chỉnh quy trình</li></ul> |

<a id="experimental-goals"></a>

## Mục tiêu thử nghiệm

Hoạt động nghiên cứu và thử nghiệm của chúng tôi tập trung vào:

<a id="technology-independence"></a>

### Độc lập công nghệ

- Tạo ứng dụng bằng nhiều tech stack khác nhau
- Kiểm chứng giả thuyết rằng Phát triển hướng đặc tả là một quy trình không gắn với công nghệ, ngôn ngữ lập trình hay framework cụ thể nào

<a id="enterprise-constraints"></a>

### Ràng buộc doanh nghiệp

- Chứng minh khả năng phát triển ứng dụng trọng yếu
- Đưa vào các ràng buộc của tổ chức (nhà cung cấp cloud, tech stack, quy chuẩn kỹ thuật)
- Hỗ trợ design system và các yêu cầu tuân thủ của doanh nghiệp

<a id="user-centric-development"></a>

### Phát triển lấy người dùng làm trung tâm

- Xây dựng ứng dụng cho các nhóm người dùng và sở thích khác nhau
- Hỗ trợ nhiều cách phát triển (từ vibe-coding đến phát triển AI-native)

<a id="creative--iterative-processes"></a>

### Quy trình sáng tạo và lặp

- Kiểm chứng ý tưởng khám phá nhiều phần triển khai song song
- Cung cấp quy trình phát triển tính năng theo vòng lặp vững chắc
- Mở rộng quy trình để xử lý các tác vụ nâng cấp và hiện đại hóa
