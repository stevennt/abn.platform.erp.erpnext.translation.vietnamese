<!-- add-breadcrumbs -->
# Ghi đè dữ liệu từ Công cụ Nhập dữ liệu (Data Import Tool)

Công cụ Nhập dữ liệu cho phép nhập các chứng từ (như Khách hàng, Nhà cung cấp, Đơn hàng, Hóa đơn, v.v.) từ tệp Excel/CSV vào ERPNext. Chính công cụ này cũng có thể được sử dụng để ghi đè các giá trị trong các chứng từ hiện có.

Việc ghi đè dữ liệu từ Công cụ Nhập dữ liệu chỉ áp dụng cho các giao dịch đã Lưu, không áp dụng cho các giao dịch đã Xác nhận.

Giả sử chúng ta có một số Mặt hàng cần ghi đè Nhóm mặt hàng. Dưới đây là các bước để ghi đè Nhóm mặt hàng cho các Mặt hàng hiện có.


## Bước 1: Tải xuống Mẫu

Mẫu được sử dụng để ghi đè dữ liệu cũng giống như mẫu được sử dụng để nhập các Mặt hàng mới. Do đó, trước tiên bạn nên tải xuống mẫu.

> Home > Settings > Data > Import/Export Data

Vì các Mặt hàng cần được ghi đè đã có sẵn trong hệ thống, khi tải xuống mẫu, hãy nhấp vào "Download with data" để lấy tất cả các Mặt hàng hiện có trong mẫu.

<img alt="Download Template" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/overwrite-1.gif">

## Bước 2: Chuẩn bị dữ liệu

Nhập giá trị mới vào cột Nhóm mặt hàng cho một Mặt hàng. Vì Nhóm mặt hàng bản thân nó là một dữ liệu danh mục (master), hãy đảm bảo Nhóm mặt hàng được nhập trong tệp bảng tính đã được thêm vào danh mục Nhóm mặt hàng.

<img alt="Update Values" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/overwrite-2.png">

Vì chúng ta chỉ đang ghi đè Nhóm mặt hàng, nên chỉ các cột sau đây là bắt buộc:

1. Cột A (vì nó chứa các giá trị chính của mẫu)
1. Name (Cột B)
1. Item Group

Các cột của các trường khác không gây ảnh hưởng có thể được xóa bỏ, ngay cả khi chúng là bắt buộc. Điều này chỉ áp dụng cho việc ghi đè, không áp dụng khi nhập các bản ghi mới.

## Bước 3: Duyệt Mẫu

Sau khi cập nhật Nhóm mặt hàng trong bảng tính, hãy quay lại Công cụ Nhập dữ liệu trong ERPNext. Duyệt và chọn Tệp/mẫu có chứa dữ liệu cần được ghi đè.

<img alt="Browse template" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/overwrite-3.gif">

## Bước 4: Tải lên

Sau khi nhấp vào Import, Nhóm mặt hàng sẽ được ghi đè.

<img alt="Upload" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/overwrite-4.png">

Nếu việc kiểm tra giá trị thất bại, hệ thống sẽ chỉ ra số hàng của bảng tính mà việc kiểm tra bị lỗi và cần được sửa đổi. Trong trường hợp đó, bạn nên sửa giá trị ở hàng đó trong bảng tính, sau đó nhập lại chính tệp đó. Nếu việc kiểm tra thất bại dù chỉ ở một hàng, không có bản ghi nào được nhập/ghi đè.