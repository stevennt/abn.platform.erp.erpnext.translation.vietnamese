<!-- add-breadcrumbs -->
# Quy trình tính lãi vay dồn tích
> Giới thiệu trong Phiên bản 13

**Bản ghi Quy trình tính lãi vay được tạo ra trong mỗi chu kỳ tính lãi vay dồn tích và cũng được sử dụng để xử lý thủ công việc tính lãi vay dồn tích.**

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/process-loan-interest-accrual-flow.png">

Để truy cập danh sách Quy trình tính lãi vay dồn tích, hãy đi đến:
> Home > Loan Management > Loan Processes > Process Loan Interest Accrual

Lãi vay sẽ được tính dồn tích hàng tháng vào ngày đầu tiên của mỗi tháng đối với các khoản vay theo yêu cầu (demand loans) và một ngày trước ngày thanh toán đối với các khoản vay có kỳ hạn (term loans) bởi một công việc chạy ngầm (background job). Nếu bạn muốn tính lãi dồn tích thủ công cho một khoản vay, bạn có thể thực hiện bằng cách sử dụng Quy trình tính lãi vay dồn tích.

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/process-loan-interest-accrual.png">

## 1. Điều kiện tiên quyết
Trước khi tạo Quy trình tính lãi vay dồn tích, trước tiên bạn phải tạo:

* [Khoản vay (Loan)](/docs/v13/user/manual/en/loan-management/loan)


## 2. Cách tạo Quy trình tính lãi vay dồn tích
1. Đi đến Danh sách Quy trình tính lãi vay dồn tích, nhấn vào Mới.
2. Nhập Ngày hạch toán (Posting Date). Ngày hạch toán là ngày mà đến đó lãi sẽ được tính dồn tích kể từ ngày tính lãi dồn tích gần nhất.
3. Nhập Loại khoản vay (Loan Type) nếu bạn muốn tính lãi cho một Loại khoản vay cụ thể. Nếu không nhập Loại khoản vay nào thì lãi sẽ được tính cho tất cả các Loại khoản vay.
4. Nhập Khoản vay (Loan) nếu bạn muốn tính lãi cho một khoản vay cụ thể. Nếu không nhập khoản vay nào thì lãi sẽ được tính cho tất cả các khoản vay.
5. Nhấn "Lưu" để lưu bản Nháp của việc Giải ngân khoản vay.
6. Nhấn "Xác nhận" để xác nhận việc Cầm cố tài sản bảo đảm khoản vay.


{next}