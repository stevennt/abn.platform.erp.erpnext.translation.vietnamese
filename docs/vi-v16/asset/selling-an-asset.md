<!-- add-breadcrumbs -->
# Bán Tài sản

Để bán một tài sản, hãy mở hồ sơ tài sản và nhấp vào nút **Sell Asset**. Thao tác này sẽ đưa bạn đến [Hóa đơn bán hàng](/docs/v16/user/manual/vi/accounts/sales-invoice). Trong Hóa đơn bán hàng, hãy nhập các chi tiết như Khách hàng và Ngày đến hạn thanh toán.

Khi Xác nhận Hóa đơn bán hàng, các bút toán kế toán sau sẽ được thực hiện:

- "Receivable Account" (Phải thu) sẽ được ghi nợ bằng số tiền bán hàng.
- "Fixed Asset Account" (Tài khoản tài sản cố định) sẽ được ghi có bằng giá trị mua của tài sản.
- "Accumulated Depreciation Account" (Tài khoản khấu hao lũy kế) sẽ được ghi nợ bằng tổng số tiền khấu hao cho đến nay.
- "Gain/Loss Account on Asset Disposal" (Tài khoản Lãi/Lỗ thanh lý tài sản) sẽ được ghi có/ghi nợ dựa trên số tiền lãi/lỗ. Tài khoản Lãi/Lỗ có thể được thiết lập trong hồ sơ Công ty.

<img class="screenshot" alt="Asset" src="https://docs.erpnext.com/docs/v16/assets/img/asset/asset-sales.png">

**Lưu ý mới trên v16:**
- **Nút lệnh nhanh:** Tại hồ sơ Khách hàng, bạn có thể sử dụng các nút **SO/Quotation** để tạo nhanh Đơn bán hàng hoặc Báo giá.
- **Quản lý tồn kho:** Tính năng **Stock Reservation** (Giữ hàng) giúp đảm bảo tài sản hoặc mặt hàng được giữ riêng cho Đơn bán hàng, tránh việc xuất kho cho các yêu cầu khác trước khi hoàn tất giao dịch.
- **Ngày cắt sổ (Cutoff date):** Khi tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO), hãy lưu ý kiểm tra ngày cắt sổ để đảm bảo tính chính xác của báo cáo tồn kho và giá vốn.

### Các chủ đề liên quan
1. [Điều chỉnh giá trị tài sản](/docs/v16/user/manual/vi/asset/asset-value-adjustment)
1. [Mua tài sản](/docs/v16/user/manual/vi/asset/purchasing-an-asset)

{next}