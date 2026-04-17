<!-- add-breadcrumbs -->
# Báo cáo Tồn kho

Báo cáo Tồn kho liệt kê số lượng mặt hàng hiện có trong một kho cụ thể.

Có nhiều báo cáo khác nhau mà bạn có thể kiểm tra mức tồn kho của mặt hàng.

#### Báo cáo Số lượng dự kiến tồn kho

Bạn có thể truy cập báo cáo này từ `Kho > Báo cáo chính > Số lượng dự kiến tồn kho`

Báo cáo này liệt kê mức tồn kho của mặt hàng theo từng mặt hàng - từng kho dựa trên tất cả các giao dịch kho. Cùng với Số lượng thực tế của một mặt hàng, nó cũng cung cấp các chi tiết khác như:

1. **Số lượng thực tế**: Số lượng hiện có trong kho.
2. **Số lượng dự kiến (Sản xuất)**: Số lượng đã được tạo Lệnh sản xuất nhưng đang chờ sản xuất.
3. **Số lượng yêu cầu**: Số lượng đã yêu cầu mua nhưng chưa đặt hàng.
4. **Số lượng đã đặt**: Số lượng đã đặt mua nhưng chưa nhận hàng.
5. **Số lượng đã đặt trước**: Số lượng đã đặt bán nhưng chưa giao.
6. **Số lượng dự kiến (Tổng hợp)**: Số lượng dự kiến được tính như sau:

<div class="well">Số lượng dự kiến = Số lượng thực tế + Số lượng dự kiến (Sản xuất) + Số lượng yêu cầu + Số lượng đã đặt - Số lượng đã đặt trước</div>

Tồn kho dự kiến được hệ thống lập kế hoạch sử dụng để theo dõi điểm đặt hàng lại và xác định số lượng đặt hàng lại. Số lượng dự kiến được công cụ lập kế hoạch sử dụng để theo dõi mức tồn kho an toàn. Các mức này được duy trì để đáp ứng các nhu cầu bất ngờ.

Việc kiểm soát chặt chẽ tồn kho dự kiến là rất quan trọng để xác định tình trạng thiếu hụt và tính toán đúng số lượng đặt hàng.

#### Các tính năng mới trong v16

Trong phiên bản v16, hệ thống quản lý tồn kho đã được nâng cấp mạnh mẽ với các tính năng sau:

* **Hệ thống Giữ chỗ Tồn kho (Stock Reservation System):** Cho phép giữ chỗ số lượng mặt hàng cho các Đơn bán hàng (SO) hoặc Lệnh sản xuất cụ thể, giúp ngăn chặn việc thiếu hụt hàng hóa khi có nhiều đơn hàng cùng lúc.
* **Báo cáo Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability Report):** Cung cấp khả năng theo dõi chi tiết lịch sử di chuyển của từng Lô hàng (Batch) hoặc Số Serial từ khi nhập kho cho đến khi xuất kho, giúp kiểm soát chất lượng và truy xuất nguồn gốc nhanh chóng.
* **Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry):** Cho phép phân bổ các chi phí liên quan (như phí vận chuyển, thuế nhập khẩu) trực tiếp vào giá trị của mặt hàng khi thực hiện Phiếu nhập hàng hoặc Phiếu kho, giúp phản ánh chính xác giá trị tồn kho.
* **Kế toán tồn kho theo từng mặt hàng (Item-Level Stock Accounting):** Tự động hóa việc ghi nhận các bút toán kế toán chi tiết cho từng mặt hàng dựa trên giá trị nhập kho, giúp việc đối soát giữa sổ cái và kho chính xác hơn.
* **Xem trước Sổ cái (Ledger Preview):** Cho phép người dùng xem nhanh các bút toán liên quan trực tiếp từ giao diện quản lý tồn kho mà không cần chuyển sang phân hệ Kế toán.