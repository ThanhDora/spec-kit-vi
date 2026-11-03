<a id="spec-persistence-models"></a>

# Các mô hình lưu giữ đặc tả

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../concepts/spec-persistence.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Spec Kit chủ ý để nhóm tự quyết định điều gì xảy ra với `spec.md`,
`plan.md` và `tasks.md` sau khi một tính năng được bàn giao. Bộ công cụ cung cấp cho bạn một
quy trình lặp lại được, nhưng không áp đặt một chiến lược duy trì artifact cụ thể nào.

Trang này đặt tên cho ba mô hình phổ biến để nhóm có thể đưa ra lựa chọn một cách rõ ràng.
Không mô hình nào là mặc định, và Spec Kit cũng không bắt buộc mô hình nào.

<a id="shared-delivery-separate-persistence"></a>

## Chung quy trình bàn giao, khác cách lưu giữ

Cả ba mô hình đều dùng cùng một quy trình bàn giao tính năng:
specify -> plan -> tasks -> implement -> converge. Lặp lại implement và
converge cho đến khi tính năng đã thống nhất được hoàn tất.

Converge đánh giá phần triển khai so với đặc tả, kế hoạch và danh sách tác vụ của tính năng,
dưới sự chi phối của hiến chương. Lệnh này chỉ ghi thêm: thao tác ghi duy nhất có thể có
là bổ sung phần việc còn lại vào `tasks.md`. Nó không chọn mô hình lưu giữ,
không viết lại ý định cho khớp với code, và không coi việc code được duyệt là đồng thuận với
ý định đã được ghi lại.

Quy trình lõi không có lệnh riêng nào tự động đối soát
khác biệt giữa `spec.md`, `plan.md` và `tasks.md`. Analyze báo cáo
các điểm không nhất quán mà không sửa artifact, còn converge chỉ bổ sung phần việc
còn lại vào `tasks.md`. Nhóm có thể tự đối soát các artifact, và extension có thể
cung cấp lệnh hoặc hook riêng để điều phối việc đối soát trong hoặc
sau khi bàn giao. Hành vi của extension không làm thay đổi trách nhiệm của
các lệnh lõi.

Lưu giữ là lựa chọn của nhóm về cách duy trì artifact **sau khi
bàn giao**, không phải một cách khác để bàn giao hay xác định mức độ hoàn tất.
Các phát hiện có thể xuất hiện trong lúc triển khai, nhưng thời điểm của chúng không quyết định
mô hình lưu giữ. Việc đối soát cũng có thể diễn ra trong lúc bàn giao mà không
trở thành một phần của quy trình lõi hay chiến lược lưu giữ. Nếu nhóm
đồng ý thay đổi contract dự kiến, hãy thể hiện rõ ý định đó trong
artifact và bàn giao dựa trên nó.

Một thay đổi về sau cần triển khai vẫn đi qua quy trình bàn giao chung
và hội tụ dựa trên các artifact thể hiện rõ ý định, dù đó là
artifact mới hay đã được sửa đổi. Xem
[Phát triển đặc tả trong dự án có sẵn](../guides/evolving-specs.md) để có hướng dẫn
thực tế.

<a id="two-separate-questions"></a>

## Hai câu hỏi riêng biệt

Phát triển hướng đặc tả có một câu hỏi về thời gian: đặc tả nên có giá trị
trong bao lâu? Một
[bài tổng quan về công cụ SDD](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
chia vòng đời đó thành ba cấp:

- **Spec-first** (đặc tả trước): viết đặc tả trước khi code, rồi cho phép bỏ nó đi.
- **Spec-anchored** (neo theo đặc tả): giữ đặc tả sau khi triển khai và dùng nó cho các thay đổi
  về sau.
- **Spec-as-source** (đặc tả là mã nguồn): coi đặc tả là nguồn duy nhất do con người chỉnh sửa và
  sinh lại các artifact triển khai từ đó.

Spec Kit còn đặt ra câu hỏi thứ hai: điều gì xảy ra với bộ artifact khi
yêu cầu thay đổi sau khi bàn giao? Các mô hình bên dưới mô tả chiến lược duy trì
đó.

<a id="flow-back-spec"></a>

## Đặc tả flow-back

Dùng flow-back (chảy ngược) khi `spec.md`, `plan.md`, `tasks.md` và phần triển khai
đều được phép tác động qua lại lẫn nhau.

Sau khi bàn giao, các phát hiện được chấp nhận có thể dẫn tới việc sửa đổi bất kỳ
artifact nào. Nhóm quyết định những phát hiện đó có ý nghĩa gì với hành vi dự kiến,
hướng tiếp cận kỹ thuật hay cách phân rã tác vụ. Nhóm có thể tự đối soát `spec.md`,
`plan.md` và `tasks.md`, hoặc dùng một extension có hành vi được mô tả là
làm việc đó. Phần triển khai là bằng chứng cho cuộc thảo luận ấy, không phải nguồn
ý định thay thế.

Đây là một quy ước duy trì do nhóm sở hữu, không phải yêu cầu phải có lệnh sửa đổi
lõi mới hay vai trò viết lại artifact cho analyze hoặc converge.
Việc đối soát do extension cung cấp vẫn là hành vi của extension, dù chạy
trong hay sau khi bàn giao. Nếu việc đối soát phát hiện ra phần việc triển khai,
hãy bàn giao thay đổi đó qua quy trình chung dựa trên các artifact thể hiện rõ
ý định.

Flow-back phù hợp khi:

- nhóm đủ nhỏ để nhận ra và đối soát độ lệch nhanh chóng
- các phát hiện khi triển khai được dự đoán sẽ định hình lại kế hoạch ban đầu
- tốc độ quan trọng hơn việc lưu từng quyết định trung gian thành lịch sử
  bất biến

Rủi ro chính là lệch nhau một cách âm thầm. Nếu nhóm thay đổi các artifact cấp thấp hơn
mà không phản ánh quyết định ngược lại vào `spec.md`, những người đóng góp sau này có thể
không biết nên tin artifact nào.

<a id="flow-forward-spec"></a>

## Đặc tả flow-forward

Dùng flow-forward (chảy xuôi) khi mỗi thư mục tính năng cần được giữ như một bản ghi lịch sử.

Trong mô hình này, các artifact đã hoàn tất được coi là bất biến. Khi yêu cầu
thay đổi, nhóm tạo một thư mục tính năng mới thay vì sửa
`spec.md`, `plan.md` hay `tasks.md` hiện có. Thư mục cũ vẫn hữu ích
cho việc kiểm toán, so sánh hoặc giải thích dự án đã đi đến trạng thái hiện tại như thế nào.

Flow-forward phù hợp khi:

- khả năng kiểm toán và truy vết là quan trọng
- các tính năng được giới hạn phạm vi rõ ràng và hiếm khi được sửa lại tại chỗ
- nhóm muốn có một chuỗi thay đổi yêu cầu rõ ràng theo thời gian

Đánh đổi chính là sự trùng lặp. Các quyết định liên quan có thể nằm rải rác ở
nhiều thư mục tính năng, nên nhóm cần thói quen đặt tên, liên kết hoặc review
giúp dễ lần theo nguồn gốc.

## Living spec

Dùng living spec (đặc tả sống) khi `spec.md` là contract và các artifact khác được
dẫn xuất từ nó.

Sau khi bàn giao, nhóm duy trì `spec.md` như một contract, cập nhật nó trước tiên khi
hành vi dự kiến thay đổi, rồi sinh lại hoặc sửa `plan.md` và
`tasks.md` từ nguồn đó. Kế hoạch và danh sách tác vụ vẫn có giá trị, nhưng chúng
được coi là các bản dẫn xuất dùng xong có thể bỏ, chứ không phải nguồn sự thật lâu dài.

Living spec phù hợp khi:

- contract của sản phẩm đủ ổn định để làm chủ quy trình
- nhóm sẵn sàng sinh lại các artifact dẫn xuất sau khi đặc tả thay đổi
- tính nhất quán giữa yêu cầu và phần triển khai quan trọng hơn việc giữ
  nguyên mọi kế hoạch trung gian

Rủi ro chính là mất đi lý do triển khai hữu ích nếu các artifact dẫn xuất bị
bỏ đi mà không lưu các quyết định quan trọng ở nơi khác.

<a id="choosing-a-model"></a>

## Chọn mô hình

Mô hình là quy ước của nhóm, không phải một thiết lập của CLI. Một dự án thậm chí có thể dùng
các mô hình khác nhau cho các khu vực khác nhau, miễn là người đóng góp biết mô hình nào
được áp dụng.

| Mô hình | Quy tắc duy trì sau bàn giao | Phù hợp nhất | Cần lưu ý |
|---|---|---|---|
| Đặc tả flow-back | Phản ánh các phát hiện được chấp nhận vào bất kỳ artifact nào, rồi đối soát | Lặp nhanh và cộng tác chặt chẽ | Các artifact lệch nhau âm thầm |
| Đặc tả flow-forward | Tạo thư mục tính năng mới cho yêu cầu mới | Lưu vết kiểm toán và rõ ràng về lịch sử | Ngữ cảnh bị trùng lặp hoặc phân mảnh |
| Living spec | Sửa `spec.md`; sinh lại các artifact dẫn xuất | Đặc tả là contract | Mất lý do trong các file được sinh lại |

Nếu nhóm của bạn chưa chọn mô hình, hãy bắt đầu bằng cách trả lời hai câu hỏi:

1. Các thư mục tính năng đã hoàn tất nên là bản ghi lịch sử hay là vùng làm việc
   có thể chỉnh sửa?
2. `spec.md` có phải nguồn sự thật duy nhất không, hay `plan.md` và `tasks.md`
   được phép trở thành các nguồn ngang hàng?

Khi đã rõ câu trả lời, hãy ghi quy ước đó vào hiến chương của dự án
hoặc tài liệu hướng dẫn người mới của nhóm để những người đóng góp sau này biết cách xử lý
thay đổi.
