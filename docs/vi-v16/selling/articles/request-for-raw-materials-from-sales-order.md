<!-- add-breadcrumbs -->
# Yêu cầu vật tư từ Đơn bán hàng

Kế hoạch sản xuất giúp người dùng lập kế hoạch sản xuất dựa trên nhiều Đơn bán hàng và hỗ trợ lập kế hoạch mua sắm vật tư cho các Mặt hàng nguyên vật liệu, dựa trên số lượng thành phẩm cần sản xuất.

Tuy nhiên, khi bạn chỉ cần lập kế hoạch cho các Mặt hàng nguyên vật liệu của một Đơn bán hàng duy nhất, công việc này trở nên khá tẻ nhạt. Do đó, bạn có thể tạo một Yêu cầu vật tư cho các nguyên vật liệu của các Thành phẩm có trong Đơn bán hàng ngay từ chính Đơn bán hàng đó.

Trong phiên bản v16, quy trình này được tối ưu hóa với tính năng **Stock Reservation** (Giữ hàng tồn kho) và các nút điều hướng nhanh từ form Khách hàng.

Để thực hiện, bạn có thể làm theo các bước dưới đây.

* Sau khi Đơn bán hàng của bạn đã được **Xác nhận**, hãy nhấp vào **Make** và chọn **Request for Raw Materials**.

![Request For Raw Materials](https://docs.erpnext.com/docs/v16/assets/img/selling/request-for-raw-materials.png)

* Một hộp thoại sẽ mở ra và hiển thị tất cả các Thành phẩm có BOM.

![Request For Raw Materials Dialog](https://docs.erpnext.com/docs/v16/assets/img/selling/request-for-raw-materials-dialog.png)

* Tại đây, bạn có thể thay đổi BOM theo ý muốn và chọn các tùy chọn cần thiết.

Giả sử, việc bật **Include Exploded Items** sẽ lấy các Nguyên vật liệu từ các Thành phần chi tiết (Exploded Items) của BOM, và việc bật **Ignore Existing Ordered Qty** sẽ tạo một Yêu cầu ngay cả khi số lượng cần thiết đã có sẵn.

* Nhấp vào **Make**, và Yêu cầu vật tư của bạn sẽ được tạo.

![Submitted Material Request](https://docs.erpnext.com/docs/v16/assets/img/selling/material-request-submitted.png)

Yêu cầu vật tư được tạo cho Nguyên vật liệu của Thành phẩm có trong Đơn bán hàng.

![Material Request](https://docs.erpnext.com/docs/v16/assets/img/selling/created-mr-from-sales-order.png)

**Lưu ý mới trong v16:**
* **Stock Reservation:** Bạn có thể thực hiện giữ hàng trong kho ngay khi tạo yêu cầu để đảm bảo vật tư luôn sẵn sàng cho kế hoạch sản xuất.
* **Cutoff date cho DN:** Khi tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO), hệ thống sẽ áp dụng ngày chốt (cutoff date) để kiểm soát chính xác thời điểm xuất kho.
* **Truy cập nhanh:** Từ form Khách hàng, bạn có thể sử dụng các nút bấm nhanh để tạo trực tiếp SO hoặc Báo giá (Quotation).

{next}