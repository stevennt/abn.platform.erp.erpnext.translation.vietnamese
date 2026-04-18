<!-- add-breadcrumbs -->
# Trung tâm chi phí

**Trung tâm chi phí là một bộ phận của tổ chức nơi các chi phí hoặc thu nhập có thể được ghi nhận.**

Trong ERPNext, bạn có thể sử dụng Trung tâm chi phí như một Trung tâm lợi nhuận.

Hệ thống tài khoản của bạn chủ yếu được thiết kế để cung cấp báo cáo cho chính phủ và các cơ quan thuế.

Hầu hết các doanh nghiệp có nhiều hoạt động như các dòng sản phẩm khác nhau, phân khúc thị trường, lĩnh vực kinh doanh, v.v. cùng chia sẻ một số chi phí chung. Lý tưởng nhất là họ nên có cấu trúc riêng để báo cáo xem họ có đang hoạt động có lãi hay không. Vì mục đích này, có một cấu trúc thay thế được gọi là Hệ thống trung tâm chi phí.

Một Trung tâm chi phí hoạt động giống như một [Accounting Dimension](accounting-dimensions.md) giúp bạn theo dõi chi phí dựa trên các khu vực cụ thể.

Trung tâm chi phí có thể được thiết lập ở các cấp độ sau:

* Công ty
* Mặt hàng
* Đơn hàng/Hóa đơn

Trung tâm chi phí có thể được liên kết với các giao dịch sau:

1. [Sales Invoice](sales-invoice.md)
1. [Purchase Invoice](purchase-invoice.md)
1. [Journal Entry](journal-entry.md)
1. [Payment Entry](payment-entry.md)
1. [Delivery Note](../stock/delivery-note.md)

Và các giao dịch khác có thể được sử dụng để lập ngân sách. Bạn cũng có thể sử dụng Trung tâm chi phí để [Budgeting](budgeting.md).

## 1. Cây Trung tâm chi phí

Bạn có thể tạo một cây Trung tâm chi phí để đại diện tốt hơn cho doanh nghiệp của mình. Mỗi bút toán Thu nhập / Chi phí cũng được gắn với một Trung tâm chi phí. Nếu 'Allow Cost Center In Entry of Balance Sheet Account' được tích chọn trong Cài đặt tài khoản, hệ thống sẽ cho phép Người dùng gắn bút toán trong các Tài khoản Bảng cân đối kế toán với một Trung tâm chi phí.

Ví dụ, nếu bạn có hai loại hình bán hàng:

 * Bán hàng trực tiếp
 * Bán hàng trực tuyến

Bạn có thể không tốn chi phí vận chuyển cho khách hàng mua trực tiếp, và không tốn tiền thuê cửa hàng cho khách hàng mua trực tuyến. Nếu bạn muốn biết lợi nhuận của từng loại hình này một cách riêng biệt, bạn nên tạo hai loại này thành các Trung tâm chi phí và đánh dấu tất cả các đơn bán hàng với Trung tâm chi phí "Walk-in" hoặc "Online". Đánh dấu tất cả các khoản mua hàng của bạn theo cách tương tự.

Do đó, khi bạn thực hiện phân tích, bạn sẽ hiểu rõ hơn về mảng nào trong hoạt động kinh doanh của mình đang hoạt động tốt hơn. Vì ERPNext có tùy chọn thêm nhiều Công ty, bạn có thể tạo các Trung tâm chi phí cho từng Công ty và quản lý chúng riêng biệt.

Để truy cập Hệ thống trung tâm chi phí, hãy đi tới:
> Home > Accounting > Budget and Cost Center > Chart of Cost Centers

## 2. Cách thiết lập Hệ thống trung tâm chi phí
1. Đi tới Hệ thống trung tâm chi phí.
1. Thêm các nút theo khu vực.
1. Thêm các nút khác theo nhu cầu của bạn.

Khi chọn một Công ty khác, hệ thống sẽ hiển thị các Trung tâm chi phí của Công ty đó.

<img class="screenshot" alt="Cost Center" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/chart-of-cost-center.png">

![Chart of Cost Centers](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/company-master.png)


### 3. Các chủ đề liên quan
1. [Budgeting](budgeting.md)
1. [Sales Invoice](sales-invoice.md)
1. [Purchase Invoice](purchase-invoice.md)

{next}