# GitHub Copilot

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/copilot.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Thiết lập [GitHub Copilot](https://code.visualstudio.com/) trong editor của bạn, hoặc dùng Copilot CLI. Khóa integration là `copilot`; thiết lập IDE không cần CLI.

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài cùng integration khác (multi-install safe). Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration copilot
```

Với dự án Spec Kit đã có, dùng `specify integration install copilot`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="default-skills-layout"></a>

## Bố cục skills mặc định

Skill được cài tại `.github/skills/speckit-<command>/SKILL.md`. Gọi chúng trong khung chat của agent bằng `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug. Đây là skill của agent, không phải lệnh terminal. Mặc định, skill được sinh ra vừa do người dùng gọi được vừa do mô hình gọi được.

<a id="user-invocable-only-skills"></a>

## Skill chỉ cho người dùng gọi

Để Copilot không tự động nạp các skill lệnh lõi của Spec Kit trong bố cục skills:

```bash
specify init my-project --integration copilot --integration-options="--no-model-invocation"
```

Lệnh này ghi `disable-model-invocation: true` vào các skill lệnh lõi. [Tài liệu agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) của VS Code cho biết thiết lập này chỉ cho phép gọi thủ công qua slash command `/`. Tài liệu skills của GitHub Copilot CLI không liệt kê trường này, nhưng khi kiểm tra thủ công với Copilot CLI 1.0.70, mô hình đã gọi công cụ `skill` cho `speckit-specify` khi không có cờ và không gọi khi có cờ, còn `/speckit-specify` gọi tường minh vẫn chạy. Khi có cờ, mô hình vẫn có thể đọc `SKILL.md` của skill như một file thông thường, nên đây không phải chặn cứng. Không nguồn nào cho biết skill có cờ này có giữ mô tả của nó ngoài ngữ cảnh của mô hình hay không.

- Tùy chọn này không có tác dụng trong bố cục commands, dù được chọn tường minh bằng `--commands` hay được giữ từ bản cài hiện có khi không truyền cờ bố cục: các file `.agent.md` và `.prompt.md` không phải skill và không có cờ nào được ghi.
- Skill của extension vẫn do mô hình gọi được, vì hook bắt buộc của extension dựa vào việc mô hình gọi chúng. Nếu hook bắt buộc của một extension chạy một lệnh lõi (`command:` của nó là một `speckit.<command>` lõi), hãy tắt tùy chọn này: mô hình không thể chạy hook đó khi skill lõi chỉ cho người dùng gọi.
- Tùy chọn này được lưu cùng các tùy chọn khác của integration và được áp dụng lại khi chạy `specify integration upgrade copilot`. Truyền `--integration-options` cho `upgrade` sẽ thay thế toàn bộ tùy chọn đã lưu; `--integration-options=""` xóa hết chúng. Tương tự, chạy lại `specify init` chỉ lưu các tùy chọn được truyền vào lần chạy đó.
- Các skill lệnh lõi mà một preset ghi đè, hoặc thôi ghi đè, sẽ bị đưa về mặc định bởi những lệnh đăng ký lại skill của preset mà không cài lại Copilot: các lệnh cài, gỡ hoặc cập nhật preset (kể cả các lệnh `specify bundle` có mang preset), `specify integration use copilot`, và `specify integration switch copilot` khi Copilot đã được cài nhưng không phải mặc định. Để áp dụng lại tùy chọn, chạy `specify integration upgrade copilot --force` khi Copilot là integration mặc định (cần `--force` vì các lệnh đó sửa file skill đã cài, và nó ghi đè các chỉnh sửa cục bộ trên file do Spec Kit quản lý).

<a id="commands-layout"></a>

## Bố cục commands

Để chọn dùng bố cục commands được hỗ trợ:

```bash
specify init my-project --integration copilot --integration-options="--commands"
```

Lệnh này cài các file `.agent.md` trong `.github/agents/`, các file `.prompt.md` đi kèm trong `.github/prompts/`, và gộp `.vscode/settings.json`. Trong bố cục này, Copilot CLI có thể chọn agent qua `/agents` hoặc gọi trực tiếp agent trong prompt.

Dùng `--integration-options="--skills"` để chọn rõ bố cục skills mặc định khi chuyển đổi một bản cài commands hiện có bằng `specify integration upgrade copilot`. Truyền nó sẽ thay thế toàn bộ tùy chọn đã lưu, nên hãy kèm những tùy chọn bạn muốn giữ: ví dụ, nếu giá trị đó không có `--no-model-invocation`, các skill được chuyển đổi sẽ được ghi ở dạng mô hình gọi được. Xem [quy tắc nâng cấp chung](cli.md#upgrade-an-integration), bao gồm giới hạn về đổi bố cục khi có artifact preset đã đăng ký.

`--skills` và `--commands` loại trừ lẫn nhau. Khi không có cờ bố cục rõ ràng, các bản cài commands được quản lý hiện có giữ nguyên bố cục khi nâng cấp hoặc kích hoạt; bản cài mới mặc định dùng skills.

Bố cục commands chỉ thêm các thiết lập và khóa con VS Code còn thiếu. Các giá trị hiện có giữ nguyên. Nếu file thiết lập hiện có là JSONC hoặc không thể phân tích thành đối tượng JSON, việc gộp sẽ bị bỏ qua kèm cảnh báo và hướng dẫn thủ công. File thiết lập hiện có đã được gộp sẽ được giữ lại khi gỡ cài đặt; file thiết lập mới tạo được theo dõi bằng manifest.

<a id="runtime-events-and-workflow-permissions"></a>

## Runtime event và quyền của workflow

Event gốc dùng `.github/hooks/speckit.json`. `--integration-options="--events false"` tắt trình xử lý event của Spec Kit. Xem [runtime event](cli.md#runtime-events).

Workflow step cần Copilot CLI, tách biệt với thiết lập IDE. Ở chế độ skills, command step truyền `/speckit-<command>` trong prompt. Ở chế độ commands, chúng chọn `--agent speckit.<command>` và truyền đối số của người dùng làm prompt, thay vì coi file agent là slash command.

Điều phối headless mặc định thêm `--yolo`, cho phép công cụ, đường dẫn và URL mà không cần phê duyệt tương tác. Đặt `SPECKIT_COPILOT_ALLOW_ALL_TOOLS=0` để Spec Kit không thêm cờ này. Biến `SPECKIT_ALLOW_ALL_TOOLS` đã ngừng hỗ trợ chỉ được chấp nhận làm phương án dự phòng. `--model` đã cấu hình và `--output-format json` khi được yêu cầu đều được chuyển tiếp.
