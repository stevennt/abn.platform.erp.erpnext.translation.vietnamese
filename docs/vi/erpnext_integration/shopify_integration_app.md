<!-- add-breadcrumbs -->
# Tích hợp Shopify - Ứng dụng Tích hợp Thương mại điện tử

Bộ kết nối Shopify sẽ lấy các đơn hàng từ Shopify và tạo Đơn bán hàng tương ứng trong ERPNext.

Trong quá trình tạo đơn bán hàng, nếu Khách hàng hoặc Mặt hàng còn thiếu trong ERPNext, hệ thống sẽ tạo mới Khách hàng/Mặt hàng bằng cách lấy các thông tin tương ứng từ Shopify.

### Cách Thiết lập Bộ kết nối?


#### Lưu ý cho người dùng Bộ kết nối Shopify cũ

Nếu bạn chưa thiết lập Bộ kết nối Shopify trên trang ERPNext của mình, bạn có thể chuyển sang bước tiếp theo.

Nếu bạn đang sử dụng tích hợp Shopify cũ được cung cấp trong ERPNext, bạn sẽ phải vô hiệu hóa bộ kết nối trước khi tiếp tục. Sau khi cài đặt ứng dụng, nó sẽ di chuyển dữ liệu hiện có, ví dụ: `product_id` duy nhất cho các mặt hàng sang một DocType riêng biệt. Sau khi bạn hoàn tất cấu hình tích hợp mới, bạn có thể xác nhận trạng thái di chuyển bằng cách đi tới DocType "Ecommerce Integration Log".

#### Cài đặt Ứng dụng

- Nếu bạn đang lưu trữ trang ERPNext trên Frappe Cloud, bạn có thể nhanh chóng cài đặt ứng dụng bằng cách đi tới Trang tổng quan trang web của mình. Ứng dụng có sẵn tại [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce-integrations)
- Nếu bạn muốn cài đặt trên Private bench trên Frappe Cloud, hãy tham khảo [tài liệu Frappe Cloud](https://frappecloud.com/docs/bench/install-custom-app)
- Nếu bạn tự lưu trữ (self-hosting) ERPNext, bạn có thể cài đặt ứng dụng bằng Frappe bench. Tham khảo [tài liệu bench](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) để cài đặt các Frappe Apps.

Kho lưu trữ của ứng dụng được lưu trữ trên GitHub: [http://github.com/frappe/ecommerce_integrations/](http://github.com/frappe/ecommerce_integrations/)

#### Tạo Ứng dụng Riêng tư (Private App) trong Shopify

1. Nhấp vào Apps trên thanh menu
<img class="screenshot" alt="Menu Section" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/app_menu.png">

2. Nhấp vào **Manage private apps** để tạo ứng dụng riêng tư
<img class="screenshot" alt="Manage Private Apps" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/manage_private_apps.png">

3. Điền đầy đủ thông tin và tạo ứng dụng. Mỗi ứng dụng sẽ có Mật khẩu (Password) và Mã bí mật chia sẻ (Shared secret) riêng
<img class="screenshot" alt="App Details" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/app_details.png">


#### Thiết lập Shopify trên ERPNext:-
Sau khi bạn đã tạo Ứng dụng Riêng tư trên Shopify, hãy thiết lập Thông tin xác thực Ứng dụng (App Credentials) và các chi tiết khác trong Shopify Setting trong ERPNext.

> Để truy cập Shopify Setting, hãy đi tới:
Thanh tìm kiếm Awesome bar > "Shopify Setting"

Lưu ý: Shopify không hỗ trợ kết nối HTTP không bảo mật. Trang ERPNext của bạn phải có khả năng chấp nhận các yêu cầu HTTPS. Hãy truy cập trang ERPNext của bạn bằng URL `https://` trước khi tiếp tục.

1. Điền Password và Shared Secret từ Ứng dụng Riêng tư của Shopify.
<img class="screenshot" alt="Setup Private App Credentials" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/app_details.png">

2. Thiết lập cấu hình Khách hàng, Công ty và Kho hàng
<img class="screenshot" alt="ERP Configurations" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/main-settings.png">

3. Thiết lập cấu hình Đồng bộ.
    Hệ thống sẽ lấy Đơn hàng từ Shopify và tạo Đơn bán hàng trong ERPNext. Bạn có thể cấu hình hệ thống ERPNext để ghi nhận thanh toán và việc hoàn tất đơn hàng đối với các đơn hàng.
<img class="screenshot" alt="Sync Configure" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/series-setting.png">

4. Thiết lập Ánh xạ Thuế (Tax Mapper).
    Chuẩn bị bộ ánh xạ thuế và phí vận chuyển cho mỗi loại thuế và phí vận chuyển mà bạn áp dụng trong Shopify.
<img class="screenshot" alt="Taxes and Shipping Charges" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/tax-mapping.png">


Sau khi thiết lập tất cả các cấu hình, hãy kích hoạt đồng bộ Shopify và Lưu cài đặt. Thao tác này sẽ đăng ký các API với Shopify và hệ thống sẽ bắt đầu đồng bộ Đơn hàng giữa Shopify và ERPNext.


### Đồng bộ Đơn hàng cũ từ Shopify

Sau khi bạn hoàn tất cấu hình Shopify và đã kích hoạt Đồng bộ Shopify, bạn cũng có tùy chọn để đồng bộ các đơn hàng cũ từ Shopify vào ERPNext. Việc đồng bộ này sẽ diễn ra dưới nền và có thể mất vài giờ tùy thuộc vào số lượng đơn hàng bạn có.


1. Kích hoạt "Sync Old Shopify Orders"
2. Nhập ngày Từ (From) và Đến (To) mà các đơn hàng cần được đồng bộ.

<img class="screenshot" alt="Sync Order By Date" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/sync-old-orders.png">


### Đồng bộ Tồn kho

Bạn có thể cập nhật tồn kho của mình với Shopify đối với các mặt hàng được đồng bộ từ Shopify. Việc đồng bộ tồn kho được thực hiện mỗi giờ một lần với một công việc được lập lịch. Mức tồn kho của các mặt hàng có thay đổi kể từ lần đồng bộ cuối cùng sẽ được đẩy sang Shopify. Mức tồn kho của các Kho trong ERPNext được ánh xạ 1:1 với các địa điểm (locations) của Shopify.

1. Để kích hoạt đồng bộ tồn kho, hãy nhấp vào ô kiểm, thao tác này sẽ hiển thị cho bạn một bảng để ánh xạ Kho của ERPNext với Địa điểm của Shopify.
2. Chọn tần suất đồng bộ. Tần suất từ 30 đến 60 phút được khuyến nghị.
3. Nhấp vào nút "Fetch Shopify Locations" để hiển thị các địa điểm Shopify trong bảng.
4. Liên kết từng địa điểm với Kho của ERPNext.
5. Lưu cài đặt.

<img class="screenshot" alt="Inventory Syncing with Shopify" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/inventory-sync.png">

> Lưu ý: Bộ kết nối này giả định rằng ERPNext là nguồn thông tin chính về mức tồn kho, bất kỳ thay đổi nào được thực hiện đối với mức tồn kho trên Shopify sẽ bị ghi đè bởi ERPNext nếu mức tồn kho trong ERPNext thay đổi.

> Lưu ý: Shopify không hỗ trợ số lượng phân số. Nếu tìm thấy số lượng phân số trong ERPNext, mức tồn kho trên Shopify sẽ được thiết lập bằng cách làm tròn xuống số nguyên gần nhất.


### Đồng bộ Mặt hàng

Bạn có thể kích hoạt đồng bộ các mặt hàng mới từ ERPNext sang Shopify bằng cách tích vào "Upload new ERPNext items to Shopify".

Bạn cũng có thể cập nhật mặt hàng trên Shopify khi cập nhật mặt hàng trong ERPNext.

Các trường sau đây sẽ được tải lên / cập nhật:

| Trường ERPNext    | Trường Shopify   |
| :-: | :-: |