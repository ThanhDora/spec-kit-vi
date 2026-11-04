<a id="authentication"></a>

# Xác thực

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/authentication.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Specify CLI dùng **xác thực theo lựa chọn chủ động** cho các request HTTP tới nguồn catalog, tải extension và kiểm tra bản phát hành. Không có thông tin xác thực nào được gửi trừ khi bạn cấu hình rõ ràng.

<a id="configuration"></a>

## Cấu hình

Tạo `~/.specify/auth.json` để bật xác thực:

```json
{
  "providers": [
    {
      "hosts": ["github.com", "api.github.com", "raw.githubusercontent.com", "codeload.github.com"],
      "provider": "github",
      "auth": "bearer",
      "token_env": "GH_TOKEN"
    }
  ]
}
```

> **Bảo mật:** Giới hạn file chỉ cho chủ sở hữu truy cập:
>
> ```bash
> chmod 600 ~/.specify/auth.json
> ```

Không có file này, mọi request HTTP đều không xác thực.

<a id="fields"></a>

## Các trường

Mỗi mục trong mảng `providers` có các trường sau:

| Trường | Bắt buộc | Mô tả |
|---|---|---|
| `hosts` | Có | Mảng hostname mà mục này áp dụng. Hỗ trợ hostname chính xác, hoặc ký tự đại diện `*.` ở đầu chỉ cho subdomain (ví dụ `*.visualstudio.com`). `*.visualstudio.com` khớp `foo.visualstudio.com`, nhưng không khớp `visualstudio.com`. Các mẫu glob khác như `*github.com` hay `gith?b.com` không được hỗ trợ. |
| `provider` | Có | Khóa provider có sẵn: `github`, `azure-devops` hoặc `bitbucket`. |
| `auth` | Có | Cơ chế xác thực (xem bên dưới). |
| `token` | Không | Giá trị token (ghi trực tiếp). Nên dùng `token_env` khi có thể. |
| `token_env` | Không | Tên biến môi trường để đọc token. |
| `username` | Với `basic` | Phần tên người dùng của thông tin xác thực Basic — với API token của Bitbucket, đó là email tài khoản Atlassian. Không được chứa `:`. |

Với xác thực `azure-ad`, cần thêm các trường:

| Trường | Bắt buộc | Mô tả |
|---|---|---|
| `tenant_id` | Có | ID tenant Azure AD. |
| `client_id` | Có | Client ID của service principal. |
| `client_secret_env` | Có | Biến môi trường chứa client secret. |

Phải đặt `token` hoặc `token_env` cho các cơ chế `bearer`, `basic-pat` và `basic`.

<a id="providers-and-auth-schemes"></a>

## Provider và cơ chế xác thực

### GitHub (`github`)

| Cơ chế | Header | Dùng cho |
|---|---|---|
| `bearer` | `Authorization: Bearer <token>` | PAT, fine-grained PAT, OAuth token, token GitHub App |
| `github-cli` | `Authorization: Bearer <token>` | Thông tin xác thực lấy khi cần qua `gh auth token` |

**Ví dụ — PAT qua biến môi trường:**

```json
{
  "hosts": ["github.com", "api.github.com", "raw.githubusercontent.com", "codeload.github.com"],
  "provider": "github",
  "auth": "bearer",
  "token_env": "GH_TOKEN"
}
```

**Ví dụ — GitHub CLI:**

```json
{
  "providers": [
    {
      "hosts": [
        "github.com",
        "api.github.com",
        "raw.githubusercontent.com",
        "codeload.github.com"
      ],
      "provider": "github",
      "auth": "github-cli"
    }
  ]
}
```

Cài [GitHub CLI](https://cli.github.com/) và chạy `gh auth login` trước khi dùng chế độ này. Specify chạy lệnh cố định `gh auth token --hostname github.com` không qua shell, lưu kết quả trong bộ nhớ cho tiến trình hiện tại và không bao giờ ghi token ra đĩa. Khoảng trắng bao quanh bị cắt bỏ; token chứa ký tự ngoài ASCII, ký tự carriage return hoặc xuống dòng bên trong sẽ bị từ chối mà không đưa token vào thông báo lỗi. Lỗi khi lấy thông tin xác thực làm request bị ảnh hưởng thất bại mà không thử thông tin xác thực khác hay request không xác thực. Chúng dùng nhóm lỗi URL hiện có, nên bên gọi vẫn giữ cách xử lý lỗi thông thường (ví dụ cảnh báo và bỏ qua một catalog không khả dụng). Kiểm tra bản phát hành và nâng cấp giữ nguyên chẩn đoán xác thực thay vì báo mất kết nối mạng. Việc tải catalog bundle trực tuyến và kiểm tra tham chiếu coi lỗi xác thực là lỗi, không coi là trường hợp không khả dụng để quay về snapshot đóng gói sẵn hay tham chiếu chưa kiểm tra.

Chỉ với `github-cli`, **hostname đầu tiên trong `hosts`** được truyền cho `gh auth token --hostname`. Hãy đặt `github.com` hoặc hostname đăng nhập GitHub CLI của instance doanh nghiệp lên đầu. Nó phải là hostname chính xác, không phải ký tự đại diện. Mọi host được liệt kê vẫn là đích khớp request được phép nhận thông tin xác thực đó; các mục sau có thể dùng ký tự đại diện được hỗ trợ. Specify không suy ra hostname của thông tin xác thực từ tiền tố dịch vụ hay URL được yêu cầu. Cache trong bộ nhớ được đánh khóa theo hostname đầu tiên. Dùng các mục provider riêng cho những host cần thông tin xác thực khác nhau. Thứ tự host không ảnh hưởng tới các chế độ xác thực hiện có.

### GitHub Enterprise Server (GHES)

Để dùng catalog hoặc extension riêng tư lưu trên một instance GitHub Enterprise Server, hãy thêm một mục `github` liệt kê các host GHES của bạn. Cùng một mục xác thực cả việc tải JSON catalog **và** tải tài nguyên bản phát hành riêng tư — Specify nhận các host được liệt kê là GitHub Enterprise và phân giải việc tải bản phát hành qua GHES REST API (`/api/v3`).

```json
{
  "providers": [
    {
      "hosts": ["ghes.example.com", "raw.ghes.example.com", "codeload.ghes.example.com"],
      "provider": "github",
      "auth": "bearer",
      "token_env": "GH_ENTERPRISE_TOKEN"
    }
  ]
}
```

Liệt kê host web **trần** (ví dụ `ghes.example.com`) — URL tải bản phát hành nằm ở đó. Nếu instance của bạn dùng subdomain isolation, hãy liệt kê thêm các subdomain `raw.` và `codeload.` mà URL catalog/extension của bạn dùng. Ký tự đại diện `*.ghes.example.com` khớp subdomain nhưng **không** khớp host trần, nên luôn liệt kê rõ host trần.

Với `auth: "github-cli"`, liệt kê hostname đăng nhập GitHub CLI của instance doanh nghiệp trước, rồi đến các host request hoặc mẫu ký tự đại diện cần nhận cùng thông tin xác thực:

```json
{
  "hosts": [
    "ghes.example.com",
    "raw.ghes.example.com",
    "codeload.ghes.example.com"
  ],
  "provider": "github",
  "auth": "github-cli"
}
```

Specify chạy `gh auth token --hostname ghes.example.com`, dùng đúng hostname đầu tiên như đã cấu hình. Dùng các mục provider riêng cho các instance GitHub riêng biệt. Host được chọn phải đã được xác thực trong GitHub CLI; khi thất bại, thông báo gợi ý `gh auth login --hostname <host>` mà không kèm đầu ra của lệnh GitHub CLI.

<a id="github-enterprise-cloud-with-data-residency-ghecom"></a>

### GitHub Enterprise Cloud với lưu trữ dữ liệu theo vùng (GHE.com)

Tenant GHE.com dùng hostname riêng cho web và REST API. Liệt kê cả hai host để Specify có thể xác thực việc tra cứu metadata bản phát hành và tải tài nguyên:

```json
{
  "providers": [
    {
      "hosts": ["tenant.ghe.com", "api.tenant.ghe.com"],
      "provider": "github",
      "auth": "bearer",
      "token_env": "GH_ENTERPRISE_TOKEN"
    }
  ]
}
```

Với URL bản phát hành trên `tenant.ghe.com`, Specify phân giải metadata và tài nguyên bản phát hành qua `api.tenant.ghe.com`. Tài nguyên trả về phải xác định cùng owner và repository, và dùng đúng endpoint số `/repos/.../releases/assets/...`. Ký tự đại diện như `*.tenant.ghe.com` khớp hostname API nhưng không khớp hostname web trần của tenant, nên hãy liệt kê rõ hostname web.

### Azure DevOps (`azure-devops`)

| Cơ chế | Header | Dùng cho |
|---|---|---|
| `basic-pat` | `Authorization: Basic base64(:<PAT>)` | Personal Access Token |
| `bearer` | `Authorization: Bearer <token>` | Token OAuth / Azure AD đã lấy sẵn |
| `azure-cli` | `Authorization: Bearer <token>` | Token lấy qua `az account get-access-token` |
| `azure-ad` | `Authorization: Bearer <token>` | Token lấy qua luồng OAuth2 client credentials |

**Ví dụ — PAT qua biến môi trường:**

```json
{
  "hosts": ["dev.azure.com"],
  "provider": "azure-devops",
  "auth": "basic-pat",
  "token_env": "AZURE_DEVOPS_PAT"
}
```

**Ví dụ — Azure CLI (đăng nhập tương tác):**

```json
{
  "hosts": ["dev.azure.com"],
  "provider": "azure-devops",
  "auth": "azure-cli"
}
```

Cần chạy `az login` từ trước.

**Ví dụ — service principal Azure AD (CI/tự động hóa):**

```json
{
  "hosts": ["dev.azure.com"],
  "provider": "azure-devops",
  "auth": "azure-ad",
  "tenant_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "client_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "client_secret_env": "AZURE_CLIENT_SECRET"
}
```

### Bitbucket (`bitbucket`)

| Cơ chế | Header | Dùng cho |
|---|---|---|
| `bearer` | `Authorization: Bearer <token>` | Access token cấp repository / project / workspace, hoặc API token Atlassian gửi không kèm email tài khoản (Bitbucket Cloud, **chỉ `api.bitbucket.org`** — xem ghi chú bên dưới); HTTP access token (Bitbucket Data Center) |
| `basic` | `Authorization: Basic base64(<username>:<token>)` | API token Atlassian (username = email tài khoản Atlassian) với `api.bitbucket.org`. App password của Bitbucket Cloud đã bị Atlassian gỡ bỏ vào ngày 28/7/2026 — hãy dùng API token hoặc access token thay thế. |

> **Ghi chú về host:** Bitbucket Cloud chia bề mặt dịch vụ theo host. `api.bitbucket.org` chấp nhận access token cấp repository/project/workspace dạng Bearer, và API token Atlassian dạng Basic (với email tài khoản làm username) hoặc dạng Bearer (không cần email), trên mọi lời gọi REST, kể cả khi tải file catalog qua `GET /2.0/repositories/<workspace>/<repo>/src/<ref>/<path>`. Host web `bitbucket.org` thông thường (trang trình duyệt, liên kết `.../raw/...`, `git clone` qua HTTPS) **không** chấp nhận cả hai loại đó — nó xác thực git-over-HTTPS bằng HTTP Basic với username nguyên văn `x-token-auth` và access token làm mật khẩu. Hãy trỏ catalog và các mục `download_url` tới `api.bitbucket.org` (bên dưới) thay vì `bitbucket.org/.../raw/...` để thông tin xác thực trong `auth.json` thực sự được áp dụng.

**Ví dụ — access token Bitbucket Cloud (khuyến nghị):**

```json
{
  "hosts": ["api.bitbucket.org"],
  "provider": "bitbucket",
  "auth": "bearer",
  "token_env": "BITBUCKET_ACCESS_TOKEN"
}
```

Tạo token với scope **Repositories: Read** trên repository (hoặc project/workspace) chứa catalog và archive của bạn. Tải file catalog bằng thông tin xác thực này qua `https://api.bitbucket.org/2.0/repositories/<workspace>/<repo>/src/<ref>/catalog.json` thay vì URL `bitbucket.org/.../raw/...`.

**Ví dụ — API token Atlassian (xác thực Basic):**

```json
{
  "hosts": ["api.bitbucket.org"],
  "provider": "bitbucket",
  "auth": "basic",
  "username": "you@example.com",
  "token_env": "ATLASSIAN_API_TOKEN"
}
```

**Ví dụ — HTTP access token của Bitbucket Data Center:**

```json
{
  "hosts": ["bitbucket.example.com"],
  "provider": "bitbucket",
  "auth": "bearer",
  "token_env": "BITBUCKET_DC_TOKEN"
}
```

> **Lưu ý:** Bitbucket Cloud phục vụ việc tải file (mục **Downloads** của repository) bằng cách chuyển hướng tới một URL Amazon S3 đã ký sẵn. Specify bỏ header `Authorization` khi chuyển hướng đó vì đích nằm ngoài các host bạn đã khai báo — điều này là bình thường và việc tải vẫn thành công, vì URL S3 tự mang quyền truy cập. Hãy ghim `sha256` trong các mục catalog để bước cuối không xác thực vẫn được kiểm tra tính toàn vẹn.

<a id="multiple-entries"></a>

## Nhiều mục

Bạn có thể cấu hình nhiều mục cho các host hoặc tổ chức khác nhau:

```json
{
  "providers": [
    {
      "hosts": ["github.com", "api.github.com", "raw.githubusercontent.com", "codeload.github.com"],
      "provider": "github",
      "auth": "bearer",
      "token_env": "GH_TOKEN"
    },
    {
      "hosts": ["dev.azure.com"],
      "provider": "azure-devops",
      "auth": "basic-pat",
      "token_env": "AZURE_DEVOPS_PAT"
    }
  ]
}
```

<a id="how-it-works"></a>

## Cách hoạt động

1. Với mỗi request HTTP đi ra, hostname của URL được so khớp với các mẫu `hosts` trong `auth.json`.
2. Nếu có mục khớp, provider tương ứng phân giải token và đính kèm header `Authorization` phù hợp. Lỗi khi lấy token qua `github-cli` kết thúc request ngay lập tức, không thử các mục khớp sau đó và không gửi request không xác thực.
3. Sau khi lấy token thành công, nếu request nhận 401 hoặc 403, mục khớp tiếp theo sẽ được thử.
4. Khi đã thử hết mọi mục khớp mà không có lỗi lấy token, một request không xác thực được thử như phương án dự phòng cuối cùng.
5. Khi chuyển hướng, header `Authorization` bị bỏ nếu đích chuyển hướng nằm ngoài các host đã khai báo của mục — ngăn rò rỉ thông tin xác thực tới CDN hoặc dịch vụ bên thứ ba.

## Template

Một file `auth.json` tham khảo đã cấu hình sẵn GitHub:

```json
{
  "providers": [
    {
      "hosts": [
        "github.com",
        "api.github.com",
        "raw.githubusercontent.com",
        "codeload.github.com"
      ],
      "provider": "github",
      "auth": "bearer",
      "token_env": "GH_TOKEN"
    }
  ]
}
```

Để dùng nó:

```bash
mkdir -p ~/.specify
# Copy the JSON above into ~/.specify/auth.json
chmod 600 ~/.specify/auth.json
```
