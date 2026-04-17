<!-- add-breadcrumbs -->
# Chương trình Khách hàng thân thiết

**Chương trình Khách hàng thân thiết cho phép Khách hàng tích lũy điểm bằng cách chi tiêu một Số tiền nhất định và cho phép họ quy đổi điểm đó trong các lần mua hàng trong tương lai.**

Chương trình Khách hàng thân thiết là một nỗ lực tiếp thị có cấu trúc và dài hạn nhằm cung cấp các ưu đãi cho Khách hàng quay lại mua hàng. Các chương trình thành công được thiết kế để thúc đẩy Khách hàng trong thị trường mục tiêu của doanh nghiệp quay lại thường xuyên hơn, mua hàng thường xuyên hơn và tránh xa các đối thủ cạnh tranh.

Để truy cập danh sách Chương trình Khách hàng thân thiết, hãy đi đến:
> Home > Retail > Retail Operations > Loyalty Program

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Chương trình Khách hàng thân thiết, bạn nên tạo các mục sau trước:

1. [Customer](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/customer)
1. [Sales Invoice](sales-invoice.md)

## 2. Cách tạo Chương trình Khách hàng thân thiết
1. Đi đến danh sách Chương trình Khách hàng thân thiết và nhấn New.
1. Nhập Tên cho Chương trình Khách hàng thân thiết.
1. Chọn chương trình là Hạng đơn (Single Tiered) hay Đa hạng (Multi Tiered) (vàng, bạc, v.v.).
1. Thiết lập ngày bắt đầu và ngày kết thúc cho chương trình.
1. Chọn Nhóm khách hàng (Customer Group) và Khu vực (Territory) mà chương trình này áp dụng, mặc định là tất cả.
1. Để áp dụng cho tất cả Khách hàng theo mặc định, hãy tích vào 'Auto Opt In (For all customers)'. Nếu không, chương trình cần được chỉ định từ [Customer master](loyalty-program.md#22-loyalty-points-in-customer).
1. Trong bảng, nhập:
 2. **Tier name**: Tên hạng được chỉ định cho Khách hàng dựa trên điều kiện của họ.
 2. **Collection Factor**: Số tiền cần chi tiêu để nhận được 1 Điểm khách hàng thân thiết trong ERPNext.
 2. **Minimum Amount**: Số tiền tối thiểu cần chi tiêu để đủ điều kiện vào một hạng.
1. Thiết lập Hệ số quy đổi (Conversion Factor), ví dụ: 10 USD = 1 điểm.
1. Lưu.

 ![Loyalty Program](https://docs.erpnext.com/docs/v13/assets/img/accounts/loyalty-program.png)

### 2.1 Phần quy đổi (Redemption section)

* **Conversion Factor**: Khi quy đổi điểm khách hàng thân thiết, hệ số này quyết định 1 Điểm khách hàng thân thiết có giá trị bao nhiêu tiền. Ví dụ, nếu một Khách hàng có 100 Điểm khách hàng thân thiết, và 1 Điểm khách hàng thân thiết = 1 USD, thì Khách hàng có thể sử dụng các Mặt hàng lên đến 100 USD bằng điểm của họ cho các lần mua hàng trong tương lai.

* **Expense Account**: Thiết lập một Tài khoản chi phí nơi bạn sẽ cung cấp các lợi ích. Điều này hữu ích để theo dõi các lợi ích được cung cấp một cách riêng biệt.

* **Expiry Duration (in days)**: Các điểm khách hàng thân thiết đã tích lũy sẽ hết hạn sau số ngày được thiết lập trong trường này.

### 2.2 Điểm khách hàng thân thiết trong Khách hàng

Thiết lập phần Chương trình Khách hàng thân thiết trong thông tin Khách hàng để chỉ định một Chương trình Khách hàng thân thiết cho một Khách hàng.

![Loyalty Program in Customer](https://docs.erpnext.com/docs/v13/assets/img/accounts/loyalty-program-in-customer.png)

**Điểm khách hàng thân thiết** đã tích lũy có thể được xem trong Trang tổng quan của Khách hàng.

![Loyalty Points](https://docs.erpnext.com/docs/v13/assets/img/accounts/loyalty-points-in-customer.png)

### 2.3 Bút toán điểm khách hàng thân thiết (Loyalty Point Entry)
Đi đến: **Accounts > Retail Operations > Loyalty Point Entry**.
Mục này đóng vai trò như một nhật ký để cung cấp cái nhìn tổng quan về việc Khách hàng nào đã tích lũy được bao nhiêu điểm dựa trên Hóa đơn bán hàng nào. Nó lưu giữ dữ liệu Hóa đơn và Khách hàng.

![Loyalty Program Entry](https://docs.erpnext.com/docs/v13/assets/img/accounts/loyalty-program-entry.png)

## 3. Chương trình Khách hàng thân thiết hoạt động như thế nào?

### 3.1 Tích lũy điểm

* Đầu tiên, một **Chương trình Khách hàng thân thiết** cần được tạo như đã giải thích ở phần đầu tiên.
* Chỉ định **Chương trình Khách hàng thân thiết** này cho một **Khách hàng**.
* Tạo một Hóa đơn bán hàng mới cho **Khách hàng** mà bạn đã chỉ định **Chương trình Khách hàng thân thiết**.
* Trong ví dụ này, một hóa đơn được tạo với tổng cộng là 3,000 INR và theo **Chương trình Khách hàng thân thiết**, với mức chi tiêu tối thiểu là 2,000 INR, hạng Bạc (Silver Tier) sẽ đủ điều kiện và với mỗi 300 INR chi tiêu, **Khách hàng** sẽ nhận được 1 điểm (do đó tổng số điểm tích lũy được trong giao dịch này là 15).
* Sau khi Xác nhận hóa đơn, một **Bút toán điểm khách hàng thân thiết** sẽ được tạo cho hóa đơn này (như hiển thị ở trên trong phần Bút toán điểm khách hàng thân thiết).
* Trong **Chương trình Khách hàng thân thiết** của chúng ta, với mức chi tiêu tối thiểu là 6,000, hạng Vàng (Gold Tier) sẽ đủ điều kiện. Vì vậy, khi một hóa đơn khác được Xác nhận với giá trị tương tự, tổng doanh số từ Khách hàng này sẽ trở thành 6,000. Khi đó, **Khách hàng** sẽ tự động được nâng lên hạng Vàng.

> Lưu ý: Mức chi tiêu tối thiểu trong Chương trình Khách hàng thân thiết không có nghĩa là giá trị tối thiểu cho một hóa đơn duy nhất. Thay vào đó, nó có nghĩa là tổng số tiền của các hóa đơn của Khách hàng theo một chương trình Khách hàng thân thiết cụ thể.

### 3.2 Quy đổi điểm

* Hãy tiếp tục từ ví dụ trên nơi chúng ta đã tạo 1 hóa đơn và tích lũy được 15 điểm từ đó. Khi tạo một hóa đơn khác cho cùng một Khách hàng, hãy đi đến phần Điểm khách hàng thân thiết và bật hộp kiểm 'Redeem Loyalty Points' (Quy đổi điểm khách hàng thân thiết).
 ![Redeem Loyalty Points](https://docs.erpnext.com/docs/v13/assets/img/accounts/redeem-loyalty-points.png)
* Các trường cho 'Loyalty Point' (Điểm khách hàng thân thiết), 'Redemption Account' (Tài khoản quy đổi) và 'Redemption Cost Center' (Trung tâm chi phí quy đổi) sẽ hiển thị dưới phần này. Tài khoản và Trung tâm chi phí sẽ được lấy từ **Chương trình Khách hàng thân thiết** đã được chỉ định cho **Khách hàng**.
* Vì Khách hàng đã tích lũy được 15 điểm, chúng ta có thể sử dụng tất cả cho đến khi hết hạn. Nếu chúng ta cố gắng sử dụng nhiều hơn số điểm đang có, một lỗi sẽ được đưa ra.
* Trong ví dụ trên, chúng ta đã sử dụng 6375 điểm để quy đổi. Việc thực hiện như vậy sẽ kích hoạt một trường khác hiển thị số tiền được tính bằng (điểm khách hàng thân thiết * Hệ số quy đổi). Vì vậy, 6375 USD sẽ được khấu trừ vào số tiền vì 'Hệ số quy đổi' của chúng ta là '1'.
* Khi Xác nhận, 2 **Bút toán điểm khách hàng thân thiết** sẽ được tạo. Một cho phần quy đổi, sẽ là một giá trị âm và một cho hóa đơn hiện tại.
 ![Loyalty Point](https://docs.erpnext.com/docs/v13/assets/img/accounts/loyalty-point-entry-redeem.png)

> Lưu ý: Đối với một hóa đơn mà điểm đã được tích lũy, nếu một hóa đơn trả hàng được tạo, nó sẽ xóa Bút toán điểm khách hàng thân thiết ban đầu và tạo một bút toán mới sau khi trừ số tiền trả hàng khỏi số tiền ban đầu. Ngoài ra, khi Hủy một hóa đơn, Bút toán điểm khách hàng thân thiết liên quan của nó cũng sẽ bị xóa.

### 4. Các chủ đề liên quan
1. [Cost Center](cost-center.md)
1. [Sales Invoice](sales-invoice.md)
1. [Customer](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/customer)