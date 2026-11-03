# Bảng thuật ngữ tiếng Việt cho Spec Kit

Tài liệu này thống nhất cách dịch thuật ngữ trong bản Việt hóa Spec Kit ([README.vi.md](../../README.vi.md), [spec-driven.vi.md](../../spec-driven.vi.md), [tài liệu tiếng Việt](index.md) và [preset `vi`](../../presets/vi/README.md)). Mục tiêu là tiếng Việt tự nhiên, chuyên nghiệp, đúng cách dân phát triển phần mềm Việt Nam đang nói, đồng thời không làm hỏng bất kỳ thứ gì mà CLI và agent phụ thuộc vào.

## 1. Nguyên tắc chung

1. **Dịch ý, không dịch từng chữ.** Câu tiếng Việt phải đọc trôi chảy; được phép đảo cấu trúc câu.
2. **Giữ thuật ngữ đã quen dùng trong giới lập trình.** Những từ như branch, commit, merge, PR, deploy, framework, API, endpoint, middleware, test, unit test, refactor, log, schema, migration, hook, preset, extension, workflow, checklist, MVP, user story giữ nguyên tiếng Anh.
3. **Lần đầu xuất hiện có thể kèm tiếng Anh trong ngoặc**, ví dụ "hiến chương (constitution)", sau đó chỉ dùng tiếng Việt.
4. **Từ khóa quy phạm** dịch thống nhất: MUST → PHẢI, MUST NOT → KHÔNG ĐƯỢC, SHOULD → NÊN, NEVER → KHÔNG BAO GIỜ, REQUIRED → BẮT BUỘC, OPTIONAL → TÙY CHỌN, CRITICAL/IMPORTANT → QUAN TRỌNG (trừ khi là mức độ nghiêm trọng, xem mục 4).
5. **Xưng hô**: Văn bản hướng dẫn agent dùng "bạn". Văn bản hướng dẫn người dùng dùng "bạn". Không dùng "quý vị", "các bạn".
6. **Ngày tháng** trong văn xuôi viết dd/mm/yyyy; ngày trong artifact vẫn theo ISO `YYYY-MM-DD`.

## 2. Những thứ KHÔNG được dịch

| Nhóm | Ví dụ | Lý do |
| --- | --- | --- |
| Tên lệnh và skill | `/speckit.specify`, `/speckit-plan`, `speckit.tasks`, `/skill:speckit-...`, `$speckit-...` | CLI đăng ký lệnh theo đúng tên này |
| Lệnh CLI và option | `specify init`, `specify preset add --dev`, `--integration`, `--script` | Là giao diện dòng lệnh |
| Placeholder của Spec Kit | `__SPECKIT_COMMAND_PLAN__`, `$ARGUMENTS`, `{SCRIPT}`, `{ARGS}`, `{extension}`, `{command}`, `{description}`, `{prompt}` | CLI thay thế lúc cài đặt hoặc lúc chạy |
| Token trong template | `[FEATURE NAME]`, `[DATE]`, `[###-feature-name]`, `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`, `[CONSTITUTION_VERSION]`, `[REMOVE IF UNUSED]`... | Lệnh `constitution` và các lệnh khác tìm đúng các token `[ALL_CAPS]` này |
| Dấu đánh dấu | `[NEEDS CLARIFICATION: ...]`, `[P]`, `[US1]`, `[X]`/`[x]`, `- [ ]` | Agent và lệnh đếm, lọc theo các dấu này |
| Mã định danh | `T001`, `FR-001`, `SC-001`, `CHK001`, `US1/AC2`, `Q1` | Dùng để truy vết |
| Tên file và thư mục | `spec.md`, `plan.md`, `tasks.md`, `research.md`, `data-model.md`, `quickstart.md`, `contracts/`, `checklists/requirements.md`, `.specify/memory/constitution.md`, `.specify/extensions.yml`, `.specify/feature.json` | Script và lệnh đọc/ghi đúng đường dẫn |
| Biến trong lệnh | `FEATURE_DIR`, `FEATURE_SPEC`, `IMPL_PLAN`, `TASKS_TEMPLATE_CONTENT`, `TEMPLATE_CONTENT`, `SPECIFY_FEATURE_DIRECTORY`, `SPEC_FILE`, `AVAILABLE_DOCS` | Là khóa JSON do script trả về |
| Khóa cấu hình | `hooks.before_plan`, `optional`, `enabled`, `condition`, `feature_numbering`, `EXECUTE_COMMAND:` | Là khóa YAML/JSON hoặc giao thức hook |
| Giá trị trạng thái máy đọc | `Converged`, `converged`, `tasks_appended`, `missing`, `partial`, `contradicts`, `unrequested`, `verified`, `go`, `kill` | Lệnh và người dùng so khớp nguyên văn |
| Mức độ nghiêm trọng | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` | Giữ nguyên để lọc và so sánh giữa các báo cáo |
| Frontmatter | mọi khóa (`description`, `handoffs`, `agent`, `scripts`, `send`, `sh`, `ps`, `py`) và giá trị kỹ thuật | Chỉ dịch giá trị của `description`, `label`, `prompt` |
| Nội dung code | code mẫu, lệnh shell, pattern ignore (`node_modules/`, `*.pyc`...) | Là mã chạy được |
| Tên sản phẩm | Spec Kit, Specify CLI, GitHub Copilot, Claude Code, Cursor... | Tên riêng |

Script `presets/vi/tools/check_translation.py` kiểm tra tự động các quy tắc trên cho preset `vi` và cho các trang trong `docs/vi/` (khối code, inline code, link, anchor và cấu trúc heading phải khớp với bản tiếng Anh).

## 3. Bảng thuật ngữ

| Tiếng Anh | Tiếng Việt | Ghi chú |
| --- | --- | --- |
| Spec-Driven Development (SDD) | Phát triển hướng đặc tả (SDD) | Giữ viết tắt SDD |
| specification, spec | đặc tả | "spec" giữ nguyên khi là tên file `spec.md` |
| feature specification | đặc tả tính năng | |
| feature | tính năng | |
| feature branch | feature branch | |
| implementation plan | kế hoạch triển khai | |
| plan / planning | kế hoạch / lập kế hoạch | |
| task, tasks | tác vụ, danh sách tác vụ | |
| task breakdown | phân rã tác vụ | |
| constitution | hiến chương (dự án) | |
| principle | nguyên tắc | |
| article (of constitution) | điều, điều khoản | "Điều I", "Điều VII" |
| amendment | sửa đổi | |
| ratified / ratification date | phê chuẩn / ngày phê chuẩn | |
| governance | quản trị | |
| clarify / clarification | làm rõ / nội dung làm rõ | |
| ambiguity | điểm mơ hồ | |
| underspecified | chưa được đặc tả đủ | |
| converge / convergence | hội tụ | Lệnh `/speckit.converge` giữ nguyên |
| analyze / analysis | phân tích | |
| implement / implementation | triển khai / phần triển khai | |
| checklist | checklist | |
| requirement | yêu cầu | |
| functional requirement | yêu cầu chức năng | |
| non-functional requirement | yêu cầu phi chức năng | |
| success criteria | tiêu chí thành công | |
| measurable outcome | kết quả đo lường được | |
| acceptance criteria | tiêu chí chấp nhận | |
| acceptance scenario | kịch bản chấp nhận | |
| Given / When / Then | Cho trước / Khi / Thì | |
| user story | user story | |
| user journey | hành trình người dùng | |
| user scenario | kịch bản người dùng | |
| edge case | trường hợp biên | |
| key entity | thực thể chính | |
| assumption | giả định | |
| dependency | phụ thuộc / thư viện phụ thuộc | Tùy ngữ cảnh |
| priority | độ ưu tiên | "Ưu tiên: P1" |
| independent test | kiểm thử độc lập | |
| technical context | bối cảnh kỹ thuật | |
| research | nghiên cứu | |
| data model | mô hình dữ liệu | |
| contract / interface contract | contract / contract giao diện | |
| contract test, integration test, unit test | contract test, integration test, unit test | |
| gate / quality gate | cổng kiểm soát / cổng kiểm soát chất lượng | |
| constitution check | kiểm tra hiến chương | |
| complexity tracking | theo dõi độ phức tạp | |
| phase | giai đoạn | "Giai đoạn 1: Thiết lập" |
| setup | thiết lập | |
| foundational | nền tảng | |
| polish & cross-cutting concerns | hoàn thiện & các vấn đề xuyên suốt | |
| checkpoint | điểm kiểm tra | |
| incremental delivery | bàn giao tăng dần | |
| artifact | artifact | Có thể giải thích "tài liệu đầu ra" lần đầu |
| coding agent | agent lập trình | |
| AI coding agent | agent lập trình AI | |
| integration (Spec Kit) | integration | Khi là cơ chế của Spec Kit |
| integration (system) | tích hợp | Khi là tích hợp hệ thống |
| extension | extension | |
| hook / pre-hook | hook / pre-hook | "Hook của extension" |
| mandatory hook / optional hook | hook bắt buộc / hook tùy chọn | |
| preset | preset | |
| workflow / workflow step / overlay | workflow / workflow step / overlay | |
| bundle | bundle | |
| catalog | catalog | |
| project-local override | ghi đè cục bộ trong dự án | |
| resolution stack | chồng phân giải | |
| handoff | bàn giao | |
| traceability | truy vết | |
| coverage | độ phủ | |
| finding | phát hiện | `Finding` giữ nguyên khi là tên cấu trúc |
| severity | mức độ nghiêm trọng | Giá trị giữ nguyên CRITICAL/HIGH/MEDIUM/LOW |
| remediation | khắc phục | |
| reviewer | người review | |
| stakeholder | các bên liên quan | |
| best practice | best practice | |
| tech stack | tech stack | |

## 4. Tên mục chuẩn trong artifact

Các lệnh tiếng Việt tham chiếu tới tên mục dưới đây, nên phải dùng đúng như bảng khi sửa template:

| Template | Tiếng Anh | Tiếng Việt |
| --- | --- | --- |
| spec | Feature Specification | Đặc tả tính năng |
| spec | User Scenarios & Testing | Kịch bản người dùng & Kiểm thử |
| spec | Edge Cases | Trường hợp biên |
| spec | Requirements / Functional Requirements | Yêu cầu / Yêu cầu chức năng |
| spec | Key Entities | Thực thể chính |
| spec | Success Criteria / Measurable Outcomes | Tiêu chí thành công / Kết quả đo lường được |
| spec | Assumptions | Giả định |
| spec (clarify) | Clarifications / Session YYYY-MM-DD | Làm rõ / Phiên YYYY-MM-DD |
| plan | Implementation Plan | Kế hoạch triển khai |
| plan | Summary / Technical Context | Tóm tắt / Bối cảnh kỹ thuật |
| plan | Constitution Check | Kiểm tra hiến chương |
| plan | Project Structure | Cấu trúc dự án |
| plan | Complexity Tracking | Theo dõi độ phức tạp |
| tasks | Phase N: Setup / Foundational / Polish | Giai đoạn N: Thiết lập / Nền tảng / Hoàn thiện |
| tasks (converge) | Phase N: Convergence | Giai đoạn N: Hội tụ |
| tasks | Dependencies & Execution Order | Phụ thuộc & Thứ tự thực hiện |
| tasks | Implementation Strategy | Chiến lược triển khai |
| constitution | Core Principles / Governance | Các nguyên tắc cốt lõi / Quản trị |
| checklist | Notes | Ghi chú |
| checklist tags | Completeness, Clarity, Consistency, Coverage, Measurability, Edge Case, Gap, Ambiguity, Conflict, Assumption, Dependency, Traceability, Exception Flow, Acceptance Criteria, Spec §X.Y | Đầy đủ, Rõ ràng, Nhất quán, Độ phủ, Đo lường được, Trường hợp biên, Thiếu, Mơ hồ, Xung đột, Giả định, Phụ thuộc, Truy vết, Luồng ngoại lệ, Tiêu chí chấp nhận, Đặc tả §X.Y |

## 5. Ví dụ câu

| Tiếng Anh | Nên dịch | Tránh |
| --- | --- | --- |
| You **MUST** consider the user input before proceeding (if not empty). | Bạn **PHẢI** xem xét đầu vào của người dùng trước khi tiếp tục (nếu không rỗng). | Bạn **PHẢI** cân nhắc người dùng đầu vào trước khi tiến hành. |
| If no hooks are registered, skip silently. | Nếu không có hook nào được đăng ký, lặng lẽ bỏ qua. | Nếu không có móc nào được ghi danh, bỏ qua một cách im lặng. |
| Every requirement must be testable. | Mỗi yêu cầu phải kiểm thử được. | Mọi yêu cầu phải có khả năng được thử nghiệm. |
| Tests are OPTIONAL. | Test là TÙY CHỌN. | Các bài kiểm tra là KHÔNG BẮT BUỘC. |

## 6. Thuật ngữ trong tài liệu (docs)

| Tiếng Anh | Tiếng Việt | Ghi chú |
| --- | --- | --- |
| quickstart | hướng dẫn nhanh | |
| walkthrough | walkthrough / hướng dẫn từng bước | Giữ "walkthrough" khi là tên mục cộng đồng |
| bundled, opt-in extension | extension đi kèm, chỉ chạy khi bạn chủ động bật | |
| first-party | chính thức (first-party) | |
| air-gapped | air-gapped | Môi trường cách ly hoàn toàn khỏi mạng |
| wheel | wheel | Định dạng package Python |
| editable install | bản cài editable | |
| install route | cách cài đặt | |
| pin (a version) | ghim (phiên bản) | |
| upgrade / refresh | nâng cấp / làm mới | |
| managed file | file được quản lý | File do Spec Kit cài và theo dõi trong manifest |
| manifest-aware | dựa trên manifest | |
| fallback | phương án dự phòng | |
| escape hatch | lối thoát | |
| runtime resolution | phân giải lúc chạy | |
| source of truth | nguồn sự thật | |
| reconcile / reconciliation | đối soát | |
| drift | độ lệch / lệch nhau | |
| flow-back / flow-forward / living spec | flow-back (chảy ngược) / flow-forward (chảy xuôi) / living spec (đặc tả sống) | Giữ tên tiếng Anh vì là tên mô hình |
| spec-first / spec-anchored / spec-as-source | giữ nguyên, kèm giải thích lần đầu | |
| roadmap | lộ trình | Tên file `roadmap.md`, `ROADMAP.md` giữ nguyên |
| slice | lát cắt | |
| epic | epic | |
| context window / context compaction | cửa sổ ngữ cảnh / nén ngữ cảnh | |
| sub-agent | sub-agent | |
| hallucinate | bịa đặt (hallucinate) | |
| greenfield / brownfield | greenfield / brownfield | |
| contract-driven development | phát triển hướng contract | |
| provider / consumer | bên cung cấp / bên sử dụng | |
| authoritative | chính thức | "contract chính thức" |
| idempotency | tính idempotent | |
| rollout / rollback | rollout / rollback | |
| breaking change | thay đổi phá vỡ tương thích | |
| deterministic | tất định | |
| agentic workflow | workflow agentic | |
| maintainer / contributor | maintainer / người đóng góp | |
| dogfooding | tự dùng (dogfooding) | |
| appetite | mức đầu tư sẵn sàng bỏ ra (appetite) | Thuật ngữ của Shape Up |
| verdict | kết luận | Giá trị `go`, `verified`... giữ nguyên |
| scaffold / scaffolding | khung / phần khung, dựng khung | |
| resolve / resolution (stack) | phân giải / chồng phân giải | Dùng cho template, lệnh, catalog, workflow |
| precedence / priority | độ ưu tiên / priority | `priority` giữ nguyên khi là trường cấu hình |
| discovery-only / install-allowed | chỉ tìm kiếm / cho phép cài | Chế độ của catalog |
| overlay / slot / anchor | overlay / slot / anchor | Thuật ngữ workflow, giữ nguyên |
| step / gate / fan-out / fan-in | step / gate / fan-out / fan-in | Loại workflow step, giữ nguyên |
| run / resume | lần chạy / resume (tiếp tục) | `run_id`, `specify workflow resume` giữ nguyên |
| capture (output) | thu (đầu ra) | `capture: true` giữ nguyên |
| interpolation / expression / filter | nội suy / biểu thức / filter | |
| strict mode | chế độ strict | `strict: true` giữ nguyên |
| vet / audit / endorse | kiểm định / kiểm định, kiểm toán / bảo chứng | |
| manifest / archive / digest | manifest / archive / digest | |
| bundle | bundle | Tên thành phần, giữ nguyên |
| submission | bài gửi | Biểu mẫu issue gửi lên catalog cộng đồng |
| walkthrough | hướng dẫn từng bước | |
| fail-closed | đóng khi lỗi | |

### Quy ước riêng cho `docs/vi/`

- Cấu trúc thư mục `docs/vi/` mô phỏng đúng `docs/` và có `toc.yml` riêng; mỗi trang có một khung ghi chú liên kết về bản tiếng Anh.
- Link tới trang đã dịch trỏ vào `docs/vi/`; link tới trang chưa dịch trỏ về bản tiếng Anh.
- Trong các bảng catalog cộng đồng (`community/`), cột tên dự án và nhãn `Read-only`/`Read+Write` giữ nguyên; chỉ dịch mô tả.
- Thông báo lỗi và chuỗi CLI trích nguyên văn (ví dụ `Command exited with code 2`, "not JSON-serializable") giữ nguyên tiếng Anh để người đọc tìm được trong log.
- Trước mỗi heading đã dịch có thẻ `<a id="...">` mang anchor của heading tiếng Anh, để mọi link có `#anchor` từ bản tiếng Anh vẫn dùng được.
- Khối code, lệnh, ví dụ prompt trong khối code, tên file và placeholder giữ nguyên tiếng Anh.
