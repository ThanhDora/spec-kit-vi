<a id="extension-publishing-guide"></a>

# Hướng dẫn phát hành extension

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../extensions/publishing.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hướng dẫn này giải thích cách phát hành extension của bạn lên catalog extension của Spec Kit để `specify extension search` có thể tìm thấy nó.

<a id="table-of-contents"></a>

## Mục lục

1. [Điều kiện tiên quyết](#prerequisites)
2. [Chuẩn bị extension](#prepare-your-extension)
3. [Gửi vào catalog](#submit-to-catalog)
4. [Quy trình phát hành](#release-workflow)
5. [Thực hành tốt](#best-practices)

---

<a id="prerequisites"></a>

## Điều kiện tiên quyết

Trước khi phát hành extension, hãy bảo đảm bạn có:

1. **Extension hợp lệ**: Một extension hoạt động được với manifest `extension.yml` hợp lệ
2. **Repository Git**: Extension được lưu trữ trên GitHub (hoặc dịch vụ lưu trữ git công khai khác)
3. **Tài liệu**: README.md có hướng dẫn cài đặt và sử dụng
4. **Giấy phép**: File giấy phép mã nguồn mở (MIT, Apache 2.0, v.v.)
5. **Quản lý phiên bản**: Semantic versioning (ví dụ 1.0.0)
6. **Kiểm thử**: Extension đã được kiểm thử trên dự án thực tế

---

<a id="prepare-your-extension"></a>

## Chuẩn bị extension

<a id="1-extension-structure"></a>

### 1. Cấu trúc extension

Bảo đảm extension của bạn theo cấu trúc chuẩn:

```text
your-extension/
├── extension.yml              # Required: Extension manifest
├── README.md                  # Required: Documentation
├── LICENSE                    # Required: License file
├── CHANGELOG.md               # Recommended: Version history
├── .gitignore                 # Recommended: Git ignore rules
│
├── commands/                  # Extension commands
│   ├── command1.md
│   └── command2.md
│
├── config-template.yml        # Config template (if needed)
│
└── docs/                      # Additional documentation
    ├── usage.md
    └── examples/
```

<a id="2-extensionyml-validation"></a>

### 2. Kiểm tra hợp lệ extension.yml

Xác minh manifest của bạn hợp lệ:

```yaml
schema_version: "1.0"

extension:
  id: "your-extension"           # Unique lowercase-hyphenated ID
  name: "Your Extension Name"     # Human-readable name
  version: "1.0.0"                # Semantic version
  description: "Brief description (one sentence)"
  author: "Your Name or Organization"
  repository: "https://github.com/your-org/spec-kit-your-extension"
  license: "MIT"
  homepage: "https://github.com/your-org/spec-kit-your-extension"

requires:
  speckit_version: ">=0.1.0"    # Required spec-kit version

provides:
  commands:                       # List all commands
    - name: "speckit.your-extension.command"
      file: "commands/command.md"
      description: "Command description"

tags:                             # 2-5 relevant tags
  - "category"
  - "tool-name"
```

**Danh sách kiểm tra hợp lệ**:

- ✅ `id` chỉ gồm chữ thường và gạch nối (không có gạch dưới, dấu cách hay ký tự đặc biệt)
- ✅ `version` theo semantic versioning (X.Y.Z)
- ✅ `description` ngắn gọn (dưới 100 ký tự)
- ✅ URL `repository` hợp lệ và công khai
- ✅ Mọi file lệnh đều tồn tại trong thư mục extension
- ✅ Tag viết thường và có tính mô tả

<a id="3-create-github-release"></a>

### 3. Tạo GitHub release

Tạo GitHub release cho phiên bản extension của bạn:

```bash
# Tag the release
git tag v1.0.0
git push origin v1.0.0

# Create release on GitHub
# Go to: https://github.com/your-org/spec-kit-your-extension/releases/new
# - Tag: v1.0.0
# - Title: v1.0.0 - Release Name
# - Description: Changelog/release notes
```

URL archive của bản phát hành sẽ là:

```text
https://github.com/your-org/spec-kit-your-extension/archive/refs/tags/v1.0.0.zip
```

<a id="4-test-installation"></a>

### 4. Kiểm thử cài đặt

Kiểm tra người dùng có thể cài từ bản phát hành của bạn:

```bash
# Test dev installation
specify extension add --dev /path/to/your-extension

# Test from GitHub archive
specify extension add <extension-name> --from https://github.com/your-org/spec-kit-your-extension/archive/refs/tags/v1.0.0.zip
```

---

<a id="submit-to-catalog"></a>

## Gửi vào catalog

<a id="understanding-the-catalogs"></a>

### Hiểu về các catalog

Spec Kit dùng hệ thống hai catalog. Để biết chi tiết cách catalog hoạt động, xem [README Extensions](https://github.com/github/spec-kit/blob/main/extensions/README.md#extension-catalogs) chính.

**Với việc phát hành extension**: Mọi extension cộng đồng được liệt kê trong `extensions/catalog.community.json`. Người dùng duyệt catalog này và sao chép những extension họ tin cậy vào `catalog.json` của mình.

<a id="how-to-submit"></a>

### Cách gửi

Để gửi extension vào catalog cộng đồng, hãy tạo issue mới theo template **[Extension Submission](https://github.com/github/spec-kit/issues/new?template=extension_submission.yml)**. Template thu thập mọi metadata bắt buộc, bao gồm:

- ID, tên và phiên bản extension
- Mô tả, tác giả và giấy phép
- Liên kết repository, URL tải về và tài liệu
- Phiên bản Spec Kit yêu cầu và các phụ thuộc công cụ (nếu có)
- Số lượng lệnh và hook
- Tag và tính năng chính
- Xác nhận đã kiểm thử

> [!IMPORTANT]
> **Không** mở pull request trực tiếp để sửa `extensions/catalog.community.json`. Mọi bài gửi extension cộng đồng phải đi qua template issue. Bài gửi không dùng template issue sẽ bị đóng, và bạn sẽ được yêu cầu gửi lại bằng template.

<a id="what-happens-after-you-submit"></a>

### Điều gì xảy ra sau khi bạn gửi

1. GitHub gắn kết luận `triage-must-have` khi issue được mở qua form Extension Submission. Tự động hóa tiếp nhận này chỉ dành cho bài gửi extension và không thay đổi tiêu chí triage thủ công đối với các issue khác.
2. Người duy trì review issue trong quá trình triage và gắn nhãn riêng `extension-submission`, nhãn này khởi động việc kiểm tra catalog tự động. Trên repository công khai này, người đóng góp không thể tự gắn nhãn đó, nên không cần gắn nhãn hay yêu cầu lại — issue chỉ đơn giản chờ trong hàng triage.
3. Workflow tự động kiểm tra bài gửi và, khi kiểm tra đạt, cập nhật `extensions/catalog.community.json` và `docs/community/extensions.md` trong một draft pull request
4. Người duy trì review pull request được sinh ra và merge khi chấp thuận
5. Extension của bạn có thể được tìm thấy qua `specify extension search`

<a id="what-maintainers-check"></a>

### Người duy trì kiểm tra những gì

- Các trường của mục catalog đầy đủ và đúng định dạng
- URL tải về truy cập được
- Repository tồn tại và có manifest `extension.yml`

> [!NOTE]
> Người duy trì **không** review, kiểm định hay kiểm thử bản thân code của extension.

<a id="typical-review-timeline"></a>

### Thời gian review thông thường

- **Review**: 3-7 ngày làm việc

<a id="updating-an-existing-extension"></a>

### Cập nhật extension hiện có

Để cập nhật một extension đã có trong catalog (ví dụ cho phiên bản mới), hãy tạo issue **[Extension Submission](https://github.com/github/spec-kit/issues/new?template=extension_submission.yml)** mới với phiên bản, URL tải về đã cập nhật và mọi trường khác đã thay đổi. Ghi rõ trong issue rằng đây là bản cập nhật cho một mục đã có.

---

<a id="release-workflow"></a>

## Quy trình phát hành

<a id="publishing-new-versions"></a>

### Phát hành phiên bản mới

Khi phát hành phiên bản mới:

1. **Cập nhật phiên bản** trong `extension.yml`:

   ```yaml
   extension:
     version: "1.1.0"  # Updated version
   ```

2. **Cập nhật CHANGELOG.md**:

   ```markdown
   ## [1.1.0] - 2026-02-15

   ### Added
   - New feature X

   ### Fixed
   - Bug fix Y
   ```

3. **Tạo GitHub release**:

   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   # Create release on GitHub
   ```

4. **Gửi bản cập nhật** bằng template [Extension Submission](https://github.com/github/spec-kit/issues/new?template=extension_submission.yml) với phiên bản và URL tải về mới. Ghi rõ trong issue rằng đây là bản cập nhật cho một mục đã có.

---

<a id="best-practices"></a>

## Thực hành tốt

<a id="extension-design"></a>

### Thiết kế extension

1. **Đơn nhiệm**: Mỗi extension nên tập trung vào một công cụ/integration
2. **Đặt tên rõ ràng**: Dùng tên mô tả rõ, không mơ hồ
3. **Tối thiểu phụ thuộc**: Tránh các phụ thuộc không cần thiết
4. **Tương thích ngược**: Tuân thủ nghiêm ngặt semantic versioning

<a id="documentation"></a>

### Tài liệu

1. **Cấu trúc README.md**:
   - Tổng quan và tính năng
   - Hướng dẫn cài đặt
   - Hướng dẫn cấu hình
   - Ví dụ sử dụng
   - Xử lý sự cố
   - Hướng dẫn đóng góp

2. **Tài liệu lệnh**:
   - Mô tả rõ ràng
   - Liệt kê điều kiện tiên quyết
   - Hướng dẫn từng bước
   - Hướng dẫn xử lý lỗi
   - Ví dụ

3. **Cấu hình**:
   - Cung cấp file template
   - Ghi lại mọi tùy chọn
   - Kèm ví dụ
   - Giải thích giá trị mặc định

<a id="security"></a>

### Bảo mật

1. **Kiểm tra đầu vào**: Kiểm tra mọi đầu vào của người dùng
2. **Không viết cứng bí mật**: Không bao giờ đưa thông tin xác thực vào
3. **Phụ thuộc an toàn**: Chỉ dùng phụ thuộc đáng tin cậy
4. **Kiểm định định kỳ**: Kiểm tra lỗ hổng

<a id="maintenance"></a>

### Bảo trì

1. **Phản hồi issue**: Xử lý issue trong vòng 1-2 tuần
2. **Cập nhật thường xuyên**: Giữ các phụ thuộc luôn được cập nhật
3. **Changelog**: Duy trì changelog chi tiết
4. **Ngừng hỗ trợ**: Thông báo trước về các thay đổi phá vỡ tương thích

<a id="community"></a>

### Cộng đồng

1. **Giấy phép**: Dùng giấy phép mã nguồn mở dễ dãi (MIT, Apache 2.0)
2. **Đóng góp**: Hoan nghênh đóng góp
3. **Quy tắc ứng xử**: Tôn trọng và hòa nhập
4. **Hỗ trợ**: Cung cấp cách để nhận trợ giúp (issue, thảo luận, email)

---

<a id="faq"></a>

## Câu hỏi thường gặp

<a id="q-can-i-publish-privateproprietary-extensions"></a>

### H: Tôi có thể phát hành extension riêng tư/độc quyền không?

Đ: Catalog chính chỉ dành cho extension công khai. Với extension riêng tư:

- Tự lưu trữ file catalog.json của riêng bạn
- Trong một dự án Spec Kit, người dùng thêm catalog của bạn: `specify extension catalog add https://your-domain.com/catalog.json --name private-catalog`

<a id="q-how-long-does-review-take"></a>

### H: Review mất bao lâu?

Đ: Thường là 3-7 ngày làm việc. Cập nhật cho extension hiện có thường nhanh hơn.

<a id="q-what-if-my-extension-is-rejected"></a>

### H: Nếu extension của tôi bị từ chối thì sao?

Đ: Bạn sẽ nhận được phản hồi về những gì cần sửa. Hãy sửa rồi gửi lại.

<a id="q-can-i-update-my-extension-anytime"></a>

### H: Tôi có thể cập nhật extension bất cứ lúc nào không?

Đ: Có, hãy tạo issue [Extension Submission](https://github.com/github/spec-kit/issues/new?template=extension_submission.yml) mới với phiên bản và URL tải về đã cập nhật. Ghi rõ rằng đây là bản cập nhật cho một mục đã có.

<a id="q-do-i-need-to-be-verified-to-be-in-the-catalog"></a>

### H: Tôi có cần được xác minh mới có mặt trong catalog không?

Đ: Không. Mọi extension cộng đồng đều được liệt kê trong catalog khi bài gửi của chúng được review và chấp nhận.

<a id="q-can-extensions-have-paid-features"></a>

### H: Extension có thể có tính năng trả phí không?

Đ: Extension nên miễn phí và mã nguồn mở. Được phép có hỗ trợ/dịch vụ thương mại, nhưng chức năng lõi phải miễn phí.

---

<a id="support"></a>

## Hỗ trợ

- **Vấn đề về catalog**: <https://github.com/statsperform/spec-kit/issues>
- **Template extension**: <https://github.com/statsperform/spec-kit-extension-template> (sắp ra mắt)
- **Hướng dẫn phát triển**: Xem [Phát triển extension](developing.md)
- **Cộng đồng**: Thảo luận và hỏi đáp

---

<a id="appendix-catalog-schema"></a>

## Phụ lục: Schema của catalog

<a id="complete-catalog-entry-schema"></a>

### Schema đầy đủ của mục catalog

```json
{
  "name": "string (required)",
  "id": "string (required, unique)",
  "description": "string (required, <200 chars)",
  "author": "string (required)",
  "version": "string (required, semver)",
  "download_url": "string (required, valid URL)",
  "sha256": "string (optional, SHA-256 hex digest of the archive at download_url; verified before install)",
  "repository": "string (required, valid URL)",
  "homepage": "string (optional, valid URL)",
  "documentation": "string (optional, valid URL)",
  "changelog": "string (optional, valid URL)",
  "license": "string (required)",
  "requires": {
    "speckit_version": "string (required, version specifier)",
    "tools": [
      {
        "name": "string (required)",
        "version": "string (optional, version specifier)",
        "required": "boolean (default: false)"
      }
    ]
  },
  "provides": {
    "commands": "integer (optional)",
    "hooks": "integer (optional)"
  },
  "tags": ["array of strings (2-10 tags)"],
  "verified": "boolean (default: false, set by maintainers)",
  "downloads": "integer (auto-updated)",
  "stars": "integer (auto-updated)",
  "created_at": "string (ISO 8601 datetime)",
  "updated_at": "string (ISO 8601 datetime)"
}
```

<a id="valid-tags"></a>

### Tag hợp lệ

Các nhóm tag khuyến nghị:

- **Integration**: jira, linear, github, gitlab, azure-devops
- **Danh mục**: issue-tracking, vcs, ci-cd, documentation, testing
- **Nền tảng**: atlassian, microsoft, google
- **Tính năng**: automation, reporting, deployment, monitoring

Dùng 2-5 tag mô tả đúng nhất extension của bạn.

---

*Cập nhật lần cuối: 2026-01-28* *Phiên bản định dạng catalog: 1.0*
