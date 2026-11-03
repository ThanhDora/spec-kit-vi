<a id="using-spec-kit-in-a-monorepo"></a>

# Dùng Spec Kit trong monorepo

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../guides/monorepo.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

Một dự án Spec Kit **gắn với thư mục**: dự án là thư mục nào
chứa `.specify/`. Một monorepo có thể chứa nhiều dự án Spec Kit độc lập
dưới cùng một thư mục gốc của repository, mỗi dự án có `.specify/`, `specs/`, hiến chương
và cách đánh số tính năng riêng.

Việc xác định thư mục gốc vốn đã ưu tiên `.specify/` **gần nhất** thay vì thư mục
cấp cao nhất của Git, nên các lệnh chạy từ bên trong một dự án thành viên sẽ xác định là dự án đó,
chứ không phải thư mục gốc của repo.

Cách tổ chức repository là chuyện riêng, tách biệt với thiết kế giao diện. Khi các dự án tương tác với nhau,
hãy dùng [Phát triển hướng contract](contract-driven-development.md) để xác định
thỏa thuận giữa chúng, mỗi contract có đúng một bên sở hữu chính thức. Các dự án
trong cùng repository có thể tham chiếu trực tiếp contract đó; các dự án ở
repository khác nhau có thể dùng một artifact có phiên bản hoặc một bản sao được đồng bộ.

<a id="layout"></a>

## Bố cục

```text
my-monorepo/
├── .git/                     # one Git repository at the root
├── apps/
│   ├── web/
│   │   └── .specify/         # Spec Kit project "web"
│   │       └── memory/constitution.md
│   └── api/
│       └── .specify/         # Spec Kit project "api"
│           └── memory/constitution.md
└── packages/
    └── ui/
        └── .specify/         # Spec Kit project "ui"
```

Khởi tạo từng dự án thành viên một cách độc lập:

```bash
specify init apps/web --integration claude
specify init apps/api --integration claude
```

Mỗi dự án có thư mục `specs/` riêng và đánh số tính năng
độc lập (`apps/web/specs/001-…`, `apps/api/specs/001-…`).

<a id="working-inside-a-member-project"></a>

## Làm việc bên trong một dự án thành viên

Quy trình mặc định không thay đổi: chuyển vào thư mục dự án rồi chạy các
slash command. Việc xác định thư mục gốc sẽ tìm `.specify/` gần nhất.

```bash
cd apps/web
# then run /speckit.specify, /speckit.plan, … in your agent
```

<a id="targeting-a-member-project-from-the-repo-root"></a>

## Nhắm tới một dự án thành viên từ thư mục gốc của repo

Với các lần chạy không tương tác hoặc trong CI mà bạn không muốn `cd`, hãy đặt
**`SPECIFY_INIT_DIR`** thành thư mục gốc của dự án thành viên (thư mục *chứa*
`.specify/`). Đường dẫn tương đối được tính từ thư mục hiện tại.

```bash
# operate on apps/web from the monorepo root (no cd required)
export SPECIFY_INIT_DIR=apps/web
```

Đường dẫn phải tồn tại và chứa `.specify/`. Nếu không, lệnh sẽ
**báo lỗi và không quay về** thư mục hiện tại hay thư mục cấp cao nhất của Git.
Điều này là có chủ ý: gõ nhầm sẽ không bao giờ ghi đặc tả vào sai dự án. Đường dẫn
không tồn tại được báo đúng như bạn đã gõ; đường dẫn tồn tại nhưng không phải
dự án Spec Kit được báo bằng đường dẫn tuyệt đối sau khi phân giải:

```text
# SPECIFY_INIT_DIR=apps/wbe  (typo: no such directory)
ERROR: SPECIFY_INIT_DIR does not point to an existing directory: apps/wbe

# SPECIFY_INIT_DIR=apps  (exists, but has no .specify/ of its own)
ERROR: SPECIFY_INIT_DIR is not a Spec Kit project (no .specify/ directory): /home/you/my-monorepo/apps
```

`SPECIFY_INIT_DIR` chọn **dự án**; `SPECIFY_FEATURE_DIRECTORY` chọn
**tính năng**. Đường dẫn tính năng tương đối được nối vào thư mục gốc của dự án đó
mà không kiểm tra có nằm bên trong hay không, nên giá trị như `../shared-feature` vẫn
trỏ ra ngoài; đường dẫn tuyệt đối được dùng nguyên trạng và cũng có thể trỏ
ra ngoài thư mục gốc của dự án. Dù thế nào, thư mục tính năng được chọn cũng không
bắt buộc phải nằm bên trong — thư mục gốc của dự án xác định dự án Spec Kit
và ngữ cảnh lệnh/cấu hình của nó, chứ không phải ranh giới chứa các tài liệu
tính năng. Hai biến này kết hợp được với nhau: đặt cả hai để chọn dự án và tính năng
mà không cần tương tác. Xem
[tài liệu tham khảo `SPECIFY_INIT_DIR`](../../reference/core.md#environment-variables) để biết
toàn bộ contract và mô hình hai trục.

Các lệnh con theo phạm vi dự án của CLI `specify` cũng tôn trọng biến này, nên chúng cũng
nhắm được tới một dự án thành viên từ thư mục gốc mà không cần `cd`:

```bash
export SPECIFY_INIT_DIR=apps/web
specify workflow list          # lists apps/web's workflows
specify integration status     # reports apps/web's integration
```

Quy tắc kiểm tra cũng giống vậy: đường dẫn phải tồn tại và chứa `.specify/`,
không quay về thư mục hiện tại.

<a id="how-specify_init_dir-reaches-your-agent"></a>

## `SPECIFY_INIT_DIR` đến được agent của bạn như thế nào

`SPECIFY_INIT_DIR` được đọc bởi các script shell mà slash command gọi
(`get_repo_root` trong Bash, `Get-RepoRoot` trong PowerShell). Biến chỉ có tác dụng
khi nó có mặt trong môi trường của shell chạy các script đó.

- **Chạy bằng script / CI:** export biến trong chính shell điều khiển các lệnh;
  ở đó nó hoạt động ổn định.
- **Agent tương tác:** việc biến đã export có đến được công cụ shell mà
  agent dùng hay không tùy thuộc vào từng agent. Hãy export `SPECIFY_INIT_DIR` *trước* khi mở
  agent, và kiểm tra một lần (ví dụ chạy `/speckit.specify` và xác nhận tính năng mới
  nằm trong `specs/` của đúng dự án mong muốn).

<a id="git-in-a-monorepo"></a>

## Git trong monorepo

> [!NOTE]
> File dự án Spec Kit gắn với **thư mục gốc dự án đã được xác định**, nhưng các thao tác Git
> vẫn chạy trong Git work tree bao ngoài. Trong monorepo chỉ có
> một Git repository ở thư mục gốc và các dự án nằm trong thư mục con, việc tạo feature
> branch sẽ tạo hoặc chuyển branch trong repository gốc dùng chung.
> Thư mục đặc tả vẫn nằm trong dự án thành viên được chọn, còn không gian tên
> branch Git thì dùng chung cho cả monorepo. Hãy quản lý branch và commit
> ở thư mục gốc của repository, hoặc khởi tạo Git riêng cho từng dự án thành viên nếu bạn muốn
> không gian tên branch tách biệt cho từng dự án.

<a id="constitutions"></a>

## Hiến chương

Mỗi dự án thành viên có `.specify/memory/constitution.md` riêng và
`/speckit.constitution` sửa file của dự án cục bộ. Spec Kit không cung cấp
cơ chế kế thừa/hiến chương gốc có sẵn; nếu bạn muốn một hiến chương tham chiếu tới
các quy tắc dùng chung ở nơi khác trong monorepo, bạn cần tự duy trì phần liên kết đó.
Nếu không, hãy sao chép hoặc đồng bộ các quy tắc kỹ thuật dùng chung cho từng dự án.
