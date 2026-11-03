<div class="landing-hero">

<img class="landing-hero-logo" src="../images/spec-kit-logo.webp" alt="" width="120" height="120">

# GitHub Spec Kit

**Xây dựng theo đặc tả, sửa lỗi hay đánh giá ý tưởng — cùng agent lập trình của bạn.**

Spec Kit trang bị cho agent lập trình những quy trình có cấu trúc, giúp ý định và bằng chứng luôn đi trước phần triển khai. Hãy bắt đầu với Phát triển hướng đặc tả (SDD), sửa lỗi hoặc đánh giá ý tưởng. Chạy một quy trình từng bước, tự động hóa nó, hoặc [tự định hình quy trình của riêng bạn](guides/customization.md) — kể cả những quy trình ngoài phát triển phần mềm.

<a href="installation.md" class="btn btn-primary btn-lg">Cài Spec Kit</a>&nbsp;
<a href="#choose-your-process" class="btn btn-outline-primary btn-lg">Chọn quy trình</a>

</div>

<!-- vi-banner:start -->

> [!NOTE]
> Đây là bản dịch tiếng Việt. Bản gốc: [English](../index.md). Thuật ngữ được thống nhất theo [Bảng thuật ngữ](GLOSSARY.md); khi có khác biệt, bản tiếng Anh là bản chính thức.

<!-- vi-banner:end -->

---

<a id="choose-your-process"></a>

## Chọn quy trình

| Bạn cần gì | Bắt đầu từ đây | Bạn nhận được gì |
| --- | --- | --- |
| Xây dựng một tính năng hoặc ứng dụng | [Phát triển hướng đặc tả](quickstart.md) | Một đặc tả được dẫn dắt xuyên suốt qua lập kế hoạch, triển khai và hội tụ |
| Chẩn đoán và sửa hành vi bị lỗi | [Sửa lỗi](guides/bugfix.md) | Một nguyên nhân đã được đánh giá, một bản sửa có giới hạn và kết quả xác minh được ghi lại |
| Quyết định một ý tưởng có đáng đầu tư hay không | [Đánh giá ý tưởng](guides/assessment.md) | Một quyết định go, clarify hoặc stop có bằng chứng hỗ trợ |

Đây là các điểm bắt đầu độc lập, không phải các giai đoạn bắt buộc. SDD có sẵn trong phần lõi.
Sửa lỗi và đánh giá ý tưởng là các extension đi kèm, chỉ chạy khi bạn chủ động bật. Đánh giá ý tưởng có thể
dùng độc lập; quyết định tiếp tục không tự động khởi động phần triển khai.

Xem [cách dự án Spec Kit vận hành SDLC có agent](guides/agentic-sdlc.md)
và những chỗ dự án dùng chính Spec Kit.

Thêm Spec Kit vào một codebase có sẵn? Hãy bắt đầu với
[hướng dẫn cho dự án có sẵn](guides/existing-projects.md).

---

<div class="pillar-grid">

<div class="pillar-card">

<a id="spec-driven-by-default"></a>

### Mặc định hướng đặc tả

Quy trình SDD lõi dùng được ngay: **Specify → Plan → Tasks → Implement → Converge**.

Xác định thứ cần xây dựng trước khi bắt tay xây dựng. Template phong phú, checklist chất lượng và phân tích chéo giữa các artifact đều có sẵn. Mỗi giai đoạn tạo ra một artifact Markdown làm đầu vào cho giai đoạn sau — cung cấp cho agent lập trình AI ngữ cảnh có cấu trúc thay vì các prompt tùy hứng.

<a href="quickstart.md" class="pillar-link">Đi qua quy trình →</a>

</div>

<div class="pillar-card">

<a id="use-any-coding-agent"></a>

### Dùng bất kỳ agent lập trình nào

<span class="pillar-stat">38 integration</span> — Copilot, Gemini, Codex, Kilo Code, Zed, Claude, Forge, Kiro và nhiều agent khác. Tự do chuyển đổi giữa các agent chỉ bằng một lệnh. Không bị khóa chặt.

Chạy `specify init` với agent bạn chọn, Spec Kit sẽ tự động thiết lập đúng file lệnh và cấu trúc thư mục. Nếu agent của bạn không có trong danh sách, integration `generic` là lối thoát dùng được cho mọi công cụ.

<a href="integrations/index.md" class="pillar-link">Xem mọi integration →</a>

</div>

<div class="pillar-card">

<a id="make-it-your-own"></a>

### Biến nó thành của riêng bạn

<span class="pillar-stat">157 extension cộng đồng</span> (hơn 90 tác giả), <span class="pillar-stat">33 preset</span> và con số vẫn đang tăng. Tinh chỉnh quy trình lõi bằng preset, mở rộng bằng extension, điều phối bằng workflow, và đóng gói tất cả thành bundle để chia sẻ — hoặc thay thế hoàn toàn quy trình. Bản thân quy trình nằm trong các thành phần này, nên bạn không bao giờ bị khóa vào SDD, hay thậm chí vào phần mềm.

Kể cả những quy trình hoàn toàn khác:

- **AIDE** — vòng đời kỹ thuật dựa trên AI gồm 7 bước
- **Canon** — workflow dựa trên baseline (spec-first, code-first, spec-drift)
- **Product Forge** — SDD theo định hướng quản lý sản phẩm
- **FX→.NET** — chuyển đổi .NET Framework trọn vẹn qua 7 giai đoạn
- **MAQA** — điều phối nhiều agent với các cổng kiểm soát đảm bảo chất lượng
- **Fiction Book Writing** — viết tiểu thuyết và văn xuôi dài, từ story bible đến bản thảo nộp đi

<a href="reference/presets.md" class="pillar-link">Preset →</a>&nbsp;&nbsp;
<a href="reference/extensions.md" class="pillar-link">Extension →</a>&nbsp;&nbsp;
<a href="reference/workflows.md" class="pillar-link">Workflow →</a>&nbsp;&nbsp;
<a href="reference/bundles.md" class="pillar-link">Bundle →</a>

</div>

<div class="pillar-card">

<a id="integrate-into-your-organization"></a>

### Tích hợp vào tổ chức của bạn

Hoạt động offline, sau tường lửa và trên **Windows, macOS và Linux**. Tự host catalog để tuyển chọn những integration, extension, preset, workflow và bundle mà tổ chức của bạn tìm thấy và khuyến nghị.

Các extension cộng đồng như CI Guard và Architecture Guard bổ sung cổng kiểm soát tuân thủ và quản trị phù hợp với cách nhóm của bạn đang làm việc.

<a href="install/air-gapped.md" class="pillar-link">Doanh nghiệp / Air-gapped →</a>&nbsp;&nbsp;
<a href="reference/overview.md" class="pillar-link">Tài liệu tham khảo →</a>

</div>

</div>

---

<div class="community-section">

<a id="built-by-the-community"></a>

## Được xây dựng bởi cộng đồng

**Hơn 270 người đóng góp** vận hành hệ sinh thái Spec Kit — từ các integration lõi đến những quy trình hoàn toàn mới. Bất kỳ ai cũng có thể tạo và phát hành extension, preset hoặc workflow.

<div class="stats-grid">
  <div class="stat-item">
    <span class="stat-number">130K+</span>
    <span class="stat-label">Sao trên GitHub</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">270+</span>
    <span class="stat-label">Người đóng góp</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">38</span>
    <span class="stat-label">Integration</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">157</span>
    <span class="stat-label">Extension</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">33</span>
    <span class="stat-label">Preset</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">7</span>
    <span class="stat-label">Dự án bạn bè</span>
  </div>
</div>

<a href="../community/presets.md">Preset</a> · <a href="../community/walkthroughs.md">Walkthrough</a> · <a href="../community/friends.md">Dự án bạn bè</a>

</div>

---

<a id="explore-the-docs"></a>

## Khám phá tài liệu

<div class="nav-cards">
  <a href="guides/agentic-sdlc.md" class="nav-card">
    <strong>SDLC có agent của Spec Kit</strong>
    <span>Cách dự án này đánh giá, xây dựng, kiểm thử, phát hành và sửa chữa các thay đổi</span>
  </a>
  <a href="quickstart.md" class="nav-card">
    <strong>Phát triển hướng đặc tả</strong>
    <span>Xác định, lập kế hoạch, triển khai và hội tụ một tính năng</span>
  </a>
  <a href="guides/bugfix.md" class="nav-card">
    <strong>Sửa lỗi</strong>
    <span>Đánh giá nguyên nhân, áp dụng bản sửa có giới hạn và xác minh kết quả</span>
  </a>
  <a href="guides/assessment.md" class="nav-card">
    <strong>Đánh giá ý tưởng</strong>
    <span>Nghiên cứu một ý tưởng và quyết định nó có đáng đầu tư hay không</span>
  </a>
  <a href="guides/customization.md" class="nav-card">
    <strong>Tùy biến Spec Kit</strong>
    <span>Điều chỉnh quy trình, thêm khả năng hoặc đóng gói một thiết lập theo vai trò</span>
  </a>
  <a href="guides/existing-projects.md" class="nav-card">
    <strong>Dự án có sẵn</strong>
    <span>Áp dụng Spec Kit an toàn vào một codebase đã có</span>
  </a>
  <a href="upgrade.md" class="nav-card">
    <strong>Nâng cấp</strong>
    <span>Giữ dự án Spec Kit hiện có luôn cập nhật qua các bản phát hành</span>
  </a>
  <a href="reference/overview.md" class="nav-card">
    <strong>Tài liệu tham khảo</strong>
    <span>Lệnh lõi, catalog, integration, extension, preset và workflow</span>
  </a>
  <a href="../community/overview.md" class="nav-card">
    <strong>Cộng đồng</strong>
    <span>Extension, preset, walkthrough và các dự án bạn bè</span>
  </a>
  <a href="local-development.md" class="nav-card">
    <strong>Phát triển</strong>
    <span>Đóng góp cho Spec Kit</span>
  </a>
  <a href="concepts/sdd.md" class="nav-card">
    <strong>SDD là gì?</strong>
    <span>Triết lý đằng sau Phát triển hướng đặc tả</span>
  </a>
  <a href="history.md" class="nav-card">
    <strong>Lịch sử</strong>
    <span>Spec Kit đã phát triển từ nền tảng SDD thành một nền tảng quy trình mở rộng được như thế nào</span>
  </a>
</div>

---

<div class="footer-cta">

```bash
uv tool install specify-cli
specify init my-project --integration copilot
```

Sẵn sàng bắt đầu? [Chọn quy trình](#choose-your-process).

</div>

<p class="text-end small text-body-secondary">Cập nhật lần cuối: 28/09/2026</p>
