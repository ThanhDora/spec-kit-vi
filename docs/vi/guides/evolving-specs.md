<a id="evolving-specs-in-existing-projects"></a>

# Phát triển đặc tả trong dự án có sẵn

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../guides/evolving-specs.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Nếu repository chưa được khởi tạo bằng Spec Kit, hãy bắt đầu với
[Áp dụng Spec Kit vào dự án có sẵn](existing-projects.md). Trang này
trình bày cách duy trì artifact của tính năng sau khi bàn giao và bàn giao các
thay đổi tiếp theo.

Dự án có sẵn cần hai vòng duy trì riêng biệt:

- **Cập nhật file dự án Spec Kit** làm mới các lệnh, script,
  template và file memory dùng chung được quản lý.
- **Phát triển artifact của tính năng** duy trì các artifact `specs/` riêng của repository
  theo quy ước lưu giữ sau bàn giao của nhóm.

Dùng [quy trình nâng cấp](../upgrade.md) khi bạn cần file dự án Spec Kit
mới hơn. Dùng một trong các mô hình lưu giữ artifact bên dưới để quyết định cách duy trì
artifact của tính năng đã hoàn tất khi yêu cầu hoặc hiểu biết rút ra từ việc triển khai
làm thay đổi một dự án có sẵn. Không mô hình nào là bắt buộc hay mặc định.

Để xem định nghĩa khái niệm của các mô hình, xem
[Các mô hình lưu giữ đặc tả](../concepts/spec-persistence.md).

<a id="shared-feature-delivery-loop"></a>

## Vòng bàn giao tính năng chung

Cả ba mô hình lưu giữ đều dùng chung một quy trình bàn giao/xác định hoàn tất:
specify -> plan -> tasks -> implement -> converge. Lặp lại triển khai và
hội tụ cho đến khi tính năng đã thống nhất được hoàn tất.

Với một tính năng mới hoặc một thay đổi về sau cần triển khai:

1. Thể hiện rõ contract dự kiến trong `spec.md`. Dùng `/speckit.specify` để
   tạo thư mục tính năng mới trong `specs/`, hoặc sửa một đặc tả hiện có
   theo quy ước lưu giữ của nhóm.
2. Chạy `/speckit.plan` hoặc sửa `plan.md` để xác định hướng triển khai.
3. Chạy `/speckit.tasks` hoặc sửa `tasks.md` để dẫn xuất phân rã công việc.
   Chạy `/speckit.analyze` trước khi triển khai để phát hiện thiếu sót giữa các artifact.
4. Chạy `/speckit.implement` và review diff kết quả của code và artifact.
5. Chạy `/speckit.converge` để đánh giá phần triển khai so với đặc tả, kế hoạch và
   danh sách tác vụ, dưới sự chi phối của hiến chương. Nếu lệnh bổ sung tác vụ cho các thiếu sót còn lại,
   hãy lặp lại `/speckit.implement` và `/speckit.converge` cho đến khi tính năng đã thống nhất
   được hoàn tất.

Converge chỉ ghi thêm: thao tác ghi duy nhất có thể có là bổ sung tác vụ vào `tasks.md`.
Lệnh không chọn chiến lược lưu giữ và không viết lại artifact để chấp nhận
code thay cho ý định đã được ghi lại.

Phần lõi không có lệnh riêng nào tự động đối soát khác biệt giữa
`spec.md`, `plan.md` và `tasks.md`. `/speckit.analyze` báo cáo các điểm không nhất quán
mà không thay đổi artifact. Nhóm có thể tự đối soát, hoặc một
extension có thể cung cấp lệnh hay hook làm việc đó trong hoặc sau khi bàn giao
theo hành vi đã được mô tả của extension đó. Những thao tác này không làm thay đổi
trách nhiệm của các lệnh lõi.

Các phát hiện có thể nảy sinh trong lúc bàn giao ở bất kỳ mô hình nào. Nếu chúng dẫn tới
một thay đổi ý định đã được thống nhất, hãy thể hiện rõ contract đã sửa trong artifact
và bàn giao dựa trên nó. Việc đối soát có thể diễn ra trong lúc bàn giao, nhưng các
lựa chọn duy trì bên dưới mô tả những gì nhóm lưu giữ sau khi bàn giao; chúng
không thay thế vòng này.

<a id="flow-forward-spec"></a>

## Đặc tả flow-forward

Dùng flow-forward khi mỗi thư mục tính năng đã hoàn tất cần được giữ như một
bản ghi lịch sử.

Sau khi bàn giao, giữ nguyên các artifact đã hoàn tất mà không thay đổi. Với
một tính năng khác hoặc một thay đổi tiếp nối cần triển khai, hãy tạo thư mục
tính năng mới và dùng vòng bàn giao chung ở trên.

Thư mục tính năng trước đó được giữ nguyên để kiểm toán, so sánh hoặc
giải thích dự án đã đi đến trạng thái hiện tại như thế nào. Hãy dùng tên tính năng rõ ràng hoặc
liên kết chéo khi một thư mục mới thay thế hoặc mở rộng công việc trước đó.

## Living spec

Dùng living spec khi `spec.md` là contract và `plan.md` cùng `tasks.md` được
dẫn xuất từ nó.

Sau khi bàn giao, duy trì `spec.md` như contract. Khi hành vi dự kiến
thay đổi, hãy sửa `spec.md` hiện có trước. Sau đó đối soát các artifact phía sau
để chúng khớp với đặc tả đã cập nhật:

1. Bắt đầu từ một working tree sạch hoặc một branch riêng để mọi thay đổi artifact
   đều review được.
2. Cập nhật `spec.md` với contract dự kiến.
3. Đối soát `plan.md` và `tasks.md` trực tiếp hoặc qua một extension theo
   quy ước đã được ghi lại của nhóm.
4. Chạy `/speckit.analyze` để báo cáo những thiếu sót còn lại giữa đặc tả, kế hoạch
   và danh sách tác vụ.

Các bước này duy trì bộ artifact; chúng không bàn giao hành vi đã thay đổi.
Nếu contract đã sửa cần triển khai, hãy dùng vòng bàn giao chung ở trên
dựa trên các artifact thể hiện rõ ý định đó.

Hãy giữ lại các lý do triển khai quan trọng trước khi thay thế artifact dẫn xuất.
Nếu một kế hoạch hay danh sách tác vụ chứa quyết định vẫn còn giá trị, hãy chủ động mang chúng
sang bản mới.

<a id="flow-back-spec"></a>

## Đặc tả flow-back

Dùng flow-back khi các phát hiện được chấp nhận định hướng việc duy trì trên toàn bộ
bộ artifact sau khi bàn giao.

Một phát hiện có thể bắt nguồn từ `spec.md`, `plan.md`, `tasks.md` hoặc
phần triển khai, kể cả trong lúc bàn giao. Khi duy trì sau bàn giao,
nhóm quyết định chấp nhận những phát hiện nào và đưa các artifact về
khớp với hướng đi đã thống nhất:

1. Ghi phát hiện vào artifact gần với phần việc nhất.
2. Quyết định nó làm thay đổi hành vi dự kiến, chiến lược triển khai, phân rã
   tác vụ, hay chỉ thay đổi code.
3. Cập nhật mọi artifact khác giờ không còn khớp với hướng đi đã được chấp nhận.
4. Chạy `/speckit.analyze` để kiểm tra thiếu sót giữa `spec.md`, `plan.md` và
   `tasks.md`.

Phần triển khai cung cấp bằng chứng cho quyết định của nhóm; chấp nhận code
không tự động biến nó thành contract dự kiến. Hãy đối soát artifact
trực tiếp hoặc qua một extension. Analyze và converge không tự động
đối soát toàn bộ artifact, và cũng không cần lệnh sửa đổi lõi nào. Nếu
hướng đi đã thống nhất cần triển khai, hãy dùng vòng bàn giao chung ở trên
dựa trên các artifact thể hiện rõ ý định.

Flow-back linh hoạt, nhưng đòi hỏi kỷ luật. Đừng để một thay đổi ở cấp thấp hơn
trong `tasks.md` hay trong code nếu `spec.md` vẫn nói khác và
đặc tả được kỳ vọng là luôn đáng tin cậy.

<a id="before-updating-spec-kit-project-files"></a>

## Trước khi cập nhật file dự án Spec Kit

Trước khi làm mới file dự án Spec Kit bằng lệnh terminal
`specify init --here --force --integration <your-agent>`, hãy bảo vệ mọi
tài liệu riêng của dự án nằm ngoài `specs/`, đặc biệt là
`.specify/memory/constitution.md` và các file đã tùy chỉnh trong
`.specify/templates/` hoặc `.specify/scripts/`. Thay `<your-agent>` bằng integration
agent lập trình AI mà dự án đích sử dụng.

Thư mục `specs/` của bạn không thuộc gói template, nhưng các file dự án dùng chung
có thể bị ghi đè khi làm mới bằng force.
