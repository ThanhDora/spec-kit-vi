---

description: "Template danh sách tác vụ để triển khai tính năng"
---

# Tác vụ: [FEATURE NAME]

**Đầu vào**: Tài liệu thiết kế trong `/specs/[###-feature-name]/`

**Điều kiện tiên quyết**: plan.md (bắt buộc), spec.md (bắt buộc cho user story), research.md, data-model.md, contracts/

**Kiểm thử**: Các ví dụ bên dưới có kèm tác vụ kiểm thử. Test là TÙY CHỌN, chỉ thêm vào khi đặc tả tính năng yêu cầu rõ ràng.

**Cách tổ chức**: Các tác vụ được nhóm theo user story để có thể triển khai và kiểm thử từng story một cách độc lập.

## Định dạng: `[ID] [P?] [Story] Description`

- **[P]**: Có thể chạy song song (khác file, không phụ thuộc lẫn nhau)
- **[Story]**: Tác vụ thuộc user story nào (ví dụ: US1, US2, US3)
- Ghi đường dẫn file chính xác trong phần mô tả

## Quy ước đường dẫn

- **Một project**: `src/`, `tests/` tại thư mục gốc của repository
- **Ứng dụng web**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` hoặc `android/src/`
- Các đường dẫn bên dưới giả định là một project; hãy điều chỉnh theo cấu trúc trong plan.md

<!--
  ============================================================================
  QUAN TRỌNG: Các tác vụ bên dưới chỉ là TÁC VỤ MẪU để minh họa.

  Lệnh __SPECKIT_COMMAND_TASKS__ PHẢI thay chúng bằng các tác vụ thực tế dựa trên:
  - Các user story trong spec.md (kèm độ ưu tiên P1, P2, P3...)
  - Yêu cầu tính năng trong plan.md
  - Các thực thể trong data-model.md
  - Các endpoint trong contracts/

  Tác vụ PHẢI được tổ chức theo user story để mỗi story có thể:
  - Triển khai độc lập
  - Kiểm thử độc lập
  - Bàn giao như một phần tăng trưởng của MVP

  KHÔNG giữ lại các tác vụ mẫu này trong file tasks.md được sinh ra.
  ============================================================================
-->

## Giai đoạn 1: Thiết lập (Hạ tầng dùng chung)

**Mục đích**: Khởi tạo dự án và cấu trúc cơ bản

- [ ] T001 Tạo cấu trúc dự án theo kế hoạch triển khai
- [ ] T002 Khởi tạo project [language] với các thư viện phụ thuộc của [framework]
- [ ] T003 [P] Cấu hình công cụ lint và format

---

## Giai đoạn 2: Nền tảng (Điều kiện tiên quyết chặn các phần khác)

**Mục đích**: Hạ tầng cốt lõi PHẢI hoàn tất trước khi triển khai BẤT KỲ user story nào

**⚠️ QUAN TRỌNG**: Không được bắt đầu bất kỳ user story nào cho tới khi giai đoạn này hoàn tất

Ví dụ về các tác vụ nền tảng (điều chỉnh theo dự án của bạn):

- [ ] T004 Thiết lập schema cơ sở dữ liệu và framework migration
- [ ] T005 [P] Triển khai framework xác thực/phân quyền
- [ ] T006 [P] Thiết lập routing API và cấu trúc middleware
- [ ] T007 Tạo các model/thực thể cơ sở mà mọi story đều phụ thuộc
- [ ] T008 Cấu hình hạ tầng xử lý lỗi và ghi log
- [ ] T009 Thiết lập quản lý cấu hình môi trường

**Điểm kiểm tra**: Nền tảng đã sẵn sàng, giờ có thể bắt đầu triển khai các user story song song

---

## Giai đoạn 3: User story 1 - [Tiêu đề] (Ưu tiên: P1) 🎯 MVP

**Mục tiêu**: [Mô tả ngắn những gì story này mang lại]

**Kiểm thử độc lập**: [Cách kiểm chứng story này tự hoạt động được]

### Kiểm thử cho user story 1 (TÙY CHỌN - chỉ khi có yêu cầu test) ⚠️

> **LƯU Ý: Viết các test này TRƯỚC, đảm bảo chúng FAIL trước khi triển khai**

- [ ] T010 [P] [US1] Contract test cho [endpoint] trong tests/contract/test_[name].py
- [ ] T011 [P] [US1] Integration test cho [hành trình người dùng] trong tests/integration/test_[name].py

### Triển khai user story 1

- [ ] T012 [P] [US1] Tạo model [Entity1] trong src/models/[entity1].py
- [ ] T013 [P] [US1] Tạo model [Entity2] trong src/models/[entity2].py
- [ ] T014 [US1] Triển khai [Service] trong src/services/[service].py (phụ thuộc T012, T013)
- [ ] T015 [US1] Triển khai [endpoint/tính năng] trong src/[location]/[file].py
- [ ] T016 [US1] Thêm kiểm tra dữ liệu đầu vào và xử lý lỗi
- [ ] T017 [US1] Thêm log cho các thao tác của user story 1

**Điểm kiểm tra**: Tới đây, user story 1 phải hoạt động đầy đủ và kiểm thử độc lập được

---

## Giai đoạn 4: User story 2 - [Tiêu đề] (Ưu tiên: P2)

**Mục tiêu**: [Mô tả ngắn những gì story này mang lại]

**Kiểm thử độc lập**: [Cách kiểm chứng story này tự hoạt động được]

### Kiểm thử cho user story 2 (TÙY CHỌN - chỉ khi có yêu cầu test) ⚠️

- [ ] T018 [P] [US2] Contract test cho [endpoint] trong tests/contract/test_[name].py
- [ ] T019 [P] [US2] Integration test cho [hành trình người dùng] trong tests/integration/test_[name].py

### Triển khai user story 2

- [ ] T020 [P] [US2] Tạo model [Entity] trong src/models/[entity].py
- [ ] T021 [US2] Triển khai [Service] trong src/services/[service].py
- [ ] T022 [US2] Triển khai [endpoint/tính năng] trong src/[location]/[file].py
- [ ] T023 [US2] Tích hợp với các thành phần của user story 1 (nếu cần)

**Điểm kiểm tra**: Tới đây, cả user story 1 VÀ 2 đều phải hoạt động độc lập

---

## Giai đoạn 5: User story 3 - [Tiêu đề] (Ưu tiên: P3)

**Mục tiêu**: [Mô tả ngắn những gì story này mang lại]

**Kiểm thử độc lập**: [Cách kiểm chứng story này tự hoạt động được]

### Kiểm thử cho user story 3 (TÙY CHỌN - chỉ khi có yêu cầu test) ⚠️

- [ ] T024 [P] [US3] Contract test cho [endpoint] trong tests/contract/test_[name].py
- [ ] T025 [P] [US3] Integration test cho [hành trình người dùng] trong tests/integration/test_[name].py

### Triển khai user story 3

- [ ] T026 [P] [US3] Tạo model [Entity] trong src/models/[entity].py
- [ ] T027 [US3] Triển khai [Service] trong src/services/[service].py
- [ ] T028 [US3] Triển khai [endpoint/tính năng] trong src/[location]/[file].py

**Điểm kiểm tra**: Tới đây, mọi user story đều phải hoạt động độc lập

---

[Thêm các giai đoạn user story khác khi cần, theo cùng mẫu trên]

---

## Giai đoạn N: Hoàn thiện & Các vấn đề xuyên suốt

**Mục đích**: Những cải tiến ảnh hưởng tới nhiều user story

- [ ] TXXX [P] Cập nhật tài liệu trong docs/
- [ ] TXXX Dọn dẹp và refactor code
- [ ] TXXX Tối ưu hiệu năng trên mọi story
- [ ] TXXX [P] Bổ sung unit test (nếu có yêu cầu) trong tests/unit/
- [ ] TXXX Tăng cường bảo mật
- [ ] TXXX Chạy kiểm chứng theo quickstart.md

---

## Phụ thuộc & Thứ tự thực hiện

### Phụ thuộc giữa các giai đoạn

- **Thiết lập (Giai đoạn 1)**: Không phụ thuộc gì, có thể bắt đầu ngay
- **Nền tảng (Giai đoạn 2)**: Phụ thuộc vào việc hoàn tất Thiết lập; CHẶN mọi user story
- **User story (Giai đoạn 3 trở đi)**: Tất cả đều phụ thuộc vào việc hoàn tất giai đoạn Nền tảng
  - Sau đó các user story có thể làm song song (nếu đủ người)
  - Hoặc làm tuần tự theo độ ưu tiên (P1 → P2 → P3)
- **Hoàn thiện (Giai đoạn cuối)**: Phụ thuộc vào việc hoàn tất mọi user story mong muốn

### Phụ thuộc giữa các user story

- **User story 1 (P1)**: Có thể bắt đầu sau Nền tảng (Giai đoạn 2), không phụ thuộc story khác
- **User story 2 (P2)**: Có thể bắt đầu sau Nền tảng (Giai đoạn 2); có thể tích hợp với US1 nhưng vẫn phải kiểm thử độc lập được
- **User story 3 (P3)**: Có thể bắt đầu sau Nền tảng (Giai đoạn 2); có thể tích hợp với US1/US2 nhưng vẫn phải kiểm thử độc lập được

### Trong mỗi user story

- Test (nếu có) PHẢI được viết và FAIL trước khi triển khai
- Model trước service
- Service trước endpoint
- Phần triển khai cốt lõi trước phần tích hợp
- Hoàn tất story trước khi chuyển sang độ ưu tiên tiếp theo

### Cơ hội làm song song

- Mọi tác vụ Thiết lập có đánh dấu [P] đều chạy song song được
- Mọi tác vụ Nền tảng có đánh dấu [P] đều chạy song song được (trong Giai đoạn 2)
- Khi giai đoạn Nền tảng hoàn tất, mọi user story có thể bắt đầu song song (nếu nhóm đủ người)
- Mọi test của một user story có đánh dấu [P] đều chạy song song được
- Các model trong một story có đánh dấu [P] đều chạy song song được
- Các thành viên khác nhau trong nhóm có thể làm song song các user story khác nhau

---

## Ví dụ làm song song: User story 1

```bash
# Chạy cùng lúc mọi test của user story 1 (nếu có yêu cầu test):
Task: "Contract test cho [endpoint] trong tests/contract/test_[name].py"
Task: "Integration test cho [hành trình người dùng] trong tests/integration/test_[name].py"

# Tạo cùng lúc mọi model của user story 1:
Task: "Tạo model [Entity1] trong src/models/[entity1].py"
Task: "Tạo model [Entity2] trong src/models/[entity2].py"
```

---

## Chiến lược triển khai

### MVP trước (chỉ user story 1)

1. Hoàn tất Giai đoạn 1: Thiết lập
2. Hoàn tất Giai đoạn 2: Nền tảng (QUAN TRỌNG, chặn mọi story)
3. Hoàn tất Giai đoạn 3: User story 1
4. **DỪNG LẠI và KIỂM CHỨNG**: Kiểm thử độc lập user story 1
5. Triển khai/demo nếu đã sẵn sàng

### Bàn giao tăng dần

1. Hoàn tất Thiết lập + Nền tảng → Nền tảng sẵn sàng
2. Thêm user story 1 → Kiểm thử độc lập → Triển khai/Demo (MVP!)
3. Thêm user story 2 → Kiểm thử độc lập → Triển khai/Demo
4. Thêm user story 3 → Kiểm thử độc lập → Triển khai/Demo
5. Mỗi story mang thêm giá trị mà không làm hỏng các story trước

### Chiến lược cho nhóm làm song song

Khi có nhiều lập trình viên:

1. Cả nhóm cùng hoàn tất Thiết lập + Nền tảng
2. Khi Nền tảng xong:
   - Lập trình viên A: User story 1
   - Lập trình viên B: User story 2
   - Lập trình viên C: User story 3
3. Các story hoàn tất và tích hợp một cách độc lập

---

## Ghi chú

- Tác vụ [P] = khác file, không phụ thuộc lẫn nhau
- Nhãn [Story] gắn tác vụ với một user story cụ thể để truy vết
- Mỗi user story phải hoàn tất và kiểm thử được một cách độc lập
- Kiểm chứng test fail trước khi triển khai
- Commit sau mỗi tác vụ hoặc mỗi nhóm tác vụ hợp lý
- Có thể dừng ở bất kỳ điểm kiểm tra nào để kiểm chứng story một cách độc lập
- Tránh: tác vụ mơ hồ, xung đột do sửa cùng file, phụ thuộc chéo giữa các story làm mất tính độc lập
