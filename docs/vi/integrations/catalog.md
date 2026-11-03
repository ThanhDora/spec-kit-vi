<a id="spec-kit-integration-catalog"></a>

# Catalog integration của Spec Kit

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/catalog.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Catalog integration cho phép tìm kiếm, quản lý phiên bản và phân phối integration cho agent AI của Spec Kit.

<a id="catalog-files"></a>

## Các file catalog

<a id="built-in-catalog-integrationscatalogjson"></a>

### Catalog có sẵn (`integrations/catalog.json`)

Chứa các integration đi kèm Spec Kit. Chúng do nhóm lõi duy trì và luôn cài được.

<a id="community-catalog-integrationscatalogcommunityjson"></a>

### Catalog cộng đồng (`integrations/catalog.community.json`)

Các integration do cộng đồng đóng góp. Nguồn cộng đồng mặc định chỉ dùng để tìm kiếm: việc liệt kê một adapter không phải là sự cho phép cài đặt, cũng không phải kiểm định code. Hãy review code bên ngoài trước khi dùng một catalog cho phép cài đặt.

<a id="catalog-configuration"></a>

## Cấu hình catalog

Lớp được cấu hình đầu tiên thay thế các lớp thấp hơn. Trong lớp đó, giá trị priority nhỏ hơn được ưu tiên:

1. **Biến môi trường** — `SPECKIT_INTEGRATION_CATALOG_URL` ghi đè mọi catalog bằng một URL duy nhất
2. **Cấu hình dự án** — `.specify/integration-catalogs.yml` trong thư mục gốc dự án
3. **Cấu hình người dùng** — `~/.specify/integration-catalogs.yml` trong thư mục home của người dùng
4. **Mặc định có sẵn** — `catalog.json` + `catalog.community.json`

Thêm catalog dự án đầu tiên sẽ thay thế các nguồn mặc định, trừ khi bạn liệt kê cả chúng trong file dự án. Xem [Catalog](../../reference/catalogs.md) để có hướng dẫn chung về tìm kiếm, độ tin cậy và nguồn riêng tư.

Ví dụ `integration-catalogs.yml`:

```yaml
catalogs:
  - url: "https://example.com/my-catalog.json"
    name: "my-catalog"
    priority: 1
    install_allowed: true
```

<a id="cli-commands"></a>

## Lệnh CLI

Duyệt bằng `specify integration list --catalog`, `search` và `info`. Xem tài liệu tham khảo CLI về [quản lý catalog](cli.md#catalog-management) và [cài adapter bên ngoài](cli.md#catalog-installed-external-adapters).

<a id="integration-descriptor-integrationyml"></a>

## File mô tả integration (`integration.yml`)

Mỗi package integration bên ngoài gồm một file mô tả `integration.yml` chỉ dành cho adapter và một `__init__.py` ở thư mục gốc export một lớp con của `IntegrationBase`. Không cần danh mục lệnh hay bản sao của template lõi:

```yaml
schema_version: "1.0"
integration:
  id: "sample-agent"
  name: "Sample Agent"
  version: "1.0.0"
  description: "Adapter for Sample Agent"
  license: "MIT"
requires:
  speckit_version: ">=1.1.2.dev0"
  tools:
    - name: "sample-agent"
      required: true
```

Các trường bắt buộc của file mô tả:

| Trường | Kiểm tra hợp lệ |
|-------|------------|
| `schema_version` | Phải là chuỗi `"1.0"` |
| `integration.id` | ID bên ngoài phải khớp `^[a-z0-9][a-z0-9-]*$`. Các tên `con`, `prn`, `aux`, `nul`, `com1` đến `com9`, và `lpt1` đến `lpt9` được dành riêng |
| `integration.name`, `integration.description` | Phải là chuỗi |
| `integration.version` | Phải là chuỗi phiên bản PEP 440 |
| `requires.speckit_version` | Bắt buộc, là chuỗi đặc tả phiên bản PEP 440 không rỗng |

`requires.tools` là tùy chọn; bỏ qua với adapter không cần file thực thi nào. Metadata `provides` kiểu cũ (tùy chọn) vẫn hợp lệ nhưng không cung cấp lệnh cho host. Xem [thiết kế integration](https://github.com/github/spec-kit/blob/main/design/integration.md#external-adapter-package-contract) để biết metadata của lớp, các phương thức lúc chạy, công cụ và yêu cầu lưu trữ.

<a id="catalog-schema"></a>

## Schema của catalog

Cả hai file catalog đều theo cùng một JSON schema:

```json
{
  "schema_version": "1.0",
  "updated_at": "2026-04-08T00:00:00Z",
  "catalog_url": "https://...",
  "integrations": {
    "sample-agent": {
      "id": "sample-agent",
      "name": "Sample Agent",
      "version": "1.0.0",
      "description": "Adapter for Sample Agent",
      "download_url": "https://example.com/sample-agent/1.0.0/sample-agent.zip",
      "tags": ["cli"]
    }
  }
}
```

<a id="top-level-fields"></a>

### Các trường cấp cao nhất

| Trường | Kiểu | Mô tả |
|-------|------|-------------|
| `schema_version` | string | Phải là `"1.0"` |
| `updated_at` | string | Timestamp ISO 8601 tùy chọn |
| `integrations` | object | Map từ ID integration → metadata |

<a id="integration-entry-fields"></a>

### Các trường của mục integration

| Trường | Kiểu | Bắt buộc | Mô tả |
|-------|------|----------|-------------|
| `id` | string | Không | ID tường minh tùy chọn; phải khớp với khóa của map |
| `name` | string | Có | Tên hiển thị dễ đọc |
| `version` | string | Có | Phiên bản PEP 440 (ví dụ `1.0.0`, `1.0.0a1`) |
| `description` | string | Có | Mô tả một dòng |
| `author` | string | Không | Tên tác giả hoặc tổ chức |
| `repository` | string | Không | URL repository mã nguồn |
| `license` | string | Không | Định danh giấy phép khớp với file mô tả |
| `tags` | array | Không | Tag để tìm kiếm (ví dụ `["cli", "ide"]`) |
| `download_url` | string | Cài từ bên ngoài | URL archive ZIP, tar.gz hoặc tgz đã ghim; HTTPS hoặc HTTP loopback |
| `sha256` | string | Không | SHA-256 của archive, gồm 64 ký tự thập lục phân |
| `requires` | object | Không | Phải khớp yêu cầu của file mô tả khi được cung cấp |
| `releases` | object | Không | [Metadata phiên bản lịch sử](cli.md#historical-integration-metadata); không phải các bản phát hành cài được |

Khóa của map và `id` được khai báo (nếu có) phải khớp với `integration.id`. Tên, phiên bản, mô tả và metadata tùy chọn về tác giả/repository/giấy phép phải khớp với file mô tả. Mục có sẵn không cần trường tải về vì phần triển khai của chúng đi kèm CLI.

<a id="installation-policy-and-storage"></a>

## Chính sách cài đặt và lưu trữ

Đăng ký catalog bằng `integration catalog add` sẽ tạo một nguồn dự án cho phép cài đặt. Đặt `install_allowed: false` trong cấu hình của nó để chỉ cho phép tìm kiếm. Không thể ghi đè chính sách này bằng `--trust-integration` hay `--force`. Mỗi lần cài/cập nhật từ bên ngoài đều hỏi xác nhận trước khi tải/import Python, trừ khi đã được cho phép trước một cách rõ ràng bằng `--trust-integration`. Tài nguyên GitHub cần xác thực dùng các provider xác thực sẵn có của Spec Kit.

Code đã cài được lưu trong `.specify/integrations/packages/<id>/` cùng thông tin nguồn gốc và hash trong `packages.json`; cả hai đều bị loại trừ bởi `.specify/.gitignore` được quản lý. Sự đồng ý cho thực thi được lưu riêng trong `~/.specify/integration-trust.json`, gắn với dự án, ID integration và digest của package đã xác minh. File được sinh ra có `<id>.manifest.json` riêng, theo dõi bằng hash.

Đừng sửa trực tiếp code package đã cài: hãy phát hành archive/phiên bản mới rồi nâng cấp. Xem tài liệu tham khảo CLI về [độ tin cậy và cấp lại quyền](cli.md#catalog-installed-external-adapters) và [nâng cấp và khôi phục](cli.md#upgrade-an-integration).

<a id="contributing"></a>

## Đóng góp

Xem [hướng dẫn đóng góp](contributing.md) để thêm integration có sẵn hoặc gửi mục catalog cho integration bên ngoài. Để thiết lập riêng cho từng agent, hãy bắt đầu từ [danh mục integration](index.md). Các lệnh dùng chung cho người dùng được mô tả trong [tài liệu tham khảo quản lý integration](cli.md).
