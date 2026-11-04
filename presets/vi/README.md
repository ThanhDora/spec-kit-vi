# Preset tiếng Việt (`vi`)

Preset này thay toàn bộ template lõi và các lệnh SDD của Spec Kit bằng bản tiếng Việt. Sau khi cài, agent lập trình sẽ viết đặc tả, kế hoạch, danh sách tác vụ, checklist, hiến chương và phản hồi cho bạn bằng tiếng Việt, trong khi tên lệnh, tên file, đường dẫn và placeholder vẫn giữ nguyên để Spec Kit hoạt động bình thường.

## Nội dung

| Loại | Tên | Thay cho |
| --- | --- | --- |
| Template | `spec-template`, `plan-template`, `tasks-template`, `checklist-template`, `constitution-template` | 5 template lõi trong `templates/` |
| Lệnh | `speckit.specify`, `speckit.clarify`, `speckit.plan`, `speckit.tasks`, `speckit.analyze`, `speckit.checklist`, `speckit.implement`, `speckit.converge`, `speckit.constitution` | 9 lệnh lõi trong `templates/commands/` |

## Cài đặt

Từ thư mục dự án đã chạy `specify init`:

```bash
# Cài từ bản clone của repo này
specify preset add --dev /đường/dẫn/tới/spec-kit-vi/presets/vi

# Kiểm tra template đang được dùng
specify preset resolve spec-template
specify preset list
```

Gỡ preset để quay về bản tiếng Anh:

```bash
specify preset remove vi
```

> [!NOTE]
> Hiến chương `.specify/memory/constitution.md` được tạo một lần lúc `specify init`. Cài preset không ghi đè file đó; lần chạy `/speckit.constitution` (hoặc `/speckit-constitution`) tiếp theo sẽ dùng template hiến chương tiếng Việt.

## Quy ước dịch

- Tên lệnh (`/speckit.*`), tên file và thư mục (`spec.md`, `plan.md`, `tasks.md`, `checklists/requirements.md`, `.specify/...`), biến môi trường, khóa JSON/YAML, placeholder (`__SPECKIT_COMMAND_*__`, `$ARGUMENTS`, `{SCRIPT}`, `{ARGS}`, `[FEATURE NAME]`, `[ALL_CAPS]`...) và các dấu đánh dấu như `[NEEDS CLARIFICATION]`, `[P]`, `[US1]`, `T001`, `FR-001`, `SC-001`, `CHK001` được giữ nguyên.
- Frontmatter giữ nguyên mọi khóa và giá trị, chỉ dịch `description`, `label` và `prompt`.
- Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../../docs/vi/GLOSSARY.md).

## Kiểm tra bản dịch

Script sau so sánh từng file tiếng Việt (template, lệnh của preset và các trang trong `docs/vi/`) với bản tiếng Anh gốc và báo lỗi nếu thiếu hoặc thừa bất kỳ placeholder, tham chiếu lệnh, inline code, khối code hay heading nào, hoặc nếu frontmatter bị thay đổi:

```bash
python presets/vi/tools/check_translation.py              # tất cả
python presets/vi/tools/check_translation.py --only preset # chỉ preset
python presets/vi/tools/check_translation.py --only docs   # chỉ docs/vi
```

Một số inline code là văn bản hiển thị cho người dùng (ví dụ `**Question:**` → `**Câu hỏi:**`) được dịch có chủ đích; danh sách này nằm trong `INLINE_TRANSLATIONS` của script.

## Đồng bộ với bản gốc

Khi upstream cập nhật `templates/` hoặc `templates/commands/`, chạy lại script kiểm tra. Mọi khác biệt về placeholder hay cấu trúc sẽ bị báo lỗi, giúp phát hiện những file cần dịch lại.

## Hạn chế đã biết

- Ở bản Spec Kit hiện tại, template do preset cung cấp được dùng nguyên văn, không được thay placeholder `__SPECKIT_COMMAND_*__` như template lõi lúc `specify init`. Vì vậy `plan-template.md`, `tasks-template.md` và `checklist-template.md` của preset này có thể để lại nguyên chuỗi như `__SPECKIT_COMMAND_PLAN__` trong các ghi chú của artifact sinh ra. Các file lệnh (`/speckit.*`) không bị ảnh hưởng vì placeholder trong lệnh vẫn được thay khi cài preset. Preset giữ nguyên placeholder để đúng với bản gốc và sẽ tự hiển thị đúng khi Spec Kit hỗ trợ thay placeholder trong template của preset.
