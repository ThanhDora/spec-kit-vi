<a id="spec-of-specs"></a>

# Đặc tả của các đặc tả

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../concepts/spec-of-specs.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Khi một tính năng quá lớn để chạy trọn một chu trình
`/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`
mà mô hình không bị mất phương hướng giữa chừng lúc triển khai, bạn có thể chia nó thành một
**lộ trình (roadmap)** gồm các tính năng con nhỏ hơn, được đặc tả độc lập. Đây là cách tiếp cận
"đặc tả của các đặc tả" (spec of specs): một lượt làm trước tiên phân rã tính năng đồ sộ thành các đặc tả
khép kín, và mỗi đặc tả chạy qua chu trình specify/plan/tasks/implement của riêng nó.

> **Khi nào nên dùng.** Trong số các chiến lược ở
> [Xử lý tính năng phức tạp](complex-features.md), phân rã là cách tốn công nhất. Chỉ dùng nó **khi các
> cách nhẹ nhàng hơn ở đó không đủ** — trước hết hãy thử giới hạn số tác vụ chạy trong mỗi lần gọi
> `/speckit.implement`, sau đó là giao việc cho sub-agent, rồi kết hợp cả hai.
> Chỉ dùng đặc tả của các đặc tả khi ngay cả một giai đoạn cũng quá lớn để xử lý trong
> một lần chạy.

Phần còn lại của trang mô tả *cách* làm việc này bằng những công cụ bạn đã có. Không
cần lệnh hay extension mới.

<a id="the-roadmap-pass"></a>

## Lượt lập lộ trình

Trước khi viết bất kỳ đặc tả con nào, hãy thực hiện một lượt phân rã duy nhất để tạo ra lộ trình.
Hãy coi đây là một cuộc trao đổi lập kế hoạch nhẹ nhàng với agent, không phải một đặc tả đầy đủ:

1. **Nêu toàn bộ tính năng.** Mô tả tính năng lớn ("epic") trong một
   hai câu để agent nắm được bức tranh tổng thể ngay từ đầu.
2. **Xác định các lát cắt độc lập.** Yêu cầu agent đề xuất một nhóm nhỏ
   tính năng con, mỗi tính năng bàn giao một phần mạch lạc của epic và có thể được đặc tả
   riêng. Hướng tới các lát cắt kiểm thử được độc lập — chỉ cần triển khai
   một lát cắt là bạn đã có thứ để trình diễn.
3. **Vạch ranh giới.** Với mỗi lát cắt, viết một dòng về ý định và một ranh giới phạm vi
   rõ ràng (cái gì thuộc phạm vi, cái gì để lại cho lát cắt anh em). Ranh giới rõ nét
   chính là điều giữ cho mỗi đặc tả con đủ nhỏ để vừa với ngữ cảnh.
4. **Sắp xếp theo phụ thuộc.** Ghi lại lát cắt nào phụ thuộc lát cắt nào và sắp xếp để
   các điều kiện tiên quyết đi trước. Các lát cắt không phụ thuộc nhau có thể được xây dựng theo
   bất kỳ thứ tự nào. Để xây dựng song song các lát cắt độc lập, hãy dùng các worktree riêng để mỗi
   lần chạy có trạng thái tính năng đang làm tách biệt.
5. **Ghi kết quả thành lộ trình.** Lưu các lát cắt vào một file lộ trình bền vững
   (bên dưới) để mọi đặc tả con về sau đều có thể trỏ ngược về đó.

Lộ trình được cố ý giữ ở mức nông: nó đặt tên và sắp thứ tự các tính năng con nhưng
**không** thiết kế chúng. Việc thiết kế diễn ra khi từng lát cắt chạy qua
`/speckit.specify` của riêng nó.

<a id="the-roadmap-artifact"></a>

## Artifact lộ trình

Lộ trình là một file Markdown bình thường do bạn viết và đưa vào quản lý phiên bản —
không có công cụ đặc biệt nào đứng sau. Hãy đặt nó ở nơi các đặc tả con tìm thấy được:

- Với epic trong phạm vi một tính năng: `specs/<epic-slug>/roadmap.md`.
- Với epic lớn hơn, xuyên suốt nhiều phần: một file `ROADMAP.md` ở cấp cao nhất.

Mỗi mục trong lộ trình có một id ổn định (dùng để liên kết về sau), một tên, ý định,
ranh giới phạm vi, các phụ thuộc, trạng thái, và — khi đặc tả con đã tồn tại — một
liên kết tới nó. Template tối giản:

```markdown
# Roadmap: <epic name>

<One or two sentences: what the epic is and why it is being decomposed.>

**Status legend**: planned · in-progress · done

| ID | Sub-feature | Intent | Scope boundary | Depends on | Status | Sub-spec |
|----|-------------|--------|----------------|-----------|--------|----------|
| R1 | <name>      | <one line> | <in / deferred> | —      | planned | — |
| R2 | <name>      | <one line> | <in / deferred> | R1     | planned | — |
| R3 | <name>      | <one line> | <in / deferred> | R1     | planned | — |
```

Giữ cột `ID` bất biến khi đã có đặc tả con tham chiếu tới nó — đó là điểm neo cho
truy vết. Điền vào cột `Sub-spec` đường dẫn tới thư mục đặc tả của từng tính năng con
khi bạn tạo nó, và cập nhật `Status` theo tiến độ công việc.

<a id="specifying-each-sub-feature"></a>

## Đặc tả từng tính năng con

Khi đã có lộ trình, hãy lần lượt làm từng mục bằng quy trình Spec Kit
thông thường — không có gì mới phải học:

1. Chọn mục tiếp theo trong lộ trình có các phụ thuộc đều đã `done` (hoặc không có phụ thuộc).
2. Chạy `/speckit.specify` chỉ cho lát cắt đó, chỉ mô tả ý định và phạm vi
   theo mục trong lộ trình. Vì lát cắt có giới hạn, đặc tả, kế hoạch và danh sách tác vụ của nó
   luôn nằm gọn trong cửa sổ ngữ cảnh.
3. Chạy `/speckit.plan`, `/speckit.tasks` và `/speckit.implement` cho lát cắt đó như
   thường lệ.
4. Đánh dấu mục trong lộ trình là `done` và chuyển sang mục tiếp theo.

Mỗi lát cắt là một tính năng Spec Kit hoàn chỉnh, độc lập, có
`spec.md`/`plan.md`/`tasks.md` riêng. Lộ trình là thứ gắn kết chúng lại với nhau.

<a id="linking-sub-specs-to-the-roadmap"></a>

## Liên kết đặc tả con với lộ trình

Để phạm vi và ý định không bị trôi giữa các lần chạy riêng biệt, mỗi đặc tả con
tham chiếu tới mục của nó trong lộ trình, và lộ trình liên kết ngược lại — một quy ước hai chiều
đơn giản, dễ tìm bằng grep:

- **Đặc tả con → lộ trình.** Trong `spec.md` của tính năng con, ghi tên lộ trình cha
  và id của mục ở dòng `Input` / tóm tắt, ví dụ:

  ```markdown
  **Input**: Parent roadmap: `specs/<epic>/roadmap.md` → entry **R3**. <feature description>
  ```

- **Lộ trình → đặc tả con.** Trong bảng lộ trình, đặt cột `Sub-spec` của mục đó thành
  thư mục của tính năng con, ví dụ `specs/<epic>-part-3/`.

Vì cả hai chiều đều là văn bản thuần, bạn có thể lần từ bất kỳ đặc tả con nào về vị trí của nó
trong epic (và tìm các đặc tả anh em) chỉ bằng một lần tìm kiếm nhanh — không cần công cụ, không cần
schema metadata.

<a id="keeping-the-roadmap-and-sub-specs-in-sync"></a>

## Giữ lộ trình và đặc tả con đồng bộ

Lộ trình là một tài liệu sống. Khi bạn hiểu thêm, hãy giữ nó và các đặc tả con
khớp nhau:

- **Lộ trình trước, rồi đối soát.** Khi phạm vi thay đổi, hãy cập nhật mục trong lộ trình
  trước, rồi cập nhật các đặc tả con bị ảnh hưởng. Lộ trình là nguồn sự thật về
  cách chia epic.
- **Tôn trọng phụ thuộc và thứ tự.** Nếu một lát cắt phụ thuộc vào lát cắt khác, hãy xây dựng
  điều kiện tiên quyết trước và tham chiếu chéo tới đặc tả con phụ thuộc để mối quan hệ
  hiện rõ từ cả hai phía.
- **Đệ quy khi lát cắt vẫn quá lớn.** Nếu một tính năng con hóa ra quá
  lớn để đặc tả trong một chu trình, hãy tạo lộ trình riêng cho nó và phân rã tiếp —
  cùng cách tiếp cận được áp dụng ở cấp thấp hơn. Đệ quy làm tăng chi phí, nên chỉ đi
  sâu đến mức mà vấn đề ngữ cảnh thực sự đòi hỏi.

<a id="worked-example"></a>

## Ví dụ minh họa

Giả sử epic là **"Thêm cổng thanh toán tự phục vụ"** — quá lớn cho
một chu trình. Lượt lập lộ trình chia nó thành ba lát cắt có thể đặc tả
độc lập.

`specs/billing-portal/roadmap.md`:

```markdown
# Roadmap: Self-service billing portal

Let customers view invoices, manage payment methods, and change plans without
contacting support. Too large for one cycle, so it is split into independent slices.

**Status legend**: planned · in-progress · done

| ID | Sub-feature        | Intent                                   | Scope boundary                              | Depends on | Status  | Sub-spec |
|----|--------------------|------------------------------------------|---------------------------------------------|-----------|---------|----------|
| R1 | Invoice history    | Customers view and download past invoices | Read-only; no payment actions               | —         | done    | specs/billing-invoices/ |
| R2 | Payment methods    | Add, remove, and set a default card       | No plan changes; assumes invoices exist     | R1        | in-progress | specs/billing-payment-methods/ |
| R3 | Plan changes       | Upgrade/downgrade the subscription plan   | Uses R2's default payment method            | R1, R2    | planned | — |
```

Sau đó từng lát cắt được đặc tả riêng. Ví dụ, `spec.md` của tính năng con **R2**
mở đầu bằng một tham chiếu ngược:

```markdown
# Feature Specification: Billing — payment methods

**Input**: Parent roadmap: `specs/billing-portal/roadmap.md` → entry **R2**.
Let customers add, remove, and set a default payment method in the billing portal.
```

Từ đây, người đọc có thể lần từ **R2** về lộ trình, thấy nó phụ thuộc vào
**R1** (lịch sử hóa đơn, đã `done`), và thấy **R3** (thay đổi gói dịch vụ) đang
chờ nó. Xây dựng R1, rồi R2, rồi R3 giúp mỗi lần chạy đều nhỏ trong khi lộ trình
vẫn giữ được hình dạng tổng thể của cả epic.

<a id="for-automation-optional"></a>

## Tự động hóa (tùy chọn)

Nếu bạn muốn tự động hóa việc ghi lộ trình và kiểm tra tính nhất quán thay vì tự duy trì
file, [extension Spec Roadmap](https://github.com/srobroek/speckit-roadmap) do cộng đồng
duy trì đi theo hướng đó. Đây là extension của bên thứ ba và không bắt buộc — quy ước thủ công
ở trên tự nó đã đủ.
