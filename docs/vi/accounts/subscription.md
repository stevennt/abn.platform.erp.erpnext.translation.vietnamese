<!-- add-breadcrumbs -->
# Đăng ký thuê bao

Nếu bạn cung cấp một dịch vụ yêu cầu gia hạn trong một khoảng thời gian nhất định hoặc bạn thanh toán một số chi phí hàng tháng như tiền thuê nhà (hàng năm, hàng tháng, hàng quý, v.v.), bạn có thể sử dụng tính năng Đăng ký thuê bao trong ERPNext để theo dõi chúng. Hồ sơ Đăng ký thuê bao sẽ ghi lại tất cả các chi tiết cần thiết để tự động tạo Hóa đơn bán hàng hoặc Hóa đơn mua hàng.

Hãy xem xét một trường hợp sử dụng chính tính năng Đăng ký thuê bao của ERPNext. Các gói lưu trữ của chúng tôi được cung cấp theo năm. Mỗi tài khoản Khách hàng đều có ngày hết hạn đăng ký, sau đó khách hàng phải gia hạn đăng ký với chúng tôi.

Để quản lý ngày hết hạn đăng ký của khách hàng và tự động tạo Hóa đơn bán hàng cho việc gia hạn, chúng ta sử dụng tính năng Đăng ký thuê bao.

Để truy cập danh sách Đăng ký thuê bao, hãy đi đến:
> Trang chủ > Kế toán > Quản lý đăng ký thuê bao > Đăng ký thuê bao

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Đăng ký thuê bao, bạn nên tạo các mục sau trước:

1. [Gói đăng ký thuê bao](subscription-plan.md)

## 2. Cách thiết lập Đăng ký thuê bao
1. Đi đến danh sách Đăng ký thuê bao và nhấn vào Mới.
1. Chọn Loại đối tác là 'Khách hàng' hoặc 'Nhà cung cấp' và chọn đối tác đó.
1. Thiết lập Ngày bắt đầu là thời điểm đăng ký thuê bao có hiệu lực.
1. Bạn cũng có thể nhập ngày kết thúc đăng ký nếu đã biết trước (tùy chọn).
1. Số ngày đến hạn là số ngày mà Khách hàng phải thanh toán Hóa đơn bán hàng đã được tạo.
1. Chọn [Gói đăng ký thuê bao](subscription-plan.md).
1. Lưu.
 ![Subscription](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/subscription.png)

Dựa trên ngày bắt đầu và ngày kết thúc đăng ký, các ngày thực tế cho hóa đơn sẽ được tính toán.

## 3. Các tính năng
### 3.1 Thời gian dùng thử
Nếu bạn đang cung cấp một thời gian dùng thử cho gói đăng ký, bạn có thể thiết lập Ngày bắt đầu dùng thử và Ngày kết thúc dùng thử. Hóa đơn sẽ không được tạo trong thời gian dùng thử và trạng thái Đăng ký thuê bao sẽ hiển thị là 'Đang dùng thử'.
![Subscription Trial](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/subscription-trial.png)

### 3.2 Hủy gia hạn tự động
Khi bật 'Hủy khi kết thúc kỳ hạn', Đăng ký thuê bao sẽ được hủy khi kết thúc kỳ hạn của nó. Ví dụ, nếu là đăng ký thuê bao hàng năm, hệ thống sẽ ngừng tạo hóa đơn sau một năm đăng ký.

### 3.3 Thuế
Bạn có thể áp dụng Thuế cho Đăng ký thuê bao bằng cách sử dụng Mẫu thuế và phí bán hàng. Truy cập trang [Mẫu thuế và phí bán hàng](../selling/sales-taxes-and-charges-template.md) để biết thêm chi tiết.

### 3.4 Áp dụng chiết khấu
Bạn có thể áp dụng thêm chiết khấu cho Đăng ký thuê bao dựa trên Tổng cộng (trước thuế) hoặc Tổng ròng (sau thuế). Bạn cũng có thể thiết lập tỷ lệ phần trăm chiết khấu. Ví dụ, mức chiết khấu 2% trên 12.000 sẽ là 240 tiền chiết khấu.
 ![Subscription Discount](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/subscription-discount.png)
Truy cập trang [Áp dụng chiết khấu](../selling/articles/applying-discount.md) để biết thêm chi tiết.

### 3.5 Tự động tạo hóa đơn
Dựa trên khoảng thời gian của [Gói đăng ký thuê bao](subscription-plan.md), các hóa đơn sẽ được tạo tự động. Cần phải bật "Tạo hóa đơn vào đầu kỳ" nếu bạn muốn tạo hóa đơn ngay khi đăng ký thuê bao có hiệu lực. Nếu "Tạo hóa đơn mới khi quá hạn" được bật, các hóa đơn mới sẽ tiếp tục được tạo ngay cả khi hóa đơn hiện tại chưa được thanh toán hoặc đã quá hạn. Nếu "Tạo hóa đơn sớm" được bật, một hóa đơn sẽ được tạo trước khi kết thúc kỳ hạn theo số ngày được nhập trong "Số ngày tạo hóa đơn sớm".

Các hóa đơn được tạo sẽ được tự động Xác nhận theo mặc định. Nếu 'Tự động Xác nhận hóa đơn' bị tắt, hóa đơn sẽ được Lưu dưới dạng Nháp.

 ![Subscription Invoices](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/subscription-invoices.png)

### 3.6 Theo tháng dương lịch
Nếu 'Theo tháng dương lịch' được bật, các tháng dương lịch phù hợp sẽ được tuân thủ ngay cả khi Ngày bắt đầu đăng ký thuê bao nằm ở giữa tháng. Ví dụ: Giả sử khoảng thời gian thanh toán là 'Tháng' và số lượng khoảng thời gian thanh toán là 3 trong gói đăng ký và Ngày bắt đầu đăng ký thuê bao là '15-04-2020', nếu 'Theo tháng dương lịch' được chọn thì hóa đơn đầu tiên sẽ được tạo cho khoảng thời gian từ '15-04-2020' đến '30-06-2020' thay vì từ '15-04-2020' đến '14-07-2020'.

### 3.8 Hủy Đăng ký thuê bao
Nếu Khách hàng quyết định hủy Đăng ký thuê bao, nó có thể được hủy trong hệ thống bằng cách sử dụng **Hủy Đăng ký thuê bao**. Hệ thống sẽ ngừng tạo hóa đơn khi một Đăng ký thuê bao bị hủy.
 ![Subscription Cancel](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/subscription-cancel.png)

### 3.9 Cập nhật Đăng ký thuê bao
Nhấp vào nút **Lấy cập nhật đăng ký thuê bao** sẽ cập nhật Đăng ký thuê bao với các hóa đơn mới nhất đã được tạo.

## 4. Sự khác biệt giữa Tự động lặp lại và Đăng ký thuê bao

| Tự động lặp lại | Đăng ký thuê bao |
|---------------|---------------|
| Áp dụng cho các giao dịch | Áp dụng cho các Mặt hàng |
| Nhiều giao dịch như Đơn bán hàng, Đơn mua hàng, Hóa đơn, Bút toán, v.v. được tự động tạo | Chỉ có Hóa đơn bán hàng và Hóa đơn mua hàng được tự động tạo |
| Chỉ có một vài tùy chọn kiểm soát | Có nhiều tùy chọn kiểm soát để xác định thời gian dùng thử, ngày đến hạn thanh toán và tạo các Gói đăng ký thuê bao |

### 5. Các chủ đề liên quan
1. [Hóa đơn bán hàng](sales-invoice.md)
1. [Hóa đơn mua hàng](purchase-invoice.md)
1. [Mặt hàng](../stock/item.md)
1. [Khách hàng](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/customer)
1. [Gói đăng ký thuê bao](subscription-plan.md)

{next}