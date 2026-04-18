<!-- add-breadcrumbs -->
# Xét nghiệm Lab

**Xét nghiệm Lab cho phép ghi lại nhiều chi tiết xét nghiệm phòng thí nghiệm bao gồm vi sinh vật, độ nhạy cảm, v.v.**

ERPNext Healthcare cho phép bạn quản lý phòng xét nghiệm lâm sàng một cách hiệu quả bằng cách cho phép bạn nhập các xét nghiệm lab và in hoặc gửi email kết quả xét nghiệm, quản lý các mẫu đã thu thập, tạo hóa đơn, v.v. Bạn có thể cấu hình Mẫu xét nghiệm Lab cho từng Xét nghiệm và định dạng kết quả của nó hoặc tạo mẫu mới như được giải thích trong [Thiết lập Phòng xét nghiệm](setup_laboratory.md)

Sau khi bạn đã cấu hình tất cả các Mẫu xét nghiệm Lab cần thiết, bạn có thể bắt đầu tạo các Xét nghiệm Lab bằng cách chọn một Mẫu xét nghiệm mỗi khi bạn tạo một Xét nghiệm.

## 1. Cách tạo một Xét nghiệm Lab

Để tạo một Xét nghiệm Lab, hãy đi tới:

> Home > Healthcare > Laboratory > Lab Test > New Lab Test

1. Thiết lập Naming Series.
2. Chọn [Mẫu xét nghiệm Lab](lab_test_template.md). Khoa Y tế sẽ tự động được lấy từ mẫu.
3. Chọn Bệnh nhân. Chi tiết bệnh nhân sẽ được tự động lấy ra.
4. Bạn có thể tùy chọn chọn Người thực hành yêu cầu và Kỹ thuật viên phòng Lab.
5. Lưu.
6. Sau khi lưu, tất cả dữ liệu đã được cấu hình trong mẫu sẽ được lấy và thiết lập trong tài liệu xét nghiệm lab.
7. Bạn có thể thay đổi dữ liệu đã cấu hình trước theo yêu cầu của mình. Thêm nhận xét nếu có, trong phần Ghi chú.

    ![Lab Test](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/lab-test.png)

8. Khi có kết quả, bạn có thể nhập chi tiết kết quả vào tài liệu Xét nghiệm Lab. Tất cả các thiết lập sẵn, Giá trị bình thường, v.v. như đã cấu hình trong Mẫu xét nghiệm Lab đều có sẵn trong Xét nghiệm Lab để dễ dàng nhập dữ liệu.

Ví dụ, Xét nghiệm theo nhóm:
    ![Lab Result](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/lab_test_2.png)

Xét nghiệm mô tả:
    ![Lab Result](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/lab-result.png)

Các thành phần mà mục _Cho phép để trống_ không được tích sẽ báo lỗi xác thực nếu để trống khi Xác nhận.

    ![Lab Result](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/result-mandatory.png)

## 2. Các tính năng

### 2.1 Tạo nhiều Xét nghiệm Lab

Bạn cũng có thể sử dụng tùy chọn "Tạo nhiều" từ danh sách xem Xét nghiệm Lab để tạo tất cả các xét nghiệm lab đã được đặt hoặc lập hóa đơn cho một bệnh nhân. Bạn có thể tạo nhiều xét nghiệm lab từ một Hóa đơn bán hàng hoặc Cuộc gặp bệnh nhân đã được tạo trước đó.

![Lab Test Multiple](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/lab_test_3.png)

Bạn có thể chọn Bệnh nhân và sau đó chọn Cuộc gặp hoặc Hóa đơn mà bạn cần lấy các xét nghiệm mà không cần phải mở Cuộc gặp/Hóa đơn bán hàng để tìm các đơn hàng.

![Lab Test](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient-encounter-lab-tests-1.png)

Các xét nghiệm được chỉ định trong phần Khám bệnh của Cuộc gặp bệnh nhân đó sẽ được lấy ra.

![Lab Test](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient-encounter-lab-tests.png)

![Lab Test](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient-encounter-lab-tests-2.png)

Trong trường hợp Hóa đơn bán hàng, các mặt hàng (các mặt hàng trong Mẫu xét nghiệm Lab) được tính phí trong hóa đơn sẽ được lấy để tạo các Xét nghiệm Lab.

### 2.2 Tự động tạo tài liệu Thu thập mẫu

Nếu Mẫu xét nghiệm Lab có cấu hình thu thập mẫu, thì khi tạo Xét nghiệm Lab, (các) tài liệu thu thập mẫu sẽ được tạo tự động. Để tạo tài liệu Thu thập mẫu cho mọi Xét nghiệm Lab, hãy bật tùy chọn _Tạo tài liệu Thu thập mẫu cho Xét nghiệm Lab_ trong Cài đặt Healthcare và cấu hình các mẫu trong Mẫu xét nghiệm Lab.

![Lab Sample Collection](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/lab-sample-collection.png)

### 2.3 Tự động tạo Xét nghiệm Lab khi Xác nhận Hóa đơn bán hàng

ERPNext Healthcare cũng cho phép tạo các Xét nghiệm Lab tự động khi bất kỳ xét nghiệm lab nào được lập hóa đơn (thông qua Hóa đơn bán hàng). Để cấu hình điều này, hãy bật tùy chọn _Tạo (các) Xét nghiệm Lab khi Xác nhận Hóa đơn bán hàng_ trong [Cài đặt Healthcare](healthcare_settings.md).

### 2.4 Kết quả xét nghiệm Vi sinh vật

Vi sinh vật là một mục nhập tùy chọn cho các xét nghiệm lab mô tả. Bạn có thể chọn vi sinh vật, thiết lập mật độ khuẩn lạc và chọn Đơn vị tính của khuẩn lạc.

### 2.5 Kết quả Độ nhạy cảm

Trong trường hợp các xét nghiệm lab mô tả, nếu tùy chọn _Độ nhạy cảm_ được bật trong mẫu, bạn có thể nhập kết quả độ nhạy cảm của mẫu đối với các loại kháng sinh khác nhau trong bảng con Độ nhạy cảm. Các danh mục chính về Độ nhạy cảm và Kháng sinh đã được cấu hình sẵn trong ERPNext. Bạn có thể mở rộng hoặc sửa đổi chúng theo nhu cầu của mình.

![Sensitivity](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/sensitivity.png)

### 2.6 Định dạng Kết quả xét nghiệm

ERPNext cũng cho phép bạn định dạng kết quả xét nghiệm cho từng xét nghiệm/sự kiện trong kết quả của bạn.

![Format Test Result](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/format-result-value.png)

![Formatted Result](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/formatted-result.png)

### 2.7 Thông báo SMS Phòng xét nghiệm

Bạn có thể cấu hình các tin nhắn để gửi thông báo SMS cho bệnh nhân bất cứ khi nào kết quả xét nghiệm lab đã sẵn sàng trong [Cài đặt Healthcare](healthcare_settings.md). Để làm điều này, trước tiên bạn phải thiết lập [Cài đặt SMS](../setting-up/sms-setting.md).

## 3. Các chủ đề liên quan

1. [Xét nghiệm Lab](lab_test.md)
1. [Thu thập mẫu](sample_collection.md)

{next}