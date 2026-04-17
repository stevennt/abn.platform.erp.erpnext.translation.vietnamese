<!-- add-breadcrumbs -->
# Giá trị mặt hàng theo FIFO và Giá trung bình gia tăng

### Các mặt hàng được định giá như thế nào?

Một trong những tính năng chính của bất kỳ hệ thống tồn kho nào là bạn có thể tìm ra giá trị của bất kỳ mặt hàng nào dựa trên giá lịch sử hoặc giá trung bình của nó. Bạn cũng có thể tìm thấy giá trị của tất cả các mặt hàng để phục vụ cho bảng cân đối kế toán.

Việc định giá rất quan trọng vì:

* Giá mua có thể biến động.
* Giá trị có thể thay đổi do một số quy trình (giá trị gia tăng).
* Giá trị có thể thay đổi do hư hỏng, thất thoát, v.v.

Bạn có thể gặp các thuật ngữ này, vì vậy hãy cùng làm rõ:

* **Rate (Mức giá):** Mức giá mà giao dịch diễn ra.
* **Valuation Rate (Giá trị định giá):** Mức giá được thiết lập để tính giá trị mặt hàng cho việc định giá của bạn.

Có hai phương pháp chính ERPNext v16 dùng để định giá các mặt hàng của bạn:

* **FIFO (Nhập trước Xuất trước):** Trong hệ thống này, ERPNext giả định rằng bạn sẽ tiêu thụ / bán những Mặt hàng được mua trước trước. Ví dụ, nếu bạn mua một Mặt hàng với giá X và sau đó vài ngày mua với giá Y, bất cứ khi nào bạn bán Mặt hàng đó, ERPNext sẽ giảm số lượng của Mặt hàng với mức giá X trước, sau đó mới đến giá Y.

<img alt="FIFO" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/stock/fifo.png">

* **Moving Average (Giá trung bình gia tăng):** Trong phương pháp này, ERPNext giả định rằng giá trị của mặt hàng tại bất kỳ thời điểm nào là mức giá trung bình của các đơn vị của Mặt hàng đó trong kho. Ví dụ, nếu giá trị của một Mặt hàng là X trong một Kho với số lượng Y và một số lượng Y1 khác được thêm vào Kho với giá X1, thì giá trị mới X2 sẽ là:

> Giá trị mới X2 = (X * Y + X1 * Y1) / (Y + Y1)

---

### Các tính năng quản lý tồn kho mới trong v16

Bên cạnh các phương pháp định giá truyền thống, ERPNext v16 mang đến các cải tiến mạnh mẽ để tối ưu hóa quản lý kho:

* **Hệ thống Giữ hàng (Stock Reservation System):** Cho phép giữ trước số lượng Mặt hàng trong Kho cho các Đơn bán hàng (SO) hoặc các yêu cầu khác, giúp đảm bảo khả năng cung ứng và lập kế hoạch chính xác.
* **Báo cáo Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability Report):** Cung cấp khả năng theo dõi toàn diện lịch sử của từng Lô hàng (Batch) hoặc Số Serial từ khi nhập kho (PR/DN) cho đến khi xuất kho, đảm bảo tính minh bạch trong quản lý chất lượng.
* **Chi phí vận chuyển tính vào giá trị tồn kho (Landed Cost cho Stock Entry):** Cho phép phân bổ các chi phí mua hàng (như vận chuyển, thuế, phí bốc xếp) trực tiếp vào giá trị của Mặt hàng khi thực hiện Phiếu nhập hàng (PR) hoặc Phiếu kho (SE), giúp giá trị định giá (Valuation Rate) phản ánh chính xác thực tế.
* **Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting):** Tăng cường độ chính xác cho các Bút toán (JE) bằng cách cho phép theo dõi chi tiết giá trị tài khoản kho gắn liền với từng loại Mặt hàng cụ thể.
* **Xem trước Sổ cái (Ledger Preview):** Cho phép người dùng xem nhanh các bút toán liên quan trực tiếp từ giao diện quản lý tồn kho, giúp đối soát giữa số lượng thực tế và giá trị kế toán trở nên dễ dàng hơn.