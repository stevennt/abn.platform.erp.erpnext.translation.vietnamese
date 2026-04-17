<!-- add-breadcrumbs -->
# Số lượng dự kiến

**Số lượng dự kiến là mức tồn kho được dự báo cho một Mặt hàng cụ thể dựa trên mức tồn kho hiện tại và các yêu cầu khác.**

Đây là số lượng tồn kho tổng thể bao gồm cả cung và cầu trong tương lai, được thực hiện như một phần của quy trình lập kế hoạch.

Tồn kho dự kiến được hệ thống lập kế hoạch sử dụng để theo dõi điểm đặt hàng lại và xác định số lượng đặt hàng lại. Số lượng dự kiến cũng được công cụ lập kế hoạch sử dụng để theo dõi mức tồn kho an toàn. Các mức này được duy trì để phục vụ các nhu cầu bất ngờ.

Việc kiểm soát chặt chẽ tồn kho dự kiến là rất quan trọng để xác định tình trạng thiếu hụt và tính toán đúng số lượng đặt hàng. Ngoài ra, với phiên bản v16, hệ thống còn hỗ trợ **Hệ thống giữ hàng tồn kho (Stock Reservation System)** giúp việc dự báo chính xác hơn dựa trên các yêu cầu đã được giữ chỗ.

<img class="screenshot" alt="Projected Quantity" src="https://docs.erpnext.com/docs/v16/assets/img/stock/projected_quantity.png">

Công thức để tính số lượng dự kiến như sau:

*Số lượng dự kiến = Số lượng thực tế + Số lượng kế hoạch + Số lượng yêu cầu + Số lượng đã đặt - Số lượng đã giữ - Số lượng đã giữ cho Sản xuất - Số lượng đã giữ cho Gia công ngoài*

* **Số lượng thực tế**: Số lượng hiện có trong Kho. Đây là lượng tồn kho vật lý thực tế mà bạn đang có.
* **Số lượng kế hoạch**: Số lượng mà Lệnh sản xuất đã được lập, nhưng đang chờ để được sản xuất.
* **Số lượng yêu cầu**: Số lượng được yêu cầu thông qua [Yêu cầu vật tư](material-request.md). Số lượng này được cộng vào khi Xác nhận Yêu cầu vật tư và được trừ đi khi Đơn mua hàng/Lệnh sản xuất/Phiếu kho được tạo dựa trên loại Yêu cầu vật tư.
* **Số lượng đã đặt**: Số lượng đã đặt mua ([Đơn mua hàng](../buying/purchase-order.md)), nhưng chưa được nhận (thông qua [Phiếu nhập hàng](purchase-receipt.md) hoặc [Hóa đơn mua hàng](../accounts/purchase-invoice.md)).
* **Số lượng đã giữ**: Số lượng đã đặt để bán bởi Khách hàng của bạn ([Đơn bán hàng](../selling/sales-order.md)), nhưng chưa được giao (thông qua [Phiếu giao hàng](delivery-note.md)). Số lượng này tăng lên khi Đơn bán hàng được Xác nhận và giảm đi khi Phiếu giao hàng hoặc Hóa đơn bán hàng được tạo dựa trên Đơn bán hàng đó được Xác nhận.
* **Số lượng đã giữ cho Sản xuất**: Nguyên vật liệu được giữ lại khi Xác nhận [Lệnh sản xuất](manufacturing/work-order.md) và giảm đi khi nguyên vật liệu được chuyển đến kho Bán thành phẩm thông qua một Phiếu kho.
* **Số lượng đã giữ cho Gia công ngoài**: Nguyên vật liệu được giữ lại khi Xác nhận Đơn mua hàng gia công ngoài. Khi nguyên vật liệu được chuyển đến Kho của Nhà cung cấp thông qua một Phiếu kho, số lượng này sẽ giảm xuống. Để biết thêm về gia công ngoài [nhấp vào đây](manufacturing/subcontracting.md).

#### Các chủ đề liên quan
1. [Kho](warehouse.md)
1. [Yêu cầu vật tư](material-request.md)