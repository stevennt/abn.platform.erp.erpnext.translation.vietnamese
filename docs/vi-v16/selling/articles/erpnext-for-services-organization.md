<!-- add-breadcrumbs -->
# ERPNext cho Doanh nghiệp Dịch vụ

**Câu hỏi:** ERPNext có vẻ như được thiết kế chủ yếu cho các đơn vị thương mại và sản xuất. Vậy ERPNext có được sử dụng bởi các công ty cung cấp dịch vụ không?

**Trả lời:**

Khoảng 30% khách hàng của ERPNext là các công ty hoạt động trong lĩnh vực dịch vụ. Đây là các công ty về phát triển phần mềm, dịch vụ chứng toán, tư vấn cá nhân và nhiều lĩnh vực khác. Bản thân chúng tôi cũng là một doanh nghiệp dịch vụ, chúng tôi sử dụng ERPNext để quản lý các hoạt động bán hàng, kế toán, hỗ trợ và nhân sự. Xem video sau để tìm hiểu cách ERPNext sử dụng ERPNext.

<iframe width="640" height="360" src="//www.youtube.com/embed/b6r7WxJMfFA" frameborder="0" allowfullscreen></iframe>

### Thiết lập Master

Việc thiết lập cho một công ty Dịch vụ khác biệt chủ yếu ở phần Mặt hàng. Họ không duy trì Tồn kho cho các Mặt hàng và do đó, không có Kho.

Để tạo một Mặt hàng Dịch vụ (không lưu kho), trong danh mục Mặt hàng, hãy bỏ chọn trường "Maintain Stock".

![Service Item](https://docs.erpnext.com/docs/v16/assets/img/selling/service-item.png)

Khi tạo Đơn bán hàng cho các dịch vụ, hãy chọn Loại đơn hàng (Order Type) là **Maintenance**. Đơn bán hàng loại Bảo trì cần ít thông tin chi tiết hơn so với đơn hàng mặt hàng tồn kho như Phiếu giao hàng, kho của mặt hàng, v.v.

**Lưu ý về Stock Reservation (Giữ hàng):** Trong phiên bản v16, nếu bạn sử dụng các tính năng liên quan đến quản lý tồn kho, hệ thống cung cấp tính năng **Stock Reservation** giúp giữ chỗ hàng hóa cho các Đơn bán hàng, đảm bảo hàng hóa được dành riêng cho khách hàng ngay khi có yêu cầu.

Công ty dịch vụ vẫn có thể thêm các mặt hàng tồn kho để quản lý tài sản cố định của họ như máy tính, nội thất và các thiết bị văn phòng khác.

### Ẩn các Tính năng không cần thiết

Vì nhiều phân hệ như Sản xuất và Kho sẽ không cần thiết cho công ty dịch vụ, bạn có thể ẩn các phân hệ đó từ:

`Setup > Permissions > Show/Hide Modules`

Các phân hệ không được chọn ở đây sẽ được ẩn khỏi tất cả Người dùng.

#### Thiết lập Tính năng (Feature Setup)

Trong biểu mẫu, có nhiều trường chỉ cần thiết cho các công ty kinh doanh thương mại và sản xuất. Những trường này có thể được ẩn đối với công ty dịch vụ. Thiết lập Tính năng là một công cụ nơi bạn có thể bật/tắt các tính năng cụ thể. Nếu một tính năng bị vô hiệu hóa, thì các trường liên quan đến tính năng đó sẽ được ẩn khỏi tất cả các biểu mẫu. Ví dụ, nếu tính năng Số serial bị vô hiệu hóa, thì trường Số serial trong Mặt hàng cũng như trong tất cả các giao dịch bán hàng và mua hàng sẽ bị ẩn.

[Để tìm hiểu thêm về Thiết lập Tính năng, hãy nhấp vào đây.](customize-erpnext/hiding-modules-and-features.md).

#### Quyền hạn

ERPNext là một hệ thống được kiểm soát bằng quyền hạn. Người dùng truy cập hệ thống dựa trên các quyền được gán cho họ. Vì vậy, nếu người dùng không được gán Vai trò liên quan đến Kho và Sản xuất, nó sẽ bị ẩn khỏi Người dùng đó. [Nhấp vào đây để tìm hiểu thêm về quản lý quyền hạn.](setting-up/users-and-permissions.html).

Bạn cũng có thể tham khảo video hướng dẫn về thiết lập Người dùng và Quyền hạn trong ERPNext.

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/8Slw1hsTmUI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

**Lưu ý về Khách hàng (Customer):** Trong phiên bản v16, tại biểu mẫu Khách hàng, bạn sẽ thấy các nút truy cập nhanh như **Quotation** hoặc **SO** để tạo nhanh Báo giá hoặc Đơn bán hàng trực tiếp từ hồ sơ Khách hàng. Ngoài ra, đối với các quy trình quản lý kho, hệ thống áp dụng ngày chốt (Cutoff date) cho Phiếu giao hàng (DN) từ Đơn bán hàng (SO) để đảm bảo tính chính xác của dữ liệu tồn kho tại thời điểm giao hàng.

{next}