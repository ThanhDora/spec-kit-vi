---
description: Tạo hoặc cập nhật đặc tả tính năng từ mô tả tính năng bằng ngôn ngữ tự nhiên.
handoffs:
  - label: Lập kế hoạch kỹ thuật
    agent: speckit.plan
    prompt: Lập kế hoạch cho đặc tả này. Tôi đang xây dựng bằng...
  - label: Làm rõ yêu cầu trong đặc tả
    agent: speckit.clarify
    prompt: Làm rõ các yêu cầu trong đặc tả
    send: true
scripts:
  sh: scripts/bash/resolve-template.sh spec-template --json
  ps: scripts/powershell/resolve-template.ps1 spec-template -Json
  py: scripts/python/resolve_template.py spec-template --json
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi viết đặc tả)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_specify`
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi tiếp tục như bình thường
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook tùy chọn** (`optional: true`):
    ```
    ## Hook của extension

    **Pre-hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```
  - **Hook bắt buộc** (`optional: false`):
    ```
    ## Hook của extension

    **Pre-hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}

    Chờ kết quả của lệnh hook trước khi chuyển sang phần Các bước thực hiện.
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua

## Các bước thực hiện

Phần văn bản người dùng gõ sau `__SPECKIT_COMMAND_SPECIFY__` trong tin nhắn kích hoạt lệnh **chính là** mô tả tính năng. Hãy coi như bạn luôn có sẵn nó trong cuộc trò chuyện này, kể cả khi `{ARGS}` hiển thị nguyên văn bên dưới. Đừng yêu cầu người dùng nhắc lại, trừ khi họ gửi lệnh trống.

Với mô tả tính năng đó, hãy làm như sau:

1. **Sinh một tên ngắn gọn** (2-4 từ) cho tính năng:
   - Phân tích mô tả tính năng và rút ra các từ khóa có ý nghĩa nhất
   - Tạo tên ngắn 2-4 từ thể hiện được bản chất của tính năng
   - Dùng dạng động từ-danh từ khi có thể (ví dụ "add-user-auth", "fix-payment-bug")
   - Giữ nguyên thuật ngữ kỹ thuật và từ viết tắt (OAuth2, API, JWT, v.v.)
   - Ngắn gọn nhưng đủ rõ để hiểu tính năng ngay khi nhìn qua
   - Tên ngắn sẽ dùng cho tên thư mục và branch, nên chỉ dùng chữ ASCII thường, số và dấu gạch ngang (tiếng Anh, hoặc tiếng Việt không dấu)
   - Ví dụ:
     - "Tôi muốn thêm chức năng xác thực người dùng" → "user-auth"
     - "Tích hợp OAuth2 cho API" → "oauth2-api-integration"
     - "Tạo dashboard phân tích số liệu" → "analytics-dashboard"
     - "Sửa lỗi timeout khi xử lý thanh toán" → "fix-payment-timeout"

2. **Tạo branch** (tùy chọn, qua hook):

   Nếu hook `before_specify` đã chạy thành công ở phần Kiểm tra trước khi thực thi bên trên, nó đã tạo/chuyển sang một git branch và xuất JSON chứa `BRANCH_NAME` và `FEATURE_NUM`. Ghi nhận các giá trị này để tham khảo, nhưng tên branch **không** quyết định tên thư mục đặc tả.

   Nếu người dùng cung cấp rõ `GIT_BRANCH_NAME`, hãy truyền nó cho hook để script tạo branch dùng đúng giá trị đó làm tên branch (bỏ qua toàn bộ bước sinh tiền tố/hậu tố).

3. **Tạo thư mục tính năng cho đặc tả**:

   Đặc tả nằm trong thư mục mặc định `specs/`, trừ khi người dùng cung cấp rõ `SPECIFY_FEATURE_DIRECTORY`.

   **Thứ tự xác định `SPECIFY_FEATURE_DIRECTORY`**:
   1. Nếu người dùng cung cấp rõ `SPECIFY_FEATURE_DIRECTORY` (ví dụ qua biến môi trường, đối số hoặc cấu hình), dùng nguyên giá trị đó
   2. Nếu không, tự sinh trong `specs/`:
      - Kiểm tra `.specify/init-options.json` để lấy `feature_numbering` (ưu tiên) hoặc `branch_numbering` (đã lỗi thời, chỉ dùng cho chuyển đổi — sẽ bị xóa trong một bản phát hành sau)
      - Nếu là `"timestamp"`: tiền tố là `YYYYMMDD-HHMMSS` (thời điểm hiện tại)
      - Nếu là `"sequential"` hoặc không có: tiền tố là `NNN` (số 3 chữ số tiếp theo còn trống sau khi quét các thư mục hiện có trong `specs/`)
      - Ghép tên thư mục: `<prefix>-<short-name>` (ví dụ `003-user-auth` hoặc `20260319-143022-user-auth`)
      - Đặt `SPECIFY_FEATURE_DIRECTORY` thành `specs/<directory-name>`
      - Nếu đã dùng `branch_numbering` (và không có `feature_numbering`), xuất một dòng cảnh báo: "⚠️ `branch_numbering` trong init-options.json đã lỗi thời. Hãy đổi tên thành `feature_numbering`."

   **Tạo thư mục và file đặc tả**:
   - Chạy `{SCRIPT}` từ thư mục gốc repository và parse `TEMPLATE_CONTENT` làm `spec-template` đang dùng. Bộ phân giải dùng chung ghép các ghi đè của dự án, lớp preset và lớp extension lên trên template lõi, bao gồm các chiến lược `append`, `prepend` và `wrap`. Nếu thất bại, dừng lại và báo lỗi phân giải; không tiếp tục chỉ với một lớp template đóng góp.
   - `mkdir -p SPECIFY_FEATURE_DIRECTORY`
   - Ghi `TEMPLATE_CONTENT` vào `SPECIFY_FEATURE_DIRECTORY/spec.md` làm điểm khởi đầu. Không sao chép file template từ ổ đĩa thay cho bước này: khi một preset ghép `spec-template`, không có file đơn lẻ nào chứa toàn bộ template.
   - Đặt `SPEC_FILE` thành `SPECIFY_FEATURE_DIRECTORY/spec.md`
   - Lưu đường dẫn đã xác định vào `.specify/feature.json`:
     ```json
     {
       "feature_directory": "<resolved feature dir>"
     }
     ```
     Ghi giá trị đường dẫn thư mục thực tế đã xác định (ví dụ `specs/003-user-auth`), không ghi nguyên văn chuỗi `SPECIFY_FEATURE_DIRECTORY`.
     Điều này giúp các lệnh phía sau (`__SPECKIT_COMMAND_PLAN__`, `__SPECKIT_COMMAND_TASKS__`, v.v.) tìm được thư mục tính năng mà không phụ thuộc vào quy ước đặt tên git branch.

   **QUAN TRỌNG**:
   - Mỗi lần gọi `__SPECKIT_COMMAND_SPECIFY__` chỉ được tạo một tính năng
   - Tên thư mục đặc tả và tên git branch là độc lập với nhau — chúng có thể giống nhau, nhưng đó là lựa chọn của người dùng
   - Thư mục và file đặc tả luôn do lệnh này tạo, không bao giờ do hook tạo

4. Dùng `TEMPLATE_CONTENT` để nắm các mục bắt buộc.

5. **NẾU CÓ**: Nạp `/memory/constitution.md` để lấy các nguyên tắc dự án và ràng buộc quản trị.

6. Thực hiện theo luồng sau:
    1. Parse mô tả của người dùng từ đối số
       Nếu rỗng: LỖI "Chưa có mô tả tính năng"
    2. Rút ra các khái niệm chính từ mô tả
       Xác định: tác nhân, hành động, dữ liệu, ràng buộc
    3. Với những khía cạnh chưa rõ:
       - Đưa ra phỏng đoán có cơ sở dựa trên bối cảnh và tiêu chuẩn ngành
       - Chỉ đánh dấu [NEEDS CLARIFICATION: câu hỏi cụ thể] khi:
         - Lựa chọn đó ảnh hưởng đáng kể tới phạm vi tính năng hoặc trải nghiệm người dùng
         - Có nhiều cách hiểu hợp lý dẫn tới hệ quả khác nhau
         - Không có giá trị mặc định hợp lý nào
       - **GIỚI HẠN: Tổng cộng tối đa 3 dấu [NEEDS CLARIFICATION]**
       - Xếp ưu tiên các điểm cần làm rõ theo mức ảnh hưởng: phạm vi > bảo mật/quyền riêng tư > trải nghiệm người dùng > chi tiết kỹ thuật
    4. Điền mục Kịch bản người dùng & Kiểm thử
       Nếu không có luồng người dùng rõ ràng: LỖI "Không xác định được kịch bản người dùng"
    5. Sinh các yêu cầu chức năng
       Mỗi yêu cầu phải kiểm thử được
       Dùng giá trị mặc định hợp lý cho các chi tiết chưa được nêu (ghi lại giả định trong mục Giả định)
    6. Định nghĩa tiêu chí thành công
       Tạo các kết quả đo lường được, không phụ thuộc công nghệ
       Bao gồm cả chỉ số định lượng (thời gian, hiệu năng, khối lượng) và thước đo định tính (mức độ hài lòng, tỷ lệ hoàn thành tác vụ)
       Mỗi tiêu chí phải kiểm chứng được mà không cần biết chi tiết triển khai
    7. Xác định các thực thể chính (nếu có liên quan tới dữ liệu)
    8. Trả về: THÀNH CÔNG (đặc tả sẵn sàng để lập kế hoạch)

7. Ghi đặc tả vào SPEC_FILE theo cấu trúc của template, thay các placeholder bằng chi tiết cụ thể rút ra từ mô tả tính năng (đối số) nhưng vẫn giữ nguyên thứ tự và heading của các mục.

8. **Kiểm tra chất lượng đặc tả**: Sau khi viết bản đặc tả đầu tiên, kiểm tra nó theo các tiêu chí chất lượng:

   a. **Tạo checklist chất lượng đặc tả**: Sinh file checklist tại `SPECIFY_FEATURE_DIRECTORY/checklists/requirements.md` theo cấu trúc template checklist với các mục kiểm tra sau:

      ```markdown
      # Checklist chất lượng đặc tả: [FEATURE NAME]

      **Mục đích**: Kiểm tra mức độ đầy đủ và chất lượng của đặc tả trước khi lập kế hoạch
      **Ngày tạo**: [DATE]
      **Tính năng**: [Link tới spec.md]

      ## Chất lượng nội dung

      - [ ] Không có chi tiết triển khai (ngôn ngữ, framework, API)
      - [ ] Tập trung vào giá trị cho người dùng và nhu cầu kinh doanh
      - [ ] Viết cho các bên liên quan không chuyên về kỹ thuật
      - [ ] Đã hoàn thành mọi mục bắt buộc

      ## Mức độ đầy đủ của yêu cầu

      - [ ] Không còn dấu [NEEDS CLARIFICATION] nào
      - [ ] Yêu cầu kiểm thử được và rõ ràng
      - [ ] Tiêu chí thành công đo lường được
      - [ ] Tiêu chí thành công không phụ thuộc công nghệ (không có chi tiết triển khai)
      - [ ] Đã định nghĩa mọi kịch bản chấp nhận
      - [ ] Đã xác định các trường hợp biên
      - [ ] Phạm vi được giới hạn rõ ràng
      - [ ] Đã xác định các phụ thuộc và giả định

      ## Mức độ sẵn sàng của tính năng

      - [ ] Mọi yêu cầu chức năng đều có tiêu chí chấp nhận rõ ràng
      - [ ] Kịch bản người dùng bao phủ các luồng chính
      - [ ] Tính năng đạt các kết quả đo lường được đã định nghĩa trong Tiêu chí thành công
      - [ ] Không có chi tiết triển khai lọt vào đặc tả

      ## Ghi chú

      - Các mục đánh dấu chưa hoàn thành cần cập nhật đặc tả trước khi chạy `__SPECKIT_COMMAND_CLARIFY__` hoặc `__SPECKIT_COMMAND_PLAN__`
      ```

   b. **Chạy kiểm tra**: Review đặc tả theo từng mục trong checklist:
      - Với mỗi mục, xác định đạt hay không đạt
      - Ghi lại các vấn đề cụ thể tìm thấy (trích dẫn các phần liên quan trong đặc tả)

   c. **Xử lý kết quả kiểm tra**:

      - **Nếu mọi mục đều đạt**: Đánh dấu checklist hoàn tất và chuyển tới mục Hook bắt buộc sau khi thực thi

      - **Nếu có mục không đạt (không tính [NEEDS CLARIFICATION])**:
        1. Liệt kê các mục không đạt và vấn đề cụ thể
        2. Cập nhật đặc tả để xử lý từng vấn đề
        3. Chạy lại bước kiểm tra cho tới khi mọi mục đều đạt (tối đa 3 vòng)
        4. Nếu sau 3 vòng vẫn không đạt, ghi các vấn đề còn lại vào phần ghi chú của checklist và cảnh báo người dùng

      - **Nếu vẫn còn dấu [NEEDS CLARIFICATION]**:
        1. Rút ra mọi dấu [NEEDS CLARIFICATION: ...] từ đặc tả
        2. **KIỂM TRA GIỚI HẠN**: Nếu có nhiều hơn 3 dấu, chỉ giữ 3 dấu quan trọng nhất (theo mức ảnh hưởng tới phạm vi/bảo mật/UX) và đưa ra phỏng đoán có cơ sở cho phần còn lại
        3. Với mỗi điểm cần làm rõ (tối đa 3), đưa các lựa chọn cho người dùng theo định dạng sau:

           ```markdown
           ## Câu hỏi [N]: [Chủ đề]

           **Bối cảnh**: [Trích phần liên quan trong đặc tả]

           **Điều cần biết**: [Câu hỏi cụ thể từ dấu NEEDS CLARIFICATION]

           **Các câu trả lời gợi ý**:

           | Lựa chọn | Câu trả lời | Hệ quả |
           |----------|-------------|--------|
           | A        | [Câu trả lời gợi ý thứ nhất] | [Điều này có ý nghĩa gì với tính năng] |
           | B        | [Câu trả lời gợi ý thứ hai] | [Điều này có ý nghĩa gì với tính năng] |
           | C        | [Câu trả lời gợi ý thứ ba] | [Điều này có ý nghĩa gì với tính năng] |
           | Tùy chọn | Tự đưa ra câu trả lời của bạn | [Giải thích cách nhập câu trả lời riêng] |

           **Lựa chọn của bạn**: _[Chờ người dùng trả lời]_
           ```

        4. **QUAN TRỌNG - Định dạng bảng**: Đảm bảo bảng markdown được định dạng đúng:
           - Khoảng cách nhất quán, các dấu gạch đứng thẳng hàng
           - Mỗi ô có khoảng trắng quanh nội dung: `| Content |` chứ không phải `|Content|`
           - Dòng phân cách tiêu đề phải có ít nhất 3 dấu gạch ngang: `|--------|`
           - Kiểm tra bảng hiển thị đúng trong chế độ xem trước markdown
        5. Đánh số câu hỏi tuần tự (Q1, Q2, Q3 - tổng cộng tối đa 3)
        6. Trình bày tất cả câu hỏi cùng lúc rồi mới chờ trả lời
        7. Chờ người dùng trả lời lựa chọn cho tất cả câu hỏi (ví dụ "Q1: A, Q2: Tùy chọn - [chi tiết], Q3: B")
        8. Cập nhật đặc tả bằng cách thay từng dấu [NEEDS CLARIFICATION] bằng câu trả lời người dùng đã chọn hoặc cung cấp
        9. Chạy lại bước kiểm tra sau khi đã giải quyết mọi điểm cần làm rõ

   d. **Cập nhật checklist**: Sau mỗi vòng kiểm tra, cập nhật file checklist với trạng thái đạt/không đạt hiện tại

## Hook bắt buộc sau khi thực thi

**Bạn PHẢI hoàn thành mục này trước khi báo hoàn tất cho người dùng.**

Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu không tồn tại, hoặc không có hook nào đăng ký dưới `hooks.after_specify`, chuyển thẳng tới phần Báo cáo hoàn tất.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_specify`.
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi chuyển tới phần Báo cáo hoàn tất.
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook bắt buộc** (`optional: false`) — **Bạn PHẢI xuất `EXECUTE_COMMAND:` cho mỗi hook bắt buộc**:
    ```
    ## Hook của extension

    **Hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
  - **Hook tùy chọn** (`optional: true`):
    ```
    ## Hook của extension

    **Hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```

## Báo cáo hoàn tất

Báo hoàn tất cho người dùng, kèm:
- `SPECIFY_FEATURE_DIRECTORY` — đường dẫn thư mục tính năng
- `SPEC_FILE` — đường dẫn file đặc tả
- Tóm tắt kết quả checklist
- Mức độ sẵn sàng cho giai đoạn tiếp theo (`__SPECKIT_COMMAND_CLARIFY__` hoặc `__SPECKIT_COMMAND_PLAN__`)

**LƯU Ý:** Việc tạo branch do hook `before_specify` (git extension) đảm nhận. Việc tạo thư mục và file đặc tả luôn do lệnh lõi này đảm nhận.

## Hướng dẫn nhanh

- Tập trung vào việc người dùng cần **GÌ** và **VÌ SAO**.
- Tránh nói LÀM THẾ NÀO để triển khai (không tech stack, API, cấu trúc code).
- Viết cho các bên liên quan phía kinh doanh, không phải cho lập trình viên.
- KHÔNG tạo checklist nhúng trong đặc tả. Việc đó thuộc về một lệnh riêng.

### Yêu cầu về các mục

- **Mục bắt buộc**: Phải hoàn thành cho mọi tính năng
- **Mục tùy chọn**: Chỉ thêm khi liên quan tới tính năng
- Khi một mục không áp dụng, xóa hẳn mục đó (đừng để "N/A")

### Dành cho AI khi sinh đặc tả

Khi tạo đặc tả này từ prompt của người dùng:

1. **Phỏng đoán có cơ sở**: Dùng bối cảnh, tiêu chuẩn ngành và các pattern phổ biến để lấp chỗ trống
2. **Ghi lại giả định**: Ghi các giá trị mặc định hợp lý vào mục Giả định
3. **Hạn chế điểm cần làm rõ**: Tối đa 3 dấu [NEEDS CLARIFICATION], chỉ dùng cho những quyết định quan trọng:
   - Ảnh hưởng đáng kể tới phạm vi tính năng hoặc trải nghiệm người dùng
   - Có nhiều cách hiểu hợp lý dẫn tới hệ quả khác nhau
   - Không có giá trị mặc định hợp lý nào
4. **Xếp ưu tiên điểm cần làm rõ**: phạm vi > bảo mật/quyền riêng tư > trải nghiệm người dùng > chi tiết kỹ thuật
5. **Suy nghĩ như một tester**: Mọi yêu cầu mơ hồ đều phải trượt mục checklist "kiểm thử được và rõ ràng"
6. **Những phần thường cần làm rõ** (chỉ khi không có giá trị mặc định hợp lý):
   - Phạm vi và giới hạn tính năng (bao gồm/loại trừ những trường hợp sử dụng cụ thể)
   - Loại người dùng và quyền hạn (nếu có thể có nhiều cách hiểu mâu thuẫn)
   - Yêu cầu bảo mật/tuân thủ (khi có ý nghĩa quan trọng về pháp lý/tài chính)

**Ví dụ về giá trị mặc định hợp lý** (đừng hỏi về những điều này):

- Lưu giữ dữ liệu: Theo thông lệ chuẩn của ngành trong lĩnh vực đó
- Mục tiêu hiệu năng: Theo kỳ vọng chuẩn của ứng dụng web/mobile, trừ khi có nêu rõ
- Xử lý lỗi: Thông báo thân thiện với người dùng, kèm phương án dự phòng phù hợp
- Phương thức xác thực: Dựa trên session chuẩn hoặc OAuth2 cho ứng dụng web
- Pattern tích hợp: Dùng pattern phù hợp với dự án (REST/GraphQL cho dịch vụ web, gọi hàm cho thư viện, đối số CLI cho công cụ, v.v.)

### Hướng dẫn về tiêu chí thành công

Tiêu chí thành công phải:

1. **Đo lường được**: Có chỉ số cụ thể (thời gian, tỷ lệ phần trăm, số lượng, tần suất)
2. **Không phụ thuộc công nghệ**: Không nhắc tới framework, ngôn ngữ, cơ sở dữ liệu hay công cụ
3. **Lấy người dùng làm trọng tâm**: Mô tả kết quả từ góc nhìn người dùng/kinh doanh, không phải bên trong hệ thống
4. **Kiểm chứng được**: Có thể kiểm thử/kiểm chứng mà không cần biết chi tiết triển khai

**Ví dụ tốt**:

- "Người dùng hoàn tất thanh toán trong vòng dưới 3 phút"
- "Hệ thống hỗ trợ 10.000 người dùng đồng thời"
- "95% lượt tìm kiếm trả kết quả trong vòng dưới 1 giây"
- "Tỷ lệ hoàn thành tác vụ tăng 40%"

**Ví dụ chưa tốt** (tập trung vào triển khai):

- "Thời gian phản hồi API dưới 200ms" (quá kỹ thuật, nên dùng "Người dùng thấy kết quả ngay lập tức")
- "Cơ sở dữ liệu xử lý được 1000 TPS" (chi tiết triển khai, nên dùng chỉ số hướng tới người dùng)
- "Component React render hiệu quả" (phụ thuộc framework)
- "Tỷ lệ cache hit của Redis trên 80%" (phụ thuộc công nghệ)

## Hoàn tất khi

- [ ] Đặc tả đã được ghi vào `SPEC_FILE` và kiểm tra theo checklist chất lượng
- [ ] Đã gọi hoặc bỏ qua các hook của extension theo đúng quy tắc trong mục Hook bắt buộc sau khi thực thi ở trên
- [ ] Đã báo hoàn tất cho người dùng, kèm thư mục tính năng, đường dẫn file đặc tả và kết quả checklist
