<!-- add-breadcrumbs -->
# Tự động tạo Yêu cầu vật tư

Để ngăn ngừa tình trạng hết hàng, bạn có thể theo dõi mức đặt hàng lại của mặt hàng. Khi mức tồn kho xuống dưới mức đặt hàng lại, quản lý mua hàng sẽ được thông báo và hướng dẫn để bắt đầu quy trình mua hàng cho mặt hàng đó.

Trong ERPNext, bạn có thể cập nhật Mức đặt hàng lại (Reorder Level) và Số lượng đặt hàng lại (Reorder Qty) của mặt hàng trong danh mục Mặt hàng (Item). Nếu cùng một mặt hàng có mức đặt hàng lại khác nhau, bạn cũng có thể cập nhật mức đặt hàng lại và số lượng đặt hàng lại theo từng kho.

<img alt="reorder level" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/reorder-request-1.png">

Với mức đặt hàng lại, bạn cũng có thể xác định hành động tiếp theo nên là gì. Có thể là mua mới hoặc chuyển hàng từ một kho khác. Dựa trên cài đặt trong danh mục Mặt hàng, mục đích cũng sẽ được cập nhật trong Yêu cầu vật tư.

<img alt="reorder level next action" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/reorder-request-2.png">

Khi tồn kho của mặt hàng chạm mức đặt hàng lại, Yêu cầu vật tư sẽ được tự động tạo. Bạn có thể kích hoạt tính năng này tại:

`Kho > Thiết lập > Thiết lập kho`

<img alt="active auto-material request" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/reorder-request-3.png">

Một Yêu cầu vật tư riêng biệt sẽ được tạo cho mỗi mặt hàng. Người dùng có vai trò Quản lý mua hàng sẽ nhận được cảnh báo email về các Yêu cầu vật tư này.

Nếu việc tự động tạo Yêu cầu vật tư thất bại, Người dùng có vai trò Quản lý mua hàng sẽ được thông báo về thông báo lỗi. Một trong những thông báo lỗi thường gặp nhất là:

**Đã xảy ra lỗi cho một số Mặt hàng khi đang tạo các Yêu cầu vật tư dựa trên Mức đặt hàng lại.**
**Ngày 01-04-2016 không nằm trong bất kỳ Năm tài chính nào.**

Một trong những lý do gây lỗi cũng có thể là do Năm tài chính. Nhấp vào [tại đây](/docs/v13/user/manual/en/accounts/articles/fiscal-year-error.html) để tìm hiểu thêm về vấn đề này.
<!-- markdown -->