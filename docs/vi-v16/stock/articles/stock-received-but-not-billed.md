<!-- add-breadcrumbs -->
# Mục đích của Tài khoản Hàng nhập kho chưa có Hóa đơn (Stock Received but not Billed)

Khi các mặt hàng mua về được nhập kho, một bút toán kế toán sẽ được thực hiện dựa trên giá trị của các mặt hàng đã mua trong tài khoản Tồn kho hoặc Tài sản cố định. Khi bạn bán và giao những mặt hàng đó, một khoản chi phí (Giá vốn hàng bán) sẽ được ghi nhận, tương đương với giá mua của các mặt hàng.

Trong phiên bản ERPNext v16, quy trình này được tối ưu hóa với các tính năng mới như **Kế toán tồn kho theo từng mặt hàng (Item-Level Stock Accounting)** và **Xem trước sổ cái (Ledger Preview)**, giúp việc đối soát giữa kho và kế toán trở nên chính xác hơn.

### Quy trình hạch toán

1. **Khi nhập kho (Thông qua Phiếu nhập hàng - PR):**
   Khi số dư tồn kho tăng lên thông qua Phiếu nhập hàng, tài khoản Kho sẽ được ghi nợ và một tài khoản điều chỉnh gọi là **Stock Received But Not Billed** (Hàng nhập kho chưa có hóa đơn) sẽ được ghi có. 

   Đồng thời, một khoản chi phí âm sẽ được ghi nhận vào tài khoản có danh mục là "Valuation" hoặc "Total and Valuation" trong bảng thuế và phí cho số tiền được thêm vào nhằm mục đích tính giá, để tránh việc ghi nhận chi phí hai lần. Với tính năng **Landed Cost cho Phiếu kho (Stock Entry)**, bạn có thể cập nhật thêm các chi phí liên quan (như vận chuyển, thuế nhập khẩu) trực tiếp vào giá trị tồn kho ngay tại bước này.

2. **Khi nhận Hóa đơn (Thông qua Hóa đơn mua hàng - Invoice):**
   Khi nhận được hóa đơn từ Nhà cung cấp, bạn sẽ lập Hóa đơn mua hàng dựa trên Phiếu nhập hàng. Tại đây, tài khoản **Stock Received But Not Billed** sẽ được ghi nợ, do đó sẽ triệt tiêu số dư trong tài khoản Hàng nhập kho chưa có hóa đơn.

### Ý nghĩa của số dư
Số dư trong tài khoản Hàng nhập kho chưa có hóa đơn cho biết giá trị của các mặt hàng đã được lập Phiếu nhập hàng nhưng chưa được lập Hóa đơn mua hàng.

Việc theo dõi sát sao tài khoản này giúp doanh nghiệp kiểm soát được các khoản nợ tiềm tàng và đảm bảo tính khớp đúng giữa số lượng hàng thực tế trong Kho (đã được quản lý qua **Lô hàng - Batch** và **Số sê-ri - Serial**) với các nghĩa vụ thanh toán với Nhà cung cấp.