# Kế hoạch triển khai: [FEATURE]

**Branch**: `[###-feature-name]` | **Ngày**: [DATE] | **Đặc tả**: [link]

**Đầu vào**: Đặc tả tính năng tại `/specs/[###-feature-name]/spec.md`

**Lưu ý**: Template này được lệnh `__SPECKIT_COMMAND_PLAN__` điền nội dung; định nghĩa của lệnh mô tả workflow thực thi.

## Tóm tắt

[Trích từ đặc tả tính năng: yêu cầu chính + hướng tiếp cận kỹ thuật rút ra từ nghiên cứu]

## Bối cảnh kỹ thuật

<!--
  CẦN THỰC HIỆN: Thay nội dung trong mục này bằng các chi tiết kỹ thuật
  của dự án. Cấu trúc ở đây chỉ mang tính gợi ý để định hướng quá trình lặp.
-->

**Ngôn ngữ/Phiên bản**: [ví dụ: Python 3.11, Swift 5.9, Rust 1.75 hoặc NEEDS CLARIFICATION]

**Thư viện phụ thuộc chính**: [ví dụ: FastAPI, UIKit, LLVM hoặc NEEDS CLARIFICATION]

**Lưu trữ**: [nếu có, ví dụ: PostgreSQL, CoreData, file hoặc N/A]

**Kiểm thử**: [ví dụ: pytest, XCTest, cargo test hoặc NEEDS CLARIFICATION]

**Nền tảng đích**: [ví dụ: máy chủ Linux, iOS 15+, WASM hoặc NEEDS CLARIFICATION]

**Loại dự án**: [ví dụ: library/cli/web-service/mobile-app/compiler/desktop-app hoặc NEEDS CLARIFICATION]

**Mục tiêu hiệu năng**: [theo lĩnh vực, ví dụ: 1000 req/s, 10k dòng/giây, 60 fps hoặc NEEDS CLARIFICATION]

**Ràng buộc**: [theo lĩnh vực, ví dụ: <200ms p95, <100MB bộ nhớ, chạy được offline hoặc NEEDS CLARIFICATION]

**Quy mô/Phạm vi**: [theo lĩnh vực, ví dụ: 10k người dùng, 1M dòng code, 50 màn hình hoặc NEEDS CLARIFICATION]

## Kiểm tra hiến chương

*CỔNG KIỂM SOÁT: Phải đạt trước khi nghiên cứu ở Giai đoạn 0. Kiểm tra lại sau khi thiết kế ở Giai đoạn 1.*

[Các cổng kiểm soát được xác định dựa trên file hiến chương]

## Cấu trúc dự án

### Tài liệu (tính năng này)

```text
specs/[###-feature]/
├── plan.md              # File này (đầu ra của lệnh __SPECKIT_COMMAND_PLAN__)
├── research.md          # Đầu ra Giai đoạn 0 (lệnh __SPECKIT_COMMAND_PLAN__)
├── data-model.md        # Đầu ra Giai đoạn 1 (lệnh __SPECKIT_COMMAND_PLAN__)
├── quickstart.md        # Đầu ra Giai đoạn 1 (lệnh __SPECKIT_COMMAND_PLAN__)
├── contracts/           # Đầu ra Giai đoạn 1 (lệnh __SPECKIT_COMMAND_PLAN__)
└── tasks.md             # Đầu ra Giai đoạn 2 (lệnh __SPECKIT_COMMAND_TASKS__ - KHÔNG do __SPECKIT_COMMAND_PLAN__ tạo)
```

### Mã nguồn (thư mục gốc của repository)
<!--
  CẦN THỰC HIỆN: Thay cây thư mục placeholder bên dưới bằng bố cục cụ thể
  của tính năng này. Xóa các phương án không dùng và mở rộng cấu trúc đã chọn
  bằng đường dẫn thật (ví dụ: apps/admin, packages/something). Kế hoạch bàn giao
  không được chứa nhãn "Phương án".
-->

```text
# [REMOVE IF UNUSED] Phương án 1: Một project (MẶC ĐỊNH)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Phương án 2: Ứng dụng web (khi phát hiện "frontend" + "backend")
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Phương án 3: Mobile + API (khi phát hiện "iOS/Android")
api/
└── [giống phần backend ở trên]

ios/ or android/
└── [cấu trúc riêng theo nền tảng: module tính năng, luồng UI, test theo nền tảng]
```

**Quyết định cấu trúc**: [Ghi lại cấu trúc đã chọn và tham chiếu tới các thư mục
thật đã nêu ở trên]

## Theo dõi độ phức tạp

> **CHỈ điền khi phần Kiểm tra hiến chương có vi phạm cần giải trình**

| Vi phạm | Vì sao cần | Lý do loại bỏ phương án đơn giản hơn |
|---------|------------|--------------------------------------|
| [ví dụ: project thứ 4] | [nhu cầu hiện tại] | [vì sao 3 project là không đủ] |
| [ví dụ: Repository pattern] | [vấn đề cụ thể] | [vì sao truy cập DB trực tiếp là không đủ] |
