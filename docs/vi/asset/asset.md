<!-- add-breadcrumbs -->
# Tài sản

**Tài sản là bất kỳ Mặt hàng có giá trị nào thuộc sở hữu của một Công ty.**

Nội thất, máy tính, điện thoại di động, máy in, ô tô, thiết bị sản xuất là những ví dụ về tài sản. Thông thường, một tài sản là một vật hữu hình nằm trong khuôn viên công ty hoặc được nhân viên mang theo. Trong một số trường hợp, tài sản có thể là một vật vô hình.

Thời gian sử dụng hữu ích của một tài sản kéo dài qua nhiều năm và do đó giá trị kinh tế của nó được phân bổ qua các năm tương ứng từ góc độ kế toán. Nếu bạn mua một chiếc máy in với giá $300 và nó dự kiến sẽ hữu dụng trong ba năm, từ góc độ kế toán, mỗi năm sẽ ghi nhận $100 là chi phí thay vì ghi nhận toàn bộ $300 vào năm đầu tiên. Hầu hết các quốc gia đều có quy định cho các cách tính toán như vậy.

Trong ERPNext, bản ghi Tài sản là trung tâm của mô-đun quản lý tài sản. Tất cả các giao dịch liên quan đến Tài sản như mua hàng, khấu hao, bảo trì, di chuyển, thanh lý, bán hàng sẽ được ghi nhận dựa trên bản ghi Tài sản.

Để truy cập danh sách Tài sản, hãy đi tới:
> Home > Assets > Assets > Asset

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Tài sản, bạn nên tạo các mục sau trước:

* [Mặt hàng](../stock/item.md) với tùy chọn 'Is Fixed Asset' được bật.
* [Danh mục tài sản](asset-category.md)

## 2. Cách tạo một Tài sản

Một Mặt hàng đại diện cho tài sản cần được tạo. Mục **'Maintain Stock'** nên được **bỏ chọn** và **'Is Fixed Asset'** phải được **chọn**.

<img class="screenshot" alt="Asset Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-item.png">

### 2.1 Tự động tạo tài sản

Bạn có thể cấu hình ERPNext để tự động tạo tài sản khi Xác nhận Phiếu nhập hàng bằng cách bật **'Auto Create Assets on Purchase'** trong Mặt hàng.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-auto-create.png">

Nếu bạn đã bật tính năng tự động tạo tài sản cho mặt hàng đại diện cho tài sản, bạn sẽ phải cung cấp vị trí tài sản khi Xác nhận Phiếu nhập hàng.

<img class="screenshot" alt="Asset Location in Purchase Receipt" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-location-in-purchase-receipt.png">

Một thông báo xác nhận việc tạo tài sản sẽ được hiển thị khi Xác nhận Phiếu nhập hàng.

<img class="screenshot" alt="Asset Creation Confirmation Message" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-auto-create-on-purchase.png">

### 2.2 Tạo tài sản thủ công

Nếu bạn muốn tạo tài sản thủ công, hãy tạo một Mặt hàng với 'Is Fixed Asset' được bật và để 'Auto Create Assets on Purchase' không được chọn. Khi Xác nhận Phiếu nhập hàng/Hóa đơn mua hàng có Mặt hàng đó, một thông báo sẽ hiển thị cho biết bạn cần tạo tài sản thủ công.

<img class="screenshot" alt="Manual Creation of Assets" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-manual-creation-message.png">

Thực hiện theo các bước dưới đây để tạo tài sản thủ công.

1. Đi tới danh sách Tài sản, nhấn vào Mới.
1. Nhập tên cho tài sản.
2. Chọn Mã mặt hàng. Tên mặt hàng và Danh mục tài sản sẽ được lấy tự động.
3. Chọn Chủ sở hữu tài sản, tức là Công ty, Nhà cung cấp hoặc Khách hàng.
4. Chọn Công ty/Nhà cung cấp/Khách hàng.
5. Chọn Phiếu nhập hàng/Hóa đơn mua hàng. Ngày mua và Tổng số tiền mua sẽ được lấy tự động.
6. Chọn một Vị trí. Ví dụ: Văn phòng Mumbai. Thông tin này sẽ được lấy tự động nếu được chỉ định trong bảng mặt hàng của Phiếu nhập hàng.
7. Thiết lập Ngày sẵn sàng sử dụng. Khấu hao sẽ được tính bắt đầu từ ngày này.
8. Lưu và Xác nhận.

Vui lòng lưu ý rằng bạn cần **tạo một bản ghi tài sản cho mỗi tài sản bạn đã mua**. Nếu bạn mua năm chiếc máy tính và chỉ tạo một Phiếu nhập hàng với số lượng là năm, thì bạn sẽ phải tạo thủ công năm bản ghi tài sản.

### 2.3 Nhập tài sản hiện có

Khi bạn chuyển từ hệ thống cũ sang ERPNext, bạn sẽ phải thêm chi tiết của tất cả các tài sản mà công ty bạn đã mua trước đó cùng với chi tiết khấu hao của từng tài sản.

Đối với một tài sản hiện có, bạn có thể tạo bản ghi tài sản trực tiếp bằng cách tích vào ô **"Is Existing Asset"** và cung cấp các chi tiết dưới đây.

* Tổng số tiền mua
* Ngày mua
* Ngày sẵn sàng sử dụng
* Khấu hao lũy kế đầu kỳ: Số tiền khấu hao lũy kế đã được ghi nhận cho một tài sản hiện có.
* Số lần khấu hao đã ghi nhận: Số lượng các bút toán khấu hao đã được ghi nhận.

Dựa trên các chi tiết này, lịch trình khấu hao cho số tiền còn lại sẽ được tạo tự động.

<img class="screenshot" alt="Existing Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/existing-asset.png">

Để biết thêm, hãy truy cập trang [Mua một Tài sản](purchasing-an-asset.md).


### 2.4 Các tùy chọn bổ sung khi tạo Tài sản

1. **Người quản lý (Custodian)**: Nhân viên sẽ quản lý tài sản.
2. **Phòng ban**: Phòng ban của Người quản lý.
3. **Ngày khấu hao tiếp theo**: Ghi ngày khấu hao tiếp theo, ngay cả khi đó là lần đầu tiên. Nếu tài sản là tài sản hiện có và việc khấu hao đã hoàn tất, hãy để trống.
4. **Tính khấu hao**: Bật ô này để tính khấu hao của Tài sản.
5. **Cho phép khấu hao hàng tháng**: Bật ô này để phân bổ số tiền khấu hao của một tài sản vào 12 tháng trong năm. Các bút toán khấu hao sẽ được thực hiện hàng tháng vào ngày được cung cấp làm Ngày bắt đầu khấu hao. Ví dụ, nếu Ngày sẵn sàng sử dụng là 22/11/2019 và Ngày bắt đầu khấu hao là 31/03/2020, lần khấu hao đầu tiên sẽ được thực hiện vào 30/11/2019, lần thứ hai vào 31/12/2019, v.v. Số tiền sẽ được phân bổ dựa trên số ngày còn lại cho đến kỳ khấu hao tiếp theo.

## 4. Các tính năng

### 4.1 Khấu hao

* **Tần suất khấu hao (Tháng)**: Số tháng giữa các lần khấu hao.
* **Tổng số lần khấu hao**: Tổng số lần khấu hao trong suốt thời gian sử dụng hữu ích của Tài sản. Trong trường hợp tài sản hiện có đã được khấu hao một phần, hãy ghi số lần khấu hao còn lại. Ví dụ, nếu