<!-- add-breadcrumbs -->
# Trường Duy trì tồn kho bị khóa trong Danh mục mặt hàng

Trong Danh mục mặt hàng, bạn có thể thấy giá trị trong các trường sau đây bị khóa (không thể chỉnh sửa):

1. Duy trì tồn kho
2. Có số lô
3. Có số serial

<img alt="Item Field Frozen" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/maintain-stock-1.png">

Đối với một Mặt hàng, một khi bút toán sổ kho (Ledger) đã được tạo, giá trị trong các trường này sẽ bị khóa. Điều này nhằm ngăn chặn người dùng thay đổi các thiết lập quan trọng, tránh gây ra sự sai lệch giữa tồn kho thực tế và số liệu tồn kho của Mặt hàng trong hệ thống.

Đối với Mặt hàng có số serial, vì mức tồn kho được tính toán dựa trên số lượng các Số serial hiện có, việc chuyển Mặt hàng thành "Không có số serial" giữa chừng sẽ làm mất tính đồng bộ, khiến mức tồn kho hiển thị trong các báo cáo không còn chính xác. Do đó, trường **Có số serial** sẽ bị khóa.

Ngoài ra, với các cập nhật mới trong phiên bản v16, việc quản lý tồn kho trở nên chặt chẽ hơn với các tính năng như:
* **Hệ thống Giữ hàng (Stock Reservation System):** Đảm bảo tính chính xác của tồn kho khả dụng.
* **Báo cáo Truy xuất nguồn gốc Số lô/Số serial (Serial/Batch Traceability Report):** Theo dõi chi tiết lịch sử di chuyển của hàng hóa.
* **Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry):** Tối ưu hóa giá trị tồn kho.
* **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Đồng bộ hóa chính xác giữa kho và sổ cái.

Để có thể chỉnh sửa các trường này một lần nữa, bạn cần phải xóa tất cả các giao dịch kho (Phiếu nhập hàng, Phiếu giao hàng, Phiếu kho,...) đã thực hiện cho Mặt hàng này. Đối với Mặt hàng có số serial và số lô, bạn cũng cần phải xóa các bản ghi Số serial và Số lô liên quan của Mặt hàng đó.