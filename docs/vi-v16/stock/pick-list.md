---
title: Danh sách lấy hàng
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Danh sách lấy hàng là một chứng từ cho biết những mặt hàng nào cần được lấy từ kho để hoàn tất các đơn hàng. Điều này đặc biệt hữu ích cho các đơn vị vận chuyển có lượng tồn kho lớn, khối lượng đơn hàng lớn hoặc khách hàng đặt nhiều Đơn vị lưu kho (SKU).
 keywords: Pick List, Picking Slip, frappe, Pick Ticket, erpnext new features, erp, open source erp, free erp, stock
---

# Danh sách lấy hàng

**Danh sách lấy hàng là một chứng từ cho biết những mặt hàng nào cần được lấy từ kho để hoàn tất các đơn hàng.**

Điều này đặc biệt hữu ích cho các đơn vị vận chuyển có lượng tồn kho lớn, khối lượng đơn hàng lớn hoặc khách hàng đặt nhiều Đơn vị lưu kho (SKU). 

Trong phiên bản v16, hệ thống được cải tiến với **Hệ thống Giữ hàng (Stock Reservation System)** giúp việc lập danh sách lấy hàng trở nên chính xác hơn, đảm bảo hàng hóa đã được giữ cho các đơn hàng cụ thể, tránh tình trạng thiếu hụt khi thực hiện lấy hàng thực tế.

Danh sách lấy hàng sẽ chọn Kho nơi có sẵn Mặt hàng theo nguyên tắc FIFO (Nhập trước - Xuất trước). Đối với các mặt hàng theo Lô hàng, hệ thống sẽ ưu tiên chọn Kho có Lô hàng gần đến hạn hết hạn nhất.

Để truy cập Danh sách lấy hàng, hãy đi tới:

> Trang chủ > Kho > Giao dịch kho > Danh sách lấy hàng

## 1. Điều kiện tiên quyết

Trước khi tạo và sử dụng Danh sách lấy hàng, bạn nên tạo các mục sau trước:

- [Mặt hàng](item.md)
- [Kho](warehouse.md)

## 2. Cách tạo Danh sách lấy hàng

1. Đi tới danh sách Danh sách lấy hàng, nhấn vào **Mới**.
 <img class='screenshot' alt='Unsaved Pick List' src='https://docs.erpnext.com/docs/v16/assets/img/stock/pick-list-unsaved-doc.png'>

1. Thiết lập Công ty.
1. Chọn Mục đích của Danh sách lấy hàng. Các tùy chọn bao gồm:

   - **Giao hàng:** Cho phép thêm Mặt hàng từ một Đơn bán hàng để giao. Sau khi **Xác nhận** Danh sách lấy hàng, một **Phiếu giao hàng** mới có thể được tạo dựa trên Kho mà các mặt hàng đã được lấy.

   - **Chuyển vật tư để sản xuất:** Cho phép chọn một Lệnh sản xuất để lấy nguyên vật liệu. Bạn sẽ chọn số lượng thành phẩm muốn sản xuất để hệ thống tính toán nguyên vật liệu cần thiết. Sau khi lấy kho, bạn có thể tạo **Phiếu kho** cho các mặt hàng đã lấy.

   - **Chuyển vật tư:** Cho phép chọn một **Yêu cầu vật tư** để lấy các mặt hàng. Sau khi lấy kho, bạn có thể tạo **Phiếu kho** cho các mặt hàng đã lấy.

1. Thêm Mặt hàng và số lượng bạn muốn lấy vào bảng Vị trí mặt hàng. Nhấn vào **Lấy vị trí mặt hàng** để hệ thống tự động đề xuất Kho và các chi tiết khác cho mỗi Mặt hàng.

1. **Kho cha:** Nếu một Kho cha được chọn, chỉ những Kho thuộc Kho cha đó mới được đề xuất.

1. **Lấy vị trí mặt hàng:** Sau khi các mặt hàng cần lấy đã được chốt, bạn có thể nhấn vào nút **Lấy vị trí mặt hàng** để lấy lựa chọn Kho cho từng mặt hàng. Tính năng này cũng giúp kiểm tra tính khả dụng của hàng hóa dựa trên dữ liệu tồn kho thực tế và các lệnh giữ hàng hiện có.

1. **Vị trí mặt hàng:** Phần này cung cấp thông tin về vị trí mặt hàng (Kho), Số serial cho các mặt hàng có số serial và số lô cho các mặt hàng theo **Lô hàng**.
 <img class='screenshot' alt='Item Locations' src='https://docs.erpnext.com/docs/v16/assets/img/stock/pick-list-item-locations.png'>

 Nếu có liên quan đến Số serial, dòng Mặt hàng sẽ hiển thị chi tiết số serial cụ thể:
 <img class='screenshot' alt='Item Location Detail' src='https://docs.erpnext.com/docs/v16/assets/img/stock/pick-list-item-location-detail.png'>

1. **Lưu** và **Xác nhận**.
 <img class='screenshot' alt='Submitted Pick List' src='https://docs.erpnext.com/docs/v16/assets/img/stock/pick-list-submitted-doc.png'>

### 2.1 Tạo Danh sách lấy hàng từ Đơn bán hàng

1. Đi tới [Đơn bán hàng](../selling/sales-order.md).
1. Nhấn vào nút **Tạo** ở góc trên bên phải và chọn **Danh sách lấy hàng**.
1. Toàn bộ dữ liệu cần thiết sẽ được lấy từ Đơn bán hàng sang.
1. Kiểm tra Bảng Vị trí mặt hàng với Kho đã được đề xuất.
1. **Lưu** chứng từ.
1. **Xác nhận** chứng từ sau khi việc lấy hàng thực tế hoàn tất và số lượng thực lấy đã được cập nhật.

**Mẹo:** Bạn có thể tạo một Danh sách lấy hàng cho nhiều Đơn bán hàng từ cùng một Khách hàng bằng cách nhấn vào **Lấy các mặt hàng** và chọn các Đơn bán hàng liên quan.

> **Lưu ý:**
>
> - Danh sách lấy hàng chỉ có thể được tạo cho các Đơn bán hàng còn các Mặt hàng đang chờ giao.
> - Một **Phiếu giao hàng** chỉ có thể được tạo nếu Danh sách lấy hàng đã được **Xác nhận**.

### 2.2 Tạo Danh sách lấy hàng từ Lệnh sản xuất

1. Đi tới [Lệnh sản xuất](https://docs.erpnext.com/docs/v16/user/manual/en/manufacturing/work-order).
1. Nhấn nút **Tạo Danh sách lấy hàng**.
1. Nhập số lượng Mặt hàng thành phẩm cần sản xuất để hệ thống tính toán lượng nguyên vật liệu cần lấy.
<img class='screenshot' alt='Dialog For qty' src='https://docs.erpnext.com/docs/v16/assets/img/stock/pick-list-dialog-for-qty.png'>

1. Kiểm tra bảng Vị trí mặt hàng với các Kho nguyên vật liệu đã được đề xuất.
1. **Lưu** chứng từ và chuyển cho nhân viên kho.
1. **Xác nhận** chứng từ sau khi việc lấy hàng hoàn tất.

> **Lưu ý:**
>
> - Danh sách lấy hàng chỉ có thể được tạo cho các Lệnh sản xuất đang ở trạng thái 'Chưa bắt đầu' hoặc 'Đang tiến hành'.
> - Một **Phiếu kho** chỉ có thể được tạo sau khi Danh sách lấy hàng đã được **Xác nhận**.

### 2.3 Tạo Danh sách lấy hàng từ Yêu cầu vật tư

1. Đi tới [Yêu cầu vật tư](material-request.md).
1. Nhấn vào nút **Tạo** và chọn **Danh sách lấy hàng**.
1. Hệ thống sẽ tự động hiển thị bảng Vị trí mặt hàng với Kho được đề xuất cho các mặt hàng trong **Yêu cầu vật tư**.