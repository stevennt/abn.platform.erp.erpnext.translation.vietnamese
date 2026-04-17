<!-- add-breadcrumbs -->
# Lỗi tồn kho âm khi Xác nhận Phiếu giao hàng

**Câu hỏi**: Khi Xác nhận một Phiếu giao hàng, hệ thống hiển thị thông báo rằng tồn kho của mặt hàng không đủ, nhưng chúng tôi thấy vẫn còn hàng trong Kho.

**Trả lời**: Khi Xác nhận Phiếu giao hàng, hệ thống sẽ kiểm tra mức tồn kho dựa trên **Ngày hạch toán** và **Giờ hạch toán** được thiết lập trên Phiếu giao hàng đó. 

Có khả năng bạn đang có sẵn tồn kho của một Mặt hàng trong Kho tại thời điểm hiện tại. Tuy nhiên, nếu bạn đang tạo Phiếu giao hàng lùi ngày (backdated), hệ thống sẽ kiểm tra xem tại đúng thời điểm **Ngày hạch toán** và **Giờ hạch toán** đó, Mặt hàng có đủ số lượng trong Kho hay không. Nếu tại thời điểm đó số lượng chưa được nhập vào kho, bạn sẽ nhận được thông báo lỗi về việc tồn kho âm.

Để kiểm tra chính xác dòng thời gian biến động hàng hóa, bạn có thể tham khảo [Báo cáo Sổ cái kho](../stock/stock-ledger.md).

**Cách xử lý**:
Nếu rơi vào trường hợp này, bạn nên chỉnh sửa **Ngày hạch toán** và **Giờ hạch toán** của Phiếu giao hàng, đảm bảo rằng thời gian này phải sau **Ngày hạch toán** và **Giờ hạch toán** của Phiếu nhập hàng (hoặc các chứng từ nhập kho khác) tương ứng của Mặt hàng đó.

---
**Các tính năng mới liên quan trong v16:**
* **Hệ thống Giữ hàng (Stock Reservation System):** Giúp quản lý việc giữ hàng cho các Đơn bán hàng, tránh tình trạng thiếu hụt hàng hóa khi thực hiện xuất kho.
* **Báo cáo Truy xuất Lô hàng/Số Serial (Serial/Batch Traceability Report):** Cho phép theo dõi chi tiết lịch sử di chuyển của từng Lô hàng hoặc Số Serial để đối soát tồn kho chính xác hơn.
* **Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry):** Tự động phân bổ các chi phí mua hàng vào giá trị tồn kho của Mặt hàng.
* **Hạch toán kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Cung cấp cái nhìn chi tiết hơn về giá trị tài chính của từng Mặt hàng trong sổ cái.