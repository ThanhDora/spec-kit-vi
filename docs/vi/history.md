<a id="history"></a>

# Lịch sử

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../history.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Spec Kit khởi đầu là một bộ công cụ giúp đặc tả trở thành điểm xuất phát của
quá trình phát triển có AI hỗ trợ. Ngay từ
[lần check-in đầy đủ đầu tiên](https://github.com/github/spec-kit/commit/28fdfaa86973d4402eecd89ba6c87d31e1edae03),
dự án đã mô tả ba cách áp dụng Phát triển hướng đặc tả:

- **Phát triển từ 0 đến 1 ("Greenfield")** sinh ra một hệ thống mới từ
  yêu cầu.
- **Khám phá sáng tạo** so sánh các phần triển khai song song, các lựa chọn công nghệ
  và thiết kế trải nghiệm.
- **Cải tiến lặp ("Brownfield")** bổ sung tính năng và hiện đại hóa
  các hệ thống có sẵn.

Cả ba đều đi từ các artifact lập kế hoạch bền vững sang triển khai:

**Specify → Plan → Tasks → Implement**

Các con đường phát triển và trình tự cốt lõi đó vẫn còn nguyên, nhưng dự án đã
lớn lên thành một nền tảng mở rộng được cho agent lập trình, các quy trình bàn giao
phần mềm và những dạng công việc có cấu trúc khác.

<a id="project-stewardship"></a>

## Quản lý dự án

Lịch sử Spec Kit gồm hai giai đoạn quản lý riêng biệt. Ghi lại chúng
ở đây giúp lưu giữ bức tranh đương thời về đội ngũ dẫn dắt dự án mà không
quy toàn bộ công sức về cho một người duy nhất.

<a id="founding-stewardship-august-2025january-2026"></a>

### Giai đoạn sáng lập: tháng 8/2025–tháng 1/2026

[Den Delimarsky](https://github.com/localden) và
[John Lam](https://github.com/jflam) đã hình thành ý tưởng Spec Kit và tạo cho dự án
hình hài đầu tiên. Den là tác giả của
[commit đầu tiên](https://github.com/github/spec-kit/commit/fa2736371e077f55c4fe145fea186bab2561386d) vào
ngày 21/08/2025 và dẫn dắt repository trong những tháng đầu.

Giai đoạn sáng lập đó đã định hình những gì người dùng vẫn nhận ra đến nay: Specify
CLI, phần khung riêng cho từng agent lập trình, hiến chương dự án, và quy trình
đặc tả → kế hoạch → tác vụ → triển khai. Giai đoạn này cũng xác định SDD là
phương pháp hữu ích cho phát triển greenfield, khám phá song song và cải tiến
brownfield, thay vì gắn phương pháp với một agent hay một tình huống phát triển
duy nhất.

<a id="community-stewardship-january-2026present"></a>

### Giai đoạn cộng đồng quản lý: tháng 1/2026–nay

[Manfred Riem](https://github.com/mnriem) đảm nhận vai trò maintainer chính từ
ngày 22/01/2026. Sự chuyển giao được thể hiện công khai khi
[mục `CODEOWNERS`](https://github.com/github/spec-kit/commit/3040d33c31d8a26d50f91aec5d62d1cecac3298c) toàn cục của repository
được đổi thành `@mnriem` vào ngày 23/02.

Trong giai đoạn này, trọng tâm của nhóm maintainer chuyển từ việc xây dựng một
mô hình có thể kết hợp sang việc dùng mô hình đó để phát hành các quy trình chính thức hoàn chỉnh. Với cộng đồng,
sự chuyển dịch này không diễn ra tuần tự: hệ thống extension dạng module ban đầu là một
đóng góp của cộng đồng, và những người đóng góp đã áp dụng và mở rộng từng thành phần cơ bản
ngay khi nó xuất hiện.

Các mốc thời gian và vai trò này cũng được ghi lại trong
[bài nhìn lại sáu tháng](https://www.manorrock.com/blog/2026/07/22/six_months_leading_spec_kit.html)
và
[bài viết nhân dịp tròn một năm](https://www.manorrock.com/blog/2026/08/21/spec_kit_turns_one.html)
của maintainer chính, và nhất quán với lịch sử commit và quyền sở hữu của repository.

<a id="milestones"></a>

## Các cột mốc

<a id="august-2025-the-foundation"></a>

### Tháng 8/2025: Nền móng

Lịch sử repository bắt đầu vào ngày 21/08/2025. Các bản phát hành đầu tiên đã xác lập
Specify CLI, các template dùng lại được và các con đường cốt lõi của Phát triển hướng đặc tả.
Việc hỗ trợ nhiều agent lập trình thông qua phần khung riêng cho từng agent, được cấu hình
tập trung, đã có từ ngày đầu, giúp quy trình độc lập với bất kỳ mô hình hay
công cụ nào.

<a id="februaryapril-2026-building-the-primitives"></a>

### Tháng 2–4/2026: Xây dựng các thành phần cơ bản

Hệ thống extension dạng module xuất hiện vào tháng 2 nhờ đóng góp của cộng đồng
từ Michal Bachorik, cho phép bổ sung khả năng mà không phải mở rộng
quy trình lõi. Tháng 3 mang đến preset dạng plugin, giúp template và
lệnh có thể được thay thế hoặc kết hợp mà vẫn giữ nguyên trải nghiệm CLI.

Phần khung cho agent từ thời sáng lập được viết lại thành một kiến trúc
integration dựa trên registry. Các tài nguyên lõi cũng được nhúng vào package Python,
giúp khởi tạo ổn định khi offline và trong môi trường air-gapped.

Workflow engine ra mắt vào tháng 4 với khả năng tự động hóa được phân phối qua catalog và các loại
workflow step có sẵn. Workflow có thể điều phối các step dùng lại được thay vì
bắt người dùng tự gọi từng lệnh. Tiếp theo là một catalog integration,
giúp việc hỗ trợ agent lập trình trở nên dễ tìm và có thể phân phối độc lập.

Mô hình có thể kết hợp này dần được mô tả qua năm thành phần cơ bản:

- **Integration** kết nối Spec Kit với agent lập trình.
- **Extension** bổ sung khả năng, lệnh, template, script và hook.
- **Preset** tùy chỉnh hoặc thay thế hành vi.
- **Workflow** tự động hóa các quy trình nhiều bước.
- **Workflow step** cung cấp các đơn vị hành vi workflow dùng lại được.

Trọng tâm trong những tháng đầu này là tạo ra bộ máy dùng lại được:
làm cho quy trình có thể cấu hình, phân phối và tự động hóa trước khi bổ sung
thêm các quy trình chính thức. Cộng đồng không chờ đến khi toàn bộ
mô hình hoàn chỉnh; họ nhanh chóng dùng các bề mặt extension và preset mới
để phát hành các khả năng và biến thể quy trình của riêng mình.

<a id="junejuly-2026-composing-and-applying-the-primitives"></a>

### Tháng 6–7/2026: Kết hợp và ứng dụng các thành phần cơ bản

Với nhóm lõi, tháng 6 đánh dấu bước chuyển từ chủ yếu xây dựng thành phần cơ bản sang sử dụng
chúng. Một catalog workflow step giúp cộng đồng cài được các loại step tùy chỉnh,
mở rộng một thành phần cơ bản đã ra mắt cùng workflow engine vào tháng 4.
Sau đó bundle cho phép đóng gói extension, preset, workflow và
step thành một thiết lập thống nhất cho một vai trò hoặc một nhóm, có thể nhắm tới một
integration cụ thể.

Catalog trở thành cầu nối giữa các thành phần cơ bản và cộng đồng. Các tác giả
cộng đồng xây dựng extension, preset, integration, workflow, loại step và
bundle; nhóm maintainer kiểm tra metadata của bài gửi và đưa các mục được chấp nhận
vào catalog cộng đồng để người dùng có thể tìm và cài đặt. Được liệt kê trong
catalog giúp thành phần được nhìn thấy, nhưng không có nghĩa code của nó đã được
kiểm định hay bảo chứng.

Đồng thời, các maintainer lõi bắt đầu dùng mô hình này để bổ sung hai quy trình chính thức
bên cạnh việc bàn giao tính năng:

- Ngày 05/06, phiên bản 0.9.5 giới thiệu
  [extension `bug`](https://github.com/github/spec-kit/commit/60302fefec541a68fcac6f0428a95ba35f2acadf) đi kèm, chỉ chạy khi bật.
  Quy trình assess → fix → test của nó giữ việc chẩn đoán, khắc phục và
  xác minh lỗi tách biệt và được ghi lại đầy đủ.
- Ngày 17/07, phiên bản 0.13.0 giới thiệu
  [extension `assess`](https://github.com/github/spec-kit/commit/208d38695fc88d8eaec7855c96e5098a852927cf) đi kèm, chỉ chạy khi bật.
  Quy trình intake → research → define → shape → decide của nó đánh giá một ý tưởng
  trước khi ý tưởng đó đi vào SDD.

Kênh phân phối cũng được mở rộng: quy trình phát hành bổ sung việc phát hành lên PyPI, và
Python trở thành loại script dự án được hỗ trợ bên cạnh Bash và PowerShell. Những
thay đổi này giúp việc cài đặt và sử dụng đa nền tảng đơn giản hơn mà vẫn giữ
hỗ trợ cho môi trường offline và doanh nghiệp.

<a id="august-2026-first-anniversary"></a>

### Tháng 8/2026: Tròn một năm

Spec Kit tròn một tuổi và phát hành phiên bản 1.0.0 vào ngày 21/08/2026. Đến lúc đó,
năm thành phần cơ bản — integration, extension, preset, workflow và workflow
step — đã tạo thành một mô hình thống nhất. Bundle kết hợp extension, preset,
workflow và step quanh một integration được chọn. Một lần làm mới README giúp các quy trình
SDD, sửa lỗi và đánh giá ý tưởng sẵn có dễ được tìm thấy hơn
qua các hướng dẫn nhanh riêng.

Phiên bản 1.0.0 không tạo ra hay đóng băng mô hình đó; nó chỉ gắn một con số tròn cho trạng thái
đang phát triển của dự án. Khi đó, tài liệu ghi nhận 38 integration cho agent lập trình,
157 extension cộng đồng, 33 preset và hơn 270 người đóng góp. Spec
Kit tiếp tục đề cao khả năng thích ứng: quy trình, integration và quy ước
có thể thay đổi trong khi agent giúp các dự án áp dụng những thay đổi đó.

[Bản phát hành 1.0.0](https://github.com/github/spec-kit/releases/tag/v1.0.0)
đánh dấu một năm làm việc chứ không phải lời hứa rằng dự án đã hoàn thành hay hình hài của nó
đã bị đóng băng. Trong bài viết cá nhân nhân dịp tròn một năm của maintainer chính,
[*Spec Kit Turns One — and Ships 1.0.0*](https://www.manorrock.com/blog/2026/08/21/spec_kit_turns_one.html),
1.0.0 **giờ chỉ là một con số**: khi agent giúp việc thích ứng với thay đổi đỡ tốn kém hơn,
giá trị dịch chuyển từ sự ổn định sang khả năng thích ứng.

Dịp kỷ niệm cũng ghi nhận tất cả những ai đã dùng Spec Kit, đặt câu hỏi với các
giả định của nó, báo cáo vấn đề, đóng góp code hoặc tài liệu, tạo
extension hoặc preset, chia sẻ ý tưởng, hay giúp ai đó bắt đầu. Cột mốc này
thuộc về cộng đồng đã đưa dự án vượt qua năm đầu tiên và
tiếp tục định hình nó.

<a id="enduring-themes"></a>

## Những chủ đề xuyên suốt

Một số chủ đề kết nối các giai đoạn quản lý và quá trình phát triển kỹ thuật
của dự án:

- **Ý định đi trước triển khai.** Đặc tả ghi lại thứ cần được
  xây dựng trước khi các quyết định kỹ thuật chi phối công việc.
- **Artifact cần bền vững.** Đặc tả, kế hoạch và danh sách tác vụ vẫn hữu ích sau
  một prompt hay một phiên làm việc với agent.
- **Quy trình cần độc lập với agent.** Nhóm có thể đổi agent lập trình
  mà không phải từ bỏ phương pháp phát triển của mình.
- **Phương pháp cần thích ứng với công việc.** Các con đường phát triển ban đầu đã phát triển
  thành một mô hình có thể kết hợp chính thức mà nhóm có thể sửa đổi, tự động hóa hoặc thay thế.
- **Cộng đồng định hình bộ công cụ.** Đóng góp của cộng đồng đã ảnh hưởng tới
  cả hạ tầng của dự án lẫn hệ sinh thái được xây dựng trên đó.

<a id="release-history"></a>

## Lịch sử phát hành

Trang này ghi lại quá trình phát triển tổng thể của dự án, không phải mọi tính năng hay
thay đổi phá vỡ tương thích. Để xem chi tiết từng bản phát hành, xem
[changelog](https://github.com/github/spec-kit/blob/main/CHANGELOG.md) và
[GitHub Releases](https://github.com/github/spec-kit/releases).
