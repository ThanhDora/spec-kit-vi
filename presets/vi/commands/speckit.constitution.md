---
description: Tạo hoặc cập nhật hiến chương dự án từ các nguyên tắc được cung cấp sẵn hoặc thu thập qua trao đổi.
handoffs:
  - label: Xây dựng đặc tả
    agent: speckit.specify
    prompt: Triển khai đặc tả tính năng dựa trên hiến chương vừa cập nhật. Tôi muốn xây dựng...
scripts:
  sh: scripts/bash/resolve-template.sh constitution-template --json
  ps: scripts/powershell/resolve-template.ps1 constitution-template -Json
  py: scripts/python/resolve_template.py constitution-template --json
---

## Đầu vào của người dùng

```text
$ARGUMENTS
```

Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng).

**Ngôn ngữ**: Viết mọi artifact và mọi phản hồi cho người dùng bằng tiếng Việt tự nhiên, chuyên nghiệp. Giữ nguyên tiếng Anh cho tên lệnh, tên file, đường dẫn, mã định danh, khóa JSON/YAML, placeholder và các dấu đánh dấu chuẩn của Spec Kit (ví dụ dấu cần làm rõ).

## Giới hạn phạm vi

Phần việc của lệnh này chỉ giới hạn ở việc cập nhật chính hiến chương dự án. Các template và lệnh
phụ thuộc đọc hiến chương lúc chạy và không bị sửa ở đây.

- Phân loại từng phần của đầu vào người dùng: hoặc là nội dung hiến chương, hoặc là một ý định
  riêng, không thuộc về quản trị.
- Nếu đầu vào có yêu cầu triển khai tính năng, sinh code, refactor, build hoặc deploy, bạn
  **KHÔNG ĐƯỢC** thực hiện chúng. Thay vào đó, hãy tách chúng ra thành các ý định để làm sau.
- Bạn **KHÔNG ĐƯỢC** tạo, sửa hay xóa file mã nguồn ứng dụng, route tính năng, component, test,
  file deploy hay bất kỳ artifact nào khác không liên quan tới workflow hiến chương.
- Nếu không rõ một chỉ dẫn có phải là nội dung hiến chương hay không, hãy hỏi để làm rõ trước khi
  thay đổi.
- Sau khi cập nhật xong hiến chương, thêm mục `Next Actions` cho mỗi ý định để làm sau. Liệt kê ý
  định ban đầu và đề xuất lệnh Spec Kit phù hợp để làm tiếp, ví dụ
  `__SPECKIT_COMMAND_SPECIFY__`, nhưng không tự gọi lệnh đó.
- Nếu không có ý định nào ngoài phạm vi quản trị, bỏ mục `Next Actions`.

## Kiểm tra trước khi thực thi

**Kiểm tra hook của extension (trước khi cập nhật hiến chương)**:
- Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.before_constitution`
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

Bạn đang cập nhật hiến chương dự án tại `.specify/memory/constitution.md`. Khung hiến chương đang
dùng được xác định lúc chạy lệnh từ `constitution-template` thông qua chồng phân giải
preset/template của Spec Kit.

Thực hiện theo luồng sau:

1. Chạy `{SCRIPT}` từ thư mục gốc repository và parse `TEMPLATE_CONTENT` làm template đang dùng.
   - Bộ phân giải dùng chung áp dụng các ghi đè của dự án, ghép các lớp preset và lớp extension
     trước khi rơi về template lõi. Bước này PHẢI thành công rồi mới được tiếp tục.
   - Nếu thất bại, dừng lại và báo lỗi phân giải; không tiếp tục chỉ với một lớp template đóng
     góp.
   - Nếu `.specify/memory/constitution.md` đã tồn tại, nạp nó làm nguồn cho các giá trị và sửa đổi
     hiện có của dự án. Giữ lại thông tin vẫn còn áp dụng được khi áp khung vừa phân giải.
   - Nếu chưa tồn tại, dùng template đã phân giải làm tài liệu ban đầu.
   - Không ghi ngược vào bất kỳ lớp template nào đang được quản lý phiên bản.
   - Xác định mọi token placeholder có dạng `[ALL_CAPS_IDENTIFIER]`.
   **QUAN TRỌNG**: Người dùng có thể cần ít hoặc nhiều nguyên tắc hơn số lượng trong template. Nếu người dùng nêu một con số cụ thể, hãy tôn trọng con số đó và vẫn theo cấu trúc chung của template. Bạn sẽ cập nhật tài liệu cho phù hợp.

2. Thu thập/suy ra giá trị cho các placeholder:
   - Nếu đầu vào của người dùng (trong cuộc trò chuyện) cung cấp giá trị, dùng giá trị đó.
   - Nếu không, suy ra từ bối cảnh hiện có của repo (README, tài liệu, các phiên bản hiến chương trước nếu có kèm theo).
   - Với các ngày quản trị: `RATIFICATION_DATE` là ngày thông qua ban đầu (nếu không biết thì hỏi hoặc đánh dấu TODO), `LAST_AMENDED_DATE` là hôm nay nếu có thay đổi, nếu không thì giữ giá trị cũ.
   - `CONSTITUTION_VERSION` phải tăng theo quy tắc semantic versioning:
     - MAJOR: Xóa bỏ hoặc định nghĩa lại nguyên tắc/quy định quản trị theo cách không tương thích ngược.
     - MINOR: Thêm nguyên tắc/mục mới hoặc mở rộng đáng kể nội dung hướng dẫn.
     - PATCH: Làm rõ, chỉnh câu chữ, sửa lỗi chính tả, tinh chỉnh không làm đổi ý nghĩa.
   - Nếu chưa rõ nên tăng loại phiên bản nào, hãy trình bày lập luận trước khi chốt.

3. Soạn nội dung hiến chương cập nhật, dùng template đã phân giải làm cấu trúc bắt buộc:
   - Thay mọi placeholder bằng nội dung cụ thể (không còn token trong ngoặc vuông, trừ những ô template được cố ý giữ lại vì dự án chưa muốn định nghĩa; phải giải thích rõ lý do cho từng ô còn lại).
   - Giữ nguyên thứ bậc heading; có thể xóa các comment sau khi đã thay, trừ khi chúng vẫn có ích cho việc làm rõ.
   - Đảm bảo mỗi mục Nguyên tắc có: dòng tên ngắn gọn, một đoạn văn (hoặc danh sách gạch đầu dòng) nêu các quy tắc không thể thương lượng, và lý do rõ ràng nếu lý do chưa hiển nhiên.
   - Đảm bảo mục Quản trị liệt kê quy trình sửa đổi, chính sách quản lý phiên bản và kỳ vọng về việc review tuân thủ.

4. Tạo một Báo cáo ảnh hưởng đồng bộ (Sync Impact Report) dưới dạng comment HTML ở đầu file hiến chương sau khi cập nhật.
   Báo cáo này chỉ là ghi chú tạm để con người review lần sửa đổi, không phải nội dung quản trị;
   nó cần được xóa trước khi commit file hiến chương đã sửa đổi.
   - Thay đổi phiên bản: cũ → mới
   - Danh sách các nguyên tắc đã sửa (tiêu đề cũ → tiêu đề mới nếu đổi tên)
   - Các mục được thêm
   - Các mục bị xóa
   - Các TODO cần làm tiếp nếu có placeholder được cố ý để lại.

5. Kiểm tra trước khi xuất kết quả cuối:
   - Không còn token trong ngoặc vuông nào chưa được giải thích.
   - Dòng phiên bản khớp với báo cáo.
   - Ngày theo định dạng ISO YYYY-MM-DD.
   - Các nguyên tắc mang tính khẳng định, kiểm chứng được và không mơ hồ ("nên" → thay bằng PHẢI/NÊN kèm lý do khi phù hợp).

6. Ghi hiến chương đã hoàn thiện trở lại `.specify/memory/constitution.md` (ghi đè).

7. Xuất bản tóm tắt cuối cùng cho người dùng, gồm:
   - Phiên bản mới và lý do tăng phiên bản.
   - Các placeholder TODO hoặc hạng mục để lại cần xử lý thủ công.
   - Commit message đề xuất (ví dụ: `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).
   - Mục `Next Actions` cho mọi ý định ngoài phạm vi quản trị đã được để lại.

Yêu cầu về định dạng & văn phong:

- Dùng heading Markdown đúng như trong template (không hạ hay nâng cấp heading).
- Ngắt các dòng giải thích dài để dễ đọc (lý tưởng là <100 ký tự) nhưng không ép ngắt dòng một cách gượng gạo.
- Giữ đúng một dòng trống giữa các mục.
- Tránh khoảng trắng thừa ở cuối dòng.

Nếu người dùng chỉ cập nhật một phần (ví dụ chỉ sửa một nguyên tắc), vẫn phải thực hiện các bước kiểm tra và quyết định phiên bản.

Nếu thiếu thông tin quan trọng (ví dụ thật sự không biết ngày phê chuẩn), chèn `TODO(<FIELD_NAME>): explanation` (phần giải thích viết bằng tiếng Việt) và ghi vào Báo cáo ảnh hưởng đồng bộ dưới mục các hạng mục để lại.

Chỉ ghi `.specify/memory/constitution.md`; không tạo hay sửa file nguồn của template.

## Kiểm tra sau khi thực thi

**Kiểm tra hook của extension (sau khi cập nhật hiến chương)**:
Kiểm tra xem `.specify/extensions.yml` có tồn tại ở thư mục gốc dự án không.
- Nếu có, đọc file và tìm các mục dưới khóa `hooks.after_constitution`
- Nếu YAML không parse được hoặc không hợp lệ, đừng âm thầm bỏ qua: báo cho người dùng biết không đọc được `.specify/extensions.yml` (kèm lỗi của parser) và chưa kiểm tra hook nào, kể cả các hook bắt buộc (`optional: false`) đăng ký ở đó, rồi tiếp tục như bình thường
- Loại bỏ các hook có `enabled` được đặt rõ là `false`. Hook không có trường `enabled` được coi là đang bật.
- Với mỗi hook còn lại, **không** được tự diễn giải hay đánh giá biểu thức `condition` của hook:
  - Nếu hook không có trường `condition`, hoặc trường này null/rỗng, coi hook là thực thi được
  - Nếu hook định nghĩa `condition` không rỗng, bỏ qua hook đó và để phần triển khai HookExecutor đánh giá điều kiện
- Với mỗi hook thực thi được, xuất nội dung sau tùy theo cờ `optional`:
  - **Hook tùy chọn** (`optional: true`):
    ```
    ## Hook của extension

    **Hook tùy chọn**: {extension}
    Lệnh: `/{command}`
    Mô tả: {description}

    Prompt: {prompt}
    Để thực thi: `/{command}`
    ```
  - **Hook bắt buộc** (`optional: false`):
    ```
    ## Hook của extension

    **Hook tự động**: {extension}
    Đang thực thi: `/{command}`
    EXECUTE_COMMAND: {command}
    ```
    Sau khi xuất khối trên, bạn PHẢI thực sự gọi hook và chờ nó chạy xong rồi mới tiếp tục. Chạy hook theo đúng cách bạn tự chạy lệnh đó trong agent/phiên làm việc này (cách gọi có thể khác với id `{command}` hiển thị nguyên văn ở trên, ví dụ agent ở chế độ skill sẽ chạy dưới dạng `/skill:speckit-...` hoặc `$speckit-...`). Chỉ xuất khối trên thì hook chưa hề được chạy.
- Nếu không có hook nào được đăng ký hoặc `.specify/extensions.yml` không tồn tại, lặng lẽ bỏ qua
