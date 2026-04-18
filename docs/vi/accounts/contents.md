<!-- add-breadcrumbs -->
# Kế toán

Cho dù bạn có kế toán viên trong đội ngũ nội bộ HAY bạn tự thực hiện HOẶC bạn chọn thuê ngoài, quy trình kế toán tài chính luôn là trung tâm của bất kỳ hệ thống quản trị doanh nghiệp nào (còn gọi là hệ thống ERP).

Trong ERPNext, các nghiệp vụ kế toán bao gồm 3 loại giao dịch chính:

  * **Hóa đơn bán hàng**: Các hóa đơn mà bạn lập cho Khách hàng đối với các sản phẩm hoặc dịch vụ bạn cung cấp.
  * **Hóa đơn mua hàng**: Các hóa đơn mà Nhà cung cấp gửi cho bạn đối với sản phẩm hoặc dịch vụ của họ.
  * **Bút toán**: Dành cho các bút toán kế toán, như thanh toán, ghi có và các loại khác.

Bạn có thể xem [video này](https://www.youtube.com/watch?v=5wjollWN0OA) để nắm bắt tổng quan về phân hệ kế toán trong ERPNext.

## 1. Các chủ đề

### 1.1 Thiết lập và Khai trương
1. [Giới thiệu](accounting-entries.md)
1. [Cài đặt Kế toán](accounts-settings.md)
1. [Công ty](../setting-up/company-setup.md)
1. [Hệ thống tài khoản](chart-of-accounts.md)
1. [Số dư đầu kỳ trong Tài khoản](opening-balance.md)
1. [Trung tâm chi phí](cost-center.md)
1. [Trung tâm chi phí phân bổ](distributed-cost-center.md)
1. [Năm tài chính](fiscal-year.md)
1. [Kỳ kế toán](accounting-period.md)
1. [Sổ tài chính](finance-book.md)
1. [Chiều kích kế toán](accounting-dimensions.md)
1. [Bộ lọc chiều kích kế toán](accounting-dimension-filter.md)
1. [Ngân hàng](bank.md)
1. [Tài khoản ngân hàng](bank-account.md)
<!-- (in development) 1. [Giao dịch ngân hàng](bank-transaction.md) -->

### 1.2 Sổ nhật ký và Thanh toán
1. [Bút toán](journal-entry.md)
1. [Mẫu bút toán](journal-entry-template.md)
1. [Bút toán thanh toán](payment-entry.md)
1. [Nhắc nợ](dunning.md)
1. [Yêu cầu thanh toán](payment-request.md)
1. [Phương thức thanh toán](mode-of-payment.md)
1. [Điều khoản thanh toán](payment-terms.md)
1. [Mẫu điều khoản thanh toán](payment-terms-template.md)
1. [Bút toán thanh toán trước](advance-payment-entry.md)
1. [Bút toán liên công ty](inter-company-journal-entry.md)

### 1.3 Lập hóa đơn
1. [Hóa đơn bán hàng](sales-invoice.md)
1. [Hóa đơn mua hàng](purchase-invoice.md)
1. [Hóa đơn liên công ty](inter-company-invoices.md)
1. [Giấy báo Có (Credit Note)](credit-note.md)
1. [Giấy báo Nợ (Debit Note)](debit-note.md)
1. [Hạn mức tín dụng](credit-limit.md)

### 1.4 Thuế
1. [Mẫu thuế mặt hàng](item-tax-template.md)
1. [Danh mục khấu trừ thuế tại nguồn](tax-withholding-category.md)
1. [Quy tắc thuế](tax-rule.md)
1. [Danh mục thuế](tax-category.md)

### 1.5 Định giá
1. [Quy tắc định giá](pricing-rule.md)
1. [Chương trình khuyến mãi](promotional-scheme.md)
1. [Đánh giá lại tỷ giá hối đoái](exchange-rate-revaluation.md)
1. [Trao đổi ngoại tệ](currency-exchange.md)
1. [Tiền tệ](currency.md)

### 1.6 Hoạt động bán lẻ
1. [Hồ sơ POS](pos-profile.md)
2. [Điểm bán hàng (POS)](point-of-sales.md)
3. [Chốt ca thu ngân POS](pos-cashier-closing.md)

### 1.7 Công cụ
1. [Đối chiếu ngân hàng](bank-reconciliation.md)
1. [Đối chiếu thanh toán](payment-reconciliation.md)
1. [Chứng từ khóa sổ kỳ kế toán](period-closing-voucher.md)
1. [Lệnh thanh toán](payment-order.md)
1. [Công cụ chuyển đổi Quickbooks](quickbooks-migrator.md)
1. [Xử lý sao kê tài khoản](process-statement-of-accounts.md)

### 1.8 Báo cáo
1. [Báo cáo kế toán](accounting-reports.md)

### 1.9 Nâng cao
1. [Kế toán đa tiền tệ](multi-currency-accounting.md)
1. [Doanh thu hoãn lại](deferred-revenue.md)
1. [Chi phí hoãn lại](deferred-expense.md)
1. [Xử lý kế toán hoãn lại](process-deferred-accounting.md)
1. [Bảo lãnh ngân hàng](bank-guarantee.md)
1. [Chương trình khách hàng thân thiết](loyalty-program.md)
1. [Lập ngân sách](budgeting.md)
1. [Tự động lặp lại](../automation/auto-repeat.md)
1. [Chiết khấu hóa đơn](invoice_discounting.md)

### 1.10 Đăng ký thuê bao
1. [Đăng ký thuê bao](subscription.md)
1. [Gói đăng ký thuê bao](subscription-plan.md)
1. [Cài đặt đăng ký thuê bao](subscription-settings.md)

### 1.11 Quản lý cổ đông
1. [Cổ đông](shareholder.md)
1. [Chuyển nhượng cổ phần](share-transfer.md)
1. [Báo cáo cổ phần](share-reports.md)

### 1.12 GST
1. [Thiết lập GST](../regional/india/gst-setup.md)
1. [Nhắc nhở GST](regional/india/