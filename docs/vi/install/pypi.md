<a id="installing-from-pypi"></a>

# Cài đặt từ PyPI

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../install/pypi.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Spec Kit được phát hành trên PyPI dưới tên [`specify-cli`](https://pypi.org/project/specify-cli/) và do nhóm maintainer Spec Kit duy trì. Cài từ PyPI là cách cài đặt thứ hai được hỗ trợ, bên cạnh việc cài từ [mã nguồn trên GitHub](../installation.md#install-from-source--persistent-installation-recommended). Hãy chọn cách phù hợp với quy trình làm việc của bạn — cả hai đều cung cấp cùng một CLI `specify`.

> [!NOTE]
> Phiên bản phát hành trên PyPI bám theo các tag phát hành trên GitHub (ví dụ PyPI `0.12.11` tương ứng với tag `v0.12.11`). `specify version` chỉ là bước kiểm tra nhanh phiên bản và môi trường chạy cục bộ — nó cho biết phiên bản đã cài nhưng không cho biết file thực thi `specify` đến từ đâu, nên không phân biệt được bản cài từ PyPI với bản cài từ Git. Để xác nhận nguồn cài đặt, hãy xem metadata nguồn mà trình quản lý package ghi lại: `pipx list --json` cho biết chính xác đặc tả cài đặt của từng công cụ; với bản cài bằng uv/pip, bạn có thể xem file `direct_url.json` theo [PEP 610](https://peps.python.org/pep-0610/) trong thư mục `*.dist-info` của package (bản cài từ Git hoặc URL sẽ ghi URL của repository/archive vào đó, còn bản cài thông thường từ PyPI index thì không tạo file này). Lưu ý rằng `pip show specify-cli` chỉ in metadata của package và không nhìn thấy các môi trường do uv/pipx quản lý từ trình thông dịch của hệ thống.

<a id="install-specify-cli"></a>

## Cài Specify CLI

Dùng công cụ Python bạn đang có:

```bash
# Using uv (recommended)
uv tool install specify-cli

# Or using pipx
pipx install specify-cli

# Or using pip
pip install specify-cli
```

Nếu bạn đã cài Spec Kit bằng uv, chạy lại `uv tool install specify-cli`
sẽ giữ nguyên phiên bản đã cài chứ không nâng cấp. Hãy so phiên bản mà
`specify version` hiển thị với [phiên bản mới nhất trên PyPI](https://pypi.org/project/specify-cli/).
Nếu bản của bạn cũ hơn, hãy làm theo mục [Nâng cấp](#upgrade) bên dưới bằng đúng công cụ đã dùng
khi cài ban đầu (uv, pipx hoặc pip) trước khi chạy `specify init`.
Đừng đổi trình cài đặt chỉ để nâng cấp: làm vậy có thể tạo ra bản cài thứ hai
trong khi `specify` cũ vẫn đứng trước trên `PATH`.

<a id="install-a-specific-release"></a>

### Cài một bản phát hành cụ thể

Ghim chính xác phiên bản để bản cài có thể tái lập (xem các phiên bản hiện có trên [PyPI](https://pypi.org/project/specify-cli/#history) hoặc [Releases](https://github.com/github/spec-kit/releases)):

```bash
# Using uv
uv tool install specify-cli==0.12.11

# Or using pipx
pipx install specify-cli==0.12.11

# Or using pip
pip install specify-cli==0.12.11
```

<a id="install-from-a-custom-or-private-package-index"></a>

## Cài từ package index tùy chỉnh hoặc riêng tư

Một số môi trường (mạng doanh nghiệp, mirror, proxy hoặc artifact feed) yêu cầu cài `specify-cli` từ một package index khác với PyPI công khai mặc định. Mỗi công cụ Python đều có cách trỏ tới index khác — hãy cấu hình trước khi chạy các lệnh cài đặt ở trên. Thay placeholder dưới đây bằng URL index của bạn.

```bash
# uv — via environment variable (applies to the whole command)
UV_DEFAULT_INDEX=https://your-index.example.com/pypi/simple/ uv tool install specify-cli

# uv — via flag
uv tool install --default-index https://your-index.example.com/pypi/simple/ specify-cli

# pipx — pass a pip argument through
pipx install specify-cli --index-url https://your-index.example.com/pypi/simple/

# pip
pip install specify-cli --index-url https://your-index.example.com/pypi/simple/
```

> [!NOTE]
> Cấu hình index này cũng áp dụng cho bản cài được ghim phiên bản, khi nâng cấp (`--force`/`--upgrade`) và khi dùng một lần — hãy đặt biến môi trường hoặc cờ tương ứng cho cả những lệnh đó. Nếu index yêu cầu xác thực, hãy làm theo tài liệu của công cụ và ưu tiên biến môi trường chứa thông tin xác thực, keyring hoặc netrc; đừng nhúng secret vào URL trên dòng lệnh vì chúng có thể lộ qua lịch sử shell, danh sách tiến trình hoặc log. Tránh commit secret. Để cài hoàn toàn offline, xem [hướng dẫn cài đặt air-gapped](air-gapped.md).

<a id="verify"></a>

## Kiểm tra

```bash
specify version
```

<a id="initialize-a-project"></a>

## Khởi tạo dự án

```bash
specify init <PROJECT_NAME> --integration copilot
```

<a id="upgrade"></a>

## Nâng cấp

Nâng cấp bằng cách cài lại package qua đúng công cụ đã dùng khi cài ban đầu. Nếu trước đây bạn đã ghim phiên bản, lưu ý rằng `uv tool upgrade` giữ nguyên phiên bản đã ghim; để chuyển sang bản phát hành mới nhất trên PyPI, hãy dùng lệnh cài không ghim phiên bản để không giữ lại phiên bản cũ:

```bash
# Using uv
uv tool install --force specify-cli

# Or using pipx
pipx install --force specify-cli

# Or using pip
pip install --upgrade specify-cli
```

> [!NOTE]
> Hiện tại `specify self upgrade` build lại các bản cài bằng `uv tool` và `pipx` từ URL bản phát hành mã nguồn trên GitHub thay vì giữ nguyên bản cài từ PyPI. Nếu muốn tiếp tục dùng PyPI, hãy dùng các lệnh của trình quản lý package ở trên. Bản cài bằng `pip install specify-cli` thông thường được coi là bản cài không được quản lý — hãy nâng cấp bằng `pip install --upgrade specify-cli`. Xem [Hướng dẫn nâng cấp](../upgrade.md) để biết chi tiết.

<a id="uninstall"></a>

## Gỡ cài đặt

```bash
# Using uv
uv tool uninstall specify-cli

# Or using pipx
pipx uninstall specify-cli

# Or using pip
pip uninstall specify-cli
```

<a id="next-steps"></a>

## Bước tiếp theo

Chuyển sang [Hướng dẫn nhanh](../quickstart.md) để khởi tạo dự án đầu tiên.
