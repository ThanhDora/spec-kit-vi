<a id="integrations"></a>

# Integration

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/index.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Integration kết nối Spec Kit với agent lập trình AI của bạn qua lệnh, skill hoặc recipe. Dùng [none](none.md) để có phần khung dùng chung mà không gắn với agent nào. Chọn một integration bên dưới để xem điều kiện tiên quyết, cách thiết lập, cú pháp gọi và các tùy chọn hoặc giới hạn riêng.

<a id="set-up-your-agent"></a>

## Thiết lập agent của bạn

Xem [hướng dẫn cài đặt](../installation.md) để biết điều kiện tiên quyết và cách cài CLI, và [bắt đầu nhanh với SDD](../quickstart.md) cho quy trình đầu tiên của bạn.

Với dự án mới:

```bash
specify init my-project --integration <key>
```

Gọi các lệnh quy trình bên trong agent lập trình, không phải trong terminal. Tài liệu thường dùng ký pháp `/speckit.*`, nhưng agent của bạn có thể dùng skill có gạch nối, skill `$` hoặc một dạng gốc khác. Xem trang của integration bạn dùng và [bảng so sánh cách gọi lệnh](cli.md#command-invocation).

<a id="adding-another-agent"></a>

## Thêm agent khác

Trong dự án đã khởi tạo, dùng [`specify integration install <key>`](cli.md#install-an-integration). Xem hướng dẫn của agent để biết trạng thái an toàn khi cài nhiều integration, và làm theo [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

Cài thêm integration không làm thay đổi mặc định. Dùng [`specify integration use <key>`](cli.md#use-an-installed-integration) để kích hoạt nó.

<a id="removing-an-agent"></a>

## Gỡ một agent

Dùng [`specify integration uninstall <key>`](cli.md#uninstall-an-integration) để gỡ integration Spec Kit của một agent, chứ không phải gỡ chính ứng dụng agent. Xem tài liệu tham khảo về gỡ cài đặt để biết cách xử lý file đã sửa và các ngoại lệ khi dọn dẹp.

Để thay thế một integration, dùng [`specify integration switch <key>`](cli.md#switch-to-a-different-integration).

<a id="working-in-a-team"></a>

## Làm việc theo nhóm

Nhóm dùng nhiều agent khác nhau có thể bắt đầu từ một dự án trung lập với agent:

```bash
specify init my-project --integration none
```

Mỗi lập trình viên chuyển sang agent mình chọn trong bản checkout cục bộ:

```bash
specify integration switch <key>
```

Sau khi phát triển, chuyển lại trước khi stage commit:

```bash
specify integration switch none
```

> [!IMPORTANT]
> Đừng sửa tay các lệnh hoặc skill của agent do Spec Kit sinh ra. Hãy duy trì tùy biến trong các [preset](../reference/presets.md) đã được review hoặc [ghi đè cục bộ trong dự án](../guides/customization.md#project-local-overrides-and-resolution). Trước khi commit, dùng [`specify integration status`](cli.md#report-integration-status) để xác nhận `none` là integration duy nhất đã cài và là mặc định. Review Git diff và các file agent còn giữ lại.

Nhóm có thể thêm kiểm tra CI cho baseline đã commit và kiểm tra pre-commit tùy chọn cho các file đã stage.

<a id="choose-an-integration"></a>

## Chọn integration

Dùng đúng khóa hiển thị bên dưới với `--integration <key>`. Integration dựa trên CLI yêu cầu đã cài CLI của agent; integration dựa trên IDE chạy qua cửa sổ chat của agent trong IDE. Mỗi trang đều liên kết tới tài liệu cài đặt của agent.

| Integration | Khóa |
| --- | --- |
| [Alquimia AI](alquimia.md) | `alquimia` |
| [Amp](amp.md) | `amp` |
| [Antigravity](agy.md) | `agy` |
| [Auggie CLI](auggie.md) | `auggie` |
| [Claude Code](claude.md) | `claude` |
| [Cline](cline.md) | `cline` |
| [CodeBuddy CLI](codebuddy.md) | `codebuddy` |
| [Codex CLI](codex.md) | `codex` |
| [Command Code](command-code.md) | `command-code` |
| [Cursor](cursor-agent.md) | `cursor-agent` |
| [DeepSeek Harness](dsh.md) | `dsh` |
| [Devin for Terminal](devin.md) | `devin` |
| [Docker Agent](docker-agent.md) | `docker-agent` |
| [Factory Droid](droid.md) | `droid` |
| [Firebender](firebender.md) | `firebender` |
| [Forge](forge.md) | `forge` |
| [Gemini CLI](gemini.md) | `gemini` |
| [GitHub Copilot](copilot.md) | `copilot` |
| [Goose](goose.md) | `goose` |
| [Grok Build](grok.md) | `grok` |
| [Hermes](hermes.md) | `hermes` |
| [IBM Bob](bob.md) | `bob` |
| [Junie](junie.md) | `junie` |
| [Kilo Code](kilocode.md) | `kilocode` |
| [Kimi Code](kimi.md) | `kimi` |
| [Kiro CLI](kiro-cli.md) | `kiro-cli` |
| [Lingma](lingma.md) | `lingma` |
| [MiniMax Code](mcode.md) | `mcode` |
| [Mistral Vibe](vibe.md) | `vibe` |
| [Muse Code](muse.md) | `muse` |
| [None: chỉ phần khung dùng chung](none.md) | `none` |
| [Oh My Pi](omp.md) | `omp` |
| [opencode](opencode.md) | `opencode` |
| [Pi Coding Agent](pi.md) | `pi` |
| [Qoder CLI](qodercli.md) | `qodercli` |
| [Qwen Code](qwen.md) | `qwen` |
| [RovoDev](rovodev.md) | `rovodev` |
| [SHAI (OVHcloud)](shai.md) | `shai` |
| [Tabnine CLI](tabnine.md) | `tabnine` |
| [Trae](trae.md) | `trae` |
| [ZCode](zcode.md) | `zcode` |
| [Zed](zed.md) | `zed` |
| [Generic: dùng agent của riêng bạn](generic.md) | `generic` |

<a id="shared-management-and-external-integrations"></a>

## Quản lý chung và integration bên ngoài

[Tài liệu tham khảo CLI integration](cli.md) mô tả hành vi dùng chung về cài đặt, nâng cấp, gỡ bỏ, trạng thái, catalog và chọn mặc định. Các quy tắc này áp dụng cho mọi integration thay vì lặp lại trên từng trang. Từng hướng dẫn cũng cho biết có hỗ trợ điều phối workflow qua CLI hay không; thiết lập IDE không cần CLI không có nghĩa là workflow step chạy được khi không có CLI.

Với agent không có trong danh sách, dùng [integration generic](generic.md) hoặc [tìm adapter bên ngoài](cli.md#search-available-integrations). Hãy review code adapter bên ngoài trước khi cho phép thực thi. Việc xuất hiện trong catalog không phải là sự bảo chứng về bảo mật; catalog cộng đồng mặc định chỉ dùng để tìm kiếm. Xem [adapter bên ngoài cài từ catalog](cli.md#catalog-installed-external-adapters) để biết yêu cầu về độ tin cậy và cài đặt.

[Tài liệu tham khảo catalog](catalog.md) mô tả metadata của file mô tả và catalog. Xem [đóng góp integration](contributing.md) để phát triển integration có sẵn hoặc phát hành adapter bên ngoài.
