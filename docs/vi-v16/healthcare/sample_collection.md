<!-- add-breadcrumbs -->
# Thu thập mẫu

Việc quản lý các mẫu đã thu thập và in nhãn cho các mẫu đó, tự động hóa việc thu thập mẫu, v.v. là rất quan trọng đối với một Phòng xét nghiệm.

## 1. Cách tạo Thu thập mẫu

Để tạo Thu thập mẫu, hãy đi đến

> Home > Healthcare > Laboratory > Sample Collection > New Sample Collection

1. Nhập tên của Bệnh nhân. Tất cả chi tiết của bệnh nhân sẽ được tự động lấy ra.
2. Chọn Lab Test Sample trong trường Sample. Bạn có thể cấu hình master Lab Test Sample theo yêu cầu của mình. Đơn vị tính (UOM) của mẫu được tự động lấy từ doc Lab Test Sample.
3. Thiết lập Số lượng mẫu đã thu thập.
4. Chọn người đã thu thập mẫu trong trường "Collected By".
5. Thiết lập Ngày và Giờ thu thập mẫu trong trường "Collected On".
6. Lưu và Xác nhận.

  ![Sample Collection](https://docs.erpnext.com/docs/v16/assets/img/healthcare/sample-collection.png)

## 2. Các tính năng

## 2.1 Tự động hóa Thu thập mẫu

Bạn cũng có thể tự động hóa việc tạo chứng từ Thu thập mẫu cho mỗi Lab Test bằng cách bật tùy chọn 'Create Sample Collection document for Lab Test' trong [Healthcare Settings](../user/manual/healthcare/healthcare_settings) và cấu hình các mẫu trong Lab Test Template.

![Lab Sample Collection](https://docs.erpnext.com/docs/v16/assets/img/healthcare/lab-sample-collection.png)

## 2.2 Dán nhãn mẫu

Việc in các thẻ nhận dạng mẫu cũng có thể thực hiện được trong ERPNext. Theo mặc định, một mẫu in có tên "Sample ID Print" được cung cấp sẵn, nhưng bạn luôn có thể tùy chỉnh trực tiếp bằng cách sử dụng [Print Format Builder](../user/manual/setting-up/print/print-format-builder.html) hoặc thậm chí tạo một [Print Format](../user/manual/customize-erpnext/print-format.html) tùy chỉnh nếu cần. Số lượng nhãn cần thiết phải được thiết lập trong trường "No. of prints" trong chứng từ Thu thập mẫu. Theo đó, bấy nhiêu nhãn sẽ được tạo ra trong chế độ xem in.

![Sample Print](https://docs.erpnext.com/docs/v16/assets/img/healthcare/sample-print.png)

## 3. Các chủ đề liên quan

1. [Lab Test](../healthcare/lab_test)
1. [Lab Test Template](../healthcare/lab_test_template)

{next}