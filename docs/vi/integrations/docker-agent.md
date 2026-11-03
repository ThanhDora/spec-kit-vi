# Docker Agent

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../integrations/docker-agent.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Hãy cài [Docker Agent](https://docs.docker.com/ai/docker-agent/) trước khi thiết lập. Khóa integration là `docker-agent`. Spec Kit nhận diện cả binary `docker-agent` độc lập lẫn plugin Docker CLI (`docker agent`).

<a id="multi-install-safety"></a>

## An toàn khi cài nhiều integration

Integration này không được khai báo là an toàn khi cài nhiều integration vì thư mục skills của nó dùng chung với các integration khác. Xem [quy tắc chung về cài nhiều integration](cli.md#can-i-install-multiple-integrations-in-the-same-project).

<a id="setup"></a>

## Thiết lập

```bash
specify init my-project --integration docker-agent
```

Với dự án Spec Kit đã có, dùng `specify integration install docker-agent`. Xem [quản lý integration](cli.md) để biết cách kích hoạt, nâng cấp và gỡ bỏ.

<a id="installed-skills-and-agent-configuration"></a>

## Skill được cài và cấu hình agent

Skill được cài tại `.agents/skills/speckit-<command>/SKILL.md`, cùng thư mục mà Codex và Zed dùng. Trong file YAML của agent được chọn, bật skill cục bộ bằng `skills: true` và cấp quyền đọc filesystem. Gọi các skill trong khung chat của agent bằng `/speckit-specify`, hoặc `/speckit-bug-assess` khi đã cài extension bug.

Cờ thiết lập tùy chọn `--integration-options="--skills"` chỉ nhắc lại mặc định; integration này luôn dựng skill. Spec Kit không sửa file YAML của agent được chọn và không đưa hook của nó vào hệ thống event gốc của Spec Kit.

<a id="workflow-configuration"></a>

## Cấu hình workflow

Điều phối workflow cần một tham chiếu cấu hình agent. Nên dùng các trường runtime có cấu trúc của command step:

```yaml
- id: specify
  type: command
  command: speckit.specify
  integration: docker-agent
  integration_args:
    - ./agent.yaml
  integration_options:
    agent: root
    safety: balanced
  input:
    args: "Describe the feature"
```

`integration_args` nhận tối đa một tham chiếu không rỗng, không được bắt đầu bằng `-`; Docker Agent kiểm tra file cục bộ hoặc mục registry được tham chiếu. Các `integration_options` được hỗ trợ là `agent` và `safety`; safety phải là `strict`, `balanced`, `restricted` hoặc `autonomous`. Đặt mô hình bằng `model` ở cấp cao nhất của step, không phải `integration_options.model`. Tùy chọn runtime không xác định hoặc sai định dạng sẽ báo lỗi rõ ràng.

Biến môi trường kiểu cũ `SPECKIT_INTEGRATION_DOCKER_AGENT_EXTRA_ARGS=./agent.yaml` vẫn được hỗ trợ khi không có tham chiếu theo từng step. Tham chiếu theo từng step ghi đè toàn bộ giá trị kiểu cũ, kể cả mọi cờ chứa trong đó. Việc điều phối dùng `run --exec`, thêm các cờ `--json` và `--model` khi được yêu cầu, và đặt prompt sau `--` để văn bản prompt không thể trở thành tùy chọn CLI. Xem [cấu hình integration theo từng step](../../reference/workflows.md#per-step-integration-configuration).
