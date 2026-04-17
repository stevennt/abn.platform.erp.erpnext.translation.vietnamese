<!-- add-breadcrumbs -->
# Cơ hội

**Cơ hội là một khách hàng tiềm năng đã được phân loại.**

Khi bạn nhận thấy dấu hiệu cho thấy khách hàng tiềm năng đang tìm kiếm một sản phẩm/dịch vụ mà bạn cung cấp, bạn có thể chuyển đổi khách hàng tiềm năng đó thành một cơ hội. Bạn cũng có thể tạo một cơ hội dựa trên một khách hàng hiện có. Có thể thu thập nhiều Cơ hội từ một khách hàng tiềm năng hoặc một khách hàng.

Để truy cập danh sách Cơ hội, hãy đi đến:
> Home > CRM > Sales Pipeline > Opportunity

## 1. Cách tạo một Cơ hội

1. Đi đến danh sách Cơ hội và nhấp vào 'Add Opportunity'.
1. Trong 'Opportunity From', chọn Lead nếu cơ hội đến từ một khách hàng tiềm năng.

   ![Creating New Opportunity](https://docs.erpnext.com/docs/v16/assets/img/crm/creating-opportunity.gif)

1. Bạn cũng có thể đi đến một Lead có trạng thái 'Open' và chọn “Opportunity” trong menu thả xuống **Create** như hình dưới đây.

    ![Create Opportunity From Lead](https://docs.erpnext.com/docs/v16/assets/img/crm/lead-to-opportunity.png)

1. Trong 'Opportunity From', chọn Khách hàng nếu cơ hội đến từ một khách hàng.

1. Chọn Opportunity Type. Mục này cho biết danh mục rộng của cơ hội như Sales, Support, Maintenance, v.v.

1. Bạn có thể thêm các chi tiết khác như Số tiền Cơ hội (Opportunity Amount), Xác suất (Probability) chuyển đổi, Tiền tệ (Currency) trong phần 'SALES'.

1. Bạn có thể ghi lại chi tiết các Mặt hàng cần thiết bằng cách nhấp vào ô kiểm 'With Items' và thêm chi tiết mặt hàng và số lượng trong phần 'Items'.

    ![Item Details in Opportunity](https://docs.erpnext.com/docs/v16/assets/img/crm/item-details-in-opportunity.png)

1. Nhập Nguồn (Source) của cơ hội trong phần SOURCE.

## 2. Các tính năng

### 2.1 Nhắc nhở theo dõi các Cơ hội

Việc liên hệ với các cơ hội theo thời gian để xây dựng mối quan hệ là rất quan trọng. Bạn có thể thiết lập các trường 'Next Contact Date' (Ngày liên hệ tiếp theo) và 'Next Contact By' (Liên hệ bởi), một sự kiện lịch sẽ được thêm cho người dùng được chọn trong trường 'Next Contact By' và một thông báo sẽ được hiển thị vào Ngày đó.

### 2.2 Tự động phân bổ Cơ hội cho Nhân viên kinh doanh

Bạn có thể xác định [Assignment Rules](/docs/v16/user/manual/en/automation/assignment-rule) để tự động phân bổ các cơ hội cho nhân viên kinh doanh.

![Opportunity Assignment](https://docs.erpnext.com/docs/v16/assets/img/crm/opportunity-assignment-rule.png)

### 2.3 Tự động đóng Cơ hội

Nếu bạn không nhận được phản hồi từ một cơ hội trong một số ngày nhất định, bạn có thể muốn cơ hội đó được tự động đóng lại.

Bạn có thể thiết lập số ngày trong [Selling Settings](/docs/v16/user/manual/en/selling/selling-settings).

![Auto Close Opportunities](https://docs.erpnext.com/docs/v16/assets/img/crm/auto-close-opportunities.png)

### 2.4 Tạo Báo giá
Bạn có thể tạo [Quotation](/docs/v16/user/manual/en/selling/quotation) từ menu thả xuống **Make**. Các giá trị trường liên quan sẽ được sao chép sang.

![Create Quotation From Opportunity](https://docs.erpnext.com/docs/v16/assets/img/crm/create-quotation-from-opportunity.png)

### 2.5 Tạo Báo giá của Nhà cung cấp

Bạn có thể cần lấy báo giá từ Nhà cung cấp dựa trên yêu cầu của khách hàng và dựa trên đó để chuẩn bị báo giá cho khách hàng của mình. Với ERPNext, bạn có thể tạo [Supplier Quotation](/docs/v16/user/manual/en/buying/supplier-quotation) ngay từ chính cơ hội đó.

> Thực hành tốt nhất: Khách hàng tiềm năng (Leads) và Cơ hội (Opportunities) thường được gọi là "Sales Pipeline" (Phễu bán hàng) của bạn, đây là những gì bạn cần theo dõi nếu muốn dự đoán được lượng công việc kinh doanh bạn sẽ có được trong tương lai. Việc theo dõi những gì đang đến để điều chỉnh nguồn lực của bạn luôn là một ý tưởng hay.

### 2.6 Ghi lại lý do mất Cơ hội

Khi một cơ hội bị mất, bạn có thể ghi lại các lý do dẫn đến việc mất đó. Điều này sẽ giúp bạn phân tích các xu hướng trong một thời gian dài và xác định các thông tin chi tiết cần thiết để cải thiện tại các lĩnh vực khác nhau trong tổ chức.

![Quotation Lost Reason](https://docs.erpnext.com/docs/v16/assets/img/crm/quotation-lost-reason.png)

### 2.7 Thời gian phản hồi đầu tiên

Khi bạn gửi phản hồi đầu tiên (email) cho một Cơ hội, hệ thống sẽ tính toán số phút phản hồi đầu tiên (Minutes to First Response) và được hiển thị trong một trường.

Một báo cáo được tạo ra gọi là 'Minutes to First Response for Opportunity'. Đọc [CRM Reports](/docs/v16/user/manual/en/CRM/crm_reports) để biết thêm chi tiết.

### 3. Các chủ đề liên quan
1. [Quotation](/docs/v16/user/manual/en/selling/quotation.html)
1. [Khách hàng](/docs/v16/user/manual/en/CRM/customer)
1. [Lead](/docs/v16/user/manual/en/CRM/lead)
1. [Supplier Quotation](/docs/v16/user/manual/en/buying/supplier-quotation)
1. [Difference between Lead, Contact, and Customer](/docs/v16/user/manual/en/CRM/articles/difference_between_lead_contact_and_customer)

{next}