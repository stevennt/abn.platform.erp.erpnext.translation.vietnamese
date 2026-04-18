<!-- add-breadcrumbs -->
# Lập kế hoạch năng lực dựa trên Lệnh sản xuất

Chức năng Lập kế hoạch năng lực giúp bạn theo dõi các công việc sản xuất được phân bổ cho từng Máy công tác.

<img alt="Role Desk Permission" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/capacity-1.png">

Dưới đây là các bước để sử dụng tính năng Lập kế hoạch năng lực trong tài khoản ERPNext của bạn.

1.  Công đoạn

    Để thêm các công đoạn, hãy đi đến:

    `Manufacturing > Bill of Materials > Operations`

2.  Máy công tác

    Thêm từng Máy công tác vào tài khoản ERPNext của bạn từ:

    `Manufacturing > Bill of Materials > Workstation`

    Trong danh mục Máy công tác, bạn có thể xác định những công đoạn nào sẽ được thực hiện trên máy đó, các chi phí liên quan là gì, và giờ làm việc của Máy công tác đó như thế nào.

3.  Định mức nguyên vật liệu (BOM):

    Trong một BOM, với danh sách các nguyên vật liệu cần thiết để sản xuất, bạn cũng có thể liệt kê các công đoạn và máy công tác mà qua đó các nguyên vật liệu đó sẽ được xử lý.

4.  Lệnh sản xuất:

    Khi Xác nhận Lệnh sản xuất, sẽ có Bảng chấm công cho các Công đoạn. Điều này giúp bạn phân bổ các công việc sản xuất cho từng Máy công tác, cũng như bạn có thể cập nhật thời gian thực tế đã thực hiện cho mỗi Công đoạn.

### Lỗi do Lập kế hoạch năng lực

**Câu hỏi:** Khi Xác nhận Lệnh sản xuất, chúng tôi nhận được thông báo lỗi sau.

<img alt="Role Desk Permission" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/capacity-2.png">

**Trả lời:** Vui lòng kiểm tra xem bạn đã cập nhật Giờ làm việc trong danh mục Máy công tác chưa? Nếu chưa, vui lòng cập nhật và sau đó thử Xác nhận Lệnh sản xuất.

Khi Xác nhận Lệnh sản xuất, các Công đoạn (như đã thêm trong BOM) sẽ được phân bổ cho máy công tác. Mỗi công đoạn nên bắt đầu và kết thúc trong cùng một ngày. Nếu hệ thống không thể sắp xếp công đoạn đó trong một ngày, hệ thống sẽ yêu cầu bạn chia nhỏ Dự án đó, để hệ thống có thể phân bổ các công đoạn nhỏ hơn trong một ngày.

Nếu bạn đã cập nhật giờ làm việc trong Máy công tác nhưng vẫn gặp lỗi này, đó là do một trong các công đoạn của bạn mất quá nhiều thời gian và không thể hoàn thành trong một ngày. Vui lòng chia nhỏ công đoạn đó thành các công đoạn nhỏ hơn, để nó có thể được phân bổ cho Máy công tác và hoàn thành trong cùng một ngày.

### Bỏ qua Giờ làm việc của Máy công tác

Nếu bạn muốn bỏ qua kiểm tra trên và cho phép sắp xếp công việc sản xuất vượt quá giờ làm việc của Máy công tác, hãy bật
Overtime trong Manufacturing Settings.

<img alt="Role Desk Permission" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/capacity-3.png">

Nếu bạn muốn vô hiệu hóa hoàn toàn tính năng Lập kế hoạch năng lực, trong Manufacturing Settings, hãy tích vào trường "Disable Capacity Planning and Time Tracking".