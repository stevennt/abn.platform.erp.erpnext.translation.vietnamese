<!-- add-breadcrumbs -->
# Lỗi tồn kho âm khi Xác nhận Phiếu giao hàng

**Câu hỏi**: Khi Xác nhận một Phiếu giao hàng, hệ thống hiển thị thông báo rằng tồn kho của mặt hàng không đủ, nhưng chúng tôi thấy vẫn còn hàng trong Kho.

**Trả lời**: Khi Xác nhận Phiếu giao hàng, mức tồn kho sẽ được kiểm tra dựa trên Ngày hạch toán và Giờ hạch toán của Phiếu giao hàng đó. Có khả năng bạn đang có sẵn tồn kho của một Mặt hàng trong Kho. Tuy nhiên, nếu bạn đang tạo Phiếu giao hàng lùi ngày, và nếu tại Ngày hạch toán và Giờ hạch toán của Phiếu giao hàng đó mặt hàng không có sẵn trong kho, bạn rất có thể sẽ nhận được thông báo lỗi về việc tồn kho âm. Bạn có thể tham khảo báo cáo Sổ cái kho để xác nhận điều này.

Nếu rơi vào trường hợp này, bạn nên chỉnh sửa Ngày hạch toán và Giờ hạch toán của Phiếu giao hàng, và đảm bảo rằng thời gian này phải sau Ngày hạch toán và Giờ hạch toán của phiếu nhập hàng mặt hàng đó.