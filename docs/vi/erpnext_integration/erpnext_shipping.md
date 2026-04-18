<!-- add-breadcrumbs -->
# ERPNext Shipping

**Ứng dụng ERPNext Shipping giúp bạn so sánh giá cước vận chuyển được cung cấp bởi nhiều nhà cung cấp dịch vụ, tạo nhãn và theo dõi trạng thái lô hàng của bạn.**

Có sẵn tích hợp với các nhà cung cấp dịch vụ sau:

1. [Packlink](https://www.packlink.com/en-GB/)
1. [LetMeShip](https://www.letmeship.com/en/)
1. [SendCloud](https://www.sendcloud.com/home-new/)

## 1. Thiết lập

Để ứng dụng hoạt động trơn tru, bạn sẽ cần tạo khóa API từ **ít nhất một** trong các nền tảng được liệt kê ở trên. Dưới đây là hướng dẫn để thiết lập chúng:

### 1.1 Packlink API

1. Đăng ký trên [Packlink PRO](https://auth.packlink.com/en-GB/pro/register?platform=PRO&platform_country=UN).
1. Làm theo [các bước này](https://support-pro.packlink.com/hc/en-gb/articles/213431749-How-to-generate-an-API-key-on-PRO) để tạo **API Key**.
1. Tìm kiếm **Packlink** trong thanh tìm kiếm (awesomebar).
1. Thêm **API Key** vào DocType Packlink, tích vào trường 'Enabled'.
1. Lưu.

<img class="screenshot" alt="Packlink API" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/packlink_api.png">

### 1.1 Sendcloud API

1. Đăng ký trên [Sendcloud](https://panel.sendcloud.sc/accounts/signup/).
1. Làm theo [các bước này](https://support.sendcloud.com/hc/en-us/articles/360024967612-Service-points-for-API-Integrations#step-1-) để tạo **Public Key** và **Secret Key**.
1. Tìm kiếm **SendCloud** trong thanh tìm kiếm (awesomebar).
1. Thêm **Public Key** vào trường 'API Key' và **Secret Key** vào trường 'API Secret' của DocType SendCloud.
1. Tích vào trường **Enabled**.
1. Lưu.

<img class="screenshot" alt="Sendcloud API" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/sendcloud_api.png">

### 1.1 LetMeShip API

1. Đăng ký trên [LetMeShip](https://www.letmeship.com/en/).
1. Làm theo [các bước này](https://www.letmeship.com/en/connect-the-shipping-interface/) để tạo **API ID** và **API Password**.
1. Tìm kiếm **LetMeShip** trong thanh tìm kiếm (awesomebar).
1. Thêm **API ID** và **API Password** vào DocType LetMeShip. Tích vào trường **Enabled**.
1. Lưu.

<img class="screenshot" alt="LetMeShip API" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/letmeship_api.png">

## 2. Các tính năng

### 2.1 So sánh giá cước vận chuyển

Sau khi một [Shipment](../stock/shipment.md) được Xác nhận, nếu ứng dụng đã được cài đặt, nút **Fetch Shipping Rates** (Lấy giá cước vận chuyển) sẽ xuất hiện. Khi nhấp vào, bạn sẽ nhận được danh sách các dịch vụ cùng với nhà cung cấp dịch vụ và giá cước của họ.

<img class="screenshot" alt="Fetch Rates" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/fetch_rates.png">

Bạn cũng có thể thêm các dịch vụ thường xuyên sử dụng vào **Preferred Services** (Dịch vụ ưu tiên) bằng cách sử dụng **Parcel Service Type** (Loại dịch vụ bưu kiện):

1. Giả sử dịch vụ được làm nổi bật là dịch vụ chúng ta thường xuyên sử dụng, hãy thêm nó vào **Preferred Services** của chúng ta.

 <img class="screenshot" alt="Highlight Service" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/service_highlight.png">

1. Đi tới **Parcel Service Type** > **New**. Tạo một **Parcel Service** mới. Trong trường hợp của chúng ta, đó là 'TNT'.
1. Thêm một **Parcel Service Type**. Trong trường hợp của chúng ta, đó sẽ là 'Economy'.
1. Thêm 'Economy' vào bảng **Parcel Service Type Alias** luôn.
1. Thêm mô tả (tùy chọn).
1. Bật trường **Show in Preferred Services List**. Lưu.

Bây giờ khi bạn nhấp vào nút **Fetch Shipping Rates**, bạn sẽ luôn thấy dịch vụ đã được làm nổi bật trước đó trong phần **Preferred Services**.

<img class="screenshot" alt="Preferred Service" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/preferred_service.png">

### 2.2 Tạo Lô hàng (Shipment)

Sau khi so sánh giá cước, bạn có thể tiến hành với bất kỳ dịch vụ nào bằng cách nhấp vào **Select** tương ứng với dòng dịch vụ phù hợp. Khi nhấp vào, một Shipment sẽ tự động được tạo trên nền tảng của nhà cung cấp dịch vụ của bạn.

Bạn sẽ thấy rằng phần **Shipment Information** được cập nhật tự động dựa trên Shipment đã được tạo.

<img class="screenshot" alt="Shipment Creation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/create_shipment.gif">

Bạn cũng có thể tìm kiếm giao dịch của mình trên nền tảng của nhà cung cấp dịch vụ bằng cách sử dụng trường **Shipment ID**.

<img class="screenshot" alt="Packlink Shipment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/packlink_shipment.png">

### 2.3 In nhãn

Để sử dụng nút **Print Shipping Label** (In nhãn vận chuyển), **Shipment ID** phải được tạo trong bản ghi hiện tại.

<img class="screenshot" alt="Print Label Button" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/print_label_button.png">

Sau đó, bạn có thể nhấp vào đó và tạo nhãn vận chuyển của mình.

<img class="screenshot" alt="Dummy Shipping Label" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/dummy_shipping_label.png">


Bạn cũng có thể theo dõi trạng thái lô hàng của mình bằng cách nhấp vào **View** > **Track Status**.

> **Lưu ý**: Các nền tảng được tích hợp hiện tại có thể không phục vụ khu vực của bạn. Vui lòng truy cập các liên kết đính kèm với chúng để biết thêm chi tiết.