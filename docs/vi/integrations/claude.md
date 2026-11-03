# Claude Code

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/claude.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Claude Code](https://www.anthropic.com/claude-code) trước khi thiết lập. Khóa integration là `claude`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration claude
```

Với dự án Spec Kit đã có, dùng `specify integration install claude`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.claude/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của Claude, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

<a id="user-invocable-only-skills"></a>

## Skill chỉ cho người dùng gọi

Mặc định, mọi skill Spec Kit cài cho Claude Code đều do mô hình gọi được, nên mô tả của chúng luôn nằm trong ngữ cảnh của Claude và bị tính vào ngân sách liệt kê skill. Trong dự án có nhiều skill, điều này có thể đẩy các skill khác ra khỏi danh sách. Để các skill lệnh lõi của Spec Kit chỉ cho người dùng gọi:

```bash
specify init my-project --integration claude --integration-options="--no-model-invocation"
```

Lệnh này ghi `disable-model-invocation: true` vào các skill lệnh lõi. Claude chỉ chạy được chúng khi người dùng gọi `/speckit-<command>`, và mô tả của chúng nằm ngoài ngữ cảnh của Claude.

- Skill của extension vẫn do mô hình gọi được, vì hook bắt buộc của extension dựa vào việc mô hình gọi chúng. Nếu hook bắt buộc của một extension chạy một lệnh lõi (`command:` của nó là một `speckit.<command>` lõi), hãy tắt tùy chọn này: mô hình không thể chạy hook đó khi skill lõi chỉ cho người dùng gọi.
- Tùy chọn này được lưu cùng các tùy chọn khác của integration và được áp dụng lại khi chạy `specify integration upgrade claude`. Truyền `--integration-options` cho `upgrade` sẽ thay thế toàn bộ tùy chọn đã lưu, nên hãy lặp lại những tùy chọn bạn muốn giữ (ví dụ `--integration-options="--events false --no-model-invocation"`); `--integration-options=""` xóa hết chúng. Tương tự, chạy lại `specify init` chỉ lưu các tùy chọn được truyền vào lần chạy đó.
- Các skill lệnh lõi mà một preset ghi đè, hoặc thôi ghi đè, sẽ bị đưa về mặc định bởi những lệnh đăng ký lại skill của preset mà không cài lại Claude: các lệnh cài, gỡ hoặc cập nhật preset (kể cả các lệnh `specify bundle` có mang preset), `specify integration use claude`, và `specify integration switch claude` khi Claude đã được cài nhưng không phải mặc định. Để áp dụng lại tùy chọn, chạy `specify integration upgrade claude --force` khi Claude là integration mặc định (cần `--force` vì các lệnh đó sửa file skill đã cài, và nó ghi đè các chỉnh sửa cục bộ trên file do Spec Kit quản lý).

<a id="runtime-events-and-workflow-dispatch"></a>

## Runtime event và điều phối workflow

Integration hỗ trợ event gốc qua `.claude/settings.json`. Dùng `--integration-options="--events false"` để tắt các trình xử lý event của Spec Kit; kết hợp với `--no-model-invocation` nếu muốn cả hai thiết lập. Xem [runtime event](cli.md#runtime-events).

Workflow step dùng `claude -p <prompt>`, kèm `--model` khi đã cấu hình và `--output-format json` khi cần đầu ra có cấu trúc. Bản thân adapter này không thêm cờ bỏ qua quyền.
