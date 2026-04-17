<!-- add-breadcrumbs -->
# Việc cần làm

ToDo là danh sách các hoạt động cần được thực hiện bởi một cá nhân cụ thể.

**Trong ERPNext, ToDo là một công cụ đơn giản nơi bạn có thể xác định các hoạt động cần thực hiện. Danh sách ToDo sẽ liệt kê tất cả các hoạt động được giao cho bạn và các hoạt động do bạn tạo ra.**

![ToDo](https://docs.erpnext.com/docs/v16/assets/img/using-erpnext/using-to-do-1.png)

Một ToDo cũng được tự động tạo khi bất kỳ Tài liệu nào khác được giao cho bạn. Xem tại [ToDo-Auto Creation](../user/manual/en/using-erpnext/articles/todo-auto-creation)

Để truy cập ToDo, hãy đi tới

> Home > Tools > ToDo

## 1. Cách tạo một ToDo

1. Đi tới danh sách ToDo, và nhấn mới.
2. Bạn sẽ được chuyển hướng đến phần Nhập nhanh (Quick Entry) cho ToDo, tại đây bạn sẽ được yêu cầu nhập mô tả cho ToDo.
3. Lưu.

 ![ToDo](https://docs.erpnext.com/docs/v16/assets/img/using-erpnext/using-to-do-2.gif)

> Lưu ý: Khi tạo một ToDo bằng cách sử dụng Nhập nhanh, theo mặc định ToDo sẽ được giao cho người tạo. Để tránh điều này và giao cho người dùng khác, hãy đảm bảo rằng bạn chỉnh sửa ToDo ở chế độ Toàn trang (Full Page).

### Thông báo ToDo

Sau khi một ToDo được tạo, người dùng được giao sẽ nhận được một thông báo cho ToDo đó.

![ToDo](https://docs.erpnext.com/docs/v16/assets/img/using-erpnext/using-todo-notification.png)

### 1.1. Các tùy chọn bổ sung khi tạo ToDo

1. **Trạng thái (Status)**: Bạn có thể xác định trạng thái của ToDo. Khi tạo, trạng thái của ToDo mặc định sẽ là 'Open' (Mở). Người dùng có thể chuyển nó thành 'Closed' (Đóng) khi công việc được hoàn thành.
2. **Mức độ ưu tiên (Priority)**: Bạn có thể xác định Mức độ ưu tiên của nhiệm vụ này là Thấp (Low), Trung bình (Medium) hoặc Cao (High).
3. **Màu sắc (Color)**: Bạn có thể chọn gán một màu cho mỗi ToDo của mình. Ví dụ: một ToDo được tạo làm lời nhắc hàng tuần để gửi báo cáo có thể được gán màu Tím (Purple), trong khi tất cả các ToDo cá nhân có thể được gán màu Vàng (Yellow).
4. **Hạn chót (Due Date)**: Bạn có thể thêm Hạn chót cho tất cả các ToDo.
5. **Giao cho (Allocated To)**: Trong trường hợp bạn đang giao một ToDo cho một Người dùng ERPNext khác, bạn có thể thực hiện việc đó tại đây.

 ![ToDo](https://docs.erpnext.com/docs/v16/assets/img/using-erpnext/using-to-do-3.png)

### 1.2. Tham chiếu

Mọi Tài liệu trong ERPNext đều có một tùy chọn gọi là 'Assign To' (Giao cho) ở thanh bên. Sử dụng tùy chọn này, bất kỳ Tài liệu nào cũng có thể được giao cho người dùng. Người dùng sẽ đồng thời được giao một ToDo.

1. **Loại tham chiếu (Reference Type)**: Khi một ToDo được tạo từ một tài liệu khác, chẳng hạn như Task (Nhiệm vụ) hoặc Issue (Vấn đề), Loại Tài liệu Tham chiếu sẽ được liên kết với ToDo tại đây. Bạn cũng có thể chọn thêm Loại Tài liệu Tham chiếu một cách thủ công.
2. **Tên tham chiếu (Reference Name)**: Khi được giao thông qua một DocType khác, tên của DocType Tham chiếu cũng sẽ được liên kết tại đây.
3. **Người giao (Assignment By)**: Khi bạn được giao một ToDo thông qua một Loại Tài liệu khác, tên của người thực hiện việc giao việc cũng sẽ được gắn thẻ.

 ![ToDo](https://docs.erpnext.com/docs/v16/assets/img/using-erpnext/using-to-do-4.png)

## 2. Trạng thái ToDo
ToDo có 3 trạng thái, mỗi trạng thái mô tả tình trạng hiện tại của một nhiệm vụ.

* **Open (Mở)**: Một ToDo theo mặc định sẽ được đánh dấu là Open khi nó được tạo.
* **Closed (Đóng)**: Khi một hoạt động được hoàn thành, ToDo có thể được đánh dấu là 'Closed' (Đóng) hoặc 'Resolved' (Đã giải quyết) hoặc 'Completed' (Đã hoàn thành). Hơn nữa, đối với các điều kiện như Vấn đề đã được giải quyết hoặc Nhiệm vụ đã hoàn thành; ToDo sẽ tự động được đóng. Nó cũng có thể được Mở lại (Reopened) nếu cần.
* **Cancelled (Hủy)**: Khi một người dùng bị xóa khỏi việc giao một ToDo/Task/Issue, ToDo liên kết với Tài liệu đó sẽ tự động được 'Cancelled' (Hủy).

 ![ToDo](https://docs.erpnext.com/docs/v16/assets/img/using-erpnext/using-to-do-5.png)


{next}