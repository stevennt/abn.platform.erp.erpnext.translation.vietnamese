<!-- add-breadcrumbs -->

> Tích hợp này hiện đã lỗi thời và sẽ bị loại bỏ trong phiên bản tương lai (v14). Chúng tôi khuyên bạn nên sử dụng [tích hợp mới được tạo dưới dạng một Frappe App](/docs/v13/user/manual/en/erpnext_integration/shopify_integration_app) với các tính năng mới tuyệt vời như đồng bộ Kho.

# Tích hợp Shopify

Bộ kết nối Shopify sẽ lấy các đơn hàng từ Shopify và tạo Đơn bán hàng tương ứng trong ERPNext.

Trong khi tạo Đơn bán hàng, nếu Khách hàng hoặc Mặt hàng còn thiếu trong ERPNext, hệ thống sẽ tạo mới Khách hàng/Mặt hàng bằng cách lấy các chi tiết tương ứng từ Shopify.

### Cách Thiết lập Bộ kết nối?

#### Tạo Một Private App trong Shopify

1. Nhấp vào Apps trên thanh menu
<img class="screenshot" alt="Menu Section" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/app_menu.png">

2. Nhấp vào **Manage private apps** để tạo private app
<img class="screenshot" alt="Manage Private Apps" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/manage_private_apps.png">

3. Điền đầy đủ thông tin và tạo ứng dụng. Mỗi ứng dụng sẽ có API key, Password và Shared secret riêng
<img class="screenshot" alt="App Details" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/app_details.png">


#### Thiết lập Shopify trên ERPNext:-
Sau khi bạn đã tạo một Private App trên Shopify, hãy thiết lập Thông tin xác thực ứng dụng (App Credentials) và các chi tiết khác trong Shopify Settings trong ERPNext.

> Để truy cập Shopify Settings, hãy đi tới:
Integrations > Shopify Settings

1. Chọn App Type là Private và điền API key, Password và Shared Secret từ Private App của Shopify.
<img class="screenshot" alt="Setup Private App Credentials" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/app_details.png">

2. Thiết lập cấu hình Khách hàng, Công ty và Kho
<img class="screenshot" alt="ERP Configurations" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/erp_configurations.png">

3. Thiết lập Cấu hình đồng bộ (Sync Configurations).
    Hệ thống sẽ lấy Đơn hàng từ Shopify và tạo Đơn bán hàng trong ERPNext. Bạn có thể cấu hình hệ thống ERPNext để ghi nhận thanh toán và việc hoàn tất đơn hàng (fulfillments) đối với các đơn hàng.
<img class="screenshot" alt="Sync Configure" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/sync_config.png">

4. Thiết lập Tax Mapper (Ánh xạ Thuế).
    Chuẩn bị bộ ánh xạ thuế và phí vận chuyển cho mỗi loại thuế và phí vận chuyển mà bạn áp dụng trong Shopify.
<img class="screenshot" alt="Taxes and Shipping Charges" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/tax_config.png">


Sau khi thiết lập tất cả các cấu hình, hãy kích hoạt đồng bộ Shopify và Lưu các cài đặt. Thao tác này sẽ đăng ký các API với Shopify và hệ thống sẽ bắt đầu đồng bộ Đơn hàng giữa Shopify và ERPNext.


### Đồng bộ Đơn hàng cũ từ Shopify

Sau khi bạn hoàn tất cấu hình Shopify và đã kích hoạt Đồng bộ Shopify, bạn cũng có tùy chọn để đồng bộ các đơn hàng cũ từ Shopify vào ERPNext. Tối đa 250 đơn hàng sẽ được đồng bộ mỗi giờ thông qua một tác vụ chạy ngầm cho đến khi tất cả các đơn hàng trong phạm vi đã nêu được đồng bộ xong.

Hóa đơn có thể được đồng bộ dựa trên hai tiêu chí sau:

#### 1. Đồng bộ đơn hàng cũ dựa trên ngày

1. Kích hoạt "Sync Missing Old Shopify Orders"
1. Chọn "Date" trong trường "Sync Based On" và nhập ngày Từ (From) và Đến (To) mà các đơn hàng cần được đồng bộ.

<img class="screenshot" alt="Sync Order By Date" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/shopify-order-sync-date.png">


#### 2. Đồng bộ đơn hàng cũ dựa trên Shopify Order ID

1. Kích hoạt "Sync Missing Old Shopify Orders"
1. Chọn "Shopify Order ID" trong trường "Sync Based On" và nhập ID đơn hàng Từ (From) và Đến (To) mà các đơn hàng cần được đồng bộ. Cách dễ nhất để lấy Shopify order ID là từ URL của đơn hàng như hiển thị trong hình dưới đây.

<img class="screenshot" alt="Shopify Order ID" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/shopify-order-id.png">

<img class="screenshot" alt="Sync Order ID" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/shopify-order-sync-id.png">

### Lưu ý:
Bộ kết nối sẽ không xử lý việc Hủy đơn hàng. Nếu bạn Hủy bất kỳ đơn hàng nào trong Shopify, bạn sẽ phải Hủy Đơn bán hàng tương ứng và các chứng từ khác trong ERPNext một cách thủ công.

#### Phiên bản 11:
Chúng tôi đã cải tiến Tích hợp Shopify để nó hoạt động theo một chiều - Bộ kết nối Shopify sẽ lấy các đơn hàng từ Shopify và tạo Đơn bán hàng tương ứng trong ERPNext, chứ không phải ngược lại.