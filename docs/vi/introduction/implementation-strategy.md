<!-- add-breadcrumbs -->
# Chiến lược Triển khai

Trước khi bạn bắt đầu quản lý các hoạt động vận hành trong ERPNext, trước tiên bạn phải làm quen với hệ thống và các thuật ngữ được sử dụng. Vì lý do này, chúng tôi khuyên rằng việc triển khai nên diễn ra theo hai giai đoạn.

  * **Giai đoạn Thử nghiệm (Test Phase)**, nơi bạn nhập các bản ghi giả lập đại diện cho các giao dịch hàng ngày của mình và **Giai đoạn Thực tế (Live Phase)**, nơi chúng ta bắt đầu nhập dữ liệu thực tế.

### Giai đoạn Thử nghiệm

  * Đọc Sách hướng dẫn.
  * Tạo một tài khoản miễn phí tại [https://erpnext.com](https://erpnext.com) (cách dễ nhất để thử nghiệm).
  * Tạo Khách hàng, Nhà cung cấp và Mặt hàng đầu tiên của bạn. Thêm một vài bản ghi nữa để bạn làm quen với chúng.
  * Tạo Nhóm khách hàng, Nhóm mặt hàng, Kho, Nhóm nhà cung cấp để bạn có thể phân loại các Mặt hàng của mình.
  * Hoàn thành một chu trình bán hàng tiêu chuẩn - Khách hàng tiềm năng > Cơ hội > Báo giá > Đơn bán hàng > Phiếu giao hàng > Hóa đơn bán hàng > Thanh toán (Bút toán).
  * Hoàn thành một chu trình mua hàng tiêu chuẩn - Yêu cầu vật tư > Đơn mua hàng > Phiếu nhập hàng > Thanh toán (Bút toán).
  * Hoàn thành một chu trình sản xuất (nếu có) - Định mức nguyên vật liệu > Công cụ lập kế hoạch sản xuất > Lệnh sản xuất > Xuất vật tư.
  * Mô phỏng một kịch bản thực tế vào hệ thống.
  * Tạo các trường tùy chỉnh, mẫu in, v.v. theo yêu cầu.

### Giai đoạn Thực tế

Khi bạn đã quen với ERPNext, hãy bắt đầu nhập dữ liệu thực tế của bạn!

  * Dọn dẹp tài khoản khỏi các dữ liệu thử nghiệm hoặc tốt hơn là bắt đầu một bản cài đặt mới.
  * Nếu bạn chỉ muốn xóa các giao dịch mà không muốn xóa dữ liệu danh mục như Mặt hàng, Khách hàng, Nhà cung cấp, Định mức nguyên vật liệu, v.v., bạn có thể xóa các giao dịch của Công ty mình và bắt đầu lại từ đầu. Để làm điều này, hãy mở Hồ sơ Công ty thông qua Kế toán > Danh mục kế toán > Công ty và xóa các giao dịch của Công ty bằng cách nhấp vào nút **Delete Company Transactions** ở dưới cùng của Biểu mẫu Công ty.
  * Bạn cũng có thể thiết lập một tài khoản mới tại [https://erpnext.com](https://erpnext.com) và sử dụng bản dùng thử miễn phí 14 ngày. [Tìm hiểu thêm các cách triển khai ERPNext](getting-started-with-erpnext)
  * Thiết lập tất cả các phân hệ với Nhóm khách hàng, Nhóm mặt hàng, Kho, Định mức nguyên vật liệu, v.v.
  * Nhập Khách hàng, Nhà cung cấp, Mặt hàng, Liên hệ và Địa chỉ bằng Công cụ Nhập dữ liệu (Data Import Tool).
  * Nhập tồn kho đầu kỳ bằng Công cụ Đối chiếu tồn kho (Stock Reconciliation Tool).
  * Tạo các bút toán kế toán đầu kỳ thông qua Bút toán và tạo các Hóa đơn bán hàng và Hóa đơn mua hàng còn tồn đọng.
  * Nếu bạn cần trợ giúp, [bạn có thể mua hỗ trợ](https://erpnext.com/pricing) hoặc [hỏi trên diễn đàn người dùng](https://discuss.erpnext.com).

{next}