<!-- add-breadcrumbs -->
# Giới thiệu

ERPNext được tích hợp sẵn đầy đủ cho tất cả các yêu cầu của một doanh nghiệp sản xuất như quản lý Kho, Trạm làm việc / Máy móc, Công đoạn, Thành phẩm, Nguyên vật liệu, theo dõi Định mức nguyên vật liệu, lập kế hoạch và thực hiện Lệnh sản xuất, thu mua, và nhiều tính năng khác nữa.

<img class="screenshot" alt="BOM" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/onboarding.png">

## 1. Dữ liệu danh mục

Phân hệ Sản xuất trong ERPNext giúp bạn quản lý Kho (địa điểm), Trạm làm việc, Công đoạn, Thành phẩm và Nguyên vật liệu. Đối với sản xuất, các Công đoạn và Trạm làm việc tương ứng là rất quan trọng, chúng có thể được cấu hình dựa trên Thành phẩm trong Định mức nguyên vật liệu. Kho rất hữu ích để lưu trữ Nguyên vật liệu và Thành phẩm. Trong ERPNext, người dùng có thể tạo các Kho riêng biệt để giữ Nguyên vật liệu và Thành phẩm.

Chi tiết thêm như dưới đây:

1. [Kho](/docs/v13/user/manual/en/stock/warehouse)
1. [Trạm làm việc / Máy móc](/docs/v13/user/manual/en/manufacturing/workstation)
1. [Công đoạn](/docs/v13/user/manual/en/manufacturing/operation)
1. [Nguyên vật liệu / Thành phẩm](/docs/v13/user/manual/en/stock/item)
1. [Quy trình sản xuất](/docs/v13/user/manual/en/manufacturing/routing)


## 2. Dữ liệu giao dịch

Phân hệ Sản xuất trong ERPNext giúp bạn duy trì Định mức nguyên vật liệu (BOM) nhiều cấp cho các Mặt hàng của mình. Nó giúp tính giá thành sản phẩm, lập kế hoạch sản xuất, tạo lệnh sản xuất cho xưởng sản xuất, tạo thẻ công việc, và lập kế hoạch tồn kho bằng cách lấy yêu cầu vật tư thông qua BOM (còn được gọi là [Lập kế hoạch nhu cầu vật tư hoặc MRP](http://erpnext.com/blog/general/what-is-mrp-and-do-yo…)).

Chi tiết thêm như dưới đây:

1. [Định mức nguyên vật liệu](/docs/v13/user/manual/en/manufacturing/bill-of-materials)
1. [Lệnh sản xuất](/docs/v13/user/manual/en/manufacturing/work-order)
1. [Thẻ công việc](/docs/v13/user/manual/en/manufacturing/job-card)
1. [Kế hoạch sản xuất](/docs/v13/user/manual/en/manufacturing/production-plan)

## 3. Các loại Kế hoạch sản xuất

Nhìn chung, có ba loại Hệ thống Kế hoạch sản xuất:

 * __Sản xuất để tồn kho (Make to Stock):__ Trong các hệ thống này, việc sản xuất được lập kế hoạch dựa trên dự báo và các Mặt hàng sau đó được bán cho các nhà phân phối hoặc khách hàng. Tất cả các hàng tiêu dùng nhanh được bán trong các cửa hàng bán lẻ như xà phòng, nước đóng chai, v.v. và đồ điện tử như điện thoại đều được sản xuất để tồn kho.
 * __Sản xuất theo đơn hàng (Make to Order):__ Trong các hệ thống này, các mặt hàng chỉ được sản xuất sau khi khách hàng đặt một số lượng nhất định theo yêu cầu của khách hàng. Ví dụ: một chiếc bánh cưới.
 * __Sản xuất theo thiết kế (Engineer to Order):__ Trong trường hợp này, mỗi đơn hàng bán là một dự án riêng biệt và phải được thiết kế và kỹ thuật hóa theo yêu cầu của khách hàng. Các ví dụ phổ biến về loại này là bất kỳ doanh nghiệp tùy chỉnh nào như đồ nội thất, máy công cụ, thiết bị chuyên dụng, gia công kim loại, v.v.

Hầu hết các doanh nghiệp sản xuất quy mô vừa và nhỏ đều dựa trên hệ thống sản xuất theo đơn hàng hoặc sản xuất theo thiết kế và ERPNext cũng vậy.

Đối với các hệ thống sản xuất theo thiết kế, phân hệ Sản xuất nên được sử dụng cùng với [phân hệ Dự án](/docs/v13/user/manual/en/projects).

## 4. Tác động của Sản xuất đối với Tồn kho

Trạng thái lệnh sản xuất phụ thuộc vào các giao dịch kho được thực hiện đối với lệnh đó. Trong ERPNext, bạn có thể chuyển nguyên vật liệu cần thiết để làm thành phẩm từ Kho lưu trữ sang Kho bán thành phẩm (Work In Progress). Từ kho bán thành phẩm, nguyên vật liệu có thể được tiêu hao bằng cách sử dụng Phiếu kho. Bạn có tùy chọn tiêu hao nguyên vật liệu hàng loạt và thêm thành phẩm, hoặc tiêu hao nguyên vật liệu trước rồi sau đó mới thêm thành phẩm.

## 5. Demo Sản xuất ERPNext

Xem video sau để biết về các tính năng trong phân hệ sản xuất.

<div class="embed-container">
 <iframe src="https://www.youtube.com/embed/xE74wdQU5cc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

<!-- <img class="screenshot" alt="Task" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/manufacturing.png"> -->

{next}