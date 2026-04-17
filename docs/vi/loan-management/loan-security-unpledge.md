<!-- add-breadcrumbs -->
# Giải chấp Tài sản đảm bảo khoản vay
> Được giới thiệu trong Phiên bản 13

**Sau khi toàn bộ số tiền vay đã được thanh toán, một bản Giải chấp Tài sản đảm bảo khoản vay sẽ được tạo để giải chấp các tài sản đảm bảo.**

<img class="screenshot" alt="Make Loan Security Unpledge" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-security-unpledge-flow.png">

Để truy cập danh sách Giải chấp Tài sản đảm bảo khoản vay, hãy đi đến:
> Home > Loan Management > Loan Security > Loan Security Unpledge

## 1. Điều kiện tiên quyết
Trước khi tạo Giải chấp Tài sản đảm bảo khoản vay, bạn phải tạo các mục sau trước:

* [Loan Security Type](/docs/v13/user/manual/en/loan-management/loan-security-type)
* [Loan Security](/docs/v13/user/manual/en/loan-management/loan-security)
* [Loan](/docs/v13/user/manual/en/loan-management/loan)


## 2. Cách tạo Giải chấp Tài sản đảm bảo khoản vay
1. Đi đến Danh sách Giải chấp Tài sản đảm bảo khoản vay, nhấn vào Mới.
2. Chọn Khoản vay mà tài sản đảm bảo sẽ được giải chấp.
3. Chọn Người đăng ký.
4. Chọn Công ty
5. Trong bảng tài sản đảm bảo, nhập Tài sản đảm bảo khoản vay và số lượng cần giải chấp. Đồng thời nhập [Loan Security Pledge](/docs/v13/user/manual/en/loan-management/loan-security-pledge) mà tài sản đảm bảo cần được giải chấp.
6. Nhấn "Lưu" để lưu bản nháp của Giải chấp Tài sản đảm bảo khoản vay.
7. Nhấn "Xác nhận" để giải chấp tài sản đảm bảo khoản vay.

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-security-unpledge.png">


### 2.1. Các cách khác để tạo Giải chấp Tài sản đảm bảo khoản vay
Bạn cũng có thể tạo Giải chấp Tài sản đảm bảo khoản vay từ một Khoản vay mà yêu cầu tất toán khoản vay đang được thực hiện thông qua nút **Create** ở góc trên bên phải.

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan-security-unpledge.png">

## 3. Các tính năng

### 3.1 Phê duyệt Yêu cầu Giải chấp Tài sản đảm bảo khoản vay
Khi được phê duyệt, Giải chấp Tài sản đảm bảo khoản vay sẽ tự động cập nhật số lượng và trạng thái trong [Loan Security Pledge](/docs/v13/user/manual/en/loan-management/loan-security-pledge) tương ứng. Trong trường hợp giải chấp toàn bộ, trạng thái trong Loan Security Pledge mà yêu cầu giải chấp hướng tới sẽ được đặt là "Unpledge", nếu không nó sẽ được đặt là "Partially Pledged". Trong trường hợp giải chấp toàn bộ, Khoản vay mà yêu cầu giải chấp hướng tới cũng sẽ được tự động đóng.

{next}