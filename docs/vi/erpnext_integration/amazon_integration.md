<!-- add-breadcrumbs -->
# Tích hợp Amazon MWS
 Trình kết nối Amazon sẽ lấy Sản phẩm và Đơn bán hàng từ sàn thương mại điện tử Amazon.
 Việc đồng bộ Sản phẩm và Đơn bán hàng được thực hiện tuần tự. Bạn phải đồng bộ sản phẩm trước khi đồng bộ Đơn bán hàng.

## Cách thiết lập Trình kết nối Amazon MWS?

### Thiết lập Thông tin xác thực trong ERPNext
Bạn có thể yêu cầu thông tin xác thực dành cho nhà phát triển từ Amazon MWS sau khi bạn đã là người bán đã đăng ký trên trang web của họ. Để biết thêm chi tiết về vấn đề này, hãy nhấp vào [tại đây](https://docs.developer.amazonservices.com/en_ES/dev_guide/DG_Registering.html).

#### 1. Thiết lập Thông tin xác thực MWS
Nhập Seller ID, AWS Access Key ID, MWS Auth Token, Secret Key, Market Place ID, Region, và Domain.
<img class="screenshot" alt="Setup Credentials" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/amazon_mws_settings_1.png">

#### 2. Thiết lập Chi tiết Đơn hàng
Thiết lập Công ty, Kho, Nhóm mặt hàng, Bảng giá, Nhóm khách hàng, Khu vực, Loại khách hàng và Nhóm tài khoản.
   Nhóm tài khoản được sử dụng để lưu giữ Hoa hồng, thuế, v.v. mà Amazon thu.
<img class="screenshot" alt="ERPNext Configurations" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/amazon_mws_settings_2.png">

#### 3. Thiết lập Cấu hình Đồng bộ
Sử dụng After Date (Ngày sau ngày này), bạn có thể đồng bộ các sản phẩm và đơn hàng được tạo sau một ngày cụ thể. Trong trường hợp bạn đang nhập nhiều dữ liệu lịch sử, bạn nên bắt đầu theo thứ tự thời gian đảo ngược của After Date và nhập dữ liệu thành từng phần nhỏ.
<img class="screenshot" alt="Sync Configurations" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/amazon_mws_settings_3.png">
Sau khi thiết lập tất cả các cấu hình, hãy nhấp vào Enable Amazon và Lưu các cài đặt. Bây giờ bạn đã sẵn sàng để sử dụng tích hợp này.

#### 4. Đồng bộ Sản phẩm
Nhấp vào nút này để đồng bộ sản phẩm. Sau khi thành công, bạn sẽ thấy các sản phẩm Amazon của mình dưới dạng Mặt hàng trong ERPNext.

<img class="screenshot" alt="Sync Configurations" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/amazon_mws_settings_4.png">
<img class="screenshot" alt="Sync Configurations" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/amazon_mws_settings_5.png">

#### 5. Đồng bộ Đơn hàng
Nhấp vào nút này để đồng bộ đơn bán hàng. Sau khi thành công, bạn sẽ thấy các Đơn hàng Amazon của mình dưới dạng Đơn bán hàng trong ERPNext. Bạn cũng có thể thiết lập bộ lập lịch để đồng bộ đơn hàng tự động.

>Trong trường hợp tài khoản nhà phát triển của bạn không có quyền truy cập vào thông tin nhận dạng cá nhân. Tên khách hàng sẽ được lưu dưới dạng kết hợp của BuyerName + &lt;Order ID&gt;.

  <img class="screenshot" alt="Sync Configurations" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/amazon_mws_settings_6.png">

### Lưu ý

Trình kết nối sẽ không xử lý việc Hủy đơn hàng. Nếu bạn đã hủy bất kỳ đơn hàng nào trên Amazon, bạn phải thực hiện Hủy Đơn bán hàng tương ứng và các chứng từ khác trong ERPNext một cách thủ công.