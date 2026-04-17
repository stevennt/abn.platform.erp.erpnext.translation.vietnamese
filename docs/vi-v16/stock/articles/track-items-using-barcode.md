<!-- add-breadcrumbs -->
# Theo dõi Mặt hàng bằng Mã vạch

Mã vạch là một giá trị được giải mã thành các đường kẻ dọc cách nhau. Máy quét mã vạch là thiết bị nhập liệu, tương tự như bàn phím. Khi quét một mã vạch, dữ liệu sẽ xuất hiện trên màn hình máy tính tại vị trí của con trỏ.

## Danh mục Mặt hàng

Để thiết lập mã vạch cho một mặt hàng cụ thể, bạn cần mở bản ghi Mặt hàng. Bạn cũng có thể nhập mã vạch trong khi tạo một Mặt hàng mới.

<img alt="Material Transfer" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/barcode-item-master.png">

Sau khi trường mã vạch được cập nhật trong danh mục Mặt hàng, các Mặt hàng có thể được truy xuất bằng mã vạch. Tính năng này sẽ khả dụng trong các giao dịch Phiếu giao hàng, Đơn bán hàng, Hóa đơn, Phiếu nhập hàng và Đối chiếu tồn kho.

<img alt="Material Transfer" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/barcode-item-selection.gif">

## Quản lý Tồn kho và Truy xuất nguồn gốc (Mới trong v16)

Trong phiên bản v16, việc sử dụng mã vạch kết hợp với quản lý Lô hàng (Batch) và Số sê-ri (Serial) đã được nâng cấp mạnh mẽ:

*   **Hệ thống Giữ hàng (Stock Reservation System):** Sử dụng mã vạch để xác nhận nhanh các Mặt hàng đã được giữ chỗ cho các Đơn bán hàng (SO), giúp tối ưu hóa quy trình đóng gói.
*   **Báo cáo Truy xuất Số sê-ri/Lô hàng (Serial/Batch Traceability Report):** Cho phép quét mã vạch để truy xuất toàn bộ lịch sử di chuyển của một Lô hàng hoặc Số sê-ri cụ thể từ khi nhập kho (PR) cho đến khi xuất kho (DN).
*   **Kế toán Tồn kho theo từng Mặt hàng (Item-Level Stock Accounting):** Mã vạch giúp đảm bảo việc ghi nhận giá trị tồn kho chính xác đến từng đơn vị sản phẩm khi thực hiện các giao dịch Phiếu kho (SE).
*   **Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry):** Khi quét mã vạch để nhập hàng, người dùng có thể dễ dàng phân bổ chi phí vận chuyển, thuế vào giá trị của Mặt hàng ngay tại thời điểm nhập.

## Sử dụng điện thoại di động / điện thoại thông minh để quét và thêm mặt hàng

Sau khi tải ứng dụng ERPNext từ [Google Play Store](https://play.google.com/store/apps/details?id=io.frappe.mobile&hl=en) hoặc [Apple App Store](https://apps.apple.com/us/app/erpnext/id1027318091).

Đăng nhập vào tài khoản ERPNext của bạn, đi đến danh mục Mặt hàng và bạn sẽ có thể quét mã vạch và thêm Mặt hàng ngay từ điện thoại thông minh của mình!

![Item Barcode using Smartphone](https://docs.erpnext.com/docs/v16/assets/img/articles/item-barcode-phone.gif)