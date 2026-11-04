# Phát triển hướng đặc tả (Specification-Driven Development – SDD)

> [!NOTE]
> Bản dịch tiếng Việt của [spec-driven.md](./spec-driven.md). Nếu có chỗ khác biệt, bản tiếng Anh là bản chính thức. Thuật ngữ được thống nhất tại [Bảng thuật ngữ](./docs/vi/GLOSSARY.md).

## Đảo ngược quyền lực

Suốt nhiều thập kỷ, mã nguồn luôn là "vua". Đặc tả phục vụ mã nguồn: chúng là giàn giáo ta dựng lên rồi bỏ đi khi "công việc thật sự" là viết code bắt đầu. Ta viết PRD để định hướng phát triển, soạn tài liệu thiết kế để làm cơ sở triển khai, vẽ sơ đồ để hình dung kiến trúc. Nhưng tất cả những thứ đó luôn đứng sau bản thân mã nguồn. Mã nguồn là sự thật. Mọi thứ khác, may lắm, chỉ là ý định tốt. Mã nguồn là nguồn sự thật duy nhất, và khi mã nguồn tiến lên, đặc tả hiếm khi theo kịp. Vì tài sản (mã nguồn) và phần triển khai là một, rất khó có được một bản triển khai song song nếu không dựa vào chính mã nguồn đó.

Phát triển hướng đặc tả (SDD) đảo ngược cấu trúc quyền lực này. Đặc tả không phục vụ mã nguồn mà mã nguồn phục vụ đặc tả. Tài liệu yêu cầu sản phẩm (PRD) không còn là hướng dẫn cho việc triển khai; nó là nguồn sinh ra phần triển khai. Kế hoạch kỹ thuật không còn là tài liệu tham khảo khi viết code; chúng là những định nghĩa chính xác tạo ra code. Đây không phải một cải tiến nhỏ trong cách ta xây dựng phần mềm, mà là việc suy nghĩ lại từ gốc: điều gì dẫn dắt quá trình phát triển.

Khoảng cách giữa đặc tả và phần triển khai đã đeo bám ngành phát triển phần mềm từ thuở ban đầu. Ta đã cố lấp nó bằng tài liệu tốt hơn, yêu cầu chi tiết hơn, quy trình chặt chẽ hơn. Những cách đó thất bại vì chúng chấp nhận khoảng cách như một điều tất yếu: chúng cố thu hẹp nó nhưng không bao giờ xóa bỏ được. SDD xóa bỏ khoảng cách bằng cách biến đặc tả, cùng các kế hoạch triển khai cụ thể sinh ra từ đặc tả, thành thứ có thể thực thi. Khi đặc tả và kế hoạch triển khai sinh ra code, không còn khoảng cách nào cả, chỉ còn sự chuyển hóa.

Sự chuyển hóa này giờ đã khả thi vì AI có thể hiểu và triển khai các đặc tả phức tạp, cũng như lập kế hoạch triển khai chi tiết. Nhưng để AI sinh code tự do mà không có cấu trúc thì chỉ tạo ra hỗn loạn. SDD mang lại cấu trúc đó thông qua các đặc tả và kế hoạch triển khai đi kèm, đủ chính xác, đầy đủ và rõ ràng để sinh ra hệ thống chạy được. Đặc tả trở thành artifact chính. Mã nguồn trở thành cách thể hiện của đặc tả (dưới dạng một bản triển khai theo kế hoạch triển khai) trong một ngôn ngữ và framework cụ thể.

Trong thế giới mới này, bảo trì phần mềm nghĩa là phát triển tiếp các đặc tả. Ý định của nhóm phát triển được diễn đạt bằng ngôn ngữ tự nhiên ("**phát triển hướng ý định**"), tài sản thiết kế, các nguyên tắc cốt lõi và những hướng dẫn khác. **Ngôn ngữ chung** của việc phát triển được nâng lên một tầng cao hơn, và mã nguồn chỉ là chặng cuối.

Gỡ lỗi nghĩa là sửa các đặc tả và kế hoạch triển khai đã sinh ra code sai. Refactor nghĩa là tái cấu trúc cho rõ ràng hơn. Toàn bộ workflow phát triển được tổ chức lại quanh đặc tả như nguồn sự thật trung tâm, còn kế hoạch triển khai và mã nguồn là đầu ra được tái tạo liên tục. Cập nhật ứng dụng với tính năng mới, hay tạo một bản triển khai song song mới vì con người vốn sáng tạo, nghĩa là xem lại đặc tả và lập kế hoạch triển khai mới. Vì vậy quy trình này là 0 -> 1, (1', ..), 2, 3, N.

Nhóm phát triển được tập trung vào sự sáng tạo, thử nghiệm và tư duy phản biện của mình.

## Workflow SDD trong thực tế

Workflow bắt đầu từ một ý tưởng, thường còn mơ hồ và chưa đầy đủ. Qua những vòng trao đổi lặp lại với AI, ý tưởng đó trở thành một PRD toàn diện. AI đặt câu hỏi làm rõ, chỉ ra các trường hợp biên và giúp định nghĩa tiêu chí chấp nhận chính xác. Những gì có thể tốn nhiều ngày họp hành và viết tài liệu trong cách phát triển truyền thống giờ diễn ra trong vài giờ tập trung viết đặc tả. Điều này làm thay đổi SDLC truyền thống: yêu cầu và thiết kế trở thành hoạt động liên tục thay vì các giai đoạn tách rời. Cách làm này hỗ trợ **quy trình làm việc nhóm**, nơi các đặc tả được cả nhóm review, được diễn đạt và quản lý phiên bản, được tạo trên branch và được merge.

Khi product manager cập nhật tiêu chí chấp nhận, các kế hoạch triển khai tự động đánh dấu những quyết định kỹ thuật bị ảnh hưởng. Khi kiến trúc sư tìm ra một pattern tốt hơn, PRD được cập nhật để phản ánh những khả năng mới.

Xuyên suốt quá trình viết đặc tả, các agent nghiên cứu thu thập bối cảnh quan trọng. Chúng tìm hiểu khả năng tương thích của thư viện, số liệu benchmark hiệu năng và các tác động về bảo mật. Các ràng buộc của tổ chức được phát hiện và áp dụng tự động: tiêu chuẩn cơ sở dữ liệu, yêu cầu xác thực và chính sách triển khai của công ty bạn được lồng ghép liền mạch vào mọi đặc tả.

Từ PRD, AI sinh ra các kế hoạch triển khai ánh xạ yêu cầu sang quyết định kỹ thuật. Mọi lựa chọn công nghệ đều có lý do được ghi lại. Mọi quyết định kiến trúc đều truy vết được về các yêu cầu cụ thể. Trong suốt quá trình, việc kiểm tra tính nhất quán liên tục nâng cao chất lượng. AI phân tích đặc tả để tìm chỗ mơ hồ, mâu thuẫn và thiếu sót, không phải như một cổng kiểm tra một lần mà như một quá trình tinh chỉnh liên tục.

Việc sinh code bắt đầu ngay khi đặc tả và kế hoạch triển khai đủ ổn định, chứ không cần phải "hoàn chỉnh". Những lần sinh đầu tiên có thể mang tính khám phá, để thử xem đặc tả có hợp lý trong thực tế không. Khái niệm nghiệp vụ trở thành mô hình dữ liệu. User story trở thành API endpoint. Kịch bản chấp nhận trở thành test. Phát triển và kiểm thử hòa làm một thông qua đặc tả: kịch bản kiểm thử không được viết sau code, mà là một phần của đặc tả sinh ra cả phần triển khai lẫn test.

Vòng phản hồi không dừng lại ở giai đoạn phát triển ban đầu. Số liệu và sự cố trên môi trường production không chỉ dẫn tới các bản hotfix mà còn cập nhật đặc tả cho lần tái tạo tiếp theo. Điểm nghẽn hiệu năng trở thành yêu cầu phi chức năng mới. Lỗ hổng bảo mật trở thành ràng buộc áp lên mọi lần sinh code về sau. Chính vòng lặp qua lại giữa đặc tả, phần triển khai và thực tế vận hành này là nơi sự thấu hiểu thật sự hình thành, và là nơi SDLC truyền thống chuyển thành một quá trình tiến hóa liên tục.

## Vì sao SDD quan trọng vào lúc này

Ba xu hướng khiến SDD không chỉ khả thi mà còn cần thiết:

Thứ nhất, năng lực của AI đã đạt tới ngưỡng mà đặc tả viết bằng ngôn ngữ tự nhiên có thể sinh ra code chạy được một cách đáng tin cậy. Mục đích không phải thay thế lập trình viên, mà là khuếch đại hiệu quả của họ bằng cách tự động hóa phần chuyển đổi máy móc từ đặc tả sang triển khai. Nó có thể mở rộng khả năng khám phá và sáng tạo, giúp dễ dàng "làm lại từ đầu", và hỗ trợ việc thêm bớt cũng như tư duy phản biện.

Thứ hai, độ phức tạp của phần mềm tiếp tục tăng theo cấp số nhân. Hệ thống hiện đại tích hợp hàng chục dịch vụ, framework và thư viện phụ thuộc. Giữ cho tất cả các mảnh ghép đó bám sát ý định ban đầu bằng quy trình thủ công ngày càng khó. SDD mang lại sự nhất quán có hệ thống thông qua việc sinh code dựa trên đặc tả. Các framework có thể sẽ tiến hóa để ưu tiên hỗ trợ AI thay vì con người, hoặc được thiết kế quanh các thành phần tái sử dụng.

Thứ ba, tốc độ thay đổi ngày càng nhanh. Yêu cầu ngày nay thay đổi nhanh hơn bao giờ hết. Chuyển hướng (pivot) không còn là ngoại lệ mà là chuyện đương nhiên. Phát triển sản phẩm hiện đại đòi hỏi lặp nhanh dựa trên phản hồi của người dùng, điều kiện thị trường và áp lực cạnh tranh. Cách phát triển truyền thống coi những thay đổi này là sự gián đoạn. Mỗi lần pivot đòi hỏi lan truyền thay đổi thủ công qua tài liệu, thiết kế và mã nguồn. Kết quả là hoặc cập nhật chậm và cẩn thận nên kìm hãm tốc độ, hoặc thay đổi nhanh và ẩu nên tích tụ nợ kỹ thuật.

SDD có thể hỗ trợ các thử nghiệm giả định kiểu "nếu... thì sao": "Nếu cần triển khai lại hoặc thay đổi ứng dụng để phục vụ nhu cầu kinh doanh là bán được nhiều áo thun hơn, ta sẽ triển khai và thử nghiệm như thế nào?"

SDD biến thay đổi yêu cầu từ chướng ngại thành một phần bình thường của workflow. Khi đặc tả dẫn dắt phần triển khai, pivot trở thành việc tái tạo có hệ thống thay vì viết lại thủ công. Đổi một yêu cầu cốt lõi trong PRD, các kế hoạch triển khai bị ảnh hưởng sẽ tự cập nhật. Sửa một user story, các API endpoint tương ứng sẽ được sinh lại. Đây không chỉ là chuyện phát triển ban đầu, mà là duy trì tốc độ kỹ thuật qua những thay đổi không thể tránh khỏi.

## Các nguyên tắc cốt lõi

**Đặc tả là ngôn ngữ chung**: Đặc tả trở thành artifact chính. Mã nguồn trở thành cách thể hiện của đặc tả trong một ngôn ngữ và framework cụ thể. Bảo trì phần mềm nghĩa là phát triển tiếp các đặc tả.

**Đặc tả thực thi được**: Đặc tả phải đủ chính xác, đầy đủ và rõ ràng để sinh ra hệ thống chạy được. Điều này xóa bỏ khoảng cách giữa ý định và phần triển khai.

**Tinh chỉnh liên tục**: Việc kiểm tra tính nhất quán diễn ra liên tục, không phải một cổng kiểm tra một lần. AI phân tích đặc tả để tìm chỗ mơ hồ, mâu thuẫn và thiếu sót như một quá trình thường trực.

**Bối cảnh dựa trên nghiên cứu**: Các agent nghiên cứu thu thập bối cảnh quan trọng trong suốt quá trình viết đặc tả, tìm hiểu các phương án kỹ thuật, tác động về hiệu năng và ràng buộc của tổ chức.

**Phản hồi hai chiều**: Thực tế trên production định hướng sự phát triển của đặc tả. Số liệu, sự cố và bài học vận hành trở thành đầu vào để tinh chỉnh đặc tả.

**Phân nhánh để khám phá**: Sinh nhiều hướng triển khai từ cùng một đặc tả để khám phá các mục tiêu tối ưu khác nhau: hiệu năng, khả năng bảo trì, trải nghiệm người dùng, chi phí.

## Các cách triển khai

Hiện nay, thực hành SDD đòi hỏi kết hợp các công cụ sẵn có và giữ kỷ luật trong suốt quá trình. Có thể thực hành phương pháp này với:

- Trợ lý AI để phát triển đặc tả qua nhiều vòng lặp
- Agent nghiên cứu để thu thập bối cảnh kỹ thuật
- Công cụ sinh code để chuyển đặc tả thành phần triển khai
- Hệ thống quản lý phiên bản được điều chỉnh cho workflow lấy đặc tả làm đầu
- Kiểm tra tính nhất quán bằng AI phân tích tài liệu đặc tả

Điểm mấu chốt là coi đặc tả là nguồn sự thật, còn mã nguồn là đầu ra được sinh ra để phục vụ đặc tả, chứ không phải ngược lại.

## Tinh gọn SDD bằng các lệnh

Phương pháp SDD được nâng tầm đáng kể nhờ ba lệnh mạnh mẽ tự động hóa workflow đặc tả → lập kế hoạch → chia tác vụ:

### Lệnh `/speckit.specify`

Lệnh này biến một mô tả tính năng đơn giản (prompt của người dùng) thành một bản đặc tả hoàn chỉnh, có cấu trúc, kèm việc quản lý repository tự động:

1. **Tự động đánh số tính năng**: Quét các đặc tả hiện có để xác định số thứ tự tính năng tiếp theo (ví dụ 001, 002, 003, …, 1000 — tự mở rộng quá 3 chữ số)
2. **Tạo branch**: Sinh tên branch có ý nghĩa từ mô tả của bạn và tự động tạo branch đó
3. **Sinh từ template**: Sao chép và tùy chỉnh template đặc tả tính năng theo yêu cầu của bạn
4. **Cấu trúc thư mục**: Tạo cấu trúc `specs/[branch-name]/` phù hợp cho mọi tài liệu liên quan

### Lệnh `/speckit.plan`

Khi đã có đặc tả tính năng, lệnh này tạo một kế hoạch triển khai toàn diện:

1. **Phân tích đặc tả**: Đọc và hiểu yêu cầu tính năng, user story và tiêu chí chấp nhận
2. **Tuân thủ hiến chương**: Đảm bảo phù hợp với hiến chương dự án và các nguyên tắc kiến trúc
3. **Chuyển đổi sang kỹ thuật**: Chuyển yêu cầu nghiệp vụ thành kiến trúc kỹ thuật và chi tiết triển khai
4. **Tài liệu chi tiết**: Sinh các tài liệu hỗ trợ về mô hình dữ liệu, API contract và kịch bản kiểm thử
5. **Kiểm chứng bằng quickstart**: Tạo hướng dẫn quickstart ghi lại các kịch bản kiểm chứng chính

### Lệnh `/speckit.tasks`

Sau khi có kế hoạch, lệnh này phân tích kế hoạch và các tài liệu thiết kế liên quan để sinh danh sách tác vụ có thể thực thi:

1. **Đầu vào**: Đọc `plan.md` (bắt buộc) và nếu có thì cả `data-model.md`, `contracts/` và `research.md`
2. **Suy ra tác vụ**: Chuyển contract, thực thể và kịch bản thành các tác vụ cụ thể
3. **Song song hóa**: Đánh dấu các tác vụ độc lập bằng `[P]` và phác thảo các nhóm có thể chạy song song an toàn
4. **Đầu ra**: Ghi `tasks.md` vào thư mục tính năng, sẵn sàng để một agent thực thi

### Ví dụ: Xây dựng tính năng chat

Đây là cách các lệnh này thay đổi workflow phát triển truyền thống:

**Cách truyền thống:**

```text
1. Viết PRD trong một tài liệu (2-3 giờ)
2. Soạn tài liệu thiết kế (2-3 giờ)
3. Dựng cấu trúc dự án thủ công (30 phút)
4. Viết đặc tả kỹ thuật (3-4 giờ)
5. Lập kế hoạch kiểm thử (2 giờ)
Tổng: ~12 giờ làm tài liệu
```

**Cách SDD dùng lệnh:**

```bash
# Bước 1: Tạo đặc tả tính năng (5 phút)
/speckit.specify Hệ thống chat thời gian thực có lịch sử tin nhắn và trạng thái online của người dùng

# Lệnh này tự động:
# - Tạo branch "003-chat-system"
# - Sinh specs/003-chat-system/spec.md
# - Điền vào đó các yêu cầu có cấu trúc

# Bước 2: Sinh kế hoạch triển khai (5 phút)
/speckit.plan WebSocket cho nhắn tin thời gian thực, PostgreSQL cho lịch sử, Redis cho trạng thái online

# Bước 3: Sinh các tác vụ thực thi được (5 phút)
/speckit.tasks

# Các lệnh trên tự động tạo:
# - specs/003-chat-system/plan.md
# - specs/003-chat-system/research.md (so sánh các thư viện WebSocket)
# - specs/003-chat-system/data-model.md (schema Message và User)
# - specs/003-chat-system/contracts/ (sự kiện WebSocket, REST endpoint)
# - specs/003-chat-system/quickstart.md (các kịch bản kiểm chứng chính)
# - specs/003-chat-system/tasks.md (danh sách tác vụ suy ra từ kế hoạch)
```

Sau 15 phút, bạn có:

- Một bản đặc tả tính năng hoàn chỉnh với user story và tiêu chí chấp nhận
- Một kế hoạch triển khai chi tiết với lựa chọn công nghệ và lý do
- API contract và mô hình dữ liệu sẵn sàng để sinh code
- Bộ kịch bản kiểm thử đầy đủ cho cả kiểm thử tự động lẫn thủ công
- Tất cả tài liệu được quản lý phiên bản đúng cách trên một feature branch

### Sức mạnh của tự động hóa có cấu trúc

Các lệnh này không chỉ tiết kiệm thời gian mà còn đảm bảo tính nhất quán và đầy đủ:

1. **Không bỏ sót chi tiết**: Template đảm bảo mọi khía cạnh đều được xem xét, từ yêu cầu phi chức năng tới xử lý lỗi
2. **Quyết định truy vết được**: Mọi lựa chọn kỹ thuật đều liên kết ngược về yêu cầu cụ thể
3. **Tài liệu sống**: Đặc tả luôn đồng bộ với mã nguồn vì chính đặc tả sinh ra mã nguồn
4. **Lặp nhanh**: Thay đổi yêu cầu và sinh lại kế hoạch trong vài phút thay vì vài ngày

Các lệnh này hiện thực hóa nguyên tắc SDD bằng cách coi đặc tả là artifact thực thi được chứ không phải tài liệu tĩnh. Chúng biến việc viết đặc tả từ một việc "bất đắc dĩ phải làm" thành động lực dẫn dắt quá trình phát triển.

### Chất lượng nhờ template: Cấu trúc ràng buộc LLM để cho kết quả tốt hơn

Sức mạnh thực sự của các lệnh này không chỉ nằm ở tự động hóa, mà ở cách template dẫn dắt hành vi của LLM để tạo ra đặc tả chất lượng cao hơn. Template đóng vai trò như những prompt tinh vi, ràng buộc đầu ra của LLM theo hướng có ích:

#### 1. **Ngăn chi tiết triển khai xuất hiện quá sớm**

Template đặc tả tính năng ghi rõ:

```text
- ✅ Tập trung vào người dùng cần GÌ và VÌ SAO
- ❌ Tránh nói LÀM THẾ NÀO để triển khai (không tech stack, API, cấu trúc code)
```

Ràng buộc này buộc LLM giữ đúng mức trừu tượng. Khi LLM có xu hướng nhảy ngay tới "triển khai bằng React với Redux", template giữ nó tập trung vào "người dùng cần dữ liệu được cập nhật theo thời gian thực". Sự tách bạch này giúp đặc tả ổn định ngay cả khi công nghệ triển khai thay đổi.

#### 2. **Buộc đánh dấu rõ những điểm chưa chắc chắn**

Cả hai template đều bắt buộc dùng dấu đánh dấu `[NEEDS CLARIFICATION]`:

```text
Khi tạo đặc tả này từ prompt của người dùng:
1. **Đánh dấu mọi chỗ mơ hồ**: Dùng [NEEDS CLARIFICATION: câu hỏi cụ thể]
2. **Không đoán**: Nếu prompt không nói rõ điều gì, hãy đánh dấu nó
```

Điều này ngăn thói quen phổ biến của LLM là đưa ra những giả định nghe hợp lý nhưng có thể sai. Thay vì đoán rằng "hệ thống đăng nhập" dùng xác thực email/mật khẩu, LLM phải đánh dấu `[NEEDS CLARIFICATION: chưa nêu phương thức xác thực - email/mật khẩu, SSO, OAuth?]`.

#### 3. **Tư duy có cấu trúc thông qua checklist**

Template có các checklist đầy đủ, đóng vai trò như "unit test" cho đặc tả:

```markdown
### Mức độ đầy đủ của yêu cầu

- [ ] Không còn dấu [NEEDS CLARIFICATION] nào
- [ ] Yêu cầu kiểm thử được và rõ ràng
- [ ] Tiêu chí thành công đo lường được
```

Các checklist này buộc LLM tự review đầu ra một cách có hệ thống, phát hiện những thiếu sót dễ bị lọt qua. Giống như trao cho LLM một khung đảm bảo chất lượng.

#### 4. **Tuân thủ hiến chương thông qua các cổng kiểm soát**

Template kế hoạch triển khai áp dụng các nguyên tắc kiến trúc thông qua cổng kiểm soát theo giai đoạn:

```markdown
### Giai đoạn -1: Cổng kiểm soát trước khi triển khai

#### Cổng đơn giản (Điều VII)

- [ ] Dùng ≤3 project?
- [ ] Không thiết kế cho tương lai xa?

#### Cổng chống trừu tượng hóa (Điều VIII)

- [ ] Dùng trực tiếp framework?
- [ ] Chỉ một cách biểu diễn model?
```

Các cổng này ngăn thiết kế quá mức bằng cách buộc LLM phải giải trình rõ ràng mọi sự phức tạp. Nếu không qua được một cổng, LLM phải ghi lý do trong mục "Theo dõi độ phức tạp", tạo ra trách nhiệm giải trình cho các quyết định kiến trúc.

#### 5. **Quản lý chi tiết theo tầng**

Template áp đặt một kiến trúc thông tin hợp lý:

```text
**QUAN TRỌNG**: Kế hoạch triển khai này cần giữ ở mức tổng quan và dễ đọc.
Mọi đoạn code mẫu, thuật toán chi tiết hay đặc tả kỹ thuật dài
phải được đặt trong file `implementation-details/` phù hợp
```

Điều này ngăn vấn đề phổ biến là đặc tả biến thành một đống code khó đọc. LLM học cách giữ mức chi tiết phù hợp, tách phần phức tạp ra file riêng trong khi giữ tài liệu chính dễ theo dõi.

#### 6. **Tư duy test trước**

Template triển khai áp đặt cách phát triển viết test trước:

```text
### Thứ tự tạo file
1. Tạo `contracts/` chứa đặc tả API
2. Tạo file test theo thứ tự: contract → integration → e2e → unit
3. Tạo file mã nguồn để các test chạy qua
```

Ràng buộc về thứ tự này đảm bảo LLM nghĩ về khả năng kiểm thử và contract trước khi triển khai, giúp đặc tả chắc chắn và dễ kiểm chứng hơn.

#### 7. **Ngăn các tính năng phỏng đoán**

Template chủ động ngăn việc phỏng đoán:

```text
- [ ] Không có tính năng phỏng đoán hay kiểu "có thể sẽ cần"
- [ ] Mọi giai đoạn đều có điều kiện tiên quyết và sản phẩm bàn giao rõ ràng
```

Điều này ngăn LLM thêm những tính năng "có thì tốt" làm phức tạp phần triển khai. Mọi tính năng đều phải truy vết được về một user story cụ thể với tiêu chí chấp nhận rõ ràng.

### Hiệu ứng cộng hưởng

Các ràng buộc này phối hợp với nhau để tạo ra những đặc tả:

- **Đầy đủ**: Checklist đảm bảo không bỏ sót gì
- **Rõ ràng**: Dấu làm rõ bắt buộc làm nổi bật những điểm chưa chắc chắn
- **Kiểm thử được**: Tư duy test trước được tích hợp sẵn vào quy trình
- **Dễ bảo trì**: Mức trừu tượng và phân tầng thông tin hợp lý
- **Triển khai được**: Các giai đoạn rõ ràng với sản phẩm bàn giao cụ thể

Template biến LLM từ một người viết sáng tạo thành một kỹ sư đặc tả có kỷ luật, hướng năng lực của nó vào việc liên tục tạo ra những đặc tả chất lượng cao, thực thi được, thực sự dẫn dắt quá trình phát triển.

## Nền tảng hiến chương: Áp đặt kỷ luật kiến trúc

Trung tâm của SDD là một bản hiến chương: tập hợp các nguyên tắc bất biến chi phối cách đặc tả trở thành mã nguồn. Hiến chương (`memory/constitution.md`) đóng vai trò như DNA kiến trúc của hệ thống, đảm bảo mọi bản triển khai được sinh ra đều giữ được tính nhất quán, sự đơn giản và chất lượng.

### Chín điều khoản phát triển

Hiến chương định nghĩa chín điều khoản định hình mọi khía cạnh của quá trình phát triển:

#### Điều I: Nguyên tắc thư viện trước

Mọi tính năng phải bắt đầu dưới dạng một thư viện độc lập, không có ngoại lệ. Điều này buộc thiết kế module hóa ngay từ đầu:

```text
Mọi tính năng trong Specify PHẢI bắt đầu dưới dạng một thư viện độc lập.
Không tính năng nào được triển khai trực tiếp trong mã ứng dụng
nếu chưa được trừu tượng hóa thành một thành phần thư viện tái sử dụng được.
```

Nguyên tắc này đảm bảo đặc tả sinh ra code module hóa, tái sử dụng được thay vì ứng dụng nguyên khối. Khi LLM sinh kế hoạch triển khai, nó phải cấu trúc các tính năng thành thư viện với ranh giới rõ ràng và ít phụ thuộc nhất.

#### Điều II: Bắt buộc có giao diện CLI

Mọi thư viện phải cung cấp chức năng của mình qua giao diện dòng lệnh:

```text
Mọi giao diện CLI PHẢI:
- Nhận văn bản làm đầu vào (qua stdin, đối số hoặc file)
- Xuất văn bản làm đầu ra (qua stdout)
- Hỗ trợ định dạng JSON để trao đổi dữ liệu có cấu trúc
```

Điều này đảm bảo khả năng quan sát và kiểm thử. LLM không thể giấu chức năng trong những class khó nhìn thấu; mọi thứ phải truy cập và kiểm chứng được qua giao diện văn bản.

#### Điều III: Bắt buộc viết test trước

Điều khoản mang tính thay đổi lớn nhất: không có code trước khi có test:

```text
Đây là điều KHÔNG THỂ THƯƠNG LƯỢNG: Mọi phần triển khai PHẢI tuân thủ nghiêm ngặt Test-Driven Development.
Không được viết code triển khai trước khi:
1. Unit test đã được viết
2. Test đã được người dùng kiểm tra và phê duyệt
3. Test đã được xác nhận là FAIL (giai đoạn Red)
```

Điều này đảo ngược hoàn toàn cách AI sinh code truyền thống. Thay vì sinh code rồi hy vọng nó chạy, LLM trước tiên phải sinh bộ test đầy đủ định nghĩa hành vi, được phê duyệt, rồi mới sinh phần triển khai.

#### Điều IV, V và VI: Quản trị do dự án tự định nghĩa

Điều IV, V và VI được cố ý để mỗi dự án tự định nghĩa trong hiến chương của mình, thay vì do Spec Kit quy định sẵn. Template hiến chương cung cấp các ô placeholder và ví dụ về các mối quan tâm như kiểm thử tích hợp, khả năng quan sát, quản lý phiên bản và thay đổi phá vỡ tương thích, nhưng các nhóm sẽ thay những placeholder đó bằng nguyên tắc phù hợp với hệ thống và tổ chức của mình.

Cách này giữ cấu trúc chín điều khoản ổn định trong khi cho phép mỗi dự án ghi vào đó các tiêu chuẩn không thể thương lượng của riêng mình. Với dự án này, Điều IV có thể quy định về bảo mật và ranh giới truy cập; với dự án khác, nó có thể định nghĩa yêu cầu kiểm thử tích hợp. Lệnh `/speckit.analyze` đánh giá hiến chương cụ thể trong dự án, nên các điều khoản do dự án tự định nghĩa này cũng tham gia vào việc kiểm tra tuân thủ giống như các ví dụ có sẵn.

#### Điều VII và VIII: Đơn giản và chống trừu tượng hóa

Cặp điều khoản này chống lại thiết kế quá mức:

```text
Mục 7.3: Cấu trúc dự án tối giản
- Tối đa 3 project cho lần triển khai đầu tiên
- Project bổ sung phải có lý do được ghi lại

Mục 8.1: Tin tưởng framework
- Dùng trực tiếp tính năng của framework thay vì bọc lại
```

Khi LLM có xu hướng tạo ra các lớp trừu tượng cầu kỳ, các điều khoản này buộc nó phải giải trình từng lớp phức tạp. "Cổng kiểm soát giai đoạn -1" trong template kế hoạch triển khai áp dụng trực tiếp các nguyên tắc này.

#### Điều IX: Ưu tiên kiểm thử tích hợp

Ưu tiên kiểm thử sát thực tế hơn unit test cô lập:

```text
Test PHẢI dùng môi trường sát thực tế:
- Ưu tiên cơ sở dữ liệu thật thay vì mock
- Dùng instance dịch vụ thật thay vì stub
- Contract test bắt buộc phải có trước khi triển khai
```

Điều này đảm bảo code được sinh ra chạy được trong thực tế, không chỉ trên lý thuyết.

### Áp dụng hiến chương thông qua template

Template kế hoạch triển khai hiện thực hóa các điều khoản này bằng những điểm kiểm tra cụ thể:

```markdown
### Giai đoạn -1: Cổng kiểm soát trước khi triển khai

#### Cổng đơn giản (Điều VII)

- [ ] Dùng ≤3 project?
- [ ] Không thiết kế cho tương lai xa?

#### Cổng chống trừu tượng hóa (Điều VIII)

- [ ] Dùng trực tiếp framework?
- [ ] Chỉ một cách biểu diễn model?

#### Cổng ưu tiên tích hợp (Điều IX)

- [ ] Đã định nghĩa contract?
- [ ] Đã viết contract test?
```

Các cổng này hoạt động như bước kiểm tra lúc biên dịch cho các nguyên tắc kiến trúc. LLM không thể đi tiếp nếu chưa qua các cổng, hoặc chưa ghi lại các ngoại lệ có lý do chính đáng trong mục "Theo dõi độ phức tạp".

### Sức mạnh của các nguyên tắc bất biến

Sức mạnh của hiến chương nằm ở tính bất biến. Chi tiết triển khai có thể thay đổi, nhưng các nguyên tắc cốt lõi thì giữ nguyên. Điều này mang lại:

1. **Nhất quán theo thời gian**: Code sinh ra hôm nay tuân theo cùng nguyên tắc với code sinh ra năm sau
2. **Nhất quán giữa các LLM**: Các model AI khác nhau tạo ra code tương thích về kiến trúc
3. **Toàn vẹn kiến trúc**: Mỗi tính năng củng cố chứ không làm suy yếu thiết kế hệ thống
4. **Bảo đảm chất lượng**: Các nguyên tắc test trước, thư viện trước và đơn giản đảm bảo code dễ bảo trì

### Sự phát triển của hiến chương

Dù các nguyên tắc là bất biến, cách áp dụng chúng có thể thay đổi:

```text
Mục 4.2: Quy trình sửa đổi
Mọi sửa đổi hiến chương này cần:
- Ghi lại rõ ràng lý do thay đổi
- Được người duy trì dự án review và phê duyệt
- Đánh giá khả năng tương thích ngược
```

Điều này cho phép phương pháp học hỏi và cải thiện mà vẫn giữ được sự ổn định. Hiến chương tự ghi lại quá trình phát triển của chính nó qua các lần sửa đổi có ghi ngày, cho thấy nguyên tắc có thể được tinh chỉnh dựa trên kinh nghiệm thực tế như thế nào.

### Hơn cả quy tắc: Một triết lý phát triển

Hiến chương không chỉ là một cuốn sổ quy tắc, mà là một triết lý định hình cách LLM suy nghĩ khi sinh code:

- **Quan sát được thay vì mờ đục**: Mọi thứ phải kiểm tra được qua giao diện CLI
- **Đơn giản thay vì khôn lỏi**: Bắt đầu đơn giản, chỉ thêm độ phức tạp khi đã chứng minh là cần
- **Tích hợp thay vì cô lập**: Kiểm thử trong môi trường thật, không phải môi trường giả lập
- **Module thay vì nguyên khối**: Mỗi tính năng là một thư viện có ranh giới rõ ràng

Bằng cách đưa các nguyên tắc này vào quá trình viết đặc tả và lập kế hoạch, SDD đảm bảo code được sinh ra không chỉ chạy được mà còn dễ bảo trì, kiểm thử được và vững chắc về kiến trúc. Hiến chương biến AI từ một công cụ sinh code thành một đối tác kiến trúc, tôn trọng và củng cố các nguyên tắc thiết kế hệ thống.

## Sự chuyển đổi

Đây không phải chuyện thay thế lập trình viên hay tự động hóa sự sáng tạo. Đây là việc khuếch đại năng lực con người bằng cách tự động hóa phần chuyển đổi máy móc. Đây là việc tạo ra một vòng phản hồi chặt chẽ, nơi đặc tả, nghiên cứu và mã nguồn cùng phát triển, mỗi vòng lặp mang lại hiểu biết sâu hơn và sự khớp nối tốt hơn giữa ý định và phần triển khai.

Phát triển phần mềm cần công cụ tốt hơn để giữ cho ý định và phần triển khai luôn khớp nhau. SDD mang lại phương pháp để đạt được điều đó thông qua những đặc tả thực thi được, sinh ra code thay vì chỉ định hướng cho nó.
