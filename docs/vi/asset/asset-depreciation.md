<!-- add-breadcrumbs -->
# Khấu hao Tài sản

Hệ thống tự động tạo lịch trình khấu hao dựa trên phương pháp khấu hao và các thông tin liên quan khác như 'Available to Use Date' (Ngày sẵn sàng sử dụng) trong hồ sơ Tài sản. Bạn cũng có thể tạo nhiều lịch trình khấu hao cho các Sổ tài chính khác nhau. Bạn cần tích vào ô 'Calculate Depreciation' (Tính khấu hao) khi tạo tài sản để tính toán khấu hao và thêm các bút toán vào bảng khấu hao trong hồ sơ Tài sản.

Các loại khấu hao trong ERPNext:

* **Straight line (Đường thẳng)**: Khấu hao được tính theo đường thẳng và được _phân bổ đều_ theo tần suất hàng tháng đã chọn. Ví dụ, giá trị tài sản hiện tại là 1000, giá trị sau khấu hao là 500 sau 5 năm, phương pháp đường thẳng sẽ đặt số tiền khấu hao là 100 cho mỗi năm. Phương pháp này hữu ích khi không có quy luật cụ thể về cách khấu hao diễn ra trong một khoảng thời gian.

* **Double Declining Balance (Số dư giảm dần kép)**: Phương pháp này còn được gọi là số dư giảm dần 200%. Trong phương pháp này, 20% sẽ được khấu hao từ giá trị hiện có mỗi lần. Ví dụ, nếu tài sản trị giá 1000, nó sẽ trị giá 800 trong kỳ tiếp theo, sau đó 20% của 800 sẽ là 160, vì vậy hiện tại tài sản trị giá 640, và cứ tiếp tục như vậy cho đến khi đạt đến giá trị cuối cùng. Nếu bạn bắt đầu vào giữa năm, mức khấu hao 10% sẽ được tính toán. Phương pháp này hữu ích khi tài sản khấu hao nhanh ở giai đoạn đầu và chậm dần về sau.

* **Written Down Value (Giá trị ghi giảm)**: Một tỷ lệ phần trăm khấu hao cố định được thiết lập và giá trị tài sản sẽ khấu hao theo tỷ lệ đó trong suốt vòng đời của tài sản. Tỷ lệ phần trăm cố định này luôn được tính trên giá trị hiện có của tài sản. Ví dụ, nếu giá trị là 1000 và 'Written Down Value' là 10% trong 5 năm, thì 10% sẽ được khấu hao mỗi năm để đạt được giá trị kỳ vọng là 600 khi kết thúc vòng đời. Hữu ích cho các phương tiện vận tải nơi mà khấu hao cao hơn trong những năm sau.

    | Giá trị hiện tại | Khấu hao | Giá trị ghi sổ |
    | -------------- | ----------- | ------------ |
    | 1000 | 100 | 900 |
    | 900 | 90 | 810 |
    | 810 | 80 | 730 |
    | 730 | 70 | 660 |
    | 660 | 60 | 600 |
    | 600 | 50 | 550 |


* **Manual (Thủ công)**: Trong phương pháp này, bạn có thể xác định Ngày lập lịch (Schedule Date) và Số tiền khấu hao (Depreciation Amount) cho mỗi kỳ.

## 1. Khấu hao theo lịch trình
Vào ngày đã lập lịch, hệ thống tạo một bút toán khấu hao bằng cách tạo một Bút toán (Journal Entry) và chính Bút toán đó sẽ được hiển thị trong bảng khấu hao để tham chiếu. Ngày khấu hao tiếp theo (Next Depreciation Date) và Giá trị hiện tại (Current Value) cũng được cập nhật sau khi Xác nhận bút toán khấu hao.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/depreciation-entry.png">

## 2. Bút toán kế toán khi khấu hao
Trong bút toán khấu hao:

- "Accumulated Depreciation Account" (Tài khoản khấu hao lũy kế) được ghi Có và
- "Depreciation Expense Account" (Tài khoản chi phí khấu hao) được ghi Nợ.

Các tài khoản liên quan có thể được thiết lập trong Danh mục Tài sản (Asset Category) hoặc Công ty (Company).

## 3. Bút toán khấu hao tự động
Bạn có thể bật tính năng tự động ghi bút toán khấu hao từ [Accounts Settings](/docs/v13/user/manual/en/accounts/accounts-settings). Việc này sẽ tự động tạo bút toán khấu hao vào ngày đã lập lịch thông qua bộ lập lịch (scheduler). Nếu không, bạn phải tạo Bút toán thủ công bằng cách nhấp vào "Make > Depreciation Entry" trong dòng Lịch trình khấu hao (Depreciation Schedule) tương ứng.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/depreciation-schedule.png">

## 4. Ví dụ
Để hiểu rõ hơn, giá trị thuần của tài sản vào các ngày khấu hao khác nhau được hiển thị trong một biểu đồ đường.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-submit.png">

### 5. Các chủ đề liên quan
1. [Bảo trì Tài sản](/docs/v13/user/manual/en/asset/asset-maintenance)
1. [Điều chỉnh Giá trị Tài sản](/docs/v13/user/manual/en/asset/asset-value-adjustment)
1. [Thanh lý Tài sản](/docs/v13/user/manual/en/asset/scrapping-an-asset)

{next}