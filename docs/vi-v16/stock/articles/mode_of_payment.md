# Phương thức thanh toán

Trong các giao dịch bán hàng và mua hàng, có nhiều lựa chọn khác nhau để quyết toán thanh toán. Chúng ta có thể thực hiện bằng tiền mặt, qua chuyển khoản ngân hàng, qua phiếu giảm giá, cùng một số hình thức khác. Trong ERPNext v16, bạn có thể tạo các Phương thức thanh toán theo nhu cầu của mình. Trong Bút toán thanh toán, bạn có thể chọn Phương thức thanh toán tương ứng.

Bạn có thể quản lý các Phương thức thanh toán tiêu chuẩn và tạo mới từ:

> Kế toán > Thiết lập > Phương thức thanh toán

<img alt="mode of payments" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/mode-of-payments.png">

Trong mỗi danh mục Phương thức thanh toán, bạn cũng có thể thiết lập một tài khoản thanh toán mặc định. Khi chọn Phương thức thanh toán, tài khoản thanh toán tương ứng sẽ được tự động lấy vào trong giao dịch.

---

## Các tính năng mới trong phiên bản v16 liên quan đến Quản lý Kho và Kế toán

Bên cạnh các tính năng thanh toán, ERPNext v16 mang đến những cải tiến quan trọng trong quản lý dòng tiền và kiểm soát hàng hóa:

### 1. Hệ thống Giữ hàng (Stock Reservation System)
Giúp doanh nghiệp quản lý việc giữ hàng cho các Đơn bán hàng (SO) hoặc các yêu cầu khác, đảm bảo hàng hóa được dành riêng cho khách hàng cụ thể, tránh tình trạng thiếu hụt khi thực hiện xuất kho.

### 2. Báo cáo Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability Report)
Cung cấp khả năng theo dõi chi tiết lịch sử của từng Lô hàng (Batch) hoặc Số Serial từ khi nhập kho (PR) cho đến khi xuất kho, giúp kiểm soát chất lượng (QI) và quản lý vòng đời sản phẩm chặt chẽ hơn.

### 3. Chi phí mua hàng cập cảng cho Phiếu kho (Landed Cost cho Stock Entry)
Cho phép phân bổ các chi phí phát sinh thêm (như phí vận chuyển, thuế nhập khẩu, phí bốc xếp) trực tiếp vào giá trị của Mặt hàng (Item) khi thực hiện Phiếu nhập hàng hoặc Phiếu kho, giúp phản ánh chính xác giá trị tồn kho.

### 4. Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting)
Nâng cao khả năng kiểm soát tài chính bằng cách cho phép theo dõi giá trị kế toán chi tiết đến từng Mặt hàng cụ thể trong hệ thống sổ cái, giúp việc đối soát giữa kho và kế toán trở nên chính xác tuyệt đối.

### 5. Xem trước Sổ cái (Ledger Preview)
Tính năng cho phép người dùng xem nhanh các Bút toán (JE) liên quan trực tiếp từ giao dịch mà không cần phải chuyển hướng sang các màn hình kế toán phức tạp, giúp tăng tốc độ kiểm tra dữ liệu.