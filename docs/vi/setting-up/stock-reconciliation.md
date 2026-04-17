<!-- add-breadcrumbs -->
# Đối chiếu tồn kho

**Đối chiếu tồn kho là quá trình kiểm đếm và đánh giá vật tư/sản phẩm, được thực hiện định kỳ và vào cuối năm nhằm mục đích:**

* **Giữ cho số lượng kiểm kê thực tế và số lượng trên sổ sách đồng bộ với nhau**
* **Định giá tồn kho để chuẩn bị cho các báo cáo kế toán**

Đối chiếu tồn kho được sử dụng để:

* Hạch toán tồn kho đầu kỳ
* Đối chiếu giữa tồn kho trên sổ sách và tồn kho thực tế

#1. Cách tạo Đối chiếu tồn kho để hạch toán tồn kho đầu kỳ

##1.1. Đối với các Mặt hàng không có số serial

Sử dụng đối chiếu tồn kho, bạn có thể cập nhật số lượng của các mặt hàng cụ thể trong một kho tại một thời điểm nhất định.

Để hạch toán tồn kho đầu kỳ:

1. Đi đến **Kho > Công cụ > Đối chiếu tồn kho > Mới**
1. Thiết lập Ngày hạch toán.
1. Thiết lập Mục đích là Tồn kho đầu kỳ.
1. Thiết lập Mã mặt hàng, Kho, Số lượng và Giá trị tính giá.
1. Chọn 'Temporary Opening' trong Tài khoản chênh lệch.
1. Chọn Trung tâm chi phí.
1. Lưu và Xác nhận.

##1.2. Đối với các Mặt hàng có số serial

Sử dụng đối chiếu tồn kho, bạn có thể thêm các mặt hàng vào kho có số serial hoặc số lô.

Để hạch toán tồn kho đầu kỳ:

1. Đi đến **Kho > Công cụ > Đối chiếu tồn kho > Mới**
1. Thiết lập Ngày hạch toán.
1. Thiết lập Mục đích là Tồn kho đầu kỳ.
1. Thiết lập Mã mặt hàng, Kho, Số lượng, Số Serial / Lô, và Giá trị tính giá.
1. Nếu bạn muốn tự động tạo số serial / số lô, hãy để trống các trường số serial và số lô.
1. Để tự động tạo số serial, bạn cần thiết lập "Serial Number Series" trong thông tin mặt hàng.
1. Để tự động tạo số lô, bạn cần bật ô "Automatically Create New Batch" trong thông tin mặt hàng.
1. Chọn 'Temporary Opening' trong Tài khoản chênh lệch.
1. Chọn Trung tâm chi phí.
1. Lưu và Xác nhận.


#2. Cách tạo Đối chiếu tồn kho để đối chiếu giữa tồn kho trên sổ sách và kiểm kê thực tế

Đối chiếu tồn kho là quá trình kiểm đếm và đánh giá hàng tồn kho, được thực hiện định kỳ và vào cuối năm nhằm định giá tổng tồn kho để chuẩn bị cho các báo cáo kế toán. Trong quá trình này, lượng tồn kho thực tế sẽ được kiểm tra và ghi nhận vào hệ thống. Lượng tồn kho thực tế và lượng tồn kho trong hệ thống phải khớp nhau và chính xác. Nếu không khớp, bạn có thể sử dụng công cụ đối chiếu tồn kho để đối chiếu số dư tồn kho và giá trị với thực tế.

Để đối chiếu tồn kho:

1. Đi đến **Kho > Công cụ > Đối chiếu tồn kho > Mới**
1. Thiết lập Ngày hạch toán.
1. Thiết lập Mục đích là Đối chiếu tồn kho.
1. Thiết lập Mã mặt hàng, Kho, Số lượng, và Giá trị tính giá.
1. Chọn một tài khoản chi phí trong Tài khoản chênh lệch.
1. Chọn Trung tâm chi phí.
1. Lưu và Xác nhận.

#3. Các tính năng

##3.1 Tải dữ liệu qua Bảng tính

Nếu bạn có nhiều mặt hàng, bạn có thể tải lên chi tiết thông qua một bảng tính.

1. Tải xuống Mẫu

  Mở một Đối chiếu tồn kho mới và nhấp vào nút Tải xuống để tải mẫu dưới định dạng CSV.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-recon-1.png">

2. Nhập dữ liệu vào mẫu CSV.

  Định dạng CSV có phân biệt chữ hoa chữ thường. Không chỉnh sửa các tiêu đề đã được thiết lập sẵn trong mẫu. Trong cột Mã mặt hàng và Kho, hãy nhập chính xác Mã mặt hàng và Kho đã được tạo trong tài khoản ERPNext của bạn. Đối với số lượng, hãy nhập mức tồn kho mà bạn muốn thiết lập cho mặt hàng đó tại một kho cụ thể.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-reco-data.png">


3. Tải tệp CSV có chứa dữ liệu bằng cách nhấp vào nút 'Tải lên'.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-recon-2.png">


4. Xem lại, Lưu và Xác nhận.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-reco-upload.gif">

5. Kiểm tra Báo cáo Sổ cái kho để xem số dư tồn kho đã được cập nhật.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-reco-ledger.png">

##3.2 Lấy Số dư tồn kho và Giá trị tính giá tại một Ngày và Thời gian cụ thể

Bạn có thể nhập số dư tồn kho và giá trị tính giá tại một ngày và thời gian cụ thể bằng cách nhấp vào nút 'Mặt hàng'. Bạn có thể cập nhật Số lượng và Giá trị tính giá khi cần thiết.

<img class="screenshot" alt="Stock Reconciliation Items Button" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock_reconciliation_items_button.gif">

#4. Cách thức hoạt động của Đối chiếu tồn kho

Khi một phiếu đối chiếu tồn kho được Xác nhận để cập nhật số lượng cho một mặt hàng trong một kho tại một ngày và thời gian cụ thể, nó sẽ không bị thay đổi bởi các giao dịch kho sau đó, ngay cả khi các giao dịch đó có ngày hạch toán trước ngày đối chiếu tồn kho.

Các ví dụ như sau:

##4.1 Đối với các Mặt hàng không có số serial
Xét một mặt hàng có mã 'ABC001' trong kho 'Mumbai'.
Giả sử tồn kho vào ngày 10 tháng 1 là 100 đơn vị.
Việc Đối chiếu tồn kho được thực hiện vào ngày 12 tháng 1 để thiết lập số dư tồn kho thành 150 đơn vị.

Sổ cái kho sẽ hiển thị như sau:
<html>
<style>
    td {
    padding:5px 10px 5px 5px;
    };
    img {
    align:center;
    };
	table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
	}
</style>
 <table border="1" cellspacing="0px">
            <tbody>
                <tr align="center" bgcolor="#EEE">
                    <td><b>Ngày hạch toán</b>
                    </td>
                    <td><b>Số lượng</b>
                    </td>
                    <td><b>Số lượng tồn</b>
                    </td>
                    <td><b>Loại chứng từ</b>
                    </td>
                </tr>
                <tr>
                    <td>10/01/2014</td>
                    <td align="center">100</td>
                    <td>100&nbsp;</td>
                    <td>Phiếu nhập hàng</td>
                </tr>
                <tr>
                    <td>12/01/2014</td>
                    <td align="center">50</td>
                    <td>150</td>
                    <td>Đối chiếu tồn kho</td>
                </tr>
            </tbody>
        </table>
</html>

Nếu một bút toán Phiếu nhập hàng mới được tạo vào ngày 5 tháng 1 năm 2014, trước ngày của Đối chiếu tồn kho...