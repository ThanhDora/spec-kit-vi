<a id="handling-complex-features"></a>

# Xử lý tính năng phức tạp

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../concepts/complex-features.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Các tính năng lớn hoặc phức tạp thường chạy trơn tru qua `/speckit.specify`,
`/speckit.plan` và `/speckit.tasks`, rồi giảm chất lượng ở giai đoạn triển khai. Giữa
một lần chạy `/speckit.implement` dài, agent có thể bắt đầu quên mất kế hoạch,
bỏ qua tác vụ hoặc bịa đặt (hallucinate) — thường ngay trước hoặc sau khi việc nén
ngữ cảnh (context compaction) được kích hoạt.

Nguyên nhân gốc là cạn cửa sổ ngữ cảnh. Khi một lần chạy triển khai
cố giữ toàn bộ tính năng trong ngữ cảnh, mô hình sẽ giảm chất lượng khi cửa sổ
đầy dần. Cách khắc phục là giới hạn phạm vi mỗi lần chạy để luôn nằm gọn
trong giới hạn ngữ cảnh.

Lệnh `/speckit.implement` nhận đầu vào tự do của người dùng mà agent
phải xem xét trước khi tiếp tục. Nhờ vậy, bạn có thể giới hạn phạm vi từng lần chạy
mà không cần thay đổi công cụ.

<a id="option-1-limit-how-many-tasks-run-per-invocation"></a>

## Cách 1: Giới hạn số tác vụ chạy trong mỗi lần gọi

Thay vì để `/speckit.implement` chạy hết mọi tác vụ một lúc, hãy yêu cầu nó
dừng sớm:

```text
/speckit.implement only execute tasks T001-T010, then stop and report progress
```

hoặc giới hạn theo giai đoạn:

```text
/speckit.implement only execute the Setup phase, then stop
```

Vì các tác vụ đã xong được đánh dấu `[X]` trong `tasks.md`, lần gọi
`/speckit.implement` tiếp theo sẽ tiếp tục từ chỗ bạn dừng. Cách này giữ mỗi lần chạy
nằm gọn trong giới hạn ngữ cảnh.

<a id="option-2-instruct-the-agent-to-use-sub-agents"></a>

## Cách 2: Yêu cầu agent dùng sub-agent

Nếu agent lập trình của bạn hỗ trợ sub-agent (ví dụ GitHub Copilot CLI hoặc
extension GitHub Copilot cho VS Code), bạn có thể yêu cầu `/speckit.implement`
giao từng tác vụ cho sub-agent:

```text
/speckit.implement delegate each parallel [P] task to a sub-agent
```

Mỗi sub-agent nhận một ngữ cảnh tập trung — một tác vụ cùng các đoạn trích liên quan
của kế hoạch — thay vì toàn bộ ngữ cảnh của tính năng, nên việc nén ngữ cảnh không bao giờ
bị kích hoạt trong phiên chính.

<a id="option-3-combine-both"></a>

## Cách 3: Kết hợp cả hai

Với tính năng rất lớn, hãy kết hợp giới hạn phạm vi và giao việc:

```text
/speckit.implement execute only the Core phase, delegate [P] tasks to sub-agents
```

<a id="option-4-decompose-the-feature-into-smaller-specs"></a>

## Cách 4: Chia tính năng thành các đặc tả nhỏ hơn

Khi ngay cả một giai đoạn cũng làm quá tải ngữ cảnh, hãy chia tính năng thành các
tính năng con được đặc tả độc lập. Mỗi tính năng con có
`spec.md`, `plan.md` và `tasks.md` riêng, và đi qua chu trình
specify/plan/tasks/implement của riêng nó.

Đây là cách tiếp cận "đặc tả của các đặc tả" (spec of specs): lượt đầu tiên chia một tính năng đồ sộ
thành các đặc tả nhỏ hơn, khép kín, mỗi đặc tả có thể được triển khai mà không làm quá tải
mô hình. Cách này tốn công nhất, nên chỉ dành cho những tính năng quá lớn để
xử lý theo cách khác.

Xem [Đặc tả của các đặc tả](spec-of-specs.md) để biết toàn bộ quy trình — cách chạy
lượt lập lộ trình, cấu trúc artifact lộ trình, liên kết các đặc tả con về lộ trình, kèm một ví dụ
minh họa đầy đủ.

<a id="which-approach-to-choose"></a>

## Chọn cách nào

| Cách | Phù hợp nhất cho |
| --- | --- |
| Giới hạn N tác vụ hoặc một giai đoạn | Mọi agent; đơn giản nhất; không cần hỗ trợ sub-agent |
| Giao việc cho sub-agent | Agent hỗ trợ sub-agent; tối đa hóa song song |
| Kết hợp giới hạn phạm vi + giao việc | Tính năng lớn trên agent hỗ trợ sub-agent; cân bằng cả hai |
| Chia thành các đặc tả nhỏ hơn | Khi ngay cả một giai đoạn cũng làm quá tải ngữ cảnh |

Trong hầu hết trường hợp, giới hạn phạm vi tác vụ mỗi lần chạy là cách khắc phục đơn giản nhất. Hãy dùng
cách giao việc cho sub-agent khi agent của bạn hỗ trợ và bạn muốn chạy song song, và chỉ
chia thành các đặc tả nhỏ hơn khi một giai đoạn vẫn quá lớn để xử lý trong một lần chạy.
