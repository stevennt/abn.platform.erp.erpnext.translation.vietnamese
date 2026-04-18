<!-- add-breadcrumbs -->

# Trường tùy chỉnh (Custom Field)

**Mọi biểu mẫu trong ERPNext đều có một bộ các trường tiêu chuẩn. Nếu bạn cần ghi lại một số thông tin nhưng không có Trường tiêu chuẩn nào có sẵn cho thông tin đó, bạn có thể chèn Trường tùy chỉnh vào biểu mẫu theo yêu cầu của mình.**

Bạn có thể đi tới [Tùy chỉnh Biểu mẫu (Customize Form)](/docs/v16/user/manual/en/customize-erpnext/customize-form) và thêm Trường vào một Biểu mẫu hoặc một loại Tài liệu _(sau đây gọi là DocType)_ cụ thể.

Để truy cập Trường tùy chỉnh, hãy đi tới:

> Trang chủ > Tùy chỉnh > Tùy chỉnh Biểu mẫu > Trường tùy chỉnh (Custom Field)

Bạn cũng có thể đi tới chế độ xem danh sách của bất kỳ DocType nào và chọn Tùy chỉnh (Customize) từ các tùy chọn Menu.

![Tùy chọn Tùy chỉnh trong Chế độ xem danh sách](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-option-in-list-view.png)

## 1. Cách tạo Trường tùy chỉnh

1. Đi tới danh sách Trường tùy chỉnh và nhấp vào Mới (New).
2. **Document**: Chọn Tài liệu mà bạn cần thêm Trường tùy chỉnh.
3. **Label**: Nhập Nhãn mà bạn muốn đặt cho Trường tùy chỉnh của mình.
4. **Field Type**: ERPNext đã có sẵn một bộ các Loại trường có thể được lấy từ menu thả xuống này. Bạn có thể chọn Loại cho Trường tùy chỉnh của mình từ menu này.
5. Cập nhật.

![Trường tùy chỉnh mới](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/new-custom-field.png)

  *Tìm hiểu thêm về các Loại trường [tại đây](/docs/v16/user/manual/en/customize-erpnext/articles/field-types.html).*

Bạn cũng có thể đi tới [Tùy chỉnh Biểu mẫu (Customize Form)](/docs/v16/user/manual/en/customize-erpnext/customize-form) để thêm, chỉnh sửa hoặc xóa một Trường trong một Biểu mẫu cụ thể.

![Thêm Trường tùy chỉnh từ Tùy chỉnh Biểu mẫu](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-erpnext-custom-field-from-customize-form.gif)

### 1.1. Chi tiết bổ sung

1. **Options**: Trường này sẽ xuất hiện khi bạn muốn dữ liệu của mình mang tính cụ thể hoặc chỉ định dữ liệu. Ví dụ: khi bạn đã chọn Loại trường là 'Select Field' (Trường lựa chọn), bạn sẽ cần nhập các tùy chọn lựa chọn tại đây.

  ![Trường tùy chỉnh với Loại trường là Select](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/custom-field-with-select-fieldtype.png)

1. **Fetch From**: Khi bạn muốn Trường tùy chỉnh là 'Link Field' (Trường liên kết), bạn sẽ cần chỉ định Biểu mẫu mà Trường này sẽ được liên kết tới. Ví dụ: bạn muốn tạo một Trường tùy chỉnh 'Project' (Dự án) trong DocType 'Item' (Mặt hàng). Bạn sẽ cần thiết lập Loại trường là 'Link' và nhập 'Project' vào trường Fetch From để đảm bảo rằng Trường được cập nhật với danh sách tất cả các DocType cần thiết.
1. **Fetch If Empty**: Ô kiểm này sẽ đảm bảo rằng Trường này sẽ không bị ghi đè dựa trên Fetch From nếu giá trị đã tồn tại.
1. **Default Value**: Nhập giá trị mặc định của Trường mà bạn muốn được lấy cho Trường này.
1. **Depends On**: Bạn có thể xác định một điều kiện tại đây để Trường được hiển thị. Ví dụ: trong DocType Item, hai trường 'Asset Category' (Danh mục tài sản) và 'Asset Naming Series' (Chuỗi đặt tên tài sản) sẽ chỉ xuất hiện nếu Trường 'Is Fixed Asset' (Là tài sản cố định) được tích chọn. Điều kiện phụ thuộc ở đây sẽ là `is_fixed_asset`.

  ![Tùy chọn Depends On](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/custom-field-dpends-on.png)

1. **Field Description**: Bạn có thể thêm mô tả của Trường tại đây, mô tả này có thể được hiển thị bên dưới Trường này.

   ![Mô tả Trường tùy chỉnh](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/custom-field-description.png)

1. **Permission Level**: Tùy chọn này cho phép bạn chỉ định vai trò nào trong tổ chức của mình sẽ có thể chỉnh sửa Trường này. Bạn có thể xem [Phân quyền dựa trên Vai trò (Role Based Permissions)](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions) để hiểu thêm về phần này.
1. **In Preview**: Nếu [Hiển thị cửa sổ xem trước (Show Preview Popup)](/docs/v16/user/manual/en/customize-erpnext/customize-form#13-more-properties) cho loại tài liệu được tích chọn, Trường sẽ được bao gồm trong cửa sổ hiện ra khi di chuột qua các liên kết của loại tài liệu (trong chế độ xem danh sách và các trường liên kết khác).
1. **Width**: Tùy chọn này sẽ xác định độ rộng được phân bổ cho Trường này khi xem Biểu mẫu ở Chế độ xem lưới (Grid View).

### 1.2. Các thuộc tính khác

* **Is Mandatory Field**: Có thể tích chọn ô này nếu bạn muốn bắt buộc phải nhập Trường này khi Xác nhận một DocType.
* **Unique**: Tích vào ô này khi bạn muốn giá trị của Trường này là duy nhất. Điều này có thể được thực hiện trong các trường hợp Trường tùy chỉnh dùng cho mã hoặc Số định danh. Ví dụ: Mã mặt hàng (Item Code) đối với Mặt hàng, Mã số thuế (GST Number) đối với Khách hàng.
* **Read Only**: Khi bạn muốn Trường này là trường chỉ đọc hoặc không thể chỉnh sửa. Trong trường hợp này, giá trị của Trường sẽ được tự động lấy từ các trường khác.
* **Hidden**: Tích vào Trường này khi bạn muốn ẩn Trường này, hoặc ẩn một Trường hiện có.
* **Print Hide**: Trong trường hợp bạn muốn nút in được ẩn khỏi Mẫu in. Hãy xem [Các trường trong Mẫu in (Fields in Print Format)](/docs/v16/user/manual/en/customize-erpnext/articles/making-fields-visible-in-print-format) để biết thêm thông tin.
* **No Copy**: Việc tích vào ô này sẽ hạn chế việc sao chép Trường này trong DocType.
* **Allow on Submit**: Tùy chọn này cho phép bạn thực hiện thay đổi đối với Trường ngay cả sau khi bạn đã Xác nhận Biểu mẫu. Hãy xem [Chỉnh sửa giá trị trong Tài liệu đã Xác nhận (Editing Value in Submitted Document)](/docs/v16/user/manual/en/customize-erpnext/articles/allow-fields-to-be-changed-after-submission) để biết thêm thông tin.
* **In List View**: Tùy chọn này sẽ làm cho trường hiển thị trong Chế độ xem danh sách của DocType.
* **In Standard Filter**: Trường sẽ trở thành một bộ lọc tiêu chuẩn trong Chế độ xem danh sách của Tài liệu.
* **In Global Search**: Khi ô này được tích, Trường này có thể được tìm thấy thông qua thanh tìm kiếm toàn cầu.