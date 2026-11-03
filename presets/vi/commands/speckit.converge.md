---
description: Đánh giá codebase hiện tại so với đặc tả, kế hoạch và tác vụ của tính năng, rồi bổ sung phần việc còn chưa xây dựng thành các tác vụ mới ở cuối tasks.md để implement hoàn thành nốt.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-spec --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireSpec -RequireTasks -IncludeTasks
  py: scripts/python/check_prerequisites.py --json --require-spec --require-tasks --include-tasks
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi hội tụ)**:

- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_converge`
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi tiếp tục như bình thường
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook tùy chọn** (`optional: true`):

    ```text
    ## Hook của extension

    **Pre-hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```

  - **Hook bắt buộc** (`optional: false`):

    ```text
    ## Hook của extension

    **Pre-hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}

    Chờ kết quả của lệnh hook trước khi chuyển sang phần Mục tiêu.
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.

- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua

## Mục tiêu

Thu hẹp khoảng cách giữa những gì đặc tả, kế hoạch và tác vụ của tính năng yêu cầu với những gì
codebase hiện đang triển khai. Đọc `spec.md`, `plan.md` và `tasks.md` như **nguồn ý định
duy nhất** (cùng hiến chương đóng vai trò ràng buộc quản trị), đánh giá trạng thái hiện tại
của code, xác định những yêu cầu, tiêu chí chấp nhận, quyết định trong kế hoạch và tác vụ
hiện có nào chưa được đáp ứng, chưa hoàn chỉnh hoặc mới chỉ đáp ứng một phần, rồi **bổ sung
từng phần việc còn lại thành một tác vụ mới, truy vết được** ở cuối `tasks.md` để
`__SPECKIT_COMMAND_IMPLEMENT__` có thể hoàn thành nó. Lệnh này CHỈ được chạy sau khi
`__SPECKIT_COMMAND_IMPLEMENT__` đã chạy trên `tasks.md` hiện tại, và sau khi `__SPECKIT_COMMAND_TASKS__` đã tạo một `tasks.md` hoàn chỉnh.

Đây **không** phải công cụ so sánh diff và **không** theo dõi thay đổi. Nó đánh giá trạng thái
hiện tại của code so với các artifact của tính năng — không dùng git, không so sánh branch, không xem lịch sử.

## Ràng buộc khi vận hành

**CHỈ BỔ SUNG, KHÔNG BAO GIỜ VIẾT LẠI**: Thao tác ghi **duy nhất** của lệnh là thêm một
mục `## Giai đoạn N: Hội tụ` mới vào `tasks.md`. Lệnh KHÔNG ĐƯỢC:

- sửa `spec.md` hay `plan.md` dưới bất kỳ hình thức nào;
- viết lại, đánh số lại, sắp xếp lại hay xóa bất kỳ tác vụ hiện có nào (kể cả tác vụ của
  một giai đoạn Hội tụ trước đó);
- sửa, tạo hay xóa bất kỳ code ứng dụng nào — hoàn thành các tác vụ được bổ sung là
  việc của `__SPECKIT_COMMAND_IMPLEMENT__`.

Khi codebase đã đáp ứng mọi thứ, lệnh PHẢI giữ `tasks.md`
**không đổi tới từng byte** (không thêm tiêu đề Hội tụ rỗng) và báo cáo kết quả sạch.

**Thẩm quyền của hiến chương**: Hiến chương dự án (`/memory/constitution.md`) là
**không thể thương lượng**. Code vi phạm một nguyên tắc PHẢI (MUST) là phát hiện có mức độ
nghiêm trọng cao nhất và sinh ra một tác vụ khắc phục tương ứng. Nếu hiến chương vẫn chỉ là
template chưa điền, hãy bỏ qua bước kiểm tra hiến chương một cách nhẹ nhàng thay vì báo lỗi.

## Các bước thực thi

### 1. Khởi tạo bối cảnh hội tụ

Chạy `{SCRIPT}` một lần từ thư mục gốc repo và parse JSON để lấy FEATURE_DIR và AVAILABLE_DOCS. Suy ra các đường dẫn tuyệt đối:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md
- CONSTITUTION = `/memory/constitution.md` (nếu có)
Nếu thiếu `spec.md`, `plan.md` hoặc `tasks.md`, DỪNG LẠI với thông báo rõ ràng, có hướng xử lý, nêu tên
lệnh tiên quyết cần chạy (`__SPECKIT_COMMAND_SPECIFY__` khi thiếu đặc tả, `__SPECKIT_COMMAND_PLAN__` khi thiếu kế hoạch,
`__SPECKIT_COMMAND_TASKS__` khi thiếu tác vụ). Không xuất kết quả dở dang.
Với dấu nháy đơn trong đối số như "I'm Groot", dùng cú pháp escape: ví dụ 'I'\''m Groot' (hoặc dùng nháy kép nếu được: "I'm Groot").

### 2. Nạp artifact (nạp dần theo nhu cầu)

Chỉ nạp phần bối cảnh tối thiểu cần thiết từ mỗi artifact:

**Từ spec.md:**

- Yêu cầu chức năng (FR-###)
- Tiêu chí thành công (SC-###) — chỉ đưa vào các mục cần phần việc xây dựng được; loại
  các chỉ số kết quả sau khi ra mắt và KPI kinh doanh
- User story và các kịch bản chấp nhận của chúng
- Trường hợp biên (nếu có)

**Từ plan.md:**

- Lựa chọn kiến trúc/stack và các quyết định kỹ thuật
- Tham chiếu mô hình dữ liệu
- Các giai đoạn và những điểm chạm được nêu tên (các file/thành phần mà kế hoạch nói sẽ được tạo hoặc sửa)
- Ràng buộc kỹ thuật

**Từ tasks.md:**

- Task ID (để tính ID tiếp theo và số thứ tự giai đoạn tiếp theo)
- Mô tả, cách nhóm theo giai đoạn và các đường dẫn file được tham chiếu

**Từ hiến chương (nếu không phải template chưa điền):**

- Tên các nguyên tắc và các câu quy phạm PHẢI/NÊN (MUST/SHOULD)

### 3. Xây dựng danh mục ý định

Tạo một mô hình nội bộ (không lặp lại nguyên văn artifact):

- **Danh mục yêu cầu**: một khóa ổn định cho mỗi FR-### / SC-### / kịch bản chấp nhận của
  user story (ví dụ `US1/AC2`), cộng với các quyết định trong kế hoạch và nguyên tắc hiến chương
  đặt ra nghĩa vụ cần xây dựng.
- **Bản đồ phạm vi code**: từ các đường dẫn file được nêu trong `plan.md` và `tasks.md`, cùng việc
  tìm theo từ khóa các khái niệm mà mỗi yêu cầu mô tả, suy ra tập file nguồn và thành phần
  nằm trong phạm vi đánh giá. Giới hạn việc đánh giá trong phạm vi này — **không** suy rộng
  phạm vi ra ngoài những gì artifact đã định nghĩa.

### 4. Đánh giá codebase và phân loại phát hiện

Đưa mọi tác vụ hiện có vào danh mục ý định, bất kể trạng thái checkbox hay thuộc giai đoạn
Hội tụ nào: việc tuyên bố đã hoàn thành không phải là bằng chứng. Kiểm chứng hành vi hiện tại
theo đặc tả, kế hoạch, tác vụ và hiến chương; với các chuỗi tác vụ sửa chữa, hãy đánh giá hành vi
cuối cùng, không đánh giá các chi tiết triển khai đã bị thay thế. Kiểm tra cả các nghĩa vụ chưa
được đáp ứng lẫn phần triển khai mâu thuẫn, vượt quá hoặc nằm ngoài ý định đã nêu.

Với mỗi mục trong danh mục ý định, xem xét code hiện tại trong phạm vi và chỉ tạo một
`Finding` khi có khoảng trống. Phân loại mỗi phát hiện theo **loại khoảng trống**:

- **`missing`**: phần việc được yêu cầu hoàn toàn không có trong code.
- **`partial`**: phần việc đã có nhưng chưa đáp ứng đầy đủ yêu cầu /
  tiêu chí chấp nhận / quyết định trong kế hoạch.
- **`contradicts`**: code làm điều mâu thuẫn với ý định đã nêu hoặc với một nguyên tắc PHẢI
  của hiến chương.
- **`unrequested`**: code chứa phần việc không được đặc tả, kế hoạch hay tác vụ yêu cầu
  (nêu ra để mọi người nắm — converge **không** xóa code, nó chỉ bổ sung một tác vụ để
  review/giải trình hoặc gỡ bỏ phần đó).

Mỗi `Finding` ghi lại: một id ổn định, `source-ref` mà nó truy vết tới, `gap-type`, mức độ
nghiêm trọng, và một mô tả ngắn dễ đọc kèm bằng chứng (file/khu vực đã quan sát).

**Trường hợp biên:**

- **Chưa có hoặc có rất ít code**: coi toàn bộ phạm vi đã đặc tả là phần việc còn lại ở loại `missing`
  thay vì báo lỗi.
- **Không còn gì phải làm**: không tạo phát hiện nào và đi theo nhánh đã hội tụ ở Bước 7.

### 5. Gán mức độ nghiêm trọng

- **CRITICAL**: vi phạm một nguyên tắc PHẢI của hiến chương, hoặc một khoảng trống `missing`/`contradicts`
  làm chặn chức năng cơ bản của một user story P1.
- **HIGH**: một khoảng trống `missing` hoặc `partial` ở một yêu cầu chức năng hay tiêu chí chấp nhận
  cốt lõi.
- **MEDIUM**: một khoảng trống `partial` ở yêu cầu thứ yếu, hoặc một phần bổ sung `unrequested` chưa có
  lý do rõ ràng.
- **LOW**: các khoảng trống một phần nhỏ, phần hoàn thiện, hoặc phần bổ sung `unrequested` ít rủi ro.

### 6. Trình bày bản tóm tắt phát hiện trong phiên

Trước khi bổ sung bất cứ thứ gì, xuất một bản tóm tắt ngắn gọn, phân theo mức độ nghiêm trọng (chưa ghi file):

## Phát hiện khi hội tụ

| ID | Loại khoảng trống | Mức độ | Nguồn | Bằng chứng | Phần việc còn lại |
|----|-------------------|--------|-------|------------|-------------------|
| F1 | missing           | HIGH   | FR-008 | Ví dụ: không thấy cơ chế chỉ-bổ-sung trong path/to/module.py khi ghi tasks.md | Thêm cơ chế bắt buộc chỉ bổ sung |

**Số liệu tóm tắt:**

- Số yêu cầu / tiêu chí chấp nhận đã kiểm tra
- Số quyết định trong kế hoạch đã kiểm tra
- Số nguyên tắc hiến chương đã kiểm tra (hoặc "bỏ qua — template")
- Số phát hiện theo loại khoảng trống (missing / partial / contradicts / unrequested)
- Số phát hiện theo mức độ nghiêm trọng

### 7. Bổ sung tác vụ hội tụ (hoặc báo đã hội tụ)

**Nếu có một hoặc nhiều phát hiện cần xử lý** (kết quả `tasks_appended`):

Bổ sung vào **cuối** `tasks.md`, theo quy ước bổ sung:

1. Quét mọi Task ID hiện có; gọi `M` là giá trị lớn nhất. Xác định số thứ tự giai đoạn tiếp theo `N`
   (giai đoạn lớn nhất hiện có + 1).
2. Ghi đúng một tiêu đề mục mới `## Giai đoạn N: Hội tụ`.
3. Xuất một mục checklist cho mỗi phát hiện cần xử lý, sắp CRITICAL/HIGH lên trước, gán
   ID có đệm số 0 `T{M+1:03d}, T{M+2:03d}, …`:

   ```markdown
   - [ ] T042 <mô tả dạng mệnh lệnh> theo <source-ref> (<gap-type>)
   ```

   `<source-ref>` truy vết tác vụ về nguồn gốc của nó: ví dụ `FR-003`, `SC-002`,
   `US1/AC2`, `plan: storage decision`, `Constitution II`.

   `<gap-type>` là một trong `missing`, `partial`, `contradicts`, `unrequested`.

   Các tác vụ xử lý vi phạm hiến chương PHẢI được xuất trước tiên và được mô tả là
   `CRITICAL`.
4. Không bao giờ dùng lại hay đánh số lại các ID hiện có. Nếu đã có một giai đoạn Hội tụ trước đó, thêm một giai đoạn mới,
   đánh số riêng, ở bên dưới — không đụng tới giai đoạn cũ.

**Nếu không có phát hiện nào cần xử lý** (kết quả `converged`):

- **Không** sửa `tasks.md` dưới bất kỳ hình thức nào — không thêm tiêu đề giai đoạn rỗng.
- Báo cáo: **"✅ Converged — phần triển khai đã đáp ứng đặc tả, kế hoạch và các tác vụ."**
- Kèm số liệu tóm tắt về những gì đã kiểm tra.

### 8. Đề xuất các bước tiếp theo (bàn giao)

- Với `tasks_appended`: nêu đã bổ sung bao nhiêu tác vụ vào giai đoạn nào, và khuyến nghị
  chạy `__SPECKIT_COMMAND_IMPLEMENT__` để hoàn thành chúng; lưu ý rằng lần chạy converge tiếp theo
  sẽ tìm thấy ít hơn hoặc không còn mục nào.
- Với `converged`: khuyến nghị chuyển sang review / mở PR. Không cần chạy implement thêm
  cho phạm vi đã đặc tả của tính năng này.

### 9. Kiểm tra hook của extension

Sau khi có kết quả, kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.

- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_converge`
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi tiếp tục như bình thường
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Báo kết quả hội tụ (`converged` hoặc `tasks_appended`) trong phiên trước khi liệt kê
  bất kỳ hook nào, để người dùng quyết định có chạy các lệnh tùy chọn tiếp theo hay không.
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook tùy chọn** (`optional: true`):

    ```text
    ## Hook của extension

    **Hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```

  - **Hook bắt buộc** (`optional: false`):

    ```text
    ## Hook của extension

    **Hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.

- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua
