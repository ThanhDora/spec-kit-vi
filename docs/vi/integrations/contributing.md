<a id="contributing-integrations"></a>

# Đóng góp integration

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/contributing.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hướng dẫn này bao gồm integration có sẵn, phát triển adapter bên ngoài và việc gửi mục vào catalog cộng đồng.

Hãy bắt đầu từ [thiết kế integration cho agent](https://github.com/github/spec-kit/blob/main/design/integration.md) để nắm các hợp đồng triển khai, quyền sở hữu và yêu cầu bàn giao.

<a id="adding-a-built-in-integration"></a>

## Thêm integration có sẵn

Integration có sẵn do nhóm lõi Spec Kit duy trì và đi kèm CLI.

Để thiết lập bản checkout, xem [phát triển cục bộ](../local-development.md). Làm theo [hướng dẫn kiểm thử cho người đóng góp](https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md#testing-deterministic-behavior) và [quy trình kiểm tra](https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md#recommended-validation-flow), rồi đến [yêu cầu đối với PR integration](https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md#integration-pull-requests).

<a id="checklist"></a>

### Danh sách kiểm tra

1. **Tạo subpackage cho integration** trong `src/specify_cli/integrations/<package_dir>/`, dùng khóa integration với dấu gạch ngang thay bằng dấu gạch dưới cho `<package_dir>`.
2. **Triển khai lớp integration** theo [Thêm một agent](https://github.com/github/spec-kit/blob/main/design/integration.md#adding-an-agent).
3. **Đăng ký integration** trong `src/specify_cli/integrations/__init__.py`.
4. **Thêm test** trong `tests/integrations/test_integration_<package_dir>.py`.
5. **Thêm mục catalog** trong `integrations/catalog.json`.
6. **Cập nhật tài liệu:** thêm `docs/integrations/<key>.md` và liên kết nó từ [trang mục lục integration](index.md) và [thanh điều hướng](../../toc.yml). Cập nhật [tài liệu tham khảo catalog](catalog.md) nếu cần, và [thiết kế integration](https://github.com/github/spec-kit/blob/main/design/integration.md) nếu hợp đồng thay đổi.

Dùng [schema của catalog](catalog.md#catalog-schema) cho định dạng mục có sẵn.

<a id="developing-an-external-adapter"></a>

## Phát triển adapter bên ngoài

Triển khai và đóng gói adapter theo [hợp đồng adapter bên ngoài](https://github.com/github/spec-kit/blob/main/design/integration.md#external-adapter-package-contract). [Tài liệu tham khảo file mô tả](catalog.md#integration-descriptor-integrationyml) mô tả metadata của package; [schema của catalog](catalog.md#catalog-schema) mô tả các mục được công bố.

Về cài đặt cục bộ và quyết định tin cậy, làm theo [adapter bên ngoài cài từ catalog](cli.md#catalog-installed-external-adapters). Xem [nâng cấp một integration](cli.md#upgrade-an-integration) để biết hành vi cập nhật.

<a id="validate-your-adapter"></a>

### Kiểm tra adapter của bạn

Kiểm thử package qua đường dẫn công khai: đăng ký một catalog thử nghiệm loopback cục bộ, cài adapter trung lập của nó, khởi động một tiến trình CLI mới, đăng ký đóng góp extension/preset, và chạy thử điều phối workflow command/prompt với một tiến trình giả vô hại.

Bao quát [hợp đồng vòng đời](https://github.com/github/spec-kit/blob/main/design/integration.md#storage-loading-and-lifecycle), bao gồm:

- Metadata/lớp không hợp lệ, từ chối tin cậy, archive không an toàn, lỗi thiết lập, và lỗi khi upgrade/uninstall.
- Code package tách khỏi manifest của file được sinh ra; rollback và dọn dẹp mà vẫn giữ file đã sửa, file không liên quan của người dùng, tiến độ workflow độc lập và các chỉnh sửa đồng thời.
- Lệnh chỉ đọc metadata không có tác dụng phụ khi import; khôi phục cưỡng bức package bị hỏng nhờ bằng chứng quyền sở hữu cục bộ, và cảnh báo cần dọn dẹp thủ công khi thiếu bằng chứng đó.
- Đích ghi là symlink, thư mục gốc được dành riêng, đường dẫn kiểu cũ không an toàn, và chồng lấn không phân biệt hoa thường giữa đường dẫn đầu ra chính và kiểu cũ.
- Điều phối dự án chồng chéo và import tương đối lười vẫn giữ đúng adapter mà không tuần tự hóa các tiến trình agent độc lập.
- Với adapter hỗ trợ event, việc thêm/gỡ và bật/tắt extension chỉ có event trong các tiến trình CLI mới, kể cả báo lỗi rõ ràng khi không nạp được code đã cài.

<a id="submitting-to-the-community-catalog"></a>

## Gửi vào catalog cộng đồng

Nhà phát triển bên ngoài có thể liệt kê integration trong `integrations/catalog.community.json` để người khác tìm thấy. Maintainer catalog review metadata của mục được liệt kê, không review phần triển khai adapter; người dùng phải tự thẩm định code. Việc được liệt kê không đồng nghĩa với quyền cài đặt.

<a id="prerequisites"></a>

### Điều kiện tiên quyết

1. **Adapter bên ngoài hoạt động được** — đã đóng gói và kiểm tra như mô tả ở trên.
2. **Repository công khai** — lưu trữ trên GitHub hoặc nền tảng tương tự.
3. **Tài liệu** — README có hướng dẫn sử dụng.
4. **Giấy phép** — file giấy phép mã nguồn mở.

Chuẩn bị mục của bạn theo [schema của catalog](catalog.md#catalog-schema). Metadata phải khớp với file mô tả trong package. Công bố một URL archive đã ghim; nên kèm digest SHA-256 của archive.

<a id="submission"></a>

### Gửi bài

1. **Fork** [repository spec-kit](https://github.com/github/spec-kit)
2. **Thêm mục của bạn** dưới khóa `integrations` trong `integrations/catalog.community.json`:

   ```json
   {
     "schema_version": "1.0",
     "integrations": {
       "sample-agent": {
         "id": "sample-agent",
         "name": "Sample Agent",
         "version": "1.0.0",
         "description": "Adapter for Sample Agent",
         "author": "your-name",
         "repository": "https://github.com/your-name/speckit-sample-agent",
         "download_url": "https://github.com/your-name/speckit-sample-agent/releases/download/v1.0.0/sample-agent.zip",
         "tags": ["cli"]
       }
     }
   }
   ```

3. **Mở pull request** kèm:
   - Mục catalog của bạn
   - Liên kết tới repository integration của bạn
   - Xác nhận rằng `integration.yml` hợp lệ

<a id="version-updates"></a>

### Cập nhật phiên bản

Để cập nhật phiên bản integration trong catalog:

1. Phát hành phiên bản mới cho integration của bạn
2. Mở PR cập nhật phiên bản, URL archive đã ghim và digest (nếu có)
3. Bảo đảm tương thích ngược hoặc ghi rõ các thay đổi phá vỡ tương thích
