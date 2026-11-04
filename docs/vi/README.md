<a id="documentation"></a>

# Tài liệu

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../README.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Thư mục này chứa mã nguồn tài liệu của Spec Kit, được build bằng [DocFX](https://dotnet.github.io/docfx/).

<a id="building-locally"></a>

## Build cục bộ

Để build tài liệu trên máy:

1. Cài DocFX:

   ```bash
   dotnet tool install -g docfx
   ```

2. Build tài liệu:

   ```bash
   cd docs
   docfx docfx.json --serve
   ```

3. Mở trình duyệt tại `http://localhost:8080` để xem tài liệu.

<a id="structure"></a>

## Cấu trúc

- `docfx.json` - File cấu hình DocFX
- `index.md` - Trang chủ tài liệu
- `toc.yml` - Cấu hình mục lục
- `installation.md` - Hướng dẫn cài đặt
- `quickstart.md` - Hướng dẫn từng bước Phát triển hướng đặc tả
- `guides/agentic-sdlc.md` - Cách Spec Kit áp dụng các thực hành SDLC có agent và truyền thống cho chính nó
- `guides/bugfix.md` - Hướng dẫn từng bước sửa lỗi
- `guides/assessment.md` - Hướng dẫn từng bước đánh giá ý tưởng
- `guides/customization.md` - Chọn và kết hợp các thành phần tùy biến
- `reference/catalogs.md` - Tìm kiếm catalog, độ tin cậy, nguồn riêng tư và thứ tự ưu tiên
- `extensions/overview.md` - Hướng dẫn sử dụng extension
- `extensions/publishing.md` - Hướng dẫn phát hành extension và gửi vào catalog
- `integrations/index.md` - Danh mục integration và hướng dẫn thiết lập chung
- `integrations/cli.md` - Tài liệu tham khảo CLI quản lý integration dùng chung
- `integrations/<key>.md` - Thiết lập, cách gọi, tùy chọn và giới hạn riêng của từng agent
- `integrations/catalog.md` - Schema của catalog và metadata của adapter bên ngoài
- `integrations/contributing.md` - Hướng dẫn đóng góp integration và catalog
- `reference/agentic-*.md` - Tài liệu tham khảo chi tiết cho các lệnh quy trình
- `vi/` - Bản dịch tiếng Việt (có `toc.yml` riêng; thuật ngữ trong `vi/GLOSSARY.md`)
- `_site/` - Đầu ra tài liệu được sinh ra (git bỏ qua)

<a id="deployment"></a>

## Triển khai

Tài liệu được tự động build và triển khai lên GitHub Pages khi có thay đổi được push lên branch `main`. Workflow được định nghĩa trong `.github/workflows/docs.yml`.
