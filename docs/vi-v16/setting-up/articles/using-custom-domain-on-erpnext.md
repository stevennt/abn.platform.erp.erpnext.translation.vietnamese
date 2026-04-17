<!-- add-breadcrumbs -->
# Sử dụng Tên miền tùy chỉnh trên ERPNext

<!-- markdown -->

Nếu bạn đã đăng ký bất kỳ gói dịch vụ nào tại [ERPNext](https://erpnext.com), chúng tôi có thể cung cấp dịch vụ trang web của bạn trên tên miền tùy chỉnh của bạn (ví dụ: http://example.com). Điều này cho phép trang web của bạn được vận hành trên một tên miền riêng.

Để kích hoạt tính năng này, trước tiên bạn sẽ phải chỉnh sửa cài đặt DNS cho tên miền của mình như sau:

- Tạo một bản ghi CNAME cho một tên miền phụ (thường là www) trỏ đến {youraccountname}.erpnext.com
- Nếu bạn muốn vận hành trang web trên một tên miền gốc (ví dụ: http://example.com), hãy thiết lập chuyển hướng URL (URL redirect) sang http://www.example.com thay vì tạo bản ghi CNAME. Việc tạo bản ghi CNAME trong trường hợp này có thể dẫn đến những hậu quả không mong muốn, bao gồm cả việc bạn không thể nhận email được nữa.

Sau khi bạn đã thiết lập các bản ghi DNS, bạn sẽ cần gửi một phiếu hỗ trợ (support ticket) bằng cách gửi email đến support@erpnext.com và chúng tôi sẽ xử lý tiếp từ đó.

**Lưu ý**: Chúng tôi không hỗ trợ HTTPS trên các tên miền tùy chỉnh. HTTPS cho phép mã hóa đầu cuối (từ trình duyệt của bạn đến máy chủ của chúng tôi). Mặc dù điều này không quá nghiêm trọng đối với trang web, nhưng chúng tôi đặc biệt khuyến nghị không nên sử dụng ứng dụng ERPNext qua một giao thức không được mã hóa. Để đảm bảo an toàn, hãy luôn sử dụng ERP tại địa chỉ erpnext.com của bạn.