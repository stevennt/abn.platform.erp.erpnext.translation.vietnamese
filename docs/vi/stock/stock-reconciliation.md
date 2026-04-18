<!-- add-breadcrumbs -->
# Đối chiếu tồn kho

**Đối chiếu tồn kho là quá trình kiểm đếm và đánh giá vật tư/sản phẩm, được thực hiện định kỳ vào cuối năm.**

Việc này được thực hiện nhằm mục đích:

* Giữ cho số lượng kiểm kê thực tế và số lượng trên sổ sách đồng bộ với nhau
* Định giá tồn kho để chuẩn bị cho các báo cáo kế toán

Tính năng Đối chiếu tồn kho trong ERPNext được sử dụng để:

* Hạch toán tồn kho đầu kỳ
* Đối chiếu giữa số lượng trên sổ sách và số lượng thực tế

Để truy cập danh sách Đối chiếu tồn kho, hãy đi tới:
> Home > Stock > Tools > Stock Reconciliation

## 1. Cách tạo Đối chiếu tồn kho để hạch toán tồn kho đầu kỳ

Sử dụng đối chiếu tồn kho, bạn có thể cập nhật số lượng của các mặt hàng cụ thể trong một kho tại một thời điểm cụ thể.
Bạn cũng có thể thêm các Mặt hàng có Số serial hoặc Số lô vào kho.

1. Đi tới danh sách Đối chiếu tồn kho, nhấn vào New.
1. Chọn Mục đích (Purpose) là 'Opening Stock'. Bạn có thể chỉnh sửa Ngày và Giờ hạch toán.
1. Chọn Mã mặt hàng (Item Code), Kho (Warehouse), Số lượng (Quantity), và Giá trị tính giá (Valuation Rate). Nếu có liên quan đến Số serial / Số lô, hãy thêm vào.
1. Nếu bạn muốn tự động tạo Số serial / Số lô, hãy để trống các trường đó.
    * Để tự động tạo Số serial, bạn cần thiết lập "Serial Number Series" trong danh mục Mặt hàng.
    * Để tự động tạo Số lô, bạn cần bật ô "Automatically Create New Batch" trong danh mục Mặt hàng.
1. Tài khoản chênh lệch (Difference Account) sẽ được thiết lập là 'Temporary Opening'.
1. Lưu và Xác nhận.

    ![Opening Stock](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/opening_stock.png)

> Lưu ý: Tùy chọn Duy trì tồn kho (Maintain Stock) phải được bật trong danh mục Mặt hàng để tính năng này hoạt động.

## 2. Cách tạo Đối chiếu tồn kho để đối chiếu số lượng trên sổ sách và kiểm kê thực tế

Đối chiếu tồn kho là quá trình kiểm đếm và đánh giá hàng tồn kho, được thực hiện định kỳ và vào cuối năm nhằm định giá tổng tồn kho để chuẩn bị các báo cáo kế toán. Trong quá trình này, lượng hàng thực tế sẽ được kiểm tra và ghi nhận vào hệ thống. Lượng hàng thực tế và lượng hàng trên hệ thống phải khớp nhau và chính xác. Nếu không khớp, bạn có thể sử dụng công cụ Đối chiếu tồn kho để đối chiếu số dư tồn kho và giá trị với thực tế.

Để đối chiếu tồn kho:

1. Đi tới danh sách Đối chiếu tồn kho, nhấn vào New
1. Chọn Mục đích (Purpose) là 'Stock Reconciliation'. Bạn có thể chỉnh sửa Ngày và Giờ hạch toán.
1. Thiết lập Mã mặt hàng (Item Code), Kho (Warehouse).
1. Số lượng và Giá trị tính giá hiện tại sẽ được lấy ra, hãy thay đổi số lượng nếu cần.
1. Tài khoản chi phí trong Tài khoản chênh lệch (Difference Account) sẽ được mặc định là 'Stock Adjustment'.
1. Trung tâm chi phí (Cost Center) mặc định sẽ là 'Main', thay đổi nếu cần.
1. Lưu và Xác nhận.

    ![Stock Reconciliation](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock_recon.png)


## 3. Các tính năng

### 3.1 Tải dữ liệu qua Bảng tính

Nếu bạn có nhiều mặt hàng, bạn có thể tải lên chi tiết thông qua một bảng tính.

1. Tải xuống Mẫu (Template)

  Mở một Đối chiếu tồn kho mới và nhấn vào nút Download để tải xuống mẫu dưới định dạng CSV.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-recon-1.png">

2. Nhập dữ liệu vào mẫu CSV.

  Định dạng CSV có phân biệt chữ hoa chữ thường. Không chỉnh sửa các tiêu đề đã được thiết lập sẵn trong mẫu. Trong cột Mã mặt hàng (Item Code) và Kho (Warehouse), hãy nhập chính xác Mã mặt hàng và Kho đã được tạo trong tài khoản ERPNext của bạn. Đối với số lượng, hãy nhập mức tồn kho mà bạn muốn thiết lập cho mặt hàng đó tại một kho cụ thể.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-reco-data.png">


3. Tải tệp CSV có chứa dữ liệu lên bằng cách nhấn vào nút 'Upload'.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-recon-2.png">


4. Xem lại, Lưu và Xác nhận.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-reco-upload.gif">

5. Kiểm tra Báo cáo Sổ cái kho (Stock Ledger Report) để xem số dư tồn kho đã được cập nhật.

  <img class="screenshot" alt="Stock Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock-reco-ledger.png">

### 3.2 Lấy Số dư tồn kho và Giá trị tính giá tại một Ngày và Giờ cụ thể

Bạn có thể nhập số dư tồn kho và giá trị tính giá tại một ngày và giờ cụ thể từ một Kho được chọn bằng cách nhấn vào nút **Items**. Bạn có thể cập nhật Số lượng và Giá trị tính giá khi cần thiết.

<img class="screenshot" alt="Stock Reconciliation Items Button" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/stock_reconciliation_items_button.gif">

## 4. Cách thức hoạt động của Đối chiếu tồn kho

Một khi phiếu Đối chiếu tồn kho được Xác nhận để cập nhật số lượng tại một ngày và giờ cụ thể cho một mặt hàng trong kho, nó sẽ không bị thay đổi bởi các giao dịch kho sau đó, ngay cả khi các giao dịch đó có ngày hạch toán trước ngày đối chiếu tồn kho. Nói cách khác, các bút toán lùi ngày sẽ không làm thay đổi số lượng tồn kho sau khi một bút toán Đối chiếu tồn kho đã được Xác nhận.

Các ví dụ như sau.

### 4.1 Đối với các Mặt hàng không có số serial
Xét một mặt hàng có mã 'ABC001' trong kho 'Mumbai'.
Giả sử tồn kho vào ngày 10 tháng 1 là 100 đơn vị.
Việc Đối chiếu tồn kho được thực hiện vào ngày 12 tháng 1 để thiết lập số dư tồn kho thành 150 đơn vị.

Sổ cái kho (Stock Ledger) sẽ hiển thị như sau:
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
                    <td>12/01/2014<