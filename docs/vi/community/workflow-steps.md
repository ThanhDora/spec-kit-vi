<a id="community-workflow-step-types"></a>

# Các loại workflow step cộng đồng

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../community/workflow-steps.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

> [!NOTE]
> Các loại workflow step cộng đồng được tạo và duy trì độc lập bởi tác giả của chúng. Người duy trì xác minh metadata của bài gửi và cấu trúc package; họ **không review, kiểm định, bảo chứng hay hỗ trợ code Python có thể thực thi**. Việc cài đặt kiểm tra và sao chép package mà không import code Python của nó. Các lệnh `specify workflow add`, `run` và `resume` về sau sẽ nạp package step đã cài, thực thi code lúc import với quyền của người dùng. Hãy review mã nguồn trước khi cài và sử dụng.

Package workflow step tùy chỉnh bổ sung một `type:` mà workflow có thể dùng ngoài các loại step có sẵn. Đường tiếp nhận chuẩn là biểu mẫu issue [Workflow Step Type Submission](https://github.com/github/spec-kit/issues/new?template=workflow_step_submission.yml) cho mục mới, cập nhật phiên bản và sửa metadata.

Mở biểu mẫu chỉ áp dụng nhãn verdict `triage-must-have`. Người duy trì áp dụng `workflow-step-submission` trong quá trình phân loại để bắt đầu kiểm tra metadata tự động. Kiểm tra thành công sẽ đề xuất thay đổi catalog và tài liệu trong một draft PR để người duy trì review. Quy trình tự động không bao giờ cài, import, thực thi hay review code Python được gửi.

Các mục được chấp nhận được công bố trong [`workflows/step-catalog.community.json`](https://github.com/github/spec-kit/blob/main/workflows/step-catalog.community.json). Catalog cộng đồng có sẵn ở chế độ **chỉ tìm kiếm**. Các mục được chấp nhận có thể xuất hiện trong `specify workflow step search` và `info`, nhưng `specify workflow step add <id>` sẽ không cài code thực thi từ nguồn đó. Sau khi review mã nguồn, hãy cài trực tiếp archive có phiên bản đã gửi bằng `--from`, hoặc dùng một catalog step được cấu hình riêng mà bạn cho phép cài một cách tường minh.

<a id="available-step-types"></a>

## Các loại step có sẵn

| Loại step | Phiên bản | Mô tả |
| --- | --- | --- |
| [Decision](https://github.com/markuswondrak/spec-kit-decision-step) (`decision`) | 0.9.0 | Các quyết định lựa chọn có giới hạn, điểm số và noul có kiểu, với xác suất gốc và chú giải điểm, dùng backend Jev và Laya. |

Decision được duy trì bởi [Markus Wondrak](https://github.com/markuswondrak). Giống các bảng bài gửi cộng đồng khác, metadata tác giả thuộc về catalog; nó không được dùng thay cho việc ghi nhận người duy trì.

Decision khai báo tương thích runtime với Spec Kit `>=0.11.0`; cài [archive phát hành có phiên bản](https://github.com/markuswondrak/spec-kit-decision-step/releases/download/v0.9.0/decision-0.9.0.zip) của nó bằng `--from` yêu cầu Spec Kit `>=1.1.0`. Trường tương thích trong catalog chỉ mang tính khuyến nghị và không được trình cài step hiện tại thực thi.

Package dùng các package PyYAML và `specify_cli` của host. Jev yêu cầu `TYPESAFE_API_KEY` (hoặc `api_key_env` đã cấu hình) và kết nối HTTPS ra ngoài tới endpoint backend đã cấu hình; Laya chạy trong tiến trình yêu cầu package tùy chọn `laya[onnx]`. Xem [tài liệu ghim theo phiên bản](https://github.com/markuswondrak/spec-kit-decision-step/blob/v0.9.0/README.md) để biết cấu hình, đầu ra, hành vi khi lỗi và tác dụng phụ, và [changelog](https://github.com/markuswondrak/spec-kit-decision-step/blob/v0.9.0/CHANGELOG.md) để biết chi tiết bản phát hành. Manifest theo giấy phép MIT ghi nhận `spec-kit-decision-step contributors` là tác giả package.

<a id="package-contract"></a>

## Hợp đồng package

Một package đã cài cung cấp một loại workflow step:

```text
my-step/
├── step.yml
├── __init__.py
└── helpers.py     # optional; every catalog-downloaded extra file is declared
```

Package phải đáp ứng hợp đồng hiện tại của trình cài và trình nạp:

- `step.yml` và `__init__.py` là file thông thường, không phải symlink, ở gốc package. Archive có thể bọc package trong đúng một thư mục cấp cao nhất.
- `step.type_key`, khóa/ID trong catalog và `StepBase.type_key` tương ứng phải giống hệt nhau.
- ID là một thành phần đường dẫn an toàn duy nhất. Trình cài từ chối dấu phân cách, dấu chấm ở đầu, dấu chấm hoặc dấu cách ở cuối, tên dành riêng, ký tự điều khiển và ký tự không hợp lệ trong tên file trên Windows. Quy trình tự động của catalog còn yêu cầu chỉ gồm chữ thường, chữ số và dấu gạch ngang, bắt đầu bằng một chữ cái.
- `__init__.py` định nghĩa một lớp con `StepBase` khớp với type key duy nhất đó. Các lớp bổ sung không khiến package cung cấp thêm loại step được đăng ký. Đây là cam kết của tác giả, không phải kiểm tra code của người duy trì.
- Đường dẫn file bổ sung dùng dấu gạch chéo xuôi, là đường dẫn tương đối và không rỗng, không chứa đoạn rỗng, `.` hay `..`, và không trùng (không phân biệt hoa thường) với `step.yml`, `__init__.py`, file khác hoặc thư mục package.
- Package nằm trong giới hạn hiện tại của trình cài: 512 mục được giữ (tính cả file và thư mục), 32 cấp thư mục và 50 MiB nội dung được giữ. Việc tải bài gửi còn có giới hạn 10 MiB mỗi file.
- `.git`, `__pycache__` và `.DS_Store` bị loại khỏi cài đặt; quy trình tự động cho bài gửi từ chối các biến thể trùng tên không phân biệt hoa thường của các thành phần này.

Xem [Package step tùy chỉnh](../reference/workflows.md#custom-step-packages) để biết đầy đủ hành vi cài đặt, kiểm tra và runtime.

<a id="submission-contract"></a>

## Hợp đồng bài gửi

Biểu mẫu issue tách các trường được code package/catalog hiện tại sử dụng khỏi các trường nguồn gốc và công bố thông tin dùng khi review metadata.

| Dữ liệu bài gửi | Hợp đồng hiện tại |
| --- | --- |
| Step type ID | Khóa catalog, `step.type_key` và `StepBase.type_key` tương ứng |
| Tên, phiên bản, mô tả, tác giả | Metadata `step.yml` và metadata catalog/registry đã cài |
| URL tải về | Archive phát hành có phiên bản dùng để kiểm thử đường cài trực tiếp từ URL được hỗ trợ |
| URL của `step.yml`, `__init__.py` và file bổ sung | URL file HTTPS chính xác được dùng khi cài từ catalog được cho phép cài tường minh; khóa file bổ sung tuân theo các giới hạn đường dẫn tương đối trong package ở trên |
| Mapping SHA-256 theo từng file | `sha256` trong catalog; các khóa phải đúng là các file mà trình cài tải về |
| Tên/số lượng loại được cung cấp | Bất biến của trình nạp: một type key khớp cho mỗi package đã cài |
| Repository, giấy phép, tài liệu, changelog | Nguồn gốc mã nguồn và bằng chứng review metadata; đây không phải trường của `step.yml` |
| Tương thích Spec Kit | Thông tin bắt buộc khi tiếp nhận; được lưu dưới dạng `requires.speckit_version` mang tính khuyến nghị, không được trình cài thực thi |
| Phụ thuộc runtime và công cụ | Thông tin bắt buộc khi tiếp nhận; CLI không phân giải hay cài phụ thuộc cho step tùy chỉnh |

Dùng URL bản phát hành GitHub có phiên bản cho archive, nhất quán với các biểu mẫu bài gửi cộng đồng khác. Phiên bản phải tương thích PEP 440 và khớp với manifest. Tag phát hành của archive phải xác định phiên bản đó, có thể có tiền tố `v` hoặc tiền tố có phạm vi, và không được chứa dấu gạch chéo. Hỗ trợ phiên bản có epoch như `1!2.0` và phiên bản cục bộ như `2.0+cpu`. Ký tự trong tag phải khớp `^[A-Za-z0-9._~+!-]+$`. Mọi URL file trong catalog phải dùng `raw.githubusercontent.com` trong repository được gửi, ghim vào đúng tag phát hành và thư mục package đó. Mapping SHA-256 theo từng file bắt buộc giúp phát hiện byte bị thay đổi ngay cả khi tag được tham chiếu bị dời đi sau này. Không gửi URL nhánh, URL `releases/latest` hay các đích di động khác.

Đường dẫn URL archive phải khớp `^[A-Za-z0-9._~+!/-]+$`. Khóa file tương đối trong package và đường dẫn file trong tag phải khớp `^[A-Za-z0-9._~/-]+$`. Dấu cách, ký tự mã hóa phần trăm (kể cả `%20` trong tên asset), query string, fragment và các đoạn đường dẫn file rỗng/dấu chấm/duyệt ngược không được quy trình tự động cho bài gửi cộng đồng chấp nhận. Hãy phát hành archive và file package với tên thuộc các bảng ký tự này thay vì mã hóa URL các ký tự không được hỗ trợ.

Archive `archive/refs/tags/<tag>` do GitHub tạo chỉ hỗ trợ `.zip` và `.tar.gz`. Archive `.tgz` phải là asset phát hành có tên dạng `releases/download/<tag>/<asset>.tgz`, không phải archive tag được tạo tự động.

Tài liệu có thể là bất kỳ file Markdown nào được ghim theo tag (`.md`, không phân biệt hoa thường) trong repository GitHub được gửi, kể cả `docs/deploy.md`; không bắt buộc tên `README.md`. Nó phải giải thích cách cài, cấu hình, phụ thuộc, đầu ra, hành vi khi lỗi, tác dụng phụ và ví dụ sử dụng trong workflow.

Trình cài archive trực tiếp bằng `--from` hiện không nhận hay xác minh digest của archive. Các trường Download URL và Testing Details được gửi cung cấp bằng chứng về bản phát hành có phiên bản và kiểm thử cài đặt, không phải bảo đảm nội dung bất biến; digest theo từng file bảo vệ đường cài riêng từ catalog. Quy trình tự động tải toàn bộ tập file đã khai báo trong một lượt để áp dụng ngân sách byte tích lũy. Nó không thực thi archive hay nội dung bên trong.

Giấy phép phải là đúng một mã giấy phép SPDX từ danh sách giấy phép chính thức, khớp với giấy phép repository được phát hiện tại tag phát hành đã gửi. Mã không xác định hoặc giấy phép đã biết nhưng không khớp sẽ làm kiểm tra thất bại. Nếu không phát hiện được giấy phép của bản phát hành hoặc kết quả không rõ ràng, việc kiểm tra bị Blocked để chờ người duy trì làm rõ thay vì đoán giấy phép. Kiểm tra metadata này không phải ý kiến pháp lý hay kiểm định code.

<a id="prepare-a-submission"></a>

## Chuẩn bị bài gửi

1. Tạo một repository mã nguồn công khai với package đầy đủ, giấy phép, tài liệu và changelog nếu có.
2. Kiểm thử cấu hình hợp lệ và không hợp lệ, `StepStatus`, đầu ra, lỗi, và mọi hành vi liên quan đến resume, step lồng nhau hoặc thực thi đồng thời.
3. Phát hành một archive có phiên bản (`.zip`, `.tar.gz` hoặc asset phát hành `.tgz` có tên) và kiểm thử nó:

   ```bash
   specify workflow step add my-step \
     --from https://github.com/your-org/my-step/releases/download/v1.0.0/my-step-1.0.0.zip
   ```

4. Công bố URL GitHub raw ghim theo tag cho `step.yml`, `__init__.py` và mọi file bổ sung của package. Tính digest SHA-256 của từng file đã tải.
5. Tạo issue bài gửi chuẩn với chính xác metadata của bản phát hành và bằng chứng kiểm thử.

<a id="automated-metadata-validation"></a>

## Kiểm tra metadata tự động

Workflow do người duy trì kích hoạt kiểm tra metadata đầy đủ, định danh manifest khớp, URL bản phát hành/file được ghim, digest theo từng file, đường dẫn và giới hạn package, tài liệu, và cam kết kiểm thử của tác giả. Nó không review code được gửi hay khẳng định xác minh hành vi thực thi của nó.

Lỗi bài gửi đã được xác nhận tạo ra nhãn `validation-failed` và các chỉnh sửa cần thực hiện. Lỗi môi trường, gồm quyền, công cụ không có sẵn, timeout và lỗi HTTP tạm thời, được đánh dấu Blocked thay vì là lỗi của bài gửi. Chỉ job kết luận có bảo vệ mới có thể áp dụng `validation-passed`, sau khi công bố thành công draft PR catalog.

Phiên bản mới giữ nguyên lịch sử phát hành hiện có trong catalog. Việc sửa metadata cùng phiên bản phải được nêu rõ và không thể thay URL file hay digest; hãy phát hành phiên bản mới khi nội dung package thay đổi. Trình xác minh do repository sở hữu chụp snapshot catalog mong đợi trước khi sửa và kiểm tra toàn bộ catalog được sinh ra trước khi tạo PR, gồm việc chuyển bản phát hành hiện tại trước đó và giữ nguyên lịch sử. Digest bị thiếu của bản phát hành hiện có sẽ chặn việc công bố cho đến khi người duy trì sửa.
