<!-- add-breadcrumbs -->
# Tích hợp WooCommerce

Sử dụng Tích hợp WooCommerce, hệ thống sẽ tạo Đơn bán hàng trong ERPNext cho các đơn hàng được tạo trên WooCommerce thông qua webhook của WooCommerce.

Khi tạo Đơn bán hàng từ WooCommerce, nếu Khách hàng hoặc Mặt hàng còn thiếu trong ERPNext, hệ thống sẽ tạo mới Khách hàng/Mặt hàng bằng cách sử dụng các chi tiết tương ứng từ dữ liệu đơn hàng WooCommerce. Hệ thống cũng tạo Địa chỉ liên kết với Khách hàng bằng cách sử dụng thông tin giao hàng từ dữ liệu đơn hàng.

## 1. Cách thiết lập WooCommerce?

### 1.1 Tạo API Key và API Secret

1. Từ thanh bên của trang web WooCommerce, nhấp vào Cài đặt (Settings).
2. Nhấp vào tab "Advanced" sau đó nhấp vào liên kết REST API.

    ![Woocommerce API](https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/wc-add-key.png)

3. Nhấp vào nút "Add key". Cung cấp các chi tiết cần thiết và nhấp vào nút "Generate API key".

    ![Woocommerce API Key](https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/wc-generate-keys.png)

### 1.2 Cài đặt Woocommerce

1. Trên trang ERPNext của bạn, đi đến: **Home > Integrations > Settings > Woocommerce Settings**.
2. Dán API key và secret đã tạo ở bước trước vào các trường "API consumer key" và "API consumer secret".
3. Trong trường "Woocommerce Server URL", hãy dán URL trang web WooCommerce của bạn.
4. Đảm bảo rằng "Enable Sync" đã được tích chọn.
5. Chọn "Tax Account" và "Freight and Forwarding Account" trong phần Account Details.
6. Chọn "Creation User" trong phần Defaults. Người dùng này sẽ được sử dụng để tạo Khách hàng, Mặt hàng và Đơn bán hàng. Đảm bảo rằng người dùng có các quyền liên quan.
7. Chọn "Công ty" (Company) sẽ được sử dụng để tạo Đơn bán hàng.
8. Nhấp Lưu (Save).
9. Sau khi lưu Cài đặt Woocommerce, "Secret" và "Endpoint" sẽ được tạo tự động.

![Woocommerce Settings](https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/woocommerce-settings.png)

### 1.3 Cài đặt Webhook Woocommerce

1. Bây giờ từ thanh bên của trang web woocommerce, đi đến Cài đặt (Settings).
2. Nhấp vào tab "Advanced" sau đó nhấp vào liên kết Webhooks và sau đó nhấp vào nút "Add webhook".
3. Đặt tên cho webhook tùy ý bạn.
4. Nhấp vào menu thả xuống Status và chọn "Active".
5. Chọn Topic là "Order created".
6. Sao chép "Endpoint" từ DocType "Woocommerce Settings" trong trang ERPNext của bạn và dán vào trường "Delivery URL".
7. Sao chép "Secret" từ DocType "Woocommerce Settings" trong trang ERPNext của bạn và dán vào trường "Secret".
8. Giữ nguyên API VERSION và nhấp vào Lưu Webhook (Save Webhook). Bây giờ nó đã được thiết lập thành công.

![Woocommerce Webhook](https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/wc-webhook.png)

Một ảnh GIF dưới đây để hiển thị toàn bộ quy trình:

![Woocommerce Set Up](https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/woocommerce-setup.gif)

> **Lưu ý:** Trong ảnh chụp màn hình và GIF ở trên, thay vì URL giao hàng trên trang web woocommerce, bạn cần dán URL mà bạn sẽ nhận được sau khi lưu "Woocommerce Settings" vào trường "Endpoint" trong bản cài đặt ERPNext của mình. Ở đây, một URL khác đã được dán vì đang sử dụng localhost.

### 1.4 Tạo đơn hàng và đồng bộ hóa Woocommerce

1. Từ trang web Woocommerce của bạn, hãy đăng ký làm người dùng tại trang Tài khoản (Account).
2. Bây giờ nhấp vào tùy chọn Địa chỉ (Addresses) và cung cấp các chi tiết bắt buộc.
3. Nhấp vào tùy chọn "Shop" và bây giờ có thể thấy các sản phẩm hiện có.
4. Thêm các sản phẩm mong muốn vào giỏ hàng và nhấp vào **View Cart**.
5. Từ giỏ hàng, sau khi bạn đã thêm các sản phẩm mong muốn, bạn có thể nhấp vào "Proceed to Checkout".
6. Tất cả chi tiết thanh toán và chi tiết Đơn hàng có thể được xem lúc này. Khi bạn đã đồng ý với các thông tin đó, hãy nhấp vào nút **Place Order**.
7. Thông báo "Order Received" sẽ xuất hiện cho biết đơn hàng đã được đặt thành công.
8. Bây giờ trên bản cài đặt ERPNext của bạn, hãy kiểm tra các DocType sau: Khách hàng (Customer), Địa chỉ (Address), Mặt hàng (Item), Đơn bán hàng (Sales Order). Chúng sẽ được lấy về và tạo từ dữ liệu webhook.
9. Trong trường hợp các đơn hàng không được đồng bộ, bạn có thể kiểm tra lỗi trong **Home > Settings > Core > Error Log**.

![Woocommerce Set Up](https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/woocommerce-order.gif)

## 2. Các tính năng

### 2.1 Mặc định (Defaults)

Trong DocType Woocommerce Settings:

- **Warehouse**: Kho này sẽ được sử dụng để tạo Đơn bán hàng. Kho mặc định là "Stores".
- **Delivery After (Days)**: Đây là khoảng thời gian (ngày) mặc định cho Ngày giao hàng trong Đơn bán hàng. Khoảng thời gian mặc định là 7 ngày kể từ ngày đặt hàng.
- **Sales Order Series**: Bạn có thể thiết lập một chuỗi riêng cho các Đơn bán hàng được tạo thông qua woocommerce. Chuỗi mặc định là "SO-WOO-".
- **UOM**: Đây là Đơn vị tính mặc định được sử dụng cho Mặt hàng và Đơn bán hàng. Đơn vị tính mặc định là "Nos".

![Woocommerce Defaults](https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/wc-defaults.png)

## 3. Các chủ đề liên quan
1. [Đơn bán hàng](../user/manual/en/selling/sales-order)
2. [Mặt hàng](../user/manual/en/stock/item)
3. [Khách hàng](../user/manual/en/CRM/customer)
4. [Địa chỉ](../user/manual/en/CRM/address)