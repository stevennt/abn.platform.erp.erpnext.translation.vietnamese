<!-- add-breadcrumbs -->
# DocType

**DocType là thành phần cốt lõi của bất kỳ ứng dụng nào dựa trên Frappe Framework.**

Nó mô tả Mô hình (Model) và Chế độ xem (View) cho dữ liệu của bạn. Nó chứa các trường nào được lưu trữ cho dữ liệu của bạn, và cách chúng hoạt động với nhau. Nó chứa thông tin về cách dữ liệu của bạn được đặt tên. Các biểu mẫu như Đơn bán hàng, Hóa đơn bán hàng, Lệnh sản xuất được thêm vào dưới dạng các DocType ở phía backend.

DocType cho phép bạn chèn các biểu mẫu tùy chỉnh vào ERPNext theo yêu cầu của mình.

Đọc [tài liệu DocType](https://frappe.io/docs/v13/user/en/understanding-doctypes) để hiểu thêm.

Để tạo một DocType mới, hãy đi tới:

> Setup > Customize > Doctype > New

## 1. Cách tạo một DocType mới:

1. **Name**: Nhập tên của DocType mới.
1. **Module**: Nhập module mà bạn muốn thêm DocType mới vào.
1. Lưu.

![Custom DocType](https://docs.erpnext.com/docs/v13/assets/img/customize/doctype-employee-transfer.png)

### 1.1. Chi tiết bổ sung

1. **Fields**

 Bạn có thể chọn thêm bao nhiêu trường tùy ý. Nhãn (Label), Loại trường (Field Type), Các trường bắt buộc (Mandatory Fields) và các Tùy chọn (Options) liên quan khác cũng có thể được thêm tại đây. Tìm hiểu thêm về các loại trường [tại đây](/docs/v13/user/manual/en/customize-erpnext/articles/field-types.html).

 ![Fields in Custom DocType](https://docs.erpnext.com/docs/v13/assets/img/customize/doctype-employee-transfer-fields.png)

1. **Naming**

 Tại đây bạn có thể chọn xem có muốn mỗi biểu mẫu trong DocType này được đặt tên tự động hay không. Như đã nêu trong phần mô tả, bạn có thể chọn mẫu để đặt tên cho các biểu mẫu. Mẫu này có thể là một Trường trong DocType, Chuỗi đặt tên (Naming Series), Nhắc nhở (Prompt), Một Chuỗi đặt tên đã xác định, hoặc Tên dựa trên Định dạng (Format based Name). Đối với việc đặt tên, bạn cũng có thể thêm Mô tả (Description) và Kiểu chữ (Name Case - như Title Case hoặc UPPER CASE) để thuận tiện cho mình.

 ![Naming Custom DocType](https://docs.erpnext.com/docs/v13/assets/img/customize/doctype-employee-transfer-naming.png)

1. **Form Settings**

 Các Cài đặt bổ sung cho Biểu mẫu, Trường hình ảnh, Tệp đính kèm, Dòng thời gian (Timeline), v.v. có thể được cấu hình tại đây. Để biết thêm về Biểu mẫu, hãy truy cập [Customize Form](/docs/v13/user/manual/en/customize-erpnext/customize-form).

 ![Custom DocType Form Settings](https://docs.erpnext.com/docs/v13/assets/img/customize/doctype-employee-transfer-form-settings.png)

1. **View Settings**

 Tại đây, bạn có thể xác định các cài đặt Chế độ xem cho DocType, như, Các trường tìm kiếm (Search Fields), Trường sắp xếp mặc định (Default Sort Field), Thứ tự sắp xếp mặc định (Default Sort Order), v.v.

1. **Permission Rules**

 Bạn có thể xác định các Quy tắc phân quyền cho DocType tại đây, và cấu hình những người dùng nào sẽ có thể sử dụng hoặc thực hiện thay đổi đối với DocType này. Tìm hiểu thêm về [Người dùng và Phân quyền](/docs/v13/user/manual/en/setting-up/users-and-permissions) tại đây.

 ![Custom DocType Permissions](https://docs.erpnext.com/docs/v13/assets/img/customize/doctype-employee-transfer-permissions.png)

1. **Web View**

 Bạn có thể chọn xem mình có muốn có Chế độ xem Web (Web View) cho DocType này hay không. Việc có Chế độ xem Web cho một DocType sẽ cho phép người dùng website của bạn có quyền truy cập vào các Biểu mẫu. Hãy tìm hiểu thêm về [Người dùng Website](/docs/v13/user/manual/en/setting-up/articles/difference-between-system-user-and-website-user).

### 1.2. Các thuộc tính khác

1. **Is Submittable**: Bạn có thể chọn xem bạn muốn DocType này chỉ được 'Lưu' hay cũng được 'Xác nhận' bằng cách tích hoặc bỏ tích ô này.
1. **Is Child Table**: Bạn có thể xác định xem có muốn DocType mới là một Bảng con (Child Table) trong một DocType khác hay không. Xem [Child Table](/docs/v13/user/manual/en/customize-erpnext/articles/customizing-data-visibility-in-child-table) để biết thêm thông tin.
1. **Is Single**: Nếu được tích, Doctype này sẽ trở thành một biểu mẫu duy nhất, giống như Đơn bán hàng, mà người dùng sẽ không thể tạo lại nhiều bản ghi. Ví dụ: Cài đặt Bán hàng trong Phân hệ Bán hàng là một DocType Single.
1. **Is Tree**: Một số DocType trong ERPNext được cấu trúc dưới dạng Cây (Tree), trong đó có một số DocType Cha và một số DocType Con. Ví dụ: DocType Công ty được cấu trúc dưới dạng Cây, có các Công ty mẹ cũng như các Công ty con, mà chúng ta gọi là công ty con. Nếu bạn muốn các DocType của mình được cấu trúc tương tự, bạn có thể bật tùy chọn này.

    ![DocType Tree View](https://docs.erpnext.com/docs/v13/assets/img/customize/doctype-treeview.png)

1. **Quick Entry**: Bạn có thể chọn xem có muốn tạo Nhập nhanh (Quick Entry) cho DocType này hay không. Điều này sẽ cho phép bạn chỉ nhập một vài chi tiết bắt buộc và Lưu DocType để tạo một bản Nhập nhanh. Ví dụ, tích vào Quick Entry trong [Bút toán](/docs/v13/user/manual/en/accounts/journal-entry#11-quick-entry).
1. **Track Changes**: Bạn có thể chọn tùy chọn này nếu muốn duy trì nhật ký các thay đổi được thực hiện đối với mỗi Biểu mẫu. Xem [Phiên bản tài liệu](/docs/v13/user/manual/en/using-erpnext/document-versioning) để hiểu thêm về điều này.
1. **Track Seen**: Bạn có thể chọn tùy chọn này nếu muốn duy trì nhật ký của tất cả Người dùng đã xem Biểu mẫu này.
1. **Track Views**: Bạn có thể chọn tùy chọn này nếu muốn duy trì nhật ký về tất cả các lần mỗi Người dùng đã Xem Biểu mẫu này.

  ![DocType Tree View](https://docs.erpnext.com/docs/v13/assets/img/customize/doctype-track-views.png)

1. **Custom?**: Trường này sẽ được tích mặc định khi thêm DocType Tùy chỉnh. Tương tự, nếu bạn đang tùy chỉnh một DocType đã tồn tại trong hệ thống, trường này mặc định sẽ không được tích.

## 2. Video

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/WSzkpPm3iIU?start=585" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

{next}