<!-- add-breadcrumbs -->
# In ra thô (Raw Printing)

> Được giới thiệu trong Phiên bản 12

**Việc gửi một chuỗi các lệnh trực tiếp đến máy in bằng ngôn ngữ gốc của nó được gọi là In thô (Raw Printing).**

Nhiều loại máy in nhiệt cần các lệnh thô này được gửi đến để thực hiện các chức năng như in mã vạch, in hóa đơn, in nhãn, v.v. Trong hầu hết các trường hợp, In thô bỏ qua trình điều khiển (driver) của máy in, giúp việc in ấn rất nhanh và đáng tin cậy. In thô cũng có khả năng thực hiện một số tính năng nâng cao như cắt giấy hóa đơn, đẩy ngăn kéo đựng tiền, v.v.

## 1. Thiết lập In thô trong ERPNext

### 1.1 Cài đặt ứng dụng QZ Tray trên máy tính khách

Tải xuống và cài đặt ứng dụng QZ Tray trên máy tính mà máy in nhiệt của bạn đang kết nối. Bạn có thể tìm thấy ứng dụng này tại [trang web chính thức](https://qz.io/download/). Hiện tại, QZ Tray hỗ trợ Windows, macOS và Linux. Trong quá trình cài đặt, bạn sẽ được yêu cầu cài đặt Java nếu chưa có, vui lòng cài đặt Java để hoàn tất quá trình cài đặt.

Các hướng dẫn thêm về việc cài đặt Ứng dụng QZ Tray có thể được tìm thấy [tại đây](https://qz.io/wiki/using-qz-tray).

### 1.2 Tạo Mẫu in Lệnh thô (Raw Commands Print Format)

Để có thể gửi các lệnh thô đến máy in, trước tiên bạn cần tạo một mẫu in bằng các lệnh thô. Ngôn ngữ Jinja Templating được sử dụng trong các lệnh thô tương tự như trong [mẫu in HTML tùy chỉnh](/docs/v13/user/manual/en/customize-erpnext/print-format).

Để tạo một mẫu in mới cho In thô:

1. Đi tới danh sách mẫu in: **Home > Settings > Printing > Print Format**
2. Nhấp vào New.
3. Chọn DocType liên quan.
4. Tích chọn các tùy chọn **Custom format** và **Raw Printing**.
5. Điền vào trường **Raw Commands** các lệnh thô cần thiết để gửi đến máy in.
6. Nhấp Lưu.

  ![Raw Commands Print Format](https://docs.erpnext.com/docs/v13/assets/img/setup/print/raw-command-print-format.png)

Hiện tại, bất kỳ ngôn ngữ máy in dựa trên chuỗi nào cũng có thể được sử dụng trong trường `Raw Commands` trong mẫu in. Việc viết các lệnh thô yêu cầu kiến thức về ngôn ngữ gốc của máy in do nhà sản xuất máy in cung cấp. Vui lòng tham khảo hướng dẫn dành cho nhà phát triển do nhà sản xuất máy in cung cấp về cách viết các lệnh gốc của họ.

### 1.3 Bật In thô trong Cài đặt in

Để bật In thô:

1. Đi tới: **Home > Settings > Printing > Print Settings > Raw Printing**.
2. Tích chọn tùy chọn **Enable Raw Printing**.
3. Lưu.

## 2. Các phương thức để sử dụng in thô trong ERPNext

Có hai cách để gửi lệnh In thô đến máy in của bạn.

### 2.1 Nhấp vào in trên trang xem trước bản in

Để in một mẫu in lệnh thô từ chế độ xem bản in của Tài liệu:

1. Chọn mẫu in phù hợp. Đối với mẫu in bằng Lệnh thô, thông báo "No Preview available" sẽ được hiển thị thay cho bản xem trước bản in.
2. Nhấp vào nút in.
3. Vui lòng cho phép yêu cầu kết nối từ QZ Tray cho các hành động mà bạn đã khởi tạo (Phím tắt: Alt + A).
   -  ![QZ Tray Prompt](https://docs.erpnext.com/docs/v13/assets/img/setup/print/qz-tray-prompt.png)
4. Bạn có thể được yêu cầu chọn "print format - printer mapping" (mẫu in - ánh xạ máy in).
   -  Việc ánh xạ này được sử dụng để gửi lệnh in đến máy in phù hợp.
   -  Máy in cần phải được cài đặt trên máy tính của bạn để có thể ánh xạ nó với một mẫu in.
     ![print format - printer mapping](https://docs.erpnext.com/docs/v13/assets/img/setup/print/printer-settings.png)
   -  Việc ánh xạ này được lưu cục bộ trên cùng một máy tính và sẽ phải được thiết lập trên mỗi máy khách.
   -  Bạn cũng có thể chỉnh sửa việc này bằng cách nhấp vào nút **Printer Settings**.

      ![Raw Printing from Print View](https://docs.erpnext.com/docs/v13/assets/img/setup/print/raw-printing-from-print-view.gif)

### 2.2 Gọi các hàm In thô từ một client script

Thông thường sẽ có yêu cầu rằng một lệnh in phải được thực hiện khi có một sự kiện nhất định xảy ra (như Xác nhận, Lưu, Sửa đổi, v.v.). Bạn có thể viết một [client script](/docs/v13/user/manual/en/customize-erpnext/client-scripts) để thực hiện việc này cho bạn.

Dưới đây là các hàm In thô liên quan:

1. hàm: `frappe.ui.form.qz_connect`
  - Một hàm bao bọc kết nối để thiết lập kết nối với ứng dụng QZ Tray.
  - Trả về một promise sẽ được giải quyết khi thiết lập kết nối thành công.
  - Cho phép các kết nối đang hoạt động hoặc không hoạt động đều được giải quyết. Do đó, nó có thể được gọi mỗi khi trước khi gửi một lệnh.
  - Ví dụ sử dụng:

```
    frappe.ui.form.qz_connect()
    .then(function () {
        return qz.print(config, data);
    })
    .then(frappe.ui.form.qz_success)
    .catch(err => {
        frappe.ui.form.qz_fail(err);
    });
```

Ở đây, `qz` là một đối tượng toàn cục được cung cấp bởi thư viện `qz-tray.js`.

2. hàm: `frappe.ui.form.qz_get_printer_list`
  - Cung cấp cho bạn danh sách các máy in có sẵn cho ứng dụng QZ Tray.
  - Trả về một promise sẽ giải quyết thành một danh sách các máy in.

  Ví dụ sử dụng:
```
     frappe.ui.form.qz_get_printer_list().then(
           // Hành động bắt buộc khi nhận được danh sách máy in.
           // Lưu ý: Danh sách máy in là một mảng các chuỗi.
      );
```

3. hàm: `frappe.ui.form.qz_success`
  - Hiển thị thông báo "Print Sent to the printer!" (Đã gửi lệnh in đến máy in!) cho người dùng. Có thể được gọi sau khi lệnh in thành công.

4. hàm: `frappe.ui.form.qz_fail`
  - Hiển thị thông báo lỗi cho người dùng. Nên được gọi khi kết nối QZ Tray thất bại.

Bạn cũng có thể truy cập trực tiếp các hàm được cung cấp bởi thư viện `qz-tray.js` thông qua đối tượng `qz`. [Nhấp vào đây để xem tài liệu thư viện qz-tray.js](https://qz.io/api/). Lưu ý: Đối tượng `qz` chỉ được khởi tạo sau khi gọi `frappe.ui.form.qz_connect` lần đầu tiên. Trong trường hợp bạn cần đối tượng `qz` trước đó, bạn có thể sử dụng `frappe.ui.form.qz_init`.

### 3. Các chủ đề liên quan
1. [Cài đặt in](/docs/v13/user/manual/en/setting-up/print/print-settings)
1. [Mẫu in](/docs/v13/user/manual/en/setting-up/print/print-format)
1. [Kiểu in](/docs/v13/user/manual/en/setting-up/print/print-style)