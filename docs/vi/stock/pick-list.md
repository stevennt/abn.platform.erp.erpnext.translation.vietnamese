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
Danh sách lấy hàng sẽ chọn Kho nơi có sẵn Mặt hàng theo nguyên tắc FIFO (Nhập trước - Xuất trước).
Việc lựa chọn Kho đối với mặt hàng theo lô sẽ khác. Trong trường hợp các mặt hàng theo lô, Kho có lô hàng gần đến hạn hết hạn nhất sẽ được lựa chọn.

Để truy cập Danh sách lấy hàng, hãy đi tới:

> Trang chủ > Kho > Giao dịch kho > Danh sách lấy hàng

## 1. Điều kiện tiên quyết

Trước khi tạo và sử dụng Danh sách lấy hàng, bạn nên tạo các mục sau trước:

- [Mặt hàng kho](item.md)
- [Kho](warehouse.md)

## 2. Cách tạo Danh sách lấy hàng

1. Đi tới danh sách Danh sách lấy hàng, nhấn vào Mới.
 <img class='screenshot' alt='Unsaved Pick List' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/pick-list-unsaved-doc.png'>

1. Thiết lập Công ty.
1. Chọn Mục đích của Danh sách lấy hàng. Đây là các tùy chọn trong Mục đích:

   - **Giao hàng:** Tùy chọn này cho phép bạn thêm các Mặt hàng từ một Đơn bán hàng để giao. Sau khi Xác nhận Danh sách lấy hàng, một Phiếu giao hàng mới có thể được tạo dựa trên Kho mà các mặt hàng đã được lấy.

   - **Chuyển vật tư để sản xuất:** Tùy chọn này cho phép bạn chọn một Lệnh sản xuất để lấy nguyên vật liệu. Bạn sẽ được hiển thị tùy chọn chọn số lượng thành phẩm mà bạn muốn lấy nguyên vật liệu. Sau khi lấy kho, bạn có thể tạo Phiếu kho cho các mặt hàng đã lấy, tức là nguyên vật liệu.

   - **Chuyển vật tư:** Tùy chọn này cho phép bạn chọn một Yêu cầu vật tư để lấy các mặt hàng. Sau khi lấy kho, bạn có thể tạo Phiếu kho cho các mặt hàng đã lấy.

1. Thêm Mặt hàng và số lượng bạn muốn lấy vào bảng Vị trí mặt hàng. Nhấn vào **Lấy vị trí mặt hàng** để lấy thông tin Kho và các chi tiết khác cho mỗi Mặt hàng.

1. **Kho cha:** Nếu một Kho cha được chọn, chỉ những Kho thuộc Kho cha đó mới được đề xuất.

1. **Lấy vị trí mặt hàng:** Sau khi các mặt hàng cần lấy đã được chốt, bạn có thể nhấn vào nút **Lấy vị trí mặt hàng** để lấy lựa chọn Kho cho từng mặt hàng. Vì Kho sẽ được tự động lấy nếu bạn lấy Mặt hàng từ bất kỳ chứng từ tham chiếu nào, nút này có thể hữu ích để thêm thủ công các Mặt hàng bổ sung hoặc thay đổi số lượng của các Mặt hàng hiện có trong bảng Vị trí mặt hàng.

1. **Vị trí mặt hàng:** Phần này sẽ có thông tin về vị trí mặt hàng (Kho), Số serial cho các mặt hàng có số serial và số lô cho các mặt hàng theo lô.
 <img class='screenshot' alt='Item Locations' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/pick-list-item-locations.png'>

 Nếu có liên quan đến Số serial, dòng Mặt hàng sẽ trông như thế này:
 <img class='screenshot' alt='Item Location Detail' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/pick-list-item-location-detail.png'>

1. Lưu và Xác nhận.
 <img class='screenshot' alt='Submitted Pick List' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/pick-list-submitted-doc.png'>

### 2.1 Tạo Danh sách lấy hàng từ Đơn bán hàng

1. Đi tới [Đơn bán hàng](../selling/sales-order.md).
1. Nhấn vào nút **Tạo** ở góc trên bên phải của biểu mẫu và sau đó nhấn tùy chọn **Danh sách lấy hàng**.
1. Sau khi bạn nhấn Danh sách lấy hàng, tất cả dữ liệu cần thiết cho Danh sách lấy hàng sẽ được lấy từ Đơn bán hàng.
1. Bạn sẽ có thể thấy Bảng Vị trí mặt hàng với Kho đã được chọn cho mỗi mặt hàng.
1. Lưu chứng từ này và nó có thể được sử dụng để lấy hàng bởi người thực hiện hoạt động này.
1. Xác nhận chứng từ sau khi việc lấy hàng hoàn tất và số lượng mặt hàng đã lấy được cập nhật trong chứng từ.

**Mẹo:** Bạn có thể tạo một Danh sách lấy hàng cho nhiều Đơn bán hàng từ cùng một Khách hàng. Nhấn vào Lấy các mặt hàng và chọn các Đơn bán hàng.

> **Lưu ý:**
>
> - Danh sách lấy hàng chỉ có thể được tạo cho các Đơn bán hàng còn các Mặt hàng đang chờ giao.
> - Một **Phiếu giao hàng** chỉ có thể được tạo nếu Danh sách lấy hàng đã được Xác nhận.

### 2.2 Tạo Danh sách lấy hàng từ Lệnh sản xuất

1. Đi tới [Lệnh sản xuất](https://docs.erpnext.com/docs/v13/user/manual/en/manufacturing/work-order).
1. Nhấn nút **Tạo Danh sách lấy hàng**.
1. Bạn sẽ thấy hộp thoại yêu cầu số lượng Mặt hàng thành phẩm. Điều này là cần thiết để tính toán số lượng mặt hàng nguyên vật liệu cần thiết để sản xuất số lượng Mặt hàng thành phẩm đã nhập.
<img class='screenshot' alt='Dialog For qty' src='https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/pick-list-dialog-for-qty.png'>

1. Bạn sẽ có thể thấy bảng Vị trí mặt hàng với Kho đã được chọn cho mỗi mặt hàng nguyên vật liệu.
1. Lưu chứng từ này và sau đó chứng từ này có thể được chuyển cho người đang thực hiện lấy hàng.
1. Xác nhận chứng từ sau khi việc lấy hàng hoàn tất và mặt hàng đã lấy được cập nhật tương ứng trong chứng từ.

> **Lưu ý:**
>
> - Danh sách lấy hàng chỉ có thể được tạo cho các Lệnh sản xuất vẫn đang ở trạng thái 'Chưa bắt đầu' hoặc 'Đang tiến hành'.
> - Một **Phiếu kho** chỉ có thể được tạo sau khi Danh sách lấy hàng đã được Xác nhận.

### 2.3 Tạo Danh sách lấy hàng từ Yêu cầu vật tư

1. Đi tới [Yêu cầu vật tư](material-request.md).
1. Nhấn vào nút **Tạo** và sau đó nhấn tùy chọn **Danh sách lấy hàng**.
1. Bạn sẽ có thể thấy bảng Vị trí mặt hàng với Kho đã được chọn cho mỗi mặt hàng trong Yêu cầu vật tư.
1. Lưu chứng từ này và sau đó chứng từ này có thể được chuyển cho người đang lấy hàng.
1. Xác nhận chứng từ sau khi việc lấy hàng hoàn tất.