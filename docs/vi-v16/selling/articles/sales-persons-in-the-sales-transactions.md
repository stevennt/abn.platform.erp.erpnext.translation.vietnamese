<!-- add-breadcrumbs -->
# Nhân viên bán hàng trong các giao dịch bán hàng

Trong ERPNext, danh mục Nhân viên bán hàng được quản lý theo [cấu trúc cây](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/articles/managing-tree-structure-masters.html). Nhân viên bán hàng có thể được lựa chọn trong tất cả các giao dịch bán hàng.

Nhân viên bán hàng cũng có thể được cập nhật trong danh mục Khách hàng. Khi chọn Khách hàng trong các giao dịch, các Nhân viên bán hàng đã được cập nhật trong Khách hàng sẽ được tự động lấy vào giao dịch bán hàng.

Ngoài ra, trong phiên bản v16, tại giao diện Khách hàng, bạn có thể truy cập nhanh các nút **Đơn bán hàng** hoặc **Báo giá** để xem lịch sử giao dịch của khách hàng đó.

<img class="screenshot" alt="Sales Person Customer" src="https://docs.erpnext.com/docs/v16/assets/img/selling/sales-person-in-customer.png">

#### Mức đóng góp của Nhân viên bán hàng

Nếu có nhiều nhân viên bán hàng cùng làm việc trên một đơn hàng, thì mức đóng góp (%) cần được thiết lập cho mỗi Nhân viên bán hàng.

<img class="screenshot" alt="Sales Person Order" src="https://docs.erpnext.com/docs/v16/assets/img/selling/sales-person-in-sales-order.png">

Khi Lưu giao dịch, dựa trên Tổng ròng và mức Đóng góp (%), `Mức đóng góp vào Tổng ròng` sẽ được tính toán cho mỗi Nhân viên bán hàng.

<div class=well>Tổng % Đóng góp cho tất cả Nhân viên bán hàng phải là 100%. Nếu chỉ có một Nhân viên bán hàng được chọn, thì % Đóng góp sẽ là 100.</div>

**Lưu ý về Giữ hàng (Stock Reservation):** Trong phiên bản v16, khi thực hiện các giao dịch bán hàng, hệ thống hỗ trợ tính năng Giữ hàng (Stock Reservation) để đảm bảo các mặt hàng đã được cam kết cho khách hàng sẽ được giữ lại trong kho, tránh việc xuất kho cho các đơn hàng khác.

#### Báo cáo giao dịch theo Nhân viên bán hàng

Kiểm tra báo cáo giao dịch của Nhân viên bán hàng tại:

`Bán hàng > Báo cáo tiêu chuẩn > Tóm tắt giao dịch theo Nhân viên bán hàng`

Báo cáo này có thể được tạo dựa trên Đơn bán hàng, Phiếu giao hàng và Hóa đơn bán hàng. Nó sẽ cho bạn biết tổng số tiền bán hàng được thực hiện bởi một nhân viên.

**Lưu ý về Ngày chốt (Cutoff date):** Đối với Phiếu giao hàng (DN) được tạo từ Đơn bán hàng (SO), hệ thống v16 cho phép quản lý chặt chẽ hơn thông qua ngày chốt (Cutoff date) để đảm bảo tính chính xác của dữ liệu tồn kho và doanh thu tại thời điểm giao hàng.

<img class="screenshot" alt="Sales Person Report" src="https://docs.erpnext.com/docs/v16/assets/img/selling/sales-person-wise-transaction-summary-report.png">

#### Hoa hồng theo Nhân viên bán hàng

ERPNext chỉ cung cấp tổng số tiền bán hàng được thực hiện bởi một Nhân viên bán hàng. Nếu bạn có chính sách hoa hồng cho Nhân viên bán hàng, bạn nên thêm Nhân viên bán hàng dưới vai trò là Đối tác bán hàng trong ERPNext. Đối với Đối tác bán hàng, bạn có thể xác định % Hoa hồng. Khi chọn Đối tác bán hàng trong một giao dịch bán hàng, dựa trên Tổng ròng, Số tiền hoa hồng cũng sẽ được tính toán. Bạn có thể kiểm tra báo cáo hoa hồng của Đối tác bán hàng tại:

`Kế toán > Báo cáo tiêu chuẩn > Hoa hồng Đối tác bán hàng`

{next}