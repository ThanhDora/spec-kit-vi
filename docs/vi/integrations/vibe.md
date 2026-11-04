# Mistral Vibe

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/vibe.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Mistral Vibe](https://github.com/mistralai/mistral-vibe) trước khi thiết lập. Khóa integration là `vibe`. Bố cục skills yêu cầu Mistral Vibe v2.0.0 trở lên.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration vibe
```

Với dự án Spec Kit đã có, dùng `specify integration install vibe`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.vibe/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Mặc định, skill được sinh ra vừa do người dùng gọi được vừa do mô hình gọi được. Cờ tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định.

<a id="user-invocable-only-skills"></a>

## Skill chỉ cho người dùng gọi

Để Mistral Vibe không tự động gọi các skill lệnh lõi của Spec Kit:

```bash
specify init my-project --integration vibe --integration-options="--no-model-invocation"
```

Lệnh này ghi `disable-model-invocation: true` vào các skill lệnh lõi. Theo [README](https://github.com/mistralai/mistral-vibe#skills-system) của Mistral Vibe, skill như vậy chỉ được gọi tường minh: bạn vẫn có thể gọi `/speckit-<command>`, nhưng mô hình không thấy và không tự động gọi nó.

- Skill của extension vẫn do mô hình gọi được, vì hook bắt buộc của extension dựa vào việc mô hình gọi chúng. Nếu hook bắt buộc của một extension chạy một lệnh lõi (`command:` của nó là một `speckit.<command>` lõi), hãy tắt tùy chọn này: mô hình không thể chạy hook đó khi skill lõi chỉ cho người dùng gọi.
- Tùy chọn này được lưu cùng các tùy chọn khác của integration và được áp dụng lại khi chạy `specify integration upgrade vibe`. Truyền `--integration-options` cho `upgrade` sẽ thay thế toàn bộ tùy chọn đã lưu; `--integration-options=""` xóa hết chúng. Tương tự, chạy lại `specify init` chỉ lưu các tùy chọn được truyền vào lần chạy đó.
- Các skill lệnh lõi mà một preset ghi đè, hoặc thôi ghi đè, sẽ bị đưa về mặc định bởi những lệnh đăng ký lại skill của preset mà không cài lại Mistral Vibe: các lệnh cài, gỡ hoặc cập nhật preset (kể cả các lệnh `specify bundle` có mang preset), `specify integration use vibe`, và `specify integration switch vibe` khi Mistral Vibe đã được cài nhưng không phải mặc định. Để áp dụng lại tùy chọn, chạy `specify integration upgrade vibe --force` khi Mistral Vibe là integration mặc định (cần `--force` vì các lệnh đó sửa file skill đã cài, và nó ghi đè các chỉnh sửa cục bộ trên file do Spec Kit quản lý).

<a id="runtime-events"></a>

## Runtime event

Event gốc dùng `.vibe/hooks.toml`. Vibe chỉ hỗ trợ `pre_tool_use`, `post_tool_use` và `stop`, được ánh xạ sang `pre_tool`, `post_tool` và `post_agent`. Các event bắt đầu phiên, kết thúc phiên và gửi prompt không được phát ra cho Vibe; trình xử lý không được hỗ trợ sẽ bị bỏ qua kèm cảnh báo. `--integration-options="--events false"` tắt trình xử lý event của Spec Kit. Xem [runtime event](cli.md#runtime-events).

Spec Kit chỉ làm mới và xóa các mục `[[hooks]]` do nó ghi, vốn mang `speckit_marker = true`. Mỗi mục kết thúc sau dòng TOML cuối cùng của nó và các dòng trống ngay sau đó, nên một comment đứng sau mục Spec Kit, chẳng hạn ghi chú phía trên hook của riêng bạn, vẫn ở lại trong file. Nếu sau khi xóa các mục của Spec Kit chỉ còn comment và dòng trống, Spec Kit sẽ xóa `.vibe/hooks.toml`, và các comment đó bị xóa theo. Spec Kit áp dụng cùng quy tắc cho `.codex/config.toml` của Codex.

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `vibe -p <prompt>` và yêu cầu `--output json` để có đầu ra có cấu trúc. Adapter bỏ qua thiết lập `model` của workflow. Thay vào đó, hãy chọn mô hình bằng cấu hình `active_model` của Vibe hoặc `VIBE_ACTIVE_MODEL`.
