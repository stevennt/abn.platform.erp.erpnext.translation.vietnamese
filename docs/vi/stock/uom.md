<!-- add-breadcrumbs -->
# Đơn vị tính (UoM)

**UoM là đơn vị được sử dụng để đo lường một Mặt hàng.**

Theo mặc định, có nhiều UoM đã được tạo sẵn trong ERPNext. Tuy nhiên, bạn có thể thêm nhiều UoM khác tùy thuộc vào trường hợp sử dụng trong doanh nghiệp của mình.
Trong UoM có một tùy chọn 'Must be Whole Number' (Phải là số nguyên). Nếu tùy chọn này được chọn, bạn không thể sử dụng các số phân số trong UoM này. Để biết thêm về phân số và UoM, hãy xem [trang này](articles/managing-fractions-in-uom.md).

Bản thân danh sách UoM chỉ lưu trữ tên. Các tỷ lệ chuyển đổi thực tế được lưu trữ trong một tài liệu gọi là 'UoM Conversion Factor' (Hệ số chuyển đổi UoM). Nếu bạn thêm các UoM mới và có kế hoạch sử dụng chúng trong các giao dịch mà chúng sẽ được chuyển đổi sang các UoM khác, bạn nên thêm chúng vào danh sách này.

Ví dụ, ở đây 1 Kg xấp xỉ bằng 2.2 Pounds và hệ số chuyển đổi chính xác được lưu trữ như sau:

![UoM conversion factor](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/uom_convert.png)