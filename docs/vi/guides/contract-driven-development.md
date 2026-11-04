<a id="contract-driven-development"></a>

# Phát triển hướng contract

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../guides/contract-driven-development.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Khi một thành phần cung cấp giao diện cho bên sử dụng bên ngoài, hãy xác định
contract mà bên sử dụng đó có thể dựa vào. **Phát triển hướng contract** (contract-driven development) nghĩa là
thống nhất contract đó, triển khai từng phía dựa trên nó, và xác minh
cả hai phía đều đáp ứng nghĩa vụ của mình.

Cách làm này nằm gọn trong Phát triển hướng đặc tả: yêu cầu sản phẩm xác lập
hành vi dự kiến; contract xác định cách các thành phần phối hợp để mang lại hành vi đó;
kế hoạch triển khai của từng thành phần mô tả giải pháp bên trong của nó. Hãy xác định
ranh giới tương tác trước, thay vì coi ranh giới repository là
bản thiết kế.

Hướng dẫn này dùng các lệnh Spec Kit hiện có và các artifact có phiên bản thông thường.
Nó không đưa ra cơ chế tự động đồng bộ contract, phân giải phụ thuộc
giữa các repository hay điều phối phát hành.

<a id="when-to-define-a-contract"></a>

## Khi nào cần xác định contract

"Bên ngoài" nghĩa là nằm ngoài ranh giới triển khai của thành phần, không
nhất thiết là ngoài tiến trình, repository hay tổ chức của nó. Ví dụ:

- Một website gọi API backend.
- Một service gọi service khác hoặc tiêu thụ event của service đó.
- Một ứng dụng dùng giao diện của thư viện hoặc plugin.
- Một quy trình tự động gọi CLI và phân tích đầu ra của nó.
- Các thành phần trao đổi file theo một định dạng đã thống nhất.

Nguyên tắc này áp dụng cho kiến trúc monolith, ứng dụng dạng module, microservice và
các kiến trúc khác. Cách tổ chức repository không quyết định có cần contract
hay không. Hình thức và mức chi tiết của contract nên tương xứng với giao diện: một thư viện nhỏ có thể
chỉ cần mô tả chữ ký hàm và hành vi, còn một HTTP API công khai có thể cần
một schema OpenAPI và các ví dụ chạy được. Không phải contract nào cũng cần
schema riêng hay một registry contract.

<a id="what-the-contract-defines"></a>

## Contract xác định những gì

Mô tả các nghĩa vụ quan sát được, giúp mỗi phía có thể được triển khai mà không
phụ thuộc vào chi tiết bên trong của phía kia:

- Đầu vào được chấp nhận và đầu ra được tạo ra, bao gồm định dạng và quy tắc kiểm tra hợp lệ.
- Hành vi và tác dụng phụ, bao gồm các trường hợp lỗi.
- Các bảo đảm tương tác liên quan, như tính idempotent, thứ tự event, thử lại
  hoặc timeout.
- Kỳ vọng về tương thích, cách đánh phiên bản và chính sách ngừng hỗ trợ.
- Ví dụ và tiêu chí xác minh cho bên cung cấp và bên sử dụng.

Chỉ riêng schema có thể chưa thể hiện hết thỏa thuận. Ví dụ, cấu trúc của một
yêu cầu đặt hàng không cho biết việc thử lại có thể tạo ra đơn hàng thứ hai hay không.
Hãy ghi lại cả những ngữ nghĩa đó. Đừng để lộ cấu trúc cơ sở dữ liệu nội bộ hay
lựa chọn triển khai, trừ khi chúng thực sự là một phần của giao diện công khai.

<a id="one-authoritative-owner"></a>

## Một bên sở hữu chính thức

**Một phía sở hữu contract chính thức; phía kia sử dụng nó.** Thông thường
thành phần cung cấp giao diện là bên sở hữu. Hãy nêu rõ quyền sở hữu của từng
giao diện, và để các bên sử dụng bị ảnh hưởng cùng tham gia thống nhất các thay đổi.
Sở hữu không có nghĩa là được thay đổi đơn phương.

| Tình huống | Cách chia sẻ contract |
|-----------|--------------------------|
| Cả hai phía cùng ở một repository | Tham chiếu cùng một file hoặc artifact chính thức thay vì duy trì các định nghĩa riêng. Các thành phần phát hành độc lập vẫn nên ghi lại phiên bản contract mà chúng hỗ trợ. |
| Hai phía ở các repository khác nhau | Phát hành một artifact/package contract có phiên bản để bên sử dụng ghim, hoặc đồng bộ một bản sao vào từng repository sử dụng. |
| Bên sử dụng giữ một bản sao được đồng bộ | Ghi lại nguồn chính thức và phiên bản hoặc commit chính xác. Coi bản sao là đầu vào chỉ đọc; đề xuất thay đổi tại nguồn. |

Với một bản sao vendored, một README đặt cạnh có thể ghi lại repository nguồn, đường dẫn
nguồn, revision bất biến hoặc digest của artifact phát hành, và quy trình cập nhật. Một
package phụ thuộc có thể ghi thông tin tương đương trong lockfile.
Hãy cấp cho bên sử dụng quyền truy cập hợp lệ vào artifact contract; họ không
cần được truy cập repository triển khai của bên cung cấp.

Việc cập nhật phải có chủ đích: thống nhất thay đổi tại nguồn chính thức, phát hành
một phiên bản, rồi review việc cập nhật phiên bản hoặc bản sao ở từng bên sử dụng. Đừng
âm thầm đồng bộ mọi bên lên "mới nhất". Một contract được ghim xác định một
thỏa thuận; nó không bảo đảm rằng bên cung cấp đang chạy vẫn hỗ trợ thỏa thuận đó.

<a id="using-the-spec-kit-workflow"></a>

## Dùng quy trình Spec Kit

1. **Xác lập ý định và xác định các giao diện.** Ghi lại hành vi người dùng
   mong muốn bằng `/speckit.specify`. Xác định thành phần nào cung cấp và
   thành phần nào sử dụng từng tương tác. Nếu chưa có contract, việc xác định nó là một phần của
   công việc, không phải điều kiện tiên quyết lẽ ra đã phải được hoàn tất ở nơi khác.
2. **Thống nhất contract trước khi triển khai các phần phụ thuộc.** Trong
   `/speckit.plan`, bên sở hữu soạn contract giao diện và review với
   các bên sử dụng. Giải quyết các câu hỏi về hành vi quan sát được và tương thích trước khi
   bất kỳ phía nào triển khai dựa trên giả định về phía kia. Sau đó mỗi phía có thể
   phát triển độc lập dựa trên phiên bản đã thống nhất.
3. **Cung cấp thỏa thuận cho từng dự án bị ảnh hưởng.** Đưa cho agent
   phiên bản chính xác của contract và nội dung truy cập được, cùng với các
   yêu cầu sản phẩm liên quan. Đừng cho rằng một đường link sẽ làm cho file của repository khác
   trở nên khả dụng. Mỗi dự án sở hữu `spec.md`, `plan.md` và
   `tasks.md` cục bộ của mình; hãy tham chiếu contract thay vì sao chép kế hoạch
   triển khai của dự án khác.
4. **Lập kế hoạch xác minh một cách rõ ràng.** Yêu cầu `/speckit.tasks` bao gồm contract test
   cho bên cung cấp và bên sử dụng, kể cả các trường hợp âm. Kiểm thử hành vi
   quan sát được chứ không chỉ cấu trúc dữ liệu. Test phía bên sử dụng dựa trên mock rất hữu ích,
   nhưng không chứng minh được bên cung cấp thật tuân thủ; hãy bao gồm cả bước xác minh
   bên cung cấp và kiểm định tích hợp.
5. **Triển khai và kiểm định từng phía.** Dùng `/speckit.implement` trong từng
   dự án, rồi chạy các bước kiểm tra đã thống nhất. Nếu việc triển khai làm lộ ra vấn đề
   của contract, hãy sửa thỏa thuận chính thức và đối soát các
   đặc tả, kế hoạch, test và phiên bản của bên sử dụng bị ảnh hưởng, thay vì tự ý sửa một
   bản sao.
6. **Phát hành các phần triển khai tương thích.** Theo dõi phiên bản thành phần
   đang chạy nào hỗ trợ phiên bản contract nào. Sắp xếp thứ tự rollout và rollback
   theo các phụ thuộc đó. Với thay đổi phá vỡ tương thích, hãy thống nhất một giai đoạn chuyển đổi và
   chồng lấn trước khi gỡ bỏ hành vi mà bên sử dụng vẫn còn dùng.

`/speckit.plan` vốn đã tạo các artifact `contracts/` theo phạm vi tính năng khi
có giao diện bên ngoài. Hãy chọn rõ artifact nào là
chính thức: một tính năng có thể soạn contract mới ở đó, hoặc đề xuất thay đổi cho
một contract đã có ở nơi khác trong dự án. Ghi lại nguồn đã được phê duyệt
và phiên bản trong các artifact của tính năng. Các bản chụp lịch sử và bản sao được đồng bộ
không phải là nguồn sự thật có thể chỉnh sửa bổ sung, và Spec Kit không
tự động phát hành hay đồng bộ chúng.

Về việc phát triển artifact sau một thay đổi, xem
[Phát triển đặc tả trong dự án có sẵn](evolving-specs.md).

<a id="worked-example-website-checkout-across-services"></a>

## Ví dụ minh họa: thanh toán trên website qua nhiều service

Xét một tính năng thanh toán giả định gồm một website, một service đơn hàng
và một service kho hàng, mỗi thành phần nằm trong repository riêng. Chưa có
contract nào được thống nhất. Yêu cầu của người dùng là: **khách hàng chỉ đặt được đơn hàng
khi các mặt hàng có thể được giữ chỗ, và việc thử lại một yêu cầu không được tạo ra
đơn hàng hoặc lượt giữ chỗ trùng lặp.**

Trước tiên hãy xác định và thống nhất hai contract. Dưới đây chỉ là tóm tắt; các
artifact chính thức còn phải xác định chi tiết đầu vào/đầu ra và các nghĩa vụ
khác đã mô tả ở trên.

| Contract | Bên sở hữu/cung cấp | Bên sử dụng | Thỏa thuận quan sát được |
|----------|----------------|----------|----------------------|
| Orders API | Service đơn hàng | Website | Chấp nhận yêu cầu đặt hàng kèm idempotency key; trả về đơn hàng hoặc một lỗi đã được định nghĩa; thử lại không được tạo đơn hàng trùng lặp. |
| Inventory API | Service kho hàng | Service đơn hàng | Giữ chỗ toàn bộ mặt hàng được yêu cầu hoặc báo không đủ hàng mà không giữ chỗ một phần; thử lại không được tạo lượt giữ chỗ trùng lặp. |

Service đơn hàng là bên cung cấp ở một giao diện và là bên sử dụng ở giao diện còn lại.
Nó sở hữu contract Orders API, không sở hữu contract Inventory API.

Một cách bố trí khả thi, dùng bản sao được đồng bộ thay vì package:

```text
inventory-repo/
  .specify/
  contracts/inventory-api.yaml     # authoritative Inventory API contract
  specs/001-reserve-inventory/

orders-repo/
  .specify/
  contracts/orders-api.yaml        # authoritative Orders API contract
  contracts/inventory-api.yaml     # read-only copy pinned to Inventory API 1.0.0
  contracts/README.md              # source revision and sync procedure
  specs/001-place-order/

website-repo/
  .specify/
  contracts/orders-api.yaml        # read-only copy pinned to Orders API 1.0.0
  contracts/README.md              # source revision and sync procedure
  specs/001-checkout/
```

Tên file và phiên bản chỉ mang tính minh họa, không phải bố cục bắt buộc của Spec Kit.
Mỗi dự án được khởi tạo độc lập và dùng quy trình SDD thông thường:

1. Nhóm kho hàng thống nhất Inventory API 1.0.0 với nhóm đơn hàng; nhóm
   đơn hàng thống nhất Orders API 1.0.0 với nhóm website. Mỗi bên sở hữu
   phát hành contract đã được phê duyệt, và các bên sử dụng ghim bản sao của mình.
2. Mỗi nhóm đặc tả và lập kế hoạch cho phần thanh toán của mình dựa trên các
   thỏa thuận đó. Website mô tả tương tác của khách hàng, service đơn hàng mô tả việc
   đặt hàng, còn service kho hàng mô tả hành vi giữ chỗ. Kế hoạch của service đơn hàng
   tính đến cả hai contract và các lỗi xảy ra giữa bước giữ chỗ và bước tạo
   đơn hàng.
3. Liên kết đặc tả tính năng cục bộ của từng bên với cùng một issue hoặc mục lộ trình
   của tính năng sản phẩm, và ghi lại phiên bản contract cùng các đặc tả hoặc PR
   liên quan của bên cung cấp/bên sử dụng. Số thứ tự tính năng và branch cục bộ không cần
   khớp nhau. Đây là truy vết, không phải một kế hoạch triển khai dùng chung.
4. Triển khai và xác minh cả hai giao diện, bao gồm thử lại, không đủ
   hàng và các lỗi. Kiểm định toàn bộ luồng thanh toán cũng như các nghĩa vụ
   contract của từng thành phần.
5. Với lần rollout đầu tiên này, hãy đưa phần triển khai của kho hàng vào hoạt động
   trước khi bật phần triển khai phụ thuộc của service đơn hàng, rồi mới bật tính năng
   thanh toán trên website. Ghi lại các phiên bản đã triển khai và ràng buộc rollback; chỉ
   phát hành contract thôi không làm cho phần triển khai của nó sẵn sàng.

Nếu về sau Orders API 1.1.0 bổ sung một ghi chú giao hàng tùy chọn, hãy đề xuất và review
thay đổi đó trong `orders-repo`, xác minh tương thích với các bên sử dụng hiện có,
rồi để website chủ động áp dụng phiên bản mới. Đừng sửa bản sao được đồng bộ
của website để tự tạo ra một khả năng mà service đơn hàng chưa
đồng ý cung cấp.

Thiết kế này vẫn dùng được nếu cả ba thành phần được chuyển vào một repository:
tham chiếu trực tiếp các contract chính thức thay vì đồng bộ bản sao.
Xem [Dùng Spec Kit trong monorepo](monorepo.md) để biết cách bố trí dự án và cách nhắm
lệnh tới đúng dự án. **Contract kết nối các phần triển khai; cách tổ chức repository chỉ
thay đổi cách chia sẻ thỏa thuận đó.**

<a id="example-control-plane-data-plane-and-integration-tests"></a>

## Ví dụ: control plane, data plane và integration test

Xét một dự án control plane (`r1`) quản lý cấu hình, một dự án data plane
(`r2`) áp dụng cấu hình đó khi xử lý lưu lượng, và một dự án integration test
(`r3`) xác minh tương tác giữa chúng. Mỗi dự án nằm trong repository riêng.
Đây là một ứng dụng khác của cùng nguyên tắc, không phải yêu cầu phải
tổ chức hệ thống theo cách này.

<a id="define-the-interaction-first"></a>

### Xác định tương tác trước

Giả sử control plane cần áp dụng một cấu hình lên data plane,
nhưng chưa có contract nào. Hãy thống nhất hành vi quan sát được trước khi
bất kỳ phía nào triển khai dựa trên giả định về phía kia:

| Khía cạnh của contract | Ví dụ thỏa thuận |
|------------------|-------------------|
| Đầu vào | Một revision cấu hình và payload với các quy tắc kiểm tra hợp lệ rõ ràng. |
| Đầu ra | Một xác nhận cho biết revision và trạng thái được chấp nhận hay đã được áp dụng; xác định cách bên gọi biết khi nào hoàn tất nếu việc áp dụng là bất đồng bộ. |
| Lỗi | Các phản hồi đã định nghĩa cho cấu hình không hợp lệ và revision cũ, trong khi cấu hình hợp lệ trước đó vẫn giữ hiệu lực. |
| Hành vi | Thử lại cùng revision và payload không áp dụng hai lần; dùng lại một revision với payload khác sẽ bị từ chối. |
| Tương thích | Xác định các phiên bản contract được hỗ trợ và giữ nguyên hành vi mà bên gọi hiện có vẫn dựa vào trong thời gian chuyển đổi. |

Trong ví dụ này, `r2` cung cấp giao diện và sở hữu contract chính thức.
Nhóm `r1` tham gia thống nhất contract và sử dụng một phiên bản được ghim.
Nhóm `r3` dùng chính phiên bản đó để xác minh tương tác, bao gồm
đầu vào không hợp lệ, thử lại và tương thích với các phần triển khai được hỗ trợ. Test
là bằng chứng cho thỏa thuận, không phải một định nghĩa cạnh tranh với nó.

Mỗi dự án giữ kế hoạch triển khai hoặc kế hoạch kiểm thử riêng. Hãy tham chiếu ý định sản phẩm
chung và phiên bản contract mà không cần một repository bao trùm,
tên branch trùng nhau hay commit nguyên tử trên cả ba repository.

<a id="evolve-an-agreed-contract-deliberately"></a>

### Phát triển contract đã thống nhất một cách có chủ đích

Trình tự rollout dưới đây được điều chỉnh từ hướng dẫn phát triển contract do
TongyiDai đóng góp. Nó giả định contract tương tác ban đầu đã được thống nhất
và đang được sử dụng.

Giả sử bên cung cấp và các bên sử dụng đồng ý thêm một trường cấu hình tùy chọn
mới. Hãy lập kế hoạch rõ ràng cho việc áp dụng tương thích:

1. **Phát hành một thay đổi tương thích.** Cập nhật contract chính thức trong `r2`,
   gán cho nó một phiên bản rõ ràng, và phát hành schema cùng các fixture kiểm tra
   tương thích. Xác minh rằng bỏ trống trường mới vẫn giữ nguyên hành vi hiện có.
2. **Triển khai hỗ trợ trước khi bật sử dụng.** Nếu `r1` cần hành vi mới từ
   `r2`, hãy triển khai `r2` ở chế độ hỗ trợ cả bên sử dụng cũ lẫn mới trước.
   Chỉ khi đó mới bật hành vi phụ thuộc trong `r1`. Thứ tự này đi theo
   phụ thuộc của giao diện, không theo tên repository hay thứ tự merge PR.
3. **Chuẩn bị integration test nhận biết phiên bản.** Bổ sung độ phủ cho `r3` sớm,
   chọn kỳ vọng theo phiên bản contract được hỗ trợ hoặc theo khả năng được khai báo rõ,
   không theo tên branch. Giữ các bước kiểm tra tương thích hiện có ở trạng thái bắt buộc. Hãy đặt cổng kiểm soát
   end-to-end mới thành bắt buộc trước khi bật tính năng, ngay khi đã có các phần triển khai
   tương thích; đừng âm thầm bỏ qua nó sau khi đã kích hoạt.
4. **Theo dõi mức độ sẵn sàng bằng tham chiếu bất biến.** Một issue hoặc lộ trình hiện có
   có thể liên kết contract đã phê duyệt, các bản phát hành của bên cung cấp và bên sử dụng, kết quả end-to-end
   và tiêu chí gỡ bỏ luồng cũ tới các commit hoặc artifact phát hành chính xác.
   Phân biệt thay đổi đã merge với phần triển khai đã chạy và sẵn sàng.
5. **Giữ một đường rollback.** Với lần rollout ưu tiên bên cung cấp này, hãy tắt hoặc
   rollback hành vi mới của bên sử dụng trước khi rollback bên cung cấp.
   Kiểm tra cả tính tương thích của trạng thái đã lưu và cấu hình; chỉ đảo ngược thứ tự
   triển khai không hoàn tác được thay đổi dữ liệu. Chỉ gỡ bỏ contract cũ trong một lần dọn dẹp
   về sau, khi đã xác nhận không còn bên sử dụng được hỗ trợ nào phụ thuộc vào nó.

Nếu không tránh được thay đổi phá vỡ tương thích, hãy mở rộng hỗ trợ để cho phép chuyển đổi, chủ động chuyển
các bên sử dụng sang, và chỉ khi đó mới loại bỏ hành vi cũ. Phát hành một contract
có phiên bản và ghi lại mức độ sẵn sàng không biến các lần triển khai riêng biệt
thành một giao dịch. Đây là các thỏa thuận và bước kiểm tra do nhóm duy trì, không phải một
cơ chế phân giải phụ thuộc hay điều phối phát hành mới của Spec Kit.
