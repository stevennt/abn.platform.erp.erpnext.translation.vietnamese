<!-- add-breadcrumbs -->
# Quản lý chênh lệch tỷ giá hối đoái

Trong ERPNext, bạn cũng có thể tạo các giao dịch bằng ngoại tệ. Khi tạo giao dịch bằng ngoại tệ, hệ thống sẽ cập nhật tỷ giá hối đoái hiện tại so với tiền tệ của Khách hàng/Nhà cung cấp và tiền tệ cơ sở của Công ty bạn. Vì Tỷ giá hối đoái luôn biến động, bạn có thể nhận được thanh toán từ khách hàng với tỷ giá khác với tỷ giá được ghi trong Hóa đơn bán hàng/Hóa đơn mua hàng. Dưới đây là hướng dẫn về cách quản lý số tiền chênh lệch có trong bút toán thanh toán do thay đổi tỷ giá hối đoái.

## Thêm Tài khoản chi phí

Để quản lý chênh lệch tiền tệ, hãy tạo Tài khoản **Exchange Gain/Loss** (Lãi/Lỗ tỷ giá). Tài khoản này thường được tạo ở bên Chi phí của báo cáo kết quả hoạt động kinh doanh (P&L). Tuy nhiên, bạn có thể đặt nó dưới một nhóm khác tùy theo yêu cầu kế toán của mình.

![Exchange Gain/Loss Ledger](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/exchange-gain-loss-ledger.png)

## Hạch toán Bút toán thanh toán

![Auto Calculate Exchange Gain Loss](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/exchange-gain-loss-auto-calculation.gif)

{next}