<a id="local-development-guide"></a>

# Hướng dẫn phát triển cục bộ

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../local-development.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hướng dẫn này chỉ cách thử nghiệm và chỉnh sửa CLI `specify` ngay trên máy mà không cần phát hành hay commit lên `main` trước.

> Script có ba biến thể: Bash (`.sh`), PowerShell (`.ps1`) và Python (`.py`). Khi chạy tương tác, `specify init` sẽ hỏi bạn chọn một loại; khi chạy không tương tác (không có TTY, hoặc có `--non-interactive`), mặc định là biến thể shell của hệ điều hành. Truyền `--script sh|ps|py` để chọn rõ ràng.

Để biết dự án dùng chính quy trình SDD và đánh giá ý tưởng của mình như thế nào, xem
[Does Spec Kit use Spec Kit?](https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md#does-spec-kit-use-spec-kit)
trong hướng dẫn đóng góp.

<a id="1-clone-and-switch-branches"></a>

## 1. Clone và chuyển branch

```bash
git clone https://github.com/github/spec-kit.git
cd spec-kit
# Work on a feature branch
git checkout -b your-feature-branch
```

<a id="2-run-the-cli-directly-fastest-feedback"></a>

## 2. Chạy CLI trực tiếp (phản hồi nhanh nhất)

Bạn có thể chạy CLI qua entrypoint của module mà không cần cài gì:

```bash
# From repo root
python -m src.specify_cli --help
python -m src.specify_cli init demo-project --integration claude --ignore-agent-tools --script sh
```

Nếu bạn thích gọi theo kiểu chạy file script (dùng shebang):

```bash
python src/specify_cli/__init__.py init demo-project --script ps
```

<a id="3-use-editable-install-isolated-environment"></a>

## 3. Dùng bản cài editable (môi trường cô lập)

Tạo một môi trường cô lập bằng `uv` để các thư viện phụ thuộc được phân giải đúng như người dùng cuối nhận được:

```bash
# Create & activate virtual env (uv auto-manages .venv)
uv venv
source .venv/bin/activate  # or on Windows PowerShell: .venv\Scripts\Activate.ps1

# Install project in editable mode
uv pip install -e .

# Now 'specify' entrypoint is available
specify --help
```

Nhờ chế độ editable, sau khi sửa code bạn chỉ cần chạy lại mà không phải cài lại.

<a id="4-invoke-with-uvx-directly-from-git-current-branch"></a>

## 4. Gọi bằng uvx trực tiếp từ Git (branch hiện tại)

`uvx` có thể chạy từ một đường dẫn cục bộ (hoặc một Git ref) để mô phỏng luồng sử dụng của người dùng:

```bash
uvx --from . specify init demo-uvx --integration copilot --ignore-agent-tools --script sh
```

Bạn cũng có thể trỏ uvx tới một branch cụ thể mà không cần merge:

```bash
# Push your working branch first
git push origin your-feature-branch
uvx --from git+https://github.com/github/spec-kit.git@your-feature-branch specify init demo-branch-test --script ps
```

<a id="4a-absolute-path-uvx-run-from-anywhere"></a>

### 4a. uvx với đường dẫn tuyệt đối (chạy từ bất kỳ đâu)

Nếu đang ở thư mục khác, hãy dùng đường dẫn tuyệt đối thay cho `.`:

```bash
uvx --from /mnt/c/GitHub/spec-kit specify --help
uvx --from /mnt/c/GitHub/spec-kit specify init demo-anywhere --integration copilot --ignore-agent-tools --script sh
```

Đặt một biến môi trường cho tiện:

```bash
export SPEC_KIT_SRC=/mnt/c/GitHub/spec-kit
uvx --from "$SPEC_KIT_SRC" specify init demo-env --integration copilot --ignore-agent-tools --script ps
```

(Tùy chọn) Định nghĩa một hàm shell:

```bash
specify-dev() { uvx --from /mnt/c/GitHub/spec-kit specify "$@"; }
# Then
specify-dev --help
```

<a id="5-testing-script-permission-logic"></a>

## 5. Kiểm thử logic phân quyền của script

Sau khi chạy `init`, kiểm tra các script shell có quyền thực thi trên hệ thống POSIX:

```bash
ls -l scripts | grep .sh
# Expect owner execute bit (e.g. -rwxr-xr-x)
```

Trên Windows, bạn sẽ dùng các script `.ps1` thay thế (không cần chmod).

<a id="6-develop-a-built-in-integration"></a>

## 6. Phát triển một integration có sẵn

Làm theo [thiết kế integration cho agent](https://github.com/github/spec-kit/blob/main/design/integration.md#adding-an-agent)
để biết contract triển khai, cách đăng ký và yêu cầu về độ phủ hành vi. Xem
[đóng góp integration](integrations/contributing.md) để biết về mục catalog
và hướng dẫn gửi bài.

<a id="7-run-lint--basic-checks"></a>

## 7. Chạy lint / các bước kiểm tra cơ bản

CI bắt buộc chạy `ruff check src tests` (xem `.github/workflows/test.yml`), nên hãy chạy cục bộ trước khi push:

```bash
uvx ruff check src tests
```

Bạn cũng có thể kiểm tra nhanh xem module có import được không:

```bash
python -c "import specify_cli; print('Import OK')"
```

<a id="8-build-a-wheel-locally-optional"></a>

## 8. Build wheel cục bộ (tùy chọn)

Kiểm định việc đóng gói trước khi phát hành:

```bash
uv build
ls dist/
```

Nếu cần, hãy cài artifact đã build vào một môi trường mới dùng xong bỏ.

<a id="9-using-a-temporary-workspace"></a>

## 9. Dùng một workspace tạm

Khi kiểm thử `init --here` trong một thư mục đã có thay đổi, hãy tạo một workspace tạm:

```bash
mkdir /tmp/spec-test && cd /tmp/spec-test
python -m src.specify_cli init --here --integration claude --ignore-agent-tools --script sh  # if repo copied here
```

Hoặc chỉ sao chép phần CLI đã sửa nếu bạn muốn một sandbox nhẹ hơn.

<a id="10-debug-network--tls-issues"></a>

## 10. Gỡ lỗi mạng / TLS

> **Đã ngừng hỗ trợ:** Cờ `--skip-tls` không còn tác dụng.
> Trước đây cờ này được dùng để bỏ qua kiểm tra TLS khi kiểm thử cục bộ.
> Nếu gặp lỗi TLS (ví dụ trong mạng doanh nghiệp), hãy cấu hình
> kho chứng chỉ hoặc proxy của môi trường thay thế.
>
> Ví dụ, đặt `SSL_CERT_FILE` hoặc cấu hình `HTTPS_PROXY` / `HTTP_PROXY`.

<a id="11-rapid-edit-loop-summary"></a>

## 11. Tóm tắt vòng chỉnh sửa nhanh

| Thao tác | Lệnh |
|--------|---------|
| Chạy CLI trực tiếp | `python -m src.specify_cli --help` |
| Cài editable | `uv pip install -e .` rồi `specify ...` |
| Chạy uvx cục bộ (thư mục gốc repo) | `uvx --from . specify ...` |
| Chạy uvx cục bộ (đường dẫn tuyệt đối) | `uvx --from /mnt/c/GitHub/spec-kit specify ...` |
| uvx từ Git branch | `uvx --from git+URL@branch specify ...` |
| Build wheel | `uv build` |

<a id="12-cleaning-up"></a>

## 12. Dọn dẹp

Xóa nhanh các artifact build / môi trường ảo:

```bash
rm -rf .venv dist build *.egg-info
```

<a id="13-common-issues"></a>

## 13. Sự cố thường gặp

| Triệu chứng | Cách khắc phục |
|---------|-----|
| `ModuleNotFoundError: typer` | Chạy `uv pip install -e .` |
| Script không có quyền thực thi (Linux) | Chạy lại init hoặc `chmod +x scripts/*.sh` |
| Không dùng được các lệnh Git | Cài extension git bằng `specify extension add git` |
| Tải về sai loại script | Truyền rõ `--script sh`, `--script ps` hoặc `--script py` |
| Lỗi TLS trong mạng doanh nghiệp | Cấu hình kho chứng chỉ hoặc proxy của môi trường. Cờ `--skip-tls` đã ngừng hỗ trợ và không có tác dụng. |

<a id="14-next-steps"></a>

## 14. Bước tiếp theo

- Cập nhật tài liệu và chạy thử Hướng dẫn nhanh bằng CLI đã sửa
- Mở PR khi đã hài lòng
- (Tùy chọn) Gắn tag phát hành khi thay đổi đã vào `main`
