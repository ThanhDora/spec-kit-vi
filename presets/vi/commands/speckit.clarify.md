---
description: Xác định những phần chưa được đặc tả đủ trong đặc tả tính năng hiện tại bằng tối đa 5 câu hỏi làm rõ có trọng tâm, rồi ghi câu trả lời trở lại vào đặc tả.
handoffs:
  - label: Lập kế hoạch kỹ thuật
    agent: speckit.plan
    prompt: Lập kế hoạch cho đặc tả này. Tôi đang xây dựng bằng...
scripts:
   sh: scripts/bash/check-prerequisites.sh --json --paths-only
   ps: scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly
   py: scripts/python/check_prerequisites.py --json --paths-only
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi làm rõ)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_clarify`
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

Mục tiêu: Phát hiện và giảm bớt những chỗ mơ hồ hoặc những điểm còn thiếu quyết định trong đặc tả tính năng đang làm, đồng thời ghi các nội dung làm rõ trực tiếp vào file đặc tả.

Lưu ý: Workflow làm rõ này cần được chạy (và hoàn tất) TRƯỚC khi gọi `__SPECKIT_COMMAND_PLAN__`. Nếu người dùng nói rõ là bỏ qua bước làm rõ (ví dụ đang làm spike thăm dò), bạn có thể tiếp tục, nhưng phải cảnh báo rằng rủi ro phải làm lại ở các bước sau sẽ tăng lên.

Các bước thực thi:

1. Chạy `{SCRIPT}` từ thư mục gốc repo **một lần** (chế độ kết hợp `--json --paths-only` / `-Json -PathsOnly`). Parse các trường tối thiểu trong JSON:
   - `FEATURE_DIR`
   - `FEATURE_SPEC`
   - (Có thể lấy thêm `IMPL_PLAN`, `TASKS` cho các luồng nối tiếp về sau.)
   - Nếu parse JSON thất bại, dừng lại và hướng dẫn người dùng chạy lại `__SPECKIT_COMMAND_SPECIFY__` hoặc kiểm tra môi trường feature branch.
   - Với dấu nháy đơn trong đối số như "I'm Groot", dùng cú pháp escape: ví dụ 'I'\''m Groot' (hoặc dùng nháy kép nếu được: "I'm Groot").

2. **NẾU CÓ**: Nạp `/memory/constitution.md` để lấy các nguyên tắc dự án và ràng buộc quản trị.

3. Nạp file đặc tả hiện tại. Quét có cấu trúc để tìm chỗ mơ hồ và đánh giá độ phủ theo bộ phân loại dưới đây. Với mỗi nhóm, đánh dấu trạng thái: Rõ ràng / Một phần / Thiếu. Tạo một bản đồ độ phủ nội bộ để xếp ưu tiên (không xuất nguyên văn bản đồ trừ khi sẽ không hỏi câu nào).

   Phạm vi & hành vi chức năng:
   - Mục tiêu cốt lõi của người dùng & tiêu chí thành công
   - Các tuyên bố rõ ràng về những gì nằm ngoài phạm vi
   - Phân biệt vai trò người dùng / persona

   Nghiệp vụ & mô hình dữ liệu:
   - Thực thể, thuộc tính, quan hệ
   - Quy tắc định danh & tính duy nhất
   - Vòng đời/chuyển trạng thái
   - Giả định về khối lượng / quy mô dữ liệu

   Tương tác & luồng UX:
   - Các hành trình / trình tự quan trọng của người dùng
   - Trạng thái lỗi/rỗng/đang tải
   - Ghi chú về khả năng tiếp cận hoặc bản địa hóa

   Thuộc tính chất lượng phi chức năng:
   - Hiệu năng (mục tiêu về độ trễ, thông lượng)
   - Khả năng mở rộng (theo chiều ngang/dọc, giới hạn)
   - Độ tin cậy & tính sẵn sàng (uptime, kỳ vọng phục hồi)
   - Khả năng quan sát (log, metric, tín hiệu tracing)
   - Bảo mật & quyền riêng tư (xác thực/phân quyền, bảo vệ dữ liệu, giả định về mối đe dọa)
   - Ràng buộc về tuân thủ / quy định pháp lý (nếu có)

   Tích hợp & phụ thuộc bên ngoài:
   - Dịch vụ/API bên ngoài và các kiểu lỗi có thể xảy ra
   - Định dạng nhập/xuất dữ liệu
   - Giả định về giao thức/phiên bản

   Trường hợp biên & xử lý lỗi:
   - Các kịch bản tiêu cực
   - Giới hạn tần suất / throttling
   - Giải quyết xung đột (ví dụ chỉnh sửa đồng thời)

   Ràng buộc & đánh đổi:
   - Ràng buộc kỹ thuật (ngôn ngữ, lưu trữ, hosting)
   - Các đánh đổi rõ ràng hoặc phương án đã bị loại

   Thuật ngữ & tính nhất quán:
   - Các thuật ngữ chuẩn trong bảng thuật ngữ
   - Các từ đồng nghĩa nên tránh / thuật ngữ đã lỗi thời

   Tín hiệu hoàn tất:
   - Khả năng kiểm thử của tiêu chí chấp nhận
   - Các chỉ báo đo lường được theo kiểu Definition of Done

   Linh tinh / placeholder:
   - Các dấu TODO / quyết định chưa được chốt
   - Tính từ mơ hồ ("mạnh mẽ", "trực quan") chưa được định lượng

   Với mỗi nhóm ở trạng thái Một phần hoặc Thiếu, thêm một câu hỏi ứng viên, trừ khi:
   - Việc làm rõ không làm thay đổi đáng kể cách triển khai hay chiến lược kiểm chứng
   - Nội dung đó cụ thể là về phương pháp triển khai, so sánh tech stack hoặc phân rã tác vụ (ghi chú nội bộ)

4. Sinh (nội bộ) một hàng đợi câu hỏi làm rõ ứng viên đã xếp ưu tiên (tối đa 5). KHÔNG xuất tất cả cùng lúc. Áp dụng các ràng buộc sau:
    - Tổng cộng tối đa 5 câu hỏi trong cả phiên.
    - Mỗi câu hỏi phải trả lời được bằng MỘT TRONG HAI cách:
       - Chọn nhanh một đáp án trắc nghiệm (2–5 phương án khác biệt, loại trừ lẫn nhau), HOẶC
       - Trả lời bằng một từ / một cụm ngắn (ràng buộc rõ: "Trả lời trong <=5 từ").
    - Chỉ đưa vào những câu hỏi mà câu trả lời ảnh hưởng đáng kể tới kiến trúc, mô hình dữ liệu, phân rã tác vụ, thiết kế kiểm thử, hành vi UX, mức sẵn sàng vận hành hoặc kiểm chứng tuân thủ.
    - Đảm bảo cân bằng độ phủ giữa các nhóm: ưu tiên các nhóm chưa giải quyết có ảnh hưởng lớn nhất; tránh hỏi hai câu ít ảnh hưởng trong khi một vùng ảnh hưởng lớn (ví dụ tư thế bảo mật) vẫn chưa được giải quyết.
    - Loại bỏ những câu đã có câu trả lời, các sở thích văn phong vụn vặt, hoặc chi tiết thực thi ở mức kế hoạch (trừ khi chúng chặn tính đúng đắn).
    - Ưu tiên những điểm làm rõ giúp giảm rủi ro phải làm lại về sau hoặc ngăn test chấp nhận bị lệch.
    - Nếu còn hơn 5 nhóm chưa được giải quyết, chọn 5 nhóm hàng đầu theo quy tắc (Mức ảnh hưởng * Mức không chắc chắn).

5. Vòng hỏi tuần tự (tương tác):
    - Đưa ra ĐÚNG MỘT câu hỏi mỗi lần.
    - **Chất lượng câu hỏi (áp dụng cho mọi câu hỏi, dù trắc nghiệm hay trả lời ngắn):**
       - Mở đầu bằng `**Câu hỏi:**`, theo sau là một câu hỏi đầy đủ kết thúc bằng `?`. Phần nội dung trước dấu `?` phải tự đứng được.
       - KHÔNG BAO GIỜ dùng nhãn chủ đề, heading của mục hay mã yêu cầu làm câu hỏi. Ví dụ `Ma trận thiết bị/runtime để nghiệm thu (FR-023)` là KHÔNG HỢP LỆ — đó là một nhãn, không phải câu hỏi.
       - Sau dấu `?`, chỉ được phép thêm một mã yêu cầu/câu hỏi tùy chọn trong ngoặc đơn. Định dạng chính xác: `**Câu hỏi:** <câu hỏi>?` hoặc `**Câu hỏi:** <câu hỏi>? (FR-023)`. Không bao giờ đặt mã trước dấu `?`, và không bao giờ dùng mã (đứng riêng hoặc kèm nhãn chủ đề) làm toàn bộ câu hỏi.
       - Ngay sau dòng câu hỏi, thêm một câu "Vì sao quan trọng" bằng ngôn ngữ dễ hiểu (điều gì bị ảnh hưởng tới việc nghiệm thu hoặc phát hành) trước phần đề xuất/các phương án.
       - Dùng từ ngữ đời thường; chỉ dùng thuật ngữ chuyên môn nếu được giải thích ngay trong câu. Tự kiểm tra: một người không biết Spec Kit vẫn phải trả lời được chỉ dựa vào dòng câu hỏi. Ngắn gọn thì được; nhãn khó hiểu thì không.
    - Với câu hỏi trắc nghiệm:
       - **Phân tích mọi phương án** và xác định **phương án phù hợp nhất** dựa trên:
          - Best practice cho loại dự án
          - Các pattern phổ biến trong những bản triển khai tương tự
          - Giảm rủi ro (bảo mật, hiệu năng, khả năng bảo trì)
          - Sự phù hợp với mọi mục tiêu hay ràng buộc rõ ràng của dự án có trong đặc tả
       - Đưa **phương án đề xuất lên đầu, thật nổi bật**, kèm lập luận rõ ràng (1-2 câu giải thích vì sao đây là lựa chọn tốt nhất).
       - Định dạng: `**Đề xuất:** Phương án [X] - <lý do>`
       - Sau đó trình bày mọi phương án dưới dạng bảng Markdown:

       | Phương án | Mô tả |
       |-----------|-------|
       | A | <Mô tả phương án A> |
       | B | <Mô tả phương án B> |
       | C | <Mô tả phương án C> (thêm D/E khi cần, tối đa 5) |
       | Ngắn | Đưa ra một câu trả lời ngắn khác (<=5 từ) (Chỉ thêm khi phù hợp có phương án trả lời tự do) |

       - Sau bảng, thêm: `Bạn có thể trả lời bằng chữ cái của phương án (ví dụ "A"), đồng ý với đề xuất bằng cách trả lời "có" hoặc "đề xuất", hoặc tự đưa ra câu trả lời ngắn.`
    - Với kiểu câu hỏi trả lời ngắn (không có các phương án rời rạc có ý nghĩa):
       - Đưa ra **câu trả lời gợi ý** dựa trên best practice và bối cảnh.
       - Định dạng: `**Gợi ý:** <câu trả lời bạn đề xuất> - <lý do ngắn gọn>`
       - Sau đó xuất: `Định dạng: Câu trả lời ngắn (<=5 từ). Bạn có thể đồng ý với gợi ý bằng cách trả lời "có" hoặc "gợi ý", hoặc tự đưa ra câu trả lời.`
    - Sau khi người dùng trả lời:
       - Nếu người dùng trả lời "có", "đề xuất" hoặc "gợi ý" (hoặc "yes", "recommended", "suggested"), dùng đề xuất/gợi ý bạn đã nêu trước đó làm câu trả lời.
       - Nếu không, kiểm tra câu trả lời có khớp với một phương án hoặc đáp ứng ràng buộc <=5 từ không.
       - Nếu còn mơ hồ, hỏi nhanh để làm rõ (vẫn tính là cùng một câu hỏi; không chuyển sang câu tiếp theo).
       - Khi đã thỏa đáng, ghi lại trong bộ nhớ làm việc (chưa ghi ra đĩa) và chuyển sang câu hỏi tiếp theo trong hàng đợi.
    - Dừng hỏi thêm khi:
       - Mọi điểm mơ hồ quan trọng đã được giải quyết sớm (các câu còn lại trong hàng đợi trở nên không cần thiết), HOẶC
       - Người dùng báo đã xong ("xong", "được rồi", "không hỏi nữa", hoặc "done", "good", "no more"), HOẶC
       - Bạn đã hỏi đủ 5 câu.
    - Không bao giờ tiết lộ trước các câu hỏi còn trong hàng đợi.
    - Nếu ngay từ đầu không có câu hỏi hợp lệ nào, báo ngay là không có điểm mơ hồ quan trọng nào.

6. Tích hợp sau MỖI câu trả lời được chấp nhận (cập nhật tăng dần):
    - Duy trì biểu diễn trong bộ nhớ của đặc tả (nạp một lần lúc bắt đầu) cùng nội dung thô của file.
    - Với câu trả lời đầu tiên được tích hợp trong phiên này:
       - Đảm bảo có mục `## Làm rõ` (nếu chưa có, tạo ngay sau mục bối cảnh/tổng quan cấp cao nhất theo template đặc tả).
       - Bên dưới mục đó, tạo (nếu chưa có) tiêu đề phụ `### Phiên YYYY-MM-DD` cho ngày hôm nay.
    - Thêm một dòng gạch đầu dòng ngay sau khi câu trả lời được chấp nhận: `- Hỏi: <câu hỏi> → Đáp: <câu trả lời cuối cùng>`.
    - Sau đó áp dụng ngay nội dung làm rõ vào (các) mục phù hợp nhất:
       - Mơ hồ về chức năng → Cập nhật hoặc thêm một gạch đầu dòng trong Yêu cầu chức năng.
       - Tương tác người dùng / phân biệt tác nhân → Cập nhật User story hoặc mục con Tác nhân (nếu có) với vai trò, ràng buộc hay kịch bản đã được làm rõ.
       - Cấu trúc dữ liệu / thực thể → Cập nhật Mô hình dữ liệu (thêm trường, kiểu, quan hệ) và giữ nguyên thứ tự; ghi chú ngắn gọn các ràng buộc được thêm.
       - Ràng buộc phi chức năng → Thêm/sửa tiêu chí đo lường được trong Tiêu chí thành công > Kết quả đo lường được (chuyển tính từ mơ hồ thành chỉ số hoặc mục tiêu cụ thể).
       - Trường hợp biên / luồng tiêu cực → Thêm một gạch đầu dòng mới trong Trường hợp biên / Xử lý lỗi (hoặc tạo mục con đó nếu template có sẵn placeholder).
       - Xung đột thuật ngữ → Chuẩn hóa thuật ngữ trên toàn bộ đặc tả; chỉ giữ thuật ngữ gốc khi cần bằng cách thêm `(trước đây gọi là "X")` một lần.
    - Nếu nội dung làm rõ khiến một phát biểu mơ hồ trước đó không còn đúng, hãy thay phát biểu đó thay vì viết trùng; không để lại nội dung lỗi thời mâu thuẫn.
    - Lưu file đặc tả SAU mỗi lần tích hợp để giảm rủi ro mất bối cảnh (ghi đè nguyên khối).
    - Giữ nguyên định dạng: không sắp xếp lại các mục không liên quan; giữ nguyên thứ bậc heading.
    - Giữ mỗi nội dung làm rõ được chèn vào ở mức tối thiểu và kiểm thử được (tránh lan man).

7. Kiểm tra (thực hiện sau MỖI lần ghi và một lượt cuối):
   - Phiên làm rõ có đúng một gạch đầu dòng cho mỗi câu trả lời được chấp nhận (không trùng lặp).
   - Tổng số câu hỏi đã hỏi (được chấp nhận) ≤ 5.
   - Các mục đã cập nhật không còn placeholder mơ hồ nào mà câu trả lời mới lẽ ra đã giải quyết.
   - Không còn phát biểu cũ nào mâu thuẫn (quét để xóa các lựa chọn thay thế giờ đã không còn hợp lệ).
   - Cấu trúc Markdown hợp lệ; chỉ được thêm các heading mới: `## Làm rõ`, `### Phiên YYYY-MM-DD`.
   - Nhất quán thuật ngữ: dùng cùng một thuật ngữ chuẩn ở mọi mục đã cập nhật.

8. Ghi đặc tả đã cập nhật trở lại `FEATURE_SPEC`.

9. **Kiểm tra lại checklist chất lượng đặc tả** (nếu có):
   - Kiểm tra `FEATURE_DIR/checklists/requirements.md` có tồn tại không.
   - Nếu KHÔNG tồn tại, lặng lẽ bỏ qua bước này.
   - Nếu có:
     1. Đọc file checklist.
     2. Xác định mọi dòng checkbox dạng task list của GitHub — các dòng khớp `- [ ]`, `- [x]` hoặc `- [X]` (không phân biệt hoa thường, chấp nhận khoảng trắng đầu dòng với các mục lồng nhau) nằm ngoài code fence. Bỏ qua mọi nội dung khác (heading, ghi chú, gạch đầu dòng không có checkbox, metadata).
     3. Với mỗi dòng checkbox, ghi lại trạng thái hiện tại (đã đánh dấu hay chưa) và nội dung mục vào danh sách ảnh chụp trước.
     4. Đánh giá lại từng mục checkbox theo đặc tả **đã cập nhật** (phiên bản vừa lưu ở bước 7).
     5. Với mỗi mục checkbox, chỉ cập nhật khi trạng thái đã đánh dấu/chưa đánh dấu thực sự thay đổi:
        - Nếu mục giờ đạt và trước đó chưa đánh dấu: đổi `[ ]` thành `[x]`.
        - Nếu mục giờ không đạt và trước đó đã đánh dấu: đổi `[x]`/`[X]` thành `[ ]`.
        - Nếu trạng thái không đổi: giữ nguyên dấu (giữ nguyên chữ hoa/thường để tránh diff vô nghĩa).
     6. Lưu file checklist đã cập nhật. **Chỉ bật/tắt phần dấu `[ ]`/`[x]` của những dòng checkbox có trạng thái thay đổi.** Mọi nội dung khác của file — heading, metadata, ghi chú, thứ tự dòng, khoảng trắng — phải giữ nguyên để tránh diff gây nhiễu.
     7. So sánh ảnh chụp trước với trạng thái hiện tại để tính ba danh sách cho Báo cáo hoàn tất:
        - **Mới đạt**: các mục chuyển từ chưa đánh dấu sang đã đánh dấu.
        - **Bị thụt lùi**: các mục chuyển từ đã đánh dấu sang chưa đánh dấu.
        - **Vẫn chưa đánh dấu**: các mục vẫn chưa được đánh dấu.
     8. Ghi lại số mục đạt trước/sau dưới dạng số mục đã đánh dấu/tổng số mục checkbox (ví dụ "12/16 → 15/16 mục đạt").

Quy tắc hành xử:

- Nếu không tìm thấy điểm mơ hồ có ý nghĩa nào (hoặc mọi câu hỏi tiềm năng đều ít ảnh hưởng), trả lời: "Không phát hiện điểm mơ hồ quan trọng nào cần làm rõ chính thức." và đề xuất đi tiếp.
- Nếu thiếu file đặc tả, hướng dẫn người dùng chạy `__SPECKIT_COMMAND_SPECIFY__` trước (không tạo đặc tả mới ở đây).
- Không bao giờ hỏi quá 5 câu (việc hỏi lại để làm rõ cho cùng một câu không tính là câu hỏi mới).
- Tránh các câu hỏi phỏng đoán về tech stack, trừ khi việc thiếu thông tin đó chặn sự rõ ràng về chức năng.
- Tôn trọng tín hiệu dừng sớm của người dùng ("dừng", "xong", "tiếp tục", hoặc "stop", "done", "proceed").
- Nếu không hỏi câu nào vì độ phủ đã đầy đủ, xuất một bản tóm tắt độ phủ ngắn gọn (mọi nhóm đều Rõ ràng) rồi đề xuất đi tiếp.
- Nếu đã hết số câu hỏi mà vẫn còn nhóm có ảnh hưởng lớn chưa giải quyết, gắn cờ rõ ràng cho chúng ở trạng thái Để lại, kèm lý do.

Bối cảnh để xếp ưu tiên: {ARGS}

## Hook bắt buộc sau khi thực thi

**Bạn PHẢI hoàn thành mục này trước khi báo hoàn tất cho người dùng.**

Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu không tồn tại, hoặc không có hook nào đăng ký dưới `hooks.after_clarify`, chuyển thẳng tới phần Báo cáo hoàn tất.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_clarify`.
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

Báo hoàn tất (sau khi vòng hỏi kết thúc hoặc dừng sớm):
- Số câu hỏi đã hỏi & đã được trả lời.
- Đường dẫn tới đặc tả đã cập nhật.
- Các mục đã chỉnh sửa (liệt kê tên).
- Trạng thái checklist chất lượng đặc tả (nếu `FEATURE_DIR/checklists/requirements.md` đã được kiểm tra lại): hiển thị số mục đạt trước/sau (ví dụ "Checklist chất lượng đặc tả: 12/16 → 15/16 mục đạt") và liệt kê mọi mục đã đổi trạng thái — cả mục mới được đánh dấu (chưa đánh dấu → đã đánh dấu) lẫn mục bị thụt lùi (đã đánh dấu → chưa đánh dấu). Nếu còn mục chưa đánh dấu, liệt kê chúng như những phần cần chú ý.
- Bảng tóm tắt độ phủ liệt kê từng nhóm phân loại với Trạng thái: Đã giải quyết (trước là Một phần/Thiếu và đã được xử lý), Để lại (vượt quá số câu hỏi cho phép, hoặc phần còn lại cụ thể là về phương pháp triển khai, so sánh tech stack hay phân rã tác vụ), Rõ ràng (đã đủ từ trước), Còn tồn đọng (vẫn Một phần/Thiếu nhưng ít ảnh hưởng).
- Nếu còn nhóm Còn tồn đọng hoặc Để lại, khuyến nghị nên chuyển sang `__SPECKIT_COMMAND_PLAN__` hay chạy lại `__SPECKIT_COMMAND_CLARIFY__` sau khi lập kế hoạch.
- Lệnh tiếp theo được đề xuất.

## Hoàn tất khi

- [ ] Đã xác định các điểm mơ hồ trong đặc tả và tích hợp nội dung làm rõ vào file đặc tả
- [ ] Đã kiểm tra lại checklist chất lượng đặc tả theo đặc tả đã cập nhật (nếu có `FEATURE_DIR/checklists/requirements.md`)
- [ ] Đã gọi hoặc bỏ qua các hook của extension theo đúng quy tắc trong mục Hook bắt buộc sau khi thực thi ở trên
- [ ] Đã báo hoàn tất cho người dùng, kèm các câu hỏi đã trả lời, các mục đã chỉnh sửa, trạng thái checklist và bản tóm tắt độ phủ
