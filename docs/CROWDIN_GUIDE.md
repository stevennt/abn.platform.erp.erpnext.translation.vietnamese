# Hướng dẫn đóng góp bản dịch qua Crowdin (kênh chính thức Frappe)

Frappe **không nhận PR** sửa file `vi.po` trên GitHub. Họ chỉ sync từ Crowdin.
Nếu muốn bản dịch vào phiên bản chính thức, làm theo các bước sau.

## 1. Đăng ký Crowdin

- Truy cập: https://crowdin.com
- Đăng ký miễn phí (email / Google)

## 2. Tham gia 3 Frappe projects

Mỗi app là một project riêng:

- **Frappe Framework**: https://crowdin.com/project/frappe
- **ERPNext**: https://crowdin.com/project/erpnext
- **Frappe HRMS**: https://crowdin.com/project/erpnext-hrms

Với mỗi project:
1. Click "Join"
2. Chọn ngôn ngữ **Vietnamese (vi)**
3. Mô tả kinh nghiệm → chờ maintainer duyệt (thường < 24h)

## 3. Upload translations (sau khi được duyệt)

Có 2 cách:

### A. Upload toàn bộ file `.po`
- Vào project → tab **Files** → chọn `main.pot` (Vietnamese)
- **Upload Translation** → chọn file `vi.po` từ `lkf-docs/translations/vi/`
- Chọn option: "Import translations from file" + "Mark as approved: NO"
  (để reviewer xác nhận từng string)

### B. Dịch từng string qua UI
- Vào project → Translation Editor
- Duyệt từng string chưa dịch → nhập translation
- Phù hợp khi chỉ bổ sung ít string

## 4. Review / Approve

- Sau khi upload, các translation cần 1-2 reviewers approve
- Reviewer thường là translation coordinator của Frappe
- Có thể mất vài ngày đến vài tuần

## 5. Release

- Khi có đủ approved translations, Frappe sync về repo `develop`
- Sau đó phát hành trong bản ERPNext tiếp theo (v16.x hoặc v17)
- Người dùng ERPNext trên thế giới sẽ nhận được bản dịch VN

## Lưu ý quan trọng

**Chất lượng bản dịch auto (gemma-4)** có thể không hoàn hảo. Khi upload, maintainer có thể:
- Reject một số string → cần chỉnh thủ công
- Comment yêu cầu sửa cụm từ
- Yêu cầu bổ sung context

**Tốt nhất**: review 200-500 strings quan trọng nhất (Customer, Supplier, Invoice,
Payment, Sales Order, Purchase Order…) trước khi upload, để đảm bảo các term chính
được dịch đúng.

## Timeline thực tế

- Ngày 1: Apply làm translator 3 projects
- Ngày 2-3: Được duyệt
- Ngày 4-7: Upload + review từng batch
- Tuần 2-4: Chờ reviewer approve
- Tháng 1-2: Vào release chính thức

## Alternative: tự maintain

Nếu không muốn chờ quy trình Crowdin, repo riêng tại
`github.com/nguyenhuuduong/erpnext-vi-translations` là đủ để community VN dùng.
