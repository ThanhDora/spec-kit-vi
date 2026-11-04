<a id="community-bundles"></a>

# Bundle cộng đồng

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../community/bundles.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

> [!NOTE]
> Bundle cộng đồng được tạo và duy trì độc lập bởi tác giả của chúng. Maintainer chỉ xác minh metadata của bài gửi đầy đủ và đúng định dạng — họ **không review, kiểm định, bảo chứng hay hỗ trợ code của bundle hoặc các thành phần mà nó cài**. Hãy review manifest của bundle, catalog thành phần và repository nguồn trước khi cài, và tự cân nhắc khi sử dụng.

Bundle kết hợp các thành phần Spec Kit hiện có — extension, preset, workflow và step — thành một chồng duy nhất cho một vai trò hoặc nhóm. Chúng hữu ích khi người dùng cần cài cùng lúc một tập thành phần đã được kiểm thử thay vì chạy nhiều lệnh cài riêng lẻ.

Các mục bundle cộng đồng được chấp nhận được công bố trong [`bundles/catalog.community.json`](https://github.com/github/spec-kit/blob/main/bundles/catalog.community.json) và được liệt kê bên dưới. Nguồn cộng đồng có sẵn ở chế độ chỉ tìm kiếm: `specify bundle search` và `specify bundle info` có thể xem các mục, nhưng cài theo ID yêu cầu thêm tường minh một catalog cho phép cài. Catalog chỉ định tường minh có độ ưu tiên mặc định cao hơn nguồn cộng đồng có sẵn. Để gửi bundle đi review, hãy tạo issue [Bundle Submission](https://github.com/github/spec-kit/issues/new?template=bundle_submission.yml).

| Bundle | Mục đích | Vai trò hoặc nhóm | Cung cấp | Catalog cần thiết | URL |
|--------|---------|--------------|----------|-------------------|-----|
| Agentstandards Multi-Vendor Architecture | Cài một hội đồng kiến trúc đa nhà cung cấp do Codex điều phối, cổng kiểm soát task cứng của nó, và workflow Spec Kit hỗ trợ. | `architecture-governance` | 1 extension, 1 preset, 1 workflow | Có tài liệu | [agentstandards](https://github.com/bbjwz/agentstandards) |
| SicarioSpec Security & Governance Bundle | Bundle quản trị an toàn theo mặc định cho GitHub Spec Kit. Bắt buộc phân loại dữ liệu, mô hình hóa mối đe dọa và các cổng xác minh do code sở hữu. | `security-engineer` | 1 extension, 11 presets | Có tài liệu | [sicario-spec](https://github.com/dfirs1car1o/sicario-spec) |
| SpecAssay | Nâng cấp Durable-ID cho Spec Kit nguyên bản: template, từ chối tại Gate 2 và xuất trace-manifest. | `developer` | 1 extension, 1 preset | Có tài liệu | [specassay](https://github.com/rdryfoos/specassay) |

<a id="what-to-submit"></a>

## Cần gửi những gì

Một bài gửi bundle nên gồm:

- Repository công khai có manifest `bundle.yml` hợp lệ.
- Bản phát hành GitHub có phiên bản với artifact bundle được tạo bằng `specify bundle build`.
- Tài liệu giải thích vai trò dự kiến, các thành phần được cài, catalog cần thiết và workflow mong đợi.
- Mục catalog đề xuất với metadata của bundle và số lượng thành phần.
- Bằng chứng kiểm thử từ một dự án Spec Kit sạch.

<a id="component-resolution"></a>

## Phân giải thành phần

Mục catalog của bundle mô tả nơi tải artifact bundle, nhưng các tham chiếu thành phần của bundle vẫn cần phân giải được khi người dùng cài nó. Tham chiếu có thể phân giải từ thành phần đóng gói kèm, thành phần đã cài, hoặc các catalog extension, preset, workflow và step đang hoạt động.

Nếu bundle của bạn phụ thuộc vào thành phần không có trong catalog mặc định của Spec Kit, hãy đưa URL các catalog cần thiết vào bài gửi và README. Kiểm thử toàn bộ quy trình cài từ một dự án sạch đã thêm các catalog đó trước khi gửi.

Ví dụ:

```bash
specify preset catalog add https://example.com/presets.json --name example-bundle --install-allowed
specify extension catalog add https://example.com/extensions.json --name example-bundle --install-allowed
curl -L -o example-bundle-1.0.0.zip https://example.com/example-bundle-1.0.0.zip
specify bundle install ./example-bundle-1.0.0.zip

# Or install by id from an install-allowed bundle catalog.
specify bundle catalog add https://example.com/bundles.json --id example-bundle-catalog --policy install-allowed
specify bundle install example-bundle
```

<a id="review-scope"></a>

## Phạm vi review

Maintainer kiểm tra rằng:

- Các trường của bài gửi đầy đủ và đúng định dạng.
- URL của artifact phát hành và tài liệu truy cập được.
- Repository chứa manifest `bundle.yml`.
- Bài gửi nêu rõ mọi catalog thành phần cần thiết.
- Mục catalog đề xuất dùng đúng cấu trúc mục catalog bundle mong đợi.

Maintainer không kiểm định hành vi của extension, preset, workflow, step hay script được cài. Người dùng nên review các thành phần đó trước khi cài một bundle cộng đồng.

<a id="updating-a-bundle"></a>

## Cập nhật bundle

Để cập nhật một bundle đã gửi, hãy tạo một issue [Bundle Submission](https://github.com/github/spec-kit/issues/new?template=bundle_submission.yml) khác với phiên bản mới, URL tải về, danh sách thành phần đã thay đổi và bằng chứng kiểm thử cập nhật. Ghi rõ issue này cập nhật một mục bundle hiện có.
