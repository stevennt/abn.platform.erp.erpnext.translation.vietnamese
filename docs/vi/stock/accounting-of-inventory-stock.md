<!-- add-breadcrumbs -->
# Kế toán Tồn kho

Giá trị của hàng tồn kho hiện có được coi là Tài sản ngắn hạn trong [Hệ thống tài khoản](../accounts/chart-of-accounts.md) của công ty. Để lập Bảng cân đối kế toán, bạn nên thực hiện các bút toán kế toán cho các tài sản đó. Thông thường có hai phương pháp kế toán hàng tồn kho khác nhau.

## 1. Kiểm kê thường xuyên (Auto/Perpetual Inventory)

Trong quy trình này, đối với mỗi giao dịch kho, hệ thống sẽ ghi các bút toán kế toán liên quan để đồng bộ số dư kho và số dư kế toán. Đây là thiết lập mặc định trong ERPNext cho các tài khoản mới. Theo mặc định, Kiểm kê thường xuyên được bật trong [Công ty](../setting-up/company-setup.md#23-stock-settings).

Khi bạn mua và nhận hàng, các mặt hàng đó được ghi nhận là tài sản của công ty (tồn kho). Khi bạn bán và giao các mặt hàng đó, một khoản chi phí (Giá vốn hàng bán) tương đương với chi phí chuyển đến của các mặt hàng sẽ được ghi nhận. Các bút toán Sổ cái được tạo ra sau mỗi giao dịch kho. Kết quả là, giá trị theo Sổ cái kho luôn khớp với số dư tài khoản liên quan. Điều này giúp cải thiện độ chính xác của Bảng cân đối kế toán và Báo cáo kết quả hoạt động kinh doanh.

Đọc [tài liệu về Kiểm kê thường xuyên](perpetual-inventory.md) để kiểm tra các bút toán kế toán cho một giao dịch kho cụ thể.


### 1.2 Ưu điểm của Kiểm kê thường xuyên

Hệ thống Kiểm kê thường xuyên sẽ giúp bạn dễ dàng duy trì tính chính xác của các giá trị tài sản và chi phí của công ty. Số dư kho sẽ luôn được đồng bộ với số dư tài khoản liên quan, vì vậy không cần phải thực hiện nhập liệu thủ công định kỳ để cân đối chúng.

Trong trường hợp có các giao dịch kho mới lùi ngày hoặc hủy/sửa đổi một giao dịch hiện có, tất cả các bút toán Sổ cái kho và Bút toán Sổ cái trong tương lai sẽ được tính toán lại cho tất cả các mặt hàng của giao dịch đó. Điều tương tự cũng áp dụng nếu có bất kỳ chi phí nào được thêm vào Phiếu nhập hàng đã Xác nhận sau đó thông qua Chứng từ chi phí chuyển đến.

> Lưu ý: Kiểm kê thường xuyên phụ thuộc hoàn toàn vào giá trị tính giá của mặt hàng. Do đó, bạn phải cẩn thận hơn khi nhập giá trị tính giá khi thực hiện bất kỳ giao dịch nhập kho nào như Phiếu nhập hàng, Phiếu nhập vật tư, hoặc Sản xuất/Đóng gói lại.

* * *

## 2. Kiểm kê định kỳ (Periodic Inventory)

Trong phương pháp này, các bút toán kế toán cần được tạo thủ công để đồng bộ số dư kho và số dư tài khoản liên quan. Hệ thống không tự động tạo các bút toán kế toán cho tài sản tại thời điểm mua hoặc bán vật tư.

Trong một kỳ kế toán, khi bạn mua và nhận hàng, một khoản chi phí được ghi nhận trong hệ thống kế toán của bạn. Bạn bán và giao một số mặt hàng này.

Vào cuối kỳ kế toán, tổng giá trị của các mặt hàng dự kiến bán cần được ghi nhận là tài sản của công ty, thường được gọi là tồn kho.

Sự chênh lệch giữa giá trị của các mặt hàng còn lại để bán và giá trị tồn kho của kỳ trước có thể là số dương hoặc số âm. Nếu là số dương, giá trị này được trừ vào chi phí (Giá vốn hàng bán) và được cộng vào tài sản (tồn kho). Nếu là số âm, một bút toán ngược sẽ được thực hiện.

Toàn bộ quy trình này được gọi là **Kiểm kê định kỳ**.

Nếu bạn là người dùng hiện tại đang sử dụng Kiểm kê định kỳ và muốn sử dụng Kiểm kê thường xuyên, bạn cần thực hiện [một vài bước](articles/migrate-to-perpetual-inventory.md) để chuyển đổi.

### 3. Các chủ đề liên quan
1. [Kiểm kê thường xuyên](perpetual-inventory.md)
1. [Chuyển đổi sang Kiểm kê thường xuyên](articles/migrate-to-perpetual-inventory.md)