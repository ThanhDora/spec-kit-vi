<a id="enterprise--air-gapped-installation"></a>

# Cài đặt cho doanh nghiệp / air-gapped

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../install/air-gapped.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Nếu môi trường của bạn chặn truy cập PyPI hoặc GitHub, bạn có thể tạo một gói wheel mang đi được trên máy có kết nối mạng rồi chuyển sang máy đích air-gapped.

<a id="step-1-build-the-wheel-on-a-connected-machine"></a>

## Bước 1: Build wheel trên máy có kết nối mạng

> **Quan trọng:** `pip download` phân giải các wheel phụ thuộc nền tảng (ví dụ PyYAML có native extension). Bạn phải chạy bước này trên máy có **cùng hệ điều hành và phiên bản Python** với máy đích air-gapped. Nếu cần hỗ trợ nhiều nền tảng, hãy lặp lại bước này trên từng hệ điều hành đích (Linux, macOS, Windows) và từng phiên bản Python.

```bash
# Clone the repository
git clone https://github.com/github/spec-kit.git
cd spec-kit

# Build the wheel
pip install build
python -m build --wheel --outdir dist/

# Download the wheel and all its runtime dependencies
pip download -d dist/ dist/specify_cli-*.whl
```

<a id="step-2-transfer-the-dist-directory"></a>

## Bước 2: Chuyển thư mục `dist/`

Sao chép toàn bộ thư mục `dist/` (chứa wheel `specify-cli` và wheel của mọi thư viện phụ thuộc) sang máy đích qua USB, thư mục chia sẻ trong mạng nội bộ hoặc phương thức chuyển dữ liệu khác đã được phê duyệt.

<a id="step-3-install-on-the-air-gapped-machine"></a>

## Bước 3: Cài đặt trên máy air-gapped

```bash
pip install --no-index --find-links=./dist specify-cli
```

<a id="step-4-initialize-a-project"></a>

## Bước 4: Khởi tạo dự án

Không cần truy cập mạng — các tài nguyên đóng gói sẵn được dùng theo mặc định:

```bash
specify init my-project --integration copilot
```

> **Lưu ý:** Cần Python 3.11+.
>
> **Lưu ý cho Windows:** Việc dựng khung dự án khi offline cần PowerShell 7+ (`pwsh`), không phải Windows PowerShell 5.x (`powershell.exe`). Cài đặt tại <https://aka.ms/powershell>.

<a id="component-catalogs-and-sources"></a>

## Catalog và nguồn của các thành phần

Các integration có sẵn và các thành phần đóng gói kèm vẫn dùng được khi không có
mạng. Việc cài đặt qua catalog cho adapter integration bên ngoài, extension,
preset, workflow, workflow step và bundle cần cả metadata của catalog lẫn các
artifact phát hành mà nó tham chiếu. Với những loại thành phần hỗ trợ nguồn
trực tiếp hoặc nguồn cục bộ, cách cài đặt đó không cần metadata của catalog.

Với mạng bị giới hạn nhưng vẫn truy cập được các dịch vụ nội bộ đã phê duyệt, hãy
host các catalog và artifact đã được review trên endpoint HTTPS nội bộ, rồi đăng ký
nguồn của từng loại thành phần bằng lệnh `catalog add` tương ứng. Với mạng hoàn toàn
tách biệt, hãy chuyển các artifact đã được review qua quy trình được phê duyệt và cài
chúng từ nguồn trực tiếp hoặc nguồn cục bộ được hỗ trợ, thay vì dựa vào một catalog
từ xa không truy cập được.

Adapter integration bên ngoài là ngoại lệ. `specify integration install`
không có tùy chọn nguồn trực tiếp hay cục bộ: lệnh này phải phân giải adapter qua
một catalog integration cho phép cài đặt và tải archive của adapter về. Để thêm
adapter bên ngoài trong môi trường cô lập, hãy đảm bảo cả catalog nội bộ đã phê
duyệt lẫn archive của adapter đều truy cập được từ đó, hoặc cài adapter trước khi
ngắt kết nối máy đích. Chỉ chuyển archive thôi là không đủ.

Bundle cần được xử lý riêng: thư mục hoặc file ZIP bundle được chuyển sang chỉ cung cấp
manifest của bundle, không chứa nội dung các thành phần mà nó liệt kê. Trước khi ngắt
kết nối, hãy cài riêng các thành phần tương ứng không nằm trong bundle. Những thành phần
có `source` khai báo rõ trong catalog vẫn cần mạng để xác minh ngay cả khi đã được cài,
và nội dung của workflow step hiện chỉ phân giải được qua catalog step. Hãy xem
[giới hạn offline của bundle](../../reference/bundles.md#install-a-bundle) trước khi
dựa vào `specify bundle install --offline`.

Xem [tài liệu tham khảo về catalog](../../reference/catalogs.md) để biết các loại catalog, chính sách
tin cậy và thứ tự ưu tiên của nguồn. Nếu endpoint nội bộ yêu cầu thông tin xác thực,
hãy cấu hình thêm phần [Xác thực](../../reference/authentication.md).

<a id="git-credential-manager-on-linux"></a>

## Git Credential Manager trên Linux

Nếu bạn gặp vấn đề xác thực Git trên Linux, bạn có thể cài Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```
