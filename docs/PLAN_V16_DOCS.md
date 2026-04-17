# Kế hoạch viết lại tài liệu ERPNext v16 tiếng Việt

## Bối cảnh

Tài liệu hiện tại dịch từ v13 (2021). ERPNext v16 (stable 06/12/2025) có **50+ tính năng mới**, thay đổi UI hoàn toàn, và nhiều breaking changes. Cần viết lại — không chỉ cập nhật.

---

## Tổng hợp thay đổi chính v13 → v16

### 1. Giao diện người dùng (ảnh hưởng TOÀN BỘ tài liệu)

| Thay đổi | Tác động |
|---|---|
| Workspace redesign hoàn toàn | Tất cả screenshot cũ đều sai, navigation thay đổi |
| Command Palette thay thế Awesome Bar cũ | Hướng dẫn tìm kiếm phải viết lại |
| List view: cột kéo thả, cuộn ngang, unlimited fields | Hướng dẫn xem danh sách thay đổi |
| Child tables: cuộn ngang, sticky columns | Hướng dẫn nhập liệu trong form thay đổi |
| Dark mode | Cần lưu ý trong screenshot |
| Chrome PDF thay wkhtmltopdf | Hướng dẫn in ấn thay đổi |
| Role-based field masking | Mô tả bảo mật mới |

**→ Hành động**: Chụp lại TOÀN BỘ screenshot trên instance LKF (đã Việt hóa)

### 2. Module Kế toán (Accounts) — thay đổi LỚN nhất

| Tính năng mới | Mô tả | Trang cần viết |
|---|---|---|
| Financial Report Templates | Mẫu báo cáo tài chính tùy chỉnh, hỗ trợ công thức | **Mới hoàn toàn** |
| Consolidated Trial Balance | Bảng cân đối thử hợp nhất đa công ty | **Mới hoàn toàn** |
| COGS vs Service Expenses tách riêng | Phân biệt giá vốn hàng bán và chi phí dịch vụ | Cập nhật P&L |
| Reporting Currency per Company | Tiền tệ báo cáo riêng cho từng công ty | Cập nhật Company setup |
| Periodic Accounting (Stock In/Out) | Ghi nhận tồn kho theo kỳ qua Journal Entry | **Mới hoàn toàn** |
| Automatic Closing Stock Posting | Tự động đóng sổ kho cuối kỳ | **Mới hoàn toàn** |
| Enhanced Budgeting | Ngân sách chi tiết theo cost center/project/dept | Cập nhật budgeting |
| Purchase Expense Booking | Ghi nhận chi phí mua hàng trực tiếp | **Mới hoàn toàn** |
| Dr/Cr column in Customer Ledger | Hiển thị rõ chiều nợ/có | Cập nhật reports |
| Accounting Dimension multi-select filters | Lọc đa chiều kế toán | Cập nhật reports |
| Custom print layouts for GL & AR | Mẫu in tùy chỉnh cho sổ cái & công nợ | Cập nhật Statement of Accounts |
| Ledger Preview trước Submit | Xem trước bút toán trước khi xác nhận | Cập nhật tất cả form kế toán |
| Payment Request failure banner | Cảnh báo lỗi yêu cầu thanh toán | Cập nhật Payment Request |

**Breaking changes:**
- `item_wise_tax_detail` JSON → child table `Item Wise Tax Detail`
- Tax Withholding refactored → `Tax Withholding Entry` child table
- `make_bank_account` API removed → dùng `frappe.new_doc`

### 3. Module Kho (Stock) — thay đổi TRUNG BÌNH

| Tính năng mới | Mô tả | Trang cần viết |
|---|---|---|
| Stock Reservation System | Giữ tồn kho cho đơn bán hàng cụ thể | **Mới hoàn toàn** |
| Serial & Batch Traceability Report | Truy xuất nguồn gốc lô hàng/serial | **Mới hoàn toàn** |
| Landed Cost cho Stock Entry & Subcontracting | Chi phí chuyển đến cho phiếu kho | Cập nhật Landed Cost |
| Item-Level Stock Accounting | Tài khoản kho theo mặt hàng/nhóm | Cập nhật Item |
| Stock valuation method per Company | Phương pháp tính giá theo công ty | Cập nhật Stock Settings |
| Ledger Preview | Xem trước sổ kho trước submit | Cập nhật Stock Entry |
| Quick Stock Balance cải tiến | Kiểm tra nhanh tồn kho | Cập nhật |

### 4. Module Mua hàng (Buying) — thay đổi NHỎ

| Tính năng mới | Mô tả | Trang cần viết |
|---|---|---|
| Non-transporter supplier filtering | Lọc NCC không phải vận tải | Cập nhật PO/PI |
| Supplier/Customer reference numbers | Bảng số tham chiếu NCC/KH | Cập nhật Supplier |
| Purchase Expense Booking | Ghi nhận chi phí mua hàng | Cập nhật Purchase Invoice |
| Email append-to cho PI | Tạo PI nháp từ email | Cập nhật Purchase Invoice |

### 5. Module Bán hàng (Selling) — thay đổi NHỎ

| Tính năng mới | Mô tả | Trang cần viết |
|---|---|---|
| Cutoff date cho Delivery Note | Chọn ngày cắt khi tạo DN từ SO | Cập nhật Sales Order |
| SO/Quotation buttons trên Customer form | Nút tạo nhanh trên form KH | Cập nhật Customer |
| Unbilled timesheets option | Tùy chọn timesheet chưa lập hóa đơn | Cập nhật Sales Invoice |

### 6. Module Sản xuất (Manufacturing) — thay đổi LỚN

| Tính năng mới | Mô tả | Trang cần viết |
|---|---|---|
| MRP (Material Requirements Planning) | Hoạch định nhu cầu vật tư | **Mới hoàn toàn** |
| Inward Subcontracting | Gia công nhận hàng (nhận NVL từ KH) | **Mới hoàn toàn** |
| Job Card: material consumption & FG | Ghi nhận NVL tiêu hao và TP tại Job Card | Cập nhật Job Card |
| Stock Reservation cho Work Order | Giữ NVL cho lệnh sản xuất | **Mới hoàn toàn** |
| Phantom BOM | BOM ảo cho lắp ráp đa cấp | **Mới hoàn toàn** |
| Landed Cost cho Subcontracting Receipt | Chi phí chuyển đến cho phiếu gia công | Cập nhật |
| Manufacturing warehouse per Company | Kho SX cấu hình theo công ty | Cập nhật Company |

### 7. POS (Điểm bán hàng) — thay đổi TRUNG BÌNH

| Tính năng mới | Mô tả |
|---|---|
| List-style item selector | Hiển thị mặt hàng dạng danh sách |
| Allow Partial Payment | Cho phép thanh toán một phần |
| Use Sales Invoice in POS | Dùng SI thay POS Invoice |
| Form reorganized (tabs) | Form chia tab mới |

### 8. HRMS — thay đổi TRUNG BÌNH

| Tính năng mới | Mô tả |
|---|---|
| Automated Overtime | Tính OT tự động theo quy tắc |
| Salary Correction (Arrears/LOP) | Điều chỉnh lương truy thu/nghỉ không lương |
| Half-day Holiday | Ngày lễ nửa ngày |
| Multi-currency Expense Claims | Khai chi phí đa tiền tệ |

### 9. Hiệu năng (Frappe Caffeine)

- Page load nhanh gấp 2x
- Report generation nhanh hơn đáng kể
- Redis caching thông minh với auto-invalidation
- Database queries tối ưu, giảm 40% server load
- Stock Ageing report giảm 50% bộ nhớ

---

## Kế hoạch thực hiện

### Phase 1: Chuẩn bị (1 tuần)
- [ ] Chụp screenshot tất cả trang chính trên instance LKF (đã Việt hóa, dark mode OFF)
- [ ] Tạo bảng thuật ngữ v16 (cập nhật từ .po files)
- [ ] Setup cấu trúc thư mục docs/vi-v16/

### Phase 2: Viết lại module ưu tiên cao (2 tuần)
- [ ] **Introduction** (8 trang) — cập nhật cho v16, thêm tính năng mới
- [ ] **Accounts** (viết lại ~50 trang + 10 trang mới)
  - Financial Report Templates (mới)
  - Consolidated Trial Balance (mới)
  - Automatic Closing Stock Posting (mới)
  - Purchase Expense Booking (mới)
  - Periodic Accounting (mới)
  - Cập nhật: Chart of Accounts, Journal Entry, Payment Entry, Sales/Purchase Invoice, POS
- [ ] **Stock** (viết lại ~30 trang + 5 trang mới)
  - Stock Reservation (mới)
  - Serial & Batch Traceability (mới)
  - Cập nhật: Item, Stock Entry, Landed Cost, Stock Settings
- [ ] **Buying** (cập nhật ~14 trang)
- [ ] **Selling** (cập nhật ~28 trang)

### Phase 3: Module bổ sung (2 tuần)
- [ ] **Manufacturing** (viết mới ~15 trang)
  - MRP, Inward Subcontracting, Phantom BOM, Stock Reservation cho WO
- [ ] **POS** (viết lại ~5 trang)
- [ ] **HRMS** (cập nhật ~10 trang)
- [ ] **Assets** (cập nhật ~5 trang)

### Phase 4: Review & hoàn thiện (1 tuần)
- [ ] Review thuật ngữ nhất quán
- [ ] Kiểm tra tất cả link nội bộ
- [ ] Kiểm tra screenshot đúng version
- [ ] Deploy lên GitHub Pages hoặc docs site

---

## Ước tính khối lượng

| Hạng mục | Số trang |
|---|---|
| Viết lại từ v13 | ~130 trang |
| Viết mới hoàn toàn | ~30 trang |
| Cập nhật nhỏ | ~50 trang |
| **Tổng** | **~210 trang** |

## Công cụ

- Dịch/viết: gemma-4-26B (local vLLM) + review thủ công
- Screenshot: Puppeteer/Playwright trên instance LKF
- Glossary: đồng bộ từ erpnext.vi.po + frappe.vi.po
- Hosting: GitHub repo `erpnext-vietnam-localization/docs/vi-v16/`

---

## Lưu ý quan trọng cho LKF

Vì LKF là doanh nghiệp cold-chain food trading, ưu tiên đặc biệt:
1. **Serial & Batch Traceability** — truy xuất lô hàng thực phẩm
2. **Stock Reservation** — giữ hàng cho đơn đặt trước
3. **Landed Cost** — chi phí vận chuyển cold-chain
4. **Quality Inspection** — kiểm tra chất lượng thực phẩm
5. **Multi-currency** — giao dịch nhập/xuất khẩu
