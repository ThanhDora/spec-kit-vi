# Hiến chương [PROJECT_NAME]
<!-- Ví dụ: Hiến chương Spec, Hiến chương TaskFlow, v.v. -->

## Các nguyên tắc cốt lõi

### [PRINCIPLE_1_NAME]
<!-- Ví dụ: I. Thư viện trước -->
[PRINCIPLE_1_DESCRIPTION]
<!-- Ví dụ: Mọi tính năng bắt đầu dưới dạng một thư viện độc lập; Thư viện phải tự chứa, kiểm thử độc lập được và có tài liệu; Phải có mục đích rõ ràng, không tạo thư viện chỉ để sắp xếp tổ chức -->

### [PRINCIPLE_2_NAME]
<!-- Ví dụ: II. Giao diện CLI -->
[PRINCIPLE_2_DESCRIPTION]
<!-- Ví dụ: Mọi thư viện cung cấp chức năng qua CLI; Giao thức vào/ra bằng văn bản: stdin/args → stdout, lỗi → stderr; Hỗ trợ cả JSON lẫn định dạng dễ đọc cho người -->

### [PRINCIPLE_3_NAME]
<!-- Ví dụ: III. Test trước (KHÔNG THỂ THƯƠNG LƯỢNG) -->
[PRINCIPLE_3_DESCRIPTION]
<!-- Ví dụ: Bắt buộc TDD: Viết test → Người dùng phê duyệt → Test fail → Rồi mới triển khai; Tuân thủ nghiêm ngặt chu trình Red-Green-Refactor -->

### [PRINCIPLE_4_NAME]
<!-- Ví dụ: IV. Kiểm thử tích hợp -->
[PRINCIPLE_4_DESCRIPTION]
<!-- Ví dụ: Các phần cần kiểm thử tích hợp: Contract test cho thư viện mới, Thay đổi contract, Giao tiếp giữa các dịch vụ, Schema dùng chung -->

### [PRINCIPLE_5_NAME]
<!-- Ví dụ: V. Khả năng quan sát, VI. Quản lý phiên bản & Thay đổi phá vỡ tương thích, VII. Đơn giản -->
[PRINCIPLE_5_DESCRIPTION]
<!-- Ví dụ: Vào/ra bằng văn bản giúp dễ gỡ lỗi; Bắt buộc log có cấu trúc; Hoặc: Định dạng MAJOR.MINOR.BUILD; Hoặc: Bắt đầu đơn giản, nguyên tắc YAGNI -->

## [SECTION_2_NAME]
<!-- Ví dụ: Ràng buộc bổ sung, Yêu cầu bảo mật, Tiêu chuẩn hiệu năng, v.v. -->

[SECTION_2_CONTENT]
<!-- Ví dụ: Yêu cầu về tech stack, tiêu chuẩn tuân thủ, chính sách triển khai, v.v. -->

## [SECTION_3_NAME]
<!-- Ví dụ: Workflow phát triển, Quy trình review, Cổng kiểm soát chất lượng, v.v. -->

[SECTION_3_CONTENT]
<!-- Ví dụ: Yêu cầu code review, cổng kiểm thử, quy trình phê duyệt triển khai, v.v. -->

## Quản trị
<!-- Ví dụ: Hiến chương có hiệu lực cao hơn mọi thông lệ khác; Mọi sửa đổi cần có tài liệu, phê duyệt và kế hoạch chuyển đổi -->

[GOVERNANCE_RULES]
<!-- Ví dụ: Mọi PR/review phải kiểm tra việc tuân thủ; Mọi độ phức tạp phải có lý do; Dùng [GUIDANCE_FILE] làm hướng dẫn phát triển khi chạy -->

**Phiên bản**: [CONSTITUTION_VERSION] | **Ngày phê chuẩn**: [RATIFICATION_DATE] | **Sửa đổi lần cuối**: [LAST_AMENDED_DATE]
<!-- Ví dụ: Phiên bản: 2.1.1 | Ngày phê chuẩn: 2025-06-13 | Sửa đổi lần cuối: 2025-07-16 -->
