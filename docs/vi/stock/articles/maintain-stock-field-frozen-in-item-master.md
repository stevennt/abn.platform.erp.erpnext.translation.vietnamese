<!-- add-breadcrumbs -->
#Trường Duy trì tồn kho bị khóa trong Danh mục mặt hàng

Trong danh mục mặt hàng, bạn có thể thấy giá trị trong các trường sau đây bị khóa.

1. Duy trì tồn kho
1. Có số lô
1. Có số serial

<img alt="Item Field Frozen" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/maintain-stock-1.png">

Đối với một mặt hàng, một khi bút toán sổ kho đã được tạo, giá trị trong các trường này sẽ bị khóa. Điều này nhằm ngăn chặn người dùng thay đổi giá trị, điều có thể dẫn đến sự sai lệch giữa tồn kho thực tế và mức tồn kho của mặt hàng trong hệ thống.

Đối với mặt hàng có số serial, vì mức tồn kho được tính toán dựa trên số lượng các Số serial hiện có, việc chuyển Mặt hàng thành không có số serial giữa chừng sẽ làm mất tính đồng bộ, và mức tồn kho của mặt hàng hiển thị trong báo cáo sẽ không chính xác, do đó trường Có số serial bị khóa.

Để có thể chỉnh sửa các trường này một lần nữa, bạn nên xóa tất cả các giao dịch kho đã thực hiện cho mặt hàng này. Đối với Mặt hàng có số serial và số lô, bạn cũng nên xóa các bản ghi Số serial và Số lô của mặt hàng này.

<!-- markdown -->