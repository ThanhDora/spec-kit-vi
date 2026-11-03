<a id="community-friends"></a>

# Dự án bạn bè trong cộng đồng

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../community/friends.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

> [!NOTE]
> Các dự án cộng đồng được liệt kê ở đây được tạo và duy trì độc lập bởi tác giả của chúng. Trừ khi được đánh dấu rõ là **dự án GitHub chính thức (first-party)**, chúng **không được GitHub review, bảo chứng hay hỗ trợ**. Hãy review mã nguồn của chúng trước khi cài và tự cân nhắc khi sử dụng.

Các dự án cộng đồng mở rộng, trực quan hóa hoặc xây dựng trên nền Spec Kit:

- **[cc-spex](https://github.com/rhuss/cc-spex)** — Plugin Claude Code bổ sung các trait có thể kết hợp trên nền Spec Kit với cổng chất lượng dựa trên [Superpowers](https://github.com/obra/superpowers), review spec/code, cô lập bằng git worktree và triển khai song song qua đội agent.

- **[VS Code Spec Kit Assistant](https://marketplace.visualstudio.com/items?itemName=rfsales.speckit-assistant)** — Extension VS Code cung cấp bộ điều phối trực quan cho toàn bộ workflow SDD (constitution → specification → planning → tasks → implementation) với hiển thị trạng thái giai đoạn, checklist task tương tác, trực quan hóa DAG, và hỗ trợ backend Claude, Gemini, GitHub Copilot và OpenAI. Yêu cầu CLI `specify` có trong PATH.

- **[SpecKit Assistant](https://www.npmjs.com/package/speckit-assistant)** — Bộ điều phối trực quan cho Phát triển hướng đặc tả (SDD). Nó kết nối đặc tả, kế hoạch và checklist task cục bộ của bạn với agent AI (Claude, Gemini, GitHub Copilot). Không cần cài toàn cục — chỉ cần chạy qua `npx speckit-assistant`.

- **[SpecKit Companion](https://marketplace.visualstudio.com/items?itemName=alfredoperez.speckit-companion)** — Extension VS Code mang giao diện đồ họa trực quan cho Spec Kit. Duyệt đặc tả trong trình xem markdown phong phú với tham chiếu file bấm được, tạo đặc tả kèm ảnh đính kèm, bình luận và tinh chỉnh từng bước ngay tại chỗ (review kiểu GitHub), theo dõi tiến độ qua workflow SDD bằng thanh bước giai đoạn trực quan, và quản lý các tài liệu định hướng như constitution và template.

- **[cc-spec-kit](https://github.com/speckit-community/cc-spec-kit)** — Plugin do cộng đồng duy trì cho Claude Code và GitHub Copilot CLI, cài skill Spec Kit qua plugin marketplace.

- **[spectatui](https://github.com/tinesoft/spectatui)** — Dashboard giao diện terminal (TUI) cho Spec Kit, cho phép theo dõi feature, quản lý đặc tả, integration, preset, workflow và extension, và giám sát workflow của agent AI. Gắn vào phiên AI hiện có hoặc khởi chạy phiên mới từ terminal. Hỗ trợ bàn phím và chuột. Hỗ trợ giao diện sáng/tối. Tùy biến được và chú trọng hiệu năng. Yêu cầu CLI `specify` có trong PATH.

- **[spec-kit-copilot](https://github.com/github/spec-kit-copilot)** — *Dự án GitHub chính thức (first-party).* **Skills plugin** cho GitHub Copilot, đưa CLI `specify` của Spec Kit tới agent Copilot trong cả Copilot CLI lẫn ứng dụng GitHub Copilot. Nó cung cấp một skill tập trung cho mỗi nhóm lệnh `specify` — setup, init, check, extensions, presets, bundles, workflows, workflow steps và self-upgrade — để bạn điều hướng và điều khiển toàn bộ hệ sinh thái Spec Kit bằng ngôn ngữ tự nhiên, để Copilot quyết định khi nào và cách chạy đúng các lệnh `specify` thay bạn.

- **[Spec Kit Workflow Cockpit](https://github.com/markuswondrak/spec-kit-workflow-cockpit)** — Bảng điều khiển terminal để chạy workflow Spec Kit cục bộ. Nó thay luồng CLI rời rạc bằng một góc nhìn trực tiếp duy nhất: thấy toàn bộ workflow trong nháy mắt, theo dõi tiến độ từng node, đọc và sửa tài liệu feature tại các cổng review của con người mà không rời terminal, và đưa ra quyết định tại gate từ các lựa chọn được trình bày rõ ràng kèm xác nhận. Nó cũng cung cấp skill `cockpit-run-context` kết nối phiên lập trình tương tác của bạn trực tiếp với lần chạy workflow hiện tại.

- **[Specstride](https://specstride.ai/)** — Bộ điều phối triển khai độc lập, dùng `tasks.md` của một feature Spec Kit và lấy `spec.md`, `plan.md` cùng các hợp đồng làm ngữ cảnh chỉ đọc. Nó chạy một agent lập trình (Claude Code, Codex hoặc model cục bộ) qua từng giai đoạn task một. Mỗi giai đoạn chỉ tiến lên khi một LLM phản biện riêng phê duyệt bằng chứng của nó theo tiêu chí chấp nhận và code. Giai đoạn bị kẹt được giao cho một bộ chẩn đoán và thử lại với phạm vi thu hẹp. Một vòng lặp tùy chọn học thiết lập theo giai đoạn từ telemetry của lần chạy và hoàn tác mọi thay đổi làm kết quả tệ hơn.

- **[Raaghu Spec Kit](https://marketplace.visualstudio.com/items?itemName=Waiin.raaghu-speckit)** — Raaghu Spec Kit đưa phát triển hướng đặc tả vào Azure DevOps. PM, BA và QA có thể tạo, review và quản lý đặc tả có cấu trúc, kế hoạch bàn giao, phân rã task và checklist chất lượng — rồi tạo và tinh chỉnh work item trên Azure Boards — tất cả từ một workspace AI có hướng dẫn ngay trong dự án. Hoạt động với Azure DevOps Services và Azure DevOps Server (on-premises).

- **[Entalpa](https://entalpa.com/spec-kit)** — Ứng dụng web được host, đọc `specs/<feature>/spec.md` và `tasks.md` từ một repository GitHub công khai, hoặc từ repository riêng tư được tải lên dạng zip hay thư mục, và gộp các feature thành một backlog hiện hành: user story, các yêu cầu `FR-`/`SC-` liên kết với chúng kèm trạng thái từ `tasks.md`, và phần làm rõ dưới dạng câu hỏi đã được trả lời. Feature sau sẽ sửa story mà nó thay đổi thay vì thêm bản sao. Xem kết quả không cần tài khoản; lưu hoặc sửa thì cần. Bản tải lên được đọc trong trình duyệt, và chỉ các file đặc tả đó, kèm đường dẫn và tên zip hoặc thư mục, được gửi đi; dù theo cách nào, việc gộp cũng gửi đặc tả tới các nhà cung cấp AI bên thứ ba. Xuất ngược lại thành một feature trong `specs/`.
