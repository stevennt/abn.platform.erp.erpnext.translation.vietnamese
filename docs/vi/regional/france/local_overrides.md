<!-- add-breadcrumbs -->
# Các giao dịch Bán hàng và Thanh toán

Để tuân thủ luật tài chính mới nhất áp dụng cho phần mềm POS, ERPNext tự động ghi lại tất cả các giao dịch bán hàng và thanh toán trong một chuỗi nhật ký liên kết.

Nếu quốc gia của bạn được thiết lập là "France", việc xóa các giao dịch bán hàng và thanh toán cũng sẽ không được phép, ngay cả khi người dùng được cấp các quyền phù hợp.

Vui lòng lưu ý rằng ERPNext vẫn chưa hoàn toàn tuân thủ Luật Tài chính năm 2016.

# Báo cáo Nhật ký liên kết (Chained log Report)

Một báo cáo chuyên dụng có tên "Transaction Log Report" luôn có sẵn để xác minh rằng chuỗi nhật ký đã ghi không bị phá vỡ.

Nếu trạng thái của cột "Chain Integrity" là "True", chuỗi nhật ký chưa bị phá vỡ.
Điều này có nghĩa là bạn có thể tra cứu toàn bộ chuỗi các sự kiện đã xảy ra trong hệ thống của mình.

Nếu trạng thái của cột "Chain Integrity" là "False", điều đó có nghĩa là có sự sai lệch trong chuỗi nhật ký.
Trong trường hợp này, hàng trước đó đã bị xóa hoặc bị thay đổi trong cơ sở dữ liệu. Đây có thể là hệ quả của một hành vi gian lận.