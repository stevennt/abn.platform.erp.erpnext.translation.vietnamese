<!-- add-breadcrumbs -->
# Nhóm tài sản

**Một Nhóm tài sản phân loại các tài sản khác nhau của một Công ty.**

Bước đầu tiên hướng tới quản lý tài sản là tạo một Nhóm tài sản dựa trên loại tài sản. Ví dụ, tất cả máy tính để bàn và máy tính xách tay của bạn có thể thuộc về một Nhóm tài sản có tên là "Thiết bị điện tử".

Trong Nhóm tài sản, bạn có thể thiết lập mặc định phương pháp khấu hao, kỳ hạn và các tài khoản liên quan đến khấu hao, những thiết lập này sẽ áp dụng cho tất cả các tài sản thuộc nhóm đó.

> **Lưu ý:** Bạn cũng có thể thiết lập mặc định các Tài khoản liên quan đến khấu hao và Trung tâm chi phí trong danh mục Công ty.

Để truy cập danh sách Nhóm tài sản, hãy đi tới:
> Home > Asset > Asset Category

## 1. Cách tạo một Nhóm tài sản
1. Nhập tên cho Nhóm tài sản.
1. Tích chọn 'Enable Capital Work in Progress Accounting' nếu bạn muốn duy trì hồ sơ của các tài sản dưới một tài khoản bảng cân đối kế toán tạm thời thay vì tài khoản tài sản tương ứng. Để biết thêm, [truy cập trang này](./purchasing-an-asset.md).
1. Lưu.

    ![Asset Category](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-category.png)

### 1.1 Các tùy chọn bổ sung khi tạo Nhóm tài sản
1. **Enable Capital Work in Progress Accounting**: Khi bật tính năng này, bút toán kế toán cho các tài sản thuộc nhóm này mà chưa được đưa vào sử dụng sẽ được ghi vào các tài khoản Chi phí xây dựng cơ bản dở dang (CWIP). Điều này xảy ra khi bạn sở hữu Tài sản nhưng nó chưa được sử dụng, tức là 'Available for Use Date' được thiết lập vào một ngày muộn hơn. Nếu bạn sử dụng tất cả tài sản của mình ngay lập tức, hãy tắt tính năng này. Khi tắt, kế toán CWIP sẽ được bỏ qua.

## 2. Các tính năng
### 2.1 Chi tiết Sổ tài chính (Finance Book)
Bạn có thể liên kết một Sổ tài chính nếu bạn báo cáo khấu hao theo các cách khác nhau. Bạn có thể nhập các trường sau:

* **Depreciation Method**: Chọn phương pháp khấu hao mà bạn sẽ dùng để ghi nhận khấu hao của các tài sản trong nhóm này. Để biết thêm, [truy cập trang này](./asset-depreciation.md).
* **Frequency of Depreciation (Months)**: Số tháng mà trong đó khấu hao sẽ được ghi sổ. Tài sản có thể bị thanh lý sau thời gian này.
* **Total Number of Depreciations**: Số lần khấu hao sẽ được ghi sổ trong khung thời gian đã chọn.
* **Rate of Depreciation**: Tỷ lệ khấu hao áp dụng cho khoảng thời gian đã chọn. Tỷ lệ này sẽ được tính toán dựa trên Phương pháp khấu hao đã chọn.

### 2.2 Chi tiết Kế toán

Các chi tiết tài khoản sau đây có thể được thiết lập để ghi nhận giá trị tài sản trong sổ cái:

* Công ty
* Tài khoản Tài sản cố định
* Tài khoản Khấu hao lũy kế
* Tài khoản Chi phí khấu hao
* Tài khoản Chi phí xây dựng cơ bản dở dang

## 3. Các chủ đề liên quan
1. [Asset](./asset.md)

{next}