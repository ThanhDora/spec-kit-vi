# Checklist [CHECKLIST TYPE]: [FEATURE NAME]

**Mục đích**: [Mô tả ngắn phạm vi của checklist này]
**Ngày tạo**: [DATE]
**Tính năng**: [Link tới spec.md hoặc tài liệu liên quan]

**Lưu ý**: Checklist tùy chỉnh này được lệnh `__SPECKIT_COMMAND_CHECKLIST__` sinh ra dựa trên bối cảnh và yêu cầu của tính năng.
**Người chịu trách nhiệm review**: Checklist này là artifact review chất lượng yêu cầu, thuộc về người review. Chỉ đánh dấu một mục `[x]` khi người review xác định tiêu chí chất lượng yêu cầu đó đã được đáp ứng.
**Ý nghĩa của dấu đánh dấu**: `[x]` nghĩa là tiêu chí đã được review và đạt về chất lượng yêu cầu. Nó không có nghĩa là phần việc triển khai đã hoàn tất.

<!--
  ============================================================================
  QUAN TRỌNG: Các mục checklist bên dưới chỉ là MỤC MẪU để minh họa.

  Lệnh __SPECKIT_COMMAND_CHECKLIST__ PHẢI thay chúng bằng các mục thực tế dựa trên:
  - Yêu cầu checklist cụ thể của người dùng
  - Yêu cầu tính năng trong spec.md
  - Bối cảnh kỹ thuật trong plan.md
  - Chi tiết triển khai trong tasks.md

  KHÔNG giữ lại các mục mẫu này trong file checklist được sinh ra.
  ============================================================================
-->

## [Nhóm 1]

- [ ] CHK001 Mục checklist đầu tiên với hành động rõ ràng
- [ ] CHK002 Mục checklist thứ hai
- [ ] CHK003 Mục checklist thứ ba

## [Nhóm 2]

- [ ] CHK004 Một mục khác trong nhóm
- [ ] CHK005 Mục có tiêu chí cụ thể
- [ ] CHK006 Mục cuối cùng trong nhóm này

## Ghi chú

- Chỉ đánh dấu `[x]` sau khi review xác nhận tiêu chí chất lượng yêu cầu đã được đáp ứng
- Để trống những mục vẫn cần làm rõ, chỉnh sửa hoặc chờ người review đánh giá
- `__SPECKIT_COMMAND_IMPLEMENT__` đọc trạng thái checkbox của checklist như một cổng kiểm soát và không được sửa các dấu đánh dấu
- `checklists/requirements.md` có vòng đời riêng, có sẵn, do `__SPECKIT_COMMAND_SPECIFY__` và `__SPECKIT_COMMAND_CLARIFY__` quản lý
- Thêm nhận xét hoặc phát hiện ngay tại dòng tương ứng
- Đính kèm link tới tài nguyên hoặc tài liệu liên quan
- Các mục được đánh số tuần tự để dễ tham chiếu
