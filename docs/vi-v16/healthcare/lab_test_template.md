<!-- add-breadcrumbs -->
# Mẫu Xét nghiệm (Lab Test Template)

**Mẫu Xét nghiệm trong ERPNext cho phép bạn tạo nhanh tất cả các loại Xét nghiệm tại phòng Lab.**

Bạn có thể cấu hình trước các sự kiện (events) và thành phần kết quả cho các loại xét nghiệm Đơn (Single), Hợp phần (Compound), Mô tả (Descriptive), hoặc Nhóm (Grouped), nhờ đó bạn không phải nhập lại các dữ liệu dư thừa mỗi lần thực hiện.

## 1. Cách tạo Mẫu Xét nghiệm

Để tạo một Mẫu Xét nghiệm, hãy đi tới:

> Home > Healthcare > Laboratory > Lab Test Template > New Lab Test Template

Dưới đây là các trường phổ biến trong Mẫu của mọi định dạng kết quả.

1. **Test Name**: Chỉ định tên của Xét nghiệm.
2. **Item Code**: Để quản lý quy trình lập hóa đơn của các xét nghiệm, các mặt hàng sẽ được tạo tự động khi tạo mẫu. Cung cấp Mã mặt hàng cho xét nghiệm tại trường này.
3. **Item Group**: Bạn có thể nhóm các xét nghiệm dựa trên các tiêu chí khác nhau bằng trường này. Tạo một Nhóm mặt hàng hoặc chọn từ các nhóm hiện có.
4. **Department**: Khoa y tế thực hiện xét nghiệm này.
5. **Result Format**: Chỉ định định dạng kết quả cho xét nghiệm:
  - Single (Đơn): Với loại xét nghiệm này, chỉ có một giá trị kết quả duy nhất được diễn giải.
  - Compound (Hợp phần): Trong xét nghiệm hợp phần, mẫu được kiểm tra cho nhiều sự kiện (events).
  - Descriptive (Mô tả): Các loại xét nghiệm này được sử dụng để kiểm tra nhiều thành phần kết quả và bạn cũng có thể cấu hình kiểm tra độ nhạy của mẫu đối với các loại kháng sinh khác nhau tại đây.
  - Grouped (Nhóm): Đây là một nhóm gồm các mẫu xét nghiệm khác.
  - No Result (Không kết quả): Đây là các xét nghiệm không có giá trị kết quả.
6. **Description**: Bạn có thể cung cấp mô tả chi tiết về xét nghiệm tại đây.
7. **Is Billable**: Đánh dấu vào đây nếu xét nghiệm có thể lập hóa đơn.
8. **Rate**: Nếu _Is Billable_ được chọn, bạn phải chỉ định đơn giá cho xét nghiệm tại trường này. Trong trường hợp này, Giá mặt hàng sẽ được cấu hình tự động khi Lưu mẫu.

### 1.1 Định dạng kết quả Đơn (Single Result Format)

Trong định dạng kết quả này, chỉ có một giá trị kết quả duy nhất được diễn giải. Sau khi điền các chi tiết được chỉ định ở bước đầu tiên, cần phải thiết lập Đơn vị tính (UOM), Đơn vị tính phụ (Secondary UOM) và Khoảng bình thường (Normal Range). Ví dụ, xét nghiệm Hemoglobin thường được dùng để kiểm tra bệnh thiếu máu, thường đi kèm với xét nghiệm hematocrit hoặc là một phần của xét nghiệm tổng phân tích tế bào máu (CBC).

![Single Result Format](https://docs.erpnext.com/docs/v16/assets/img/healthcare/single-result.png)

### 1.2 Định dạng kết quả Hợp phần (Compound Result Format)

Trong định dạng kết quả này, mẫu được kiểm tra cho nhiều sự kiện. Các sự kiện này cần được cấu hình trong bảng "Compound". Bạn có thể thiết lập các Sự kiện và chỉ định Đơn vị tính (UOM), Đơn vị tính phụ (Secondary UOM), Hệ số chuyển đổi (Conversion Factor) và Khoảng bình thường (Normal Range) cho mỗi sự kiện. Nếu có một số kết quả sự kiện không cần phải chỉ định trong Xét nghiệm, bạn có thể chọn "Allow Blank" (Cho phép để trống) cho sự kiện đó. Nếu không chọn mục này, hệ thống sẽ không cho phép bạn Xác nhận Xét nghiệm trừ khi tất cả các giá trị kết quả đã được thiết lập.

![Compound Result Format](https://docs.erpnext.com/docs/v16/assets/img/healthcare/compound-result.png)

### 1.3 Định dạng kết quả Mô tả (Descriptive Result Format)

Các loại xét nghiệm này được sử dụng để kiểm tra nhiều thành phần kết quả. Bạn cũng có thể cấu hình kiểm tra độ nhạy của mẫu đối với các loại kháng sinh khác nhau bằng cách bật tùy chọn "Sensitivity" (Độ nhạy) trong mẫu. Bạn có thể sử dụng tùy chọn "Allow Blank" để cho phép để trống các mục nhập kết quả cho một số thành phần nhất định.

![Descriptive Result Format](https://docs.erpnext.com/docs/v16/assets/img/healthcare/descriptive-result.png)

### 1.4 Định dạng kết quả Nhóm (Grouped Result Format)

Định dạng kết quả nhóm được sử dụng để tạo kết quả Xét nghiệm như một nhóm gồm các xét nghiệm hoặc sự kiện khác, ví dụ: Tổng phân tích huyết học (Complete Haemogram). Xét nghiệm tổng phân tích huyết học là một nhóm các xét nghiệm được thực hiện trên một mẫu máu. Tổng phân tích huyết học đóng vai trò như một bảng sàng lọc rộng để kiểm tra sự hiện diện của bất kỳ bệnh tật hoặc nhiễm trùng nào trong cơ thể. Các xét nghiệm huyết học chủ yếu kiểm tra ba thành phần của máu:

- Xét nghiệm hemoglobin thường được dùng để kiểm tra bệnh thiếu máu, thường đi kèm với xét nghiệm hematocrit hoặc là một phần của xét nghiệm tổng phân tích tế bào máu (CBC).
- Xét nghiệm máu DLC là xét nghiệm đo tỷ lệ phần trăm của từng loại bạch cầu (WBCs) trong cơ thể.
- TLC là xét nghiệm xác định số lượng bạch cầu (WBCs) trong cơ thể chúng ta.
- Neutrophils (Sự kiện)

Bạn có thể cấu hình Đơn vị tính (UOM), Đơn vị tính phụ (Secondary UOM) và Khoảng bình thường (Normal Range) trong trường hợp của các sự kiện. Khi chọn các xét nghiệm khác trong bảng, hệ thống sẽ tự động lấy mô tả và đơn giá của các xét nghiệm đơn/hợp phần đó.

![Grouped Result Format](https://docs.erpnext.com/docs/v16/assets/img/healthcare/grouped-result.png)

## 2. Các tính năng

### 2.1 Tự động tạo Mặt hàng cho các Mẫu

Các mẫu cho phép bạn quản lý mặt hàng có thể lập hóa đơn, đơn giá, v.v. cho một xét nghiệm cụ thể. Hệ thống sẽ tự động tạo một Mặt hàng liên kết với mẫu khi mẫu được Lưu. Nếu mẫu có thể lập hóa đơn, thì giá mặt hàng cũng sẽ được tạo cho nó.

![Lab Test Item](https://docs.erpnext.com/docs/v16/assets/img/healthcare/lab-test-item.png)

Bạn có thể thay đổi Mã mặt hàng liên kết với Mẫu Xét nghiệm nếu cần, bằng cách sử dụng nút **Change Template Code**.

### 2.2 Vô hiệu hóa Mẫu

Bạn có thể vô hiệu hóa các mẫu khi chúng không được sử dụng bằng cách đánh dấu vào ô "Disabled" (Đã vô hiệu hóa). Mặt hàng liên kết cũng sẽ bị vô hiệu hóa khi vô hiệu hóa một Mẫu Xét nghiệm.

### 2.3 Mã hóa Y tế (Medical Coding)

Bạn cũng có thể cấu hình Tiêu chuẩn Mã Y tế (Medical Code Standard) và Mã Y tế (Medical Code) cho các mẫu của...