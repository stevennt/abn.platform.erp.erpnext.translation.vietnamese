<!-- add-breadcrumbs -->
# Giá trị mặt hàng theo FIFO và Giá trung bình gia tăng

### Các mặt hàng được định giá như thế nào?

Một trong những tính năng chính của bất kỳ hệ thống tồn kho nào là bạn có thể tìm ra giá trị của bất kỳ mặt hàng nào dựa trên giá lịch sử hoặc giá trung bình của nó. Bạn cũng có thể tìm thấy giá trị của tất cả các mặt hàng để phục vụ cho bảng cân đối kế toán.

Việc định giá rất quan trọng vì:

  * Giá mua có thể biến động.
  * Giá trị có thể thay đổi do một số quy trình (giá trị gia tăng).
  * Giá trị có thể thay đổi do hư hỏng, thất thoát, v.v.

Bạn có thể gặp các thuật ngữ này, vì vậy hãy cùng làm rõ:

  * Rate: Mức giá mà giao dịch diễn ra.
  * Valuation Rate: Mức giá được thiết lập để tính giá trị mặt hàng cho việc định giá của bạn.

Có hai phương pháp chính mà ERPNext dùng để định giá các mặt hàng của bạn.

  * **FIFO (First In First Out):** Trong hệ thống này, ERPNext giả định rằng bạn sẽ tiêu thụ / bán những Mặt hàng được mua trước trước. Ví dụ, nếu bạn mua một Mặt hàng với giá X và sau đó vài ngày mua với giá Y, bất cứ khi nào bạn bán Mặt hàng đó, ERPNext sẽ giảm số lượng của Mặt hàng với mức giá X trước, sau đó mới đến giá Y.

<img alt="FIFO" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/stock/fifo.png">

  * **Moving Average (Giá trung bình gia tăng):** Trong phương pháp này, ERPNext giả định rằng giá trị của mặt hàng tại bất kỳ thời điểm nào là mức giá trung bình của các đơn vị của Mặt hàng đó trong kho. Ví dụ, nếu giá trị của một Mặt hàng là X trong một Kho với số lượng Y và một số lượng Y1 khác được thêm vào Kho với giá X1, thì giá trị mới X2 sẽ là:

> Giá trị mới X2 = (X * Y + X1 * Y1) / (Y + Y1)