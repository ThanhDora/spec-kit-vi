<a id="community-walkthroughs"></a>

# Hướng dẫn từng bước của cộng đồng

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../../community/walkthroughs.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](../GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

> [!NOTE]
> Các hướng dẫn từng bước của cộng đồng được tạo và duy trì độc lập bởi tác giả của chúng. Chúng **không được GitHub review, bảo chứng hay hỗ trợ**. Hãy review nội dung trước khi làm theo và tự cân nhắc khi sử dụng.

Xem Phát triển hướng đặc tả trong thực tế qua nhiều kịch bản khác nhau với các hướng dẫn từng bước do cộng đồng đóng góp. Chúng là ví dụ chỉ để đọc hữu ích về các luồng đã hoàn thành, nhưng không phải đầu ra chuẩn chính thức cho đặc tả, kế hoạch hay task được sinh ra.

- **[Công cụ CLI .NET greenfield](https://github.com/mnriem/spec-kit-dotnet-cli-demo)** — Xây dựng Timezone Utility dưới dạng công cụ CLI .NET một file nhị phân từ thư mục trống, bao quát toàn bộ workflow spec-kit: constitution, specify, plan, tasks và implement nhiều lượt bằng agent GitHub Copilot.

- **[Nền tảng Spring Boot + React greenfield](https://github.com/mnriem/spec-kit-spring-react-demo)** — Xây dựng từ đầu một nền tảng phân tích hiệu năng LLM (REST API, biểu đồ, theo dõi vòng lặp) bằng Spring Boot, React nhúng, PostgreSQL và Docker Compose, có cả bước clarify và một lượt phân tích tính nhất quán giữa các artifact.

- **[Mở rộng CMS ASP.NET brownfield](https://github.com/mnriem/spec-kit-aspnet-brownfield-demo)** — Mở rộng một CMS .NET mã nguồn mở có sẵn (CarrotCakeCMS-Core, ~307.000 dòng C#, Razor, SQL, JavaScript và file cấu hình) với hai feature mới — hạ tầng Docker Compose đa nền tảng và REST API headless xác thực bằng token — minh họa cách spec-kit áp dụng vào codebase hiện có khi chưa có đặc tả hay constitution.

- **[Mở rộng runtime Java brownfield](https://github.com/mnriem/spec-kit-java-brownfield-demo)** — Mở rộng một runtime Jakarta EE mã nguồn mở có sẵn (Piranha, ~420.000 dòng Java, XML, JSP, HTML và file cấu hình trên 180 module Maven) với Server Admin Console có bảo vệ bằng mật khẩu, minh họa spec-kit trên một dự án Java nhiều module lớn chưa có đặc tả hay constitution.

- **[Demo dashboard Go / React brownfield](https://github.com/mnriem/spec-kit-go-brownfield-demo)** — Minh họa spec-kit được điều khiển hoàn toàn từ **terminal bằng GitHub Copilot CLI**. Mở rộng hệ thống hỗ trợ mặt đất Hermes mã nguồn mở của NASA (Go) với một dashboard telemetry web nhẹ dựa trên React, cho thấy toàn bộ workflow constitution → specify → plan → tasks → implement hoạt động từ terminal.

- **[Spring Boot MVC greenfield với preset tùy chỉnh](https://github.com/mnriem/spec-kit-pirate-speak-preset-demo)** — Xây dựng từ đầu một ứng dụng Spring Boot MVC bằng preset tùy chỉnh giọng cướp biển, minh họa cách preset có thể định hình lại toàn bộ trải nghiệm spec-kit: đặc tả thành "Voyage Manifests", kế hoạch thành "Battle Plans" và task thành "Crew Assignments" — tất cả được sinh ra hoàn toàn bằng giọng cướp biển mà không thay đổi công cụ nào.

- **[Spring Boot + React greenfield với extension tùy chỉnh](https://github.com/mnriem/spec-kit-aide-extension-demo)** — Hướng dẫn qua **extension AIDE**, một extension cộng đồng bổ sung cho spec-kit một workflow hướng đặc tả thay thế với đặc tả cấp cao (tầm nhìn) và đặc tả cấp thấp (work item) được tổ chức trong vòng đời lặp 7 bước: vision → roadmap → progress tracking → work queue → work items → execution → feedback loops. Dùng một nền tảng giao dịch gia đình (Spring Boot 4, React 19, PostgreSQL, Docker Compose) làm kịch bản để minh họa cách cơ chế extension cho phép cắm vào một phong cách phát triển hướng đặc tả khác mà không thay đổi công cụ lõi nào — tận dụng đúng nghĩa chữ "Kit" trong Spec Kit.
