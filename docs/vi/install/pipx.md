<a id="installing-with-pipx"></a>

# Cài đặt bằng pipx

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../install/pipx.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

[pipx](https://pipx.pypa.io/) là công cụ cài ứng dụng CLI Python vào các môi trường cô lập. Nó không cần [uv](https://docs.astral.sh/uv/).

<a id="install-specify-cli"></a>

## Cài Specify CLI

Để ổn định, hãy ghim một tag phát hành cụ thể (xem bản mới nhất trong [Releases](https://github.com/github/spec-kit/releases)):

```bash
# Install a specific stable release (recommended — replace vX.Y.Z with the
# latest tag, keeping the leading v, e.g. v0.12.11 not 0.12.11)
pipx install git+https://github.com/github/spec-kit.git@vX.Y.Z

# Or install latest from main (may include unreleased changes)
pipx install git+https://github.com/github/spec-kit.git
```

<a id="verify"></a>

## Kiểm tra

```bash
specify version
```

<a id="upgrade"></a>

## Nâng cấp

```bash
pipx install --force git+https://github.com/github/spec-kit.git@vX.Y.Z
```

<a id="uninstall"></a>

## Gỡ cài đặt

```bash
pipx uninstall specify-cli
```

<a id="next-steps"></a>

## Bước tiếp theo

Chuyển sang [Hướng dẫn nhanh](../quickstart.md) để khởi tạo dự án đầu tiên.
