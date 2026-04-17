<!-- add-breadcrumbs -->
# Cài đặt Kế toán

Có nhiều cài đặt kế toán khác nhau trong ERPNext để hạn chế và cấu hình các hành động trong phân hệ Kế toán.

![Account Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/account-settings.png)

## 1. Tài khoản bị đóng băng đến ngày
Đóng băng các giao dịch kế toán đến một ngày cụ thể, không ai có thể tạo/sửa đổi bút toán ngoại trừ Vai trò được chỉ định.

## 2. Vai trò được phép thiết lập Tài khoản đóng băng & Sửa đổi các bút toán đã đóng băng
Người dùng có Vai trò này được phép thiết lập các tài khoản bị đóng băng và tạo/sửa đổi các bút toán kế toán đối với các tài khoản đã đóng băng.

## 3. Xác định Danh mục Thuế Địa chỉ từ
[Danh mục thuế](tax-category.md) có thể được thiết lập trên Địa chỉ. Một địa chỉ có thể là địa chỉ Giao hàng hoặc địa chỉ Thanh toán. Thiết lập địa chỉ nào sẽ được chọn khi áp dụng Danh mục Thuế.

## 4. Phần trăm cho phép lập hóa đơn vượt mức
Phần trăm mà bạn có thể lập hóa đơn vượt quá giá trị giao dịch. Ví dụ, nếu giá trị đơn hàng cho một Mặt hàng là $100 và phần trăm ở đây được thiết lập là 10% thì bạn được phép lập hóa đơn với số tiền $110.

## 5. Vai trò được phép lập hóa đơn vượt mức
Người dùng có vai trò này được phép lập hóa đơn vượt quá phần trăm cho phép.

## 6. Kiểm soát viên tín dụng
Chọn vai trò được phép Xác nhận các giao dịch vượt quá hạn mức tín dụng đã thiết lập. Hạn mức tín dụng có thể được thiết lập trong biểu mẫu Khách hàng.

## 7. Kiểm tra tính duy nhất của Số hóa đơn Nhà cung cấp
Khi được chọn, các Hóa đơn mua hàng có cùng 'Số hóa đơn Nhà cung cấp' sẽ không được phép. Điều này hữu ích để tránh các bút toán trùng lặp.

## 8. Thực hiện Thanh toán qua Bút toán
Khi được chọn, nếu người dùng tiến hành thực hiện thanh toán từ một hóa đơn, hệ thống sẽ mở một Bút toán thay vì một Bút toán thanh toán.

## 9. Hủy liên kết Thanh toán khi Hủy Hóa đơn
Nếu được chọn, hệ thống sẽ hủy liên kết khoản thanh toán đối với hóa đơn tương ứng. Theo mặc định, nếu một Bút toán thanh toán đã được Xác nhận, hóa đơn liên kết không thể bị Hủy cho đến khi Bút toán thanh toán cũng được Hủy. Khi hủy liên kết, giờ đây bạn có thể Hủy và Sửa đổi các hóa đơn. Nhưng các khoản thanh toán sẽ không được liên kết và được coi là các khoản thanh toán tạm ứng.

## 10. Hủy liên kết Thanh toán tạm ứng khi Hủy Đơn hàng
Tương tự như tùy chọn trước, tùy chọn này sẽ hủy liên kết bất kỳ khoản thanh toán tạm ứng nào được thực hiện đối với Đơn mua hàng/Đơn bán hàng.


## 11. Tự động ghi bút toán Khấu hao Tài sản
Khi được chọn, một bút toán tự động cho việc khấu hao tài sản sẽ được tạo dựa trên ngày đầu tiên được thiết lập. Ví dụ, việc khấu hao hàng năm cho một mặt hàng sẽ được lập lịch cho 3/4 năm tiếp theo dựa trên Số lần khấu hao đã ghi (Number of Depreciations Booked) được thiết lập trong danh mục Tài sản. Để biết thêm chi tiết, hãy truy cập trang [Khấu hao Tài sản](https://docs.erpnext.com/docs/v13/user/manual/en/asset/asset-depreciation).

## 12. Cho phép Trung tâm chi phí trong bút toán Tài khoản Bảng cân đối kế toán
Nếu được chọn, hệ thống sẽ cho phép người dùng gắn các bút toán trong Tài khoản Bảng cân đối kế toán với một Trung tâm chi phí. Theo mặc định, Trung tâm chi phí chỉ có sẵn cho tài khoản Lãi/Lỗ.

## 13. Tự động thêm Thuế và các khoản phí từ Mẫu thuế Mặt hàng
Bật tính năng này sẽ tự động điền bảng Thuế trong các giao dịch nếu một [Mẫu thuế Mặt hàng](item-tax-template.md) được thiết lập cho một Mặt hàng và Mặt hàng đó được chọn trong giao dịch.

## 14. Tự động lấy Điều khoản thanh toán
Bật tính năng này sẽ tự động lấy Điều khoản thanh toán dựa trên Nhà cung cấp.

## 15. Cài đặt In

![Account Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/print-accounts-settings.png)

* **Hiển thị Thuế bao gồm trong bản in**: Các loại thuế được áp dụng sẽ được hiển thị trong chế độ xem in.
* **Hiển thị Lịch trình thanh toán trong bản in**: Bảng Lịch trình thanh toán sẽ hiển thị khi sử dụng [Điều khoản thanh toán](payment-terms.md). Bật tính năng này sẽ hiển thị bảng này trong chế độ xem in.

## 16. Cho phép Tỷ giá hối đoái cũ
Nên bỏ chọn mục này nếu bạn muốn ERPNext kiểm tra độ trễ của các bản ghi được lấy từ Tỷ giá hối đoái trong các giao dịch ngoại tệ. Nếu bỏ chọn, trường tỷ giá hối đoái sẽ ở chế độ chỉ đọc trong các tài liệu.

Số ngày cũ (Stale Days) là số ngày được sử dụng khi quyết định xem một bản ghi Tỷ giá hối đoái có bị coi là cũ hay không. Điều này có hiệu lực khi 'Cho phép tỷ giá cũ' được **tắt**. Vì vậy, nếu Số ngày cũ được thiết lập là 10, các tỷ giá cũ trong vòng 10 ngày sẽ được cho phép. Nếu Cho phép tỷ giá cũ được bật, sẽ không có giới hạn thời gian cho độ trễ của tỷ giá.

Nếu cho phép tỷ giá cũ, thứ tự lấy tỷ giá là:

* Tỷ giá mới nhất từ biểu mẫu Tỷ giá hối đoái
* Nếu không tìm thấy Tỷ giá hối đoái, tỷ giá mới nhất theo thị trường sẽ được lấy tự động

Nếu không cho phép tỷ giá cũ, thứ tự lấy tỷ giá là:

* Tỷ giá mới nhất từ biểu mẫu Tỷ giá hối đoái trong phạm vi số ngày được thiết lập trong 'Số ngày cũ'
* Nếu không tìm thấy Tỷ giá hối đoái, tỷ giá mới nhất theo thị trường sẽ được lấy tự động


## 17. Sử dụng Định dạng Dòng tiền Tùy chỉnh
Bạn có thể chọn sử dụng các Định dạng Dòng tiền Tùy chỉnh để tùy chỉnh giao diện của báo cáo Dòng tiền. Để biết thêm, hãy [truy cập trang này](articles/how-to-customise-cash-flow-report.md).

{next}