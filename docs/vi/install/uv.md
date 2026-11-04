<a id="installing-uv"></a>

# Cài đặt uv

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../install/uv.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

[uv](https://docs.astral.sh/uv/) là trình quản lý package Python tốc độ cao của [Astral](https://astral.sh/). Spec Kit dùng `uv` (qua `uvx` hoặc `uv tool install`) để chạy CLI `specify` mà không làm "bẩn" môi trường Python toàn cục của bạn.

> [!NOTE]
> **Đã có uv?** Chạy `uv --version` để xác nhận uv đã được cài, rồi quay lại [Hướng dẫn cài đặt](../installation.md).

<a id="installation"></a>

## Cài đặt

<a id="macos-and-linux--standalone-installer"></a>

### macOS và Linux — trình cài đặt độc lập

Cách nhanh nhất để cài uv trên macOS hoặc Linux là dùng script shell chính thức:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Khi script chạy xong, làm theo hướng dẫn mà trình cài đặt in ra để thêm uv vào `PATH`, rồi mở một terminal mới.

<a id="windows--standalone-installer"></a>

### Windows — trình cài đặt độc lập

Chạy lệnh sau trong **Command Prompt hoặc PowerShell**:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Khi script chạy xong, mở một terminal mới để file thực thi `uv` có trong `PATH`.

### macOS — Homebrew

```bash
brew install uv
```

### Windows — WinGet

```powershell
winget install --id=astral-sh.uv -e
```

### Windows — Scoop

```powershell
scoop install uv
```

<a id="verification"></a>

## Kiểm tra

Xác nhận uv đã được cài và có trong `PATH`:

```bash
uv --version
```

Bạn sẽ thấy kết quả tương tự `uv 0.x.y (...)`.

<a id="further-reading"></a>

## Đọc thêm

Với các tùy chọn nâng cao (tự cập nhật, thiết lập proxy, gỡ cài đặt...), xem [tài liệu cài đặt uv](https://docs.astral.sh/uv/getting-started/installation/) chính thức.
