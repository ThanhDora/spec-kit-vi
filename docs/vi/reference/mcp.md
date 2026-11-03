# MCP server

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../reference/mcp.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

> [!WARNING]
> `specify mcp` đang ở giai đoạn thử nghiệm. Danh mục lệnh và hợp đồng công cụ của nó có thể thay đổi trước khi bề mặt MCP được tuyên bố ổn định.

```bash
specify mcp
```

Khởi động một server Model Context Protocol **chỉ qua stdio**. Lệnh không cung cấp HTTP, SSE, quản lý daemon/service hay tùy chọn chọn phương thức truyền tải. Hãy cấu hình MCP host để khởi chạy `specify mcp` như một tiến trình con cục bộ.

Vì stdout mang các frame giao thức MCP, server không in banner Spec Kit, đầu ra Rich, thông báo khởi động, cảnh báo hay log ra đó.

<a id="tools"></a>

## Công cụ

Server cung cấp các công cụ chính thức với đầu vào và kết quả có kiểu. Tất cả đều chỉ đọc, chỉ cục bộ (không truy cập mạng) và từ chối đối số không mong đợi.

| Công cụ | Mục đích |
| --- | --- |
| `specify_version` | Trả về phiên bản CLI đã cài, runtime, hệ thống và khả năng tính năng. Không nhận đối số. |
| `specify_artifact_list` | Trả về một trang đã phân trang trong danh mục artifact của dự án (`command`, `template`, `script`, `hook`) |
| `specify_artifact_info` | Trả về một artifact và toàn bộ chồng kết hợp của nó |
| `specify_workflow_list` | Liệt kê các workflow đã cài và cảnh báo về mục bị bỏ qua theo thứ tự trong registry |

Các công cụ artifact nhận `project_directory` tuyệt đối tùy chọn; mặc định là thư mục khởi chạy server.

`specify_artifact_list` còn nhận `limit` (1-1000, mặc định 100) và `cursor`. Kết quả của nó có `rows`, `next_cursor` và `truncated`; khi `truncated` là true, truyền `next_cursor` làm `cursor` để lấy trang tiếp theo.

`specify_artifact_info` nhận `identifier` (tên trần hoặc `kind:name`) và `kind` tùy chọn (`command`, `template`, `script` hoặc `hook`).

`specify artifact lookup` không có qua MCP: nó chưa có thao tác dùng chung có kiểu, nên không có công cụ `specify_artifact_lookup` nào được đăng ký.

Ba công cụ chung cũng được đăng ký, và chỉ hỗ trợ lệnh dấu chấm `version`; mọi tên lệnh khác bị từ chối với lỗi công cụ `unavailable_command`.

| Công cụ | Mục đích |
| --- | --- |
| `specify_list_commands` | Liệt kê các lệnh CLI được công cụ chung hỗ trợ |
| `specify_describe_command` | Mô tả một lệnh CLI dấu chấm được hỗ trợ |
| `specify_run_command` | Chạy một lệnh được hỗ trợ qua Specify CLI thật |

Server không cung cấp thao tác thay đổi dữ liệu, thao tác cài đặt hay cập nhật, việc thực thi workflow, xác nhận hay các cấp truy cập.

<a id="installed-workflow-list"></a>

## Danh sách workflow đã cài

`specify_workflow_list` nhận `project_directory` tuyệt đối tùy chọn (mặc định: thư mục khởi chạy server) và `limit` (1–1000, mặc định 100). Nó chỉ đọc registry workflow đã cài; không bao giờ nạp step tùy chỉnh, tải catalog, sửa file hay thực thi workflow.

Kết quả có `items` theo thứ tự và một boolean `truncated`. Mục workflow có `kind: "workflow"`, `id`, `name`, `version`, `description` có thể null, và `enabled`. Các mục registry riêng lẻ sai định dạng tạo ra mục `kind: "warning"` với `code: "invalid_registry_entry"`, `workflow_id` và `message` ở đúng vị trí ban đầu của chúng. Giới hạn tính cả workflow lẫn cảnh báo. `truncated: true` cho biết rõ là có mục bị lược bỏ; tăng `limit` để lấy thêm, tối đa
1000. Không có cursor để tiếp tục. CLI vẫn giữ danh sách đầy đủ.

File registry bị thiếu cho ra danh sách rỗng. File registry bị hỏng hoặc không đọc được cho ra `workflow_registry_read_failed`; lưu trữ không an toàn cho ra `unsafe_workflow_storage`. Các lỗi mong đợi khác là `invalid_project_directory` và `not_a_spec_kit_project`. Lỗi chứa `code`, `message`, `details` và `retryable` trong `error`, với `isError: true`. Lỗi bất ngờ dùng `internal_error` đã làm sạch; kết quả thao tác không hợp lệ dùng `invalid_operation_result`. Phản hồi vượt quá 1 MiB cho ra lỗi `response_too_large` có thể thử lại thay vì thành công một phần; hãy thử lại với giới hạn nhỏ hơn. Chi tiết ngoại lệ của registry không được đưa ra qua MCP.

Giá trị `limit` ngoài phạm vi bị từ chối trước khi thao tác chạy và cho ra lỗi kiểm tra đầu vào chỉ có văn bản, không có nội dung có cấu trúc; xem [Lỗi kiểm tra đầu vào](#input-validation-errors).

Việc liệt kê workflow đọc nội dung registry qua chủ thể chính sách `FileHelper` của dự án được chọn, từ chối Windows junction và các reparse point không được hỗ trợ tại ranh giới đọc. Symlink thông thường trong registry workflow vẫn không được phép. Các nơi gọi registry workflow khác không được công cụ này chuyển đổi. Các kiểm tra này không cung cấp sandbox của hệ điều hành hay giới hạn filesystem không có race condition; registry vẫn được phân tích toàn bộ trước khi áp dụng giới hạn số mục.

Kết quả thao tác vượt giới hạn số mục được yêu cầu, hoặc báo bị cắt bớt mà không lấp đầy giới hạn đó, bị từ chối là `invalid_operation_result`. Schema đầu ra cũng giới hạn `items` ở 1000.

<a id="input-validation-errors"></a>

## Lỗi kiểm tra đầu vào

Các công cụ chính thức kiểm tra đối số theo schema đầu vào trước khi chạy. Đối số không mong đợi, `limit` ngoài phạm vi, `cursor` sai định dạng hoặc `kind` không được hỗ trợ bị từ chối như một lỗi công cụ MCP chỉ có văn bản, không có nội dung có cấu trúc, nên client không thể đọc `error.code` từ đó.

<a id="version-tool-result-and-errors"></a>

## Kết quả và lỗi của công cụ version

`specify_version` trả về trực tiếp đối tượng kết quả. Nếu thao tác thất bại, nó trả về lỗi công cụ MCP có nội dung có cấu trúc gồm `error.code` (`invalid_operation_result` hoặc `internal_error`), `error.message` và `error.details`.

<a id="artifact-results-and-errors"></a>

## Kết quả và lỗi của artifact

Công cụ artifact trả về kết quả dưới dạng nội dung có cấu trúc. Lỗi thao tác là lỗi công cụ MCP có nội dung có cấu trúc gồm `error.code`, `error.message`, `error.details` và `error.retryable`. Cả hai công cụ artifact có thể trả về `invalid_project_directory`, `not_a_spec_kit_project`, `artifact_resolution_failed`, `invalid_operation_result` và `internal_error`. `specify_artifact_info` còn có thể trả về `invalid_artifact_identifier`, `unknown_artifact`, `unknown_hook` và `ambiguous_artifact`. Kết quả lớn hơn 1 MiB trả về lỗi `response_too_large` có thể thử lại; với công cụ list, hãy thử lại với `limit` nhỏ hơn.

<a id="generic-tool-result-and-errors"></a>

## Kết quả và lỗi của công cụ chung

`specify_run_command` gọi lệnh chuẩn bên dưới trong một tiến trình con tách biệt, dùng cùng môi trường Python với CLI đang chạy:

```bash
specify version --json
```

Khi thành công, công cụ MCP trả về trực tiếp đối tượng JSON của lệnh đó với `cli_version`, `runtime`, `system` và `features`. Nó không bọc kết quả trong các trường chung `schema_version`, `ok` hay `result`.

Khi CLI thất bại, adapter đọc lỗi JSON có cấu trúc từ stderr và trả về lỗi công cụ MCP chứa `error.code`, `error.message` và `error.details`. Đầu ra tiến trình con rỗng, sai định dạng, lẫn lộn hoặc không phải JSON được báo là `adapter_internal_error` đã làm sạch; server không bao giờ thay bằng kết quả dự phòng trông như thành công hay để lộ traceback.
