# Factory Droid

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/droid.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Factory Droid](https://docs.factory.ai/cli/getting-started/overview) trước khi thiết lập. Khóa integration là `droid`.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration droid
```

Với dự án Spec Kit đã có, dùng `specify integration install droid`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills"></a>

## Skill được cài

Skill được cài tại `.factory/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent, ví dụ `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Mặc định, skill được sinh ra vừa do người dùng gọi được vừa do mô hình gọi được.

<a id="user-invocable-only-skills"></a>

## Skill chỉ cho người dùng gọi

Để Droid không tự động gọi các skill lệnh lõi của Spec Kit:

```bash
specify init my-project --integration droid --integration-options="--no-model-invocation"
```

Lệnh này ghi `disable-model-invocation: true` vào các skill lệnh lõi. Trong Droid 1.0.0, mô hình không còn liệt kê chúng trong các skill có sẵn, nên không tự chạy chúng khi không được yêu cầu, trong khi `/speckit-<command>` và điều phối workflow vẫn chạy được. Đây không phải chặn cứng: một prompt nêu tên skill (ví dụ "use the speckit-specify skill") vẫn cho phép mô hình gọi nó qua công cụ `Skill`. [Tài liệu skills](https://docs.factory.com/cli/configuration/skills) của Factory không mô tả hành vi này.

- Skill của extension vẫn do mô hình gọi được, vì hook bắt buộc của extension dựa vào việc mô hình gọi chúng. Nếu hook bắt buộc của một extension chạy một lệnh lõi (`command:` của nó là một `speckit.<command>` lõi), hãy tắt tùy chọn này: mô hình không thể chạy hook đó khi skill lõi chỉ cho người dùng gọi.
- Tùy chọn này được lưu cùng các tùy chọn khác của integration và được áp dụng lại khi chạy `specify integration upgrade droid`. Truyền `--integration-options` cho `upgrade` sẽ thay thế toàn bộ tùy chọn đã lưu; `--integration-options=""` xóa hết chúng. Tương tự, chạy lại `specify init` chỉ lưu các tùy chọn được truyền vào lần chạy đó.
- Các skill lệnh lõi mà một preset ghi đè, hoặc thôi ghi đè, sẽ bị đưa về mặc định bởi những lệnh đăng ký lại skill của preset mà không cài lại Droid: các lệnh cài, gỡ hoặc cập nhật preset (kể cả các lệnh `specify bundle` có mang preset), `specify integration use droid`, và `specify integration switch droid` khi Droid đã được cài nhưng không phải mặc định. Để áp dụng lại tùy chọn, chạy `specify integration upgrade droid --force` khi Droid là integration mặc định (cần `--force` vì các lệnh đó sửa file skill đã cài, và nó ghi đè các chỉnh sửa cục bộ trên file do Spec Kit quản lý).

<a id="workflow-dispatch"></a>

## Điều phối workflow

Workflow step dùng `droid exec <prompt>`, chuyển tiếp `--model` và yêu cầu `--output-format json` khi phù hợp. Spec Kit không thêm cờ bỏ qua quyền. Người vận hành có thể cấu hình rõ cờ quyền qua `SPECKIT_INTEGRATION_DROID_EXTRA_ARGS`; các đối số đó đứng sau cờ mô hình/đầu ra của Spec Kit và có thể ghi đè chúng khi phân tích cờ trùng lặp. Tùy chọn thiết lập riêng duy nhất của integration này là `--no-model-invocation`.
