<!-- add-breadcrumbs -->
# Bán Tài sản

Để bán một tài sản, hãy mở hồ sơ tài sản và nhấp vào nút **Sell Asset**. Thao tác này sẽ đưa bạn đến [Sales Invoice](../accounts/sales-invoice.md). Trong Sales Invoice, hãy nhập các chi tiết như Khách hàng và Ngày đến hạn thanh toán.

Khi Xác nhận Sales Invoice, các bút toán kế toán sau sẽ được thực hiện:

- "Receivable Account" (Phải thu) sẽ được ghi nợ bằng số tiền bán hàng.
- "Fixed Asset Account" sẽ được ghi có bằng giá trị mua của tài sản.
- "Accumulated Depreciation Account" sẽ được ghi nợ bằng tổng số tiền khấu hao cho đến nay.
- "Gain/Loss Account on Asset Disposal" sẽ được ghi có/ghi nợ dựa trên số tiền lãi/lỗ. Tài khoản Lãi/Lỗ có thể được thiết lập trong hồ sơ Công ty.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-sales.png">

### Các chủ đề liên quan
1. [Asset Value Adjustment](asset-value-adjustment.md)
1. [Purchasing an Asset](purchasing-an-asset.md)

{next}