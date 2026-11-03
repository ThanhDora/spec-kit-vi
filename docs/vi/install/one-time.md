<a id="one-time-usage-uvx"></a>

# Dùng một lần (uvx)

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../install/one-time.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Nếu bạn muốn dùng thử Spec Kit mà không cài cố định, hãy dùng `uvx` để chạy trực tiếp. Lệnh này tải công cụ vào một môi trường tạm và môi trường đó bị xóa khi lệnh chạy xong.

> [!NOTE]
> Các lệnh dưới đây cần **[uv](https://docs.astral.sh/uv/)**. Nếu bạn gặp lỗi `command not found: uvx`, hãy [cài uv trước](uv.md).

<a id="run-specify-cli"></a>

## Chạy Specify CLI

```bash
# Create a new project (latest from main)
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>

# Or target a specific release (replace vX.Y.Z with a tag from Releases;
# keep the leading v, e.g. v0.12.11 not 0.12.11)
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <PROJECT_NAME>

# Initialize in the current directory
uvx --from git+https://github.com/github/spec-kit.git specify init . --integration copilot

# Or use the --here flag
uvx --from git+https://github.com/github/spec-kit.git specify init --here --integration copilot
```

<a id="when-to-use-persistent-installation-instead"></a>

## Khi nào nên cài đặt lâu dài

Nếu bạn định dùng Spec Kit thường xuyên, nên cài đặt lâu dài:

- Công cụ luôn được cài sẵn và có trong PATH
- Không phải tải lại mỗi lần gọi
- Quản lý công cụ tốt hơn với `uv tool list`, `uv tool upgrade`, `uv tool uninstall`

Xem [Hướng dẫn cài đặt](../installation.md) chính để biết cách cài đặt lâu dài.
