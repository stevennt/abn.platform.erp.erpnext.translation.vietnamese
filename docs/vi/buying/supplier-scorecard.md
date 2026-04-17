<!-- add-breadcrumbs -->
# Bảng điểm Nhà cung cấp

**Bảng điểm Nhà cung cấp là một công cụ đánh giá được sử dụng để đánh giá hiệu suất của các nhà cung cấp.**

Bảng điểm nhà cung cấp có thể được sử dụng để theo dõi chất lượng mặt hàng, việc giao hàng và khả năng phản hồi của nhà cung cấp trong các khoảng thời gian dài. Dữ liệu này thường được sử dụng để hỗ trợ trong các quyết định mua hàng.
Một Bảng điểm Nhà cung cấp được tạo thủ công cho từng nhà cung cấp.

Để truy cập Bảng điểm Nhà cung cấp, hãy đi đến:
> Home > Buying > Supplier Scorecard > Supplier Scorecard


## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Bảng điểm Nhà cung cấp, bạn nên tạo các mục sau trước:

* [Supplier](supplier.md)

## 1. Cách tạo Bảng điểm Nhà cung cấp

1. Đi đến danh sách Supplier Scorecard, nhấp vào New.
2. Chọn một Nhà cung cấp để chấm điểm.
3. Chọn giai đoạn đánh giá là hàng tuần, hàng tháng hoặc hàng năm.
4. Thiết lập hàm chấm điểm (chi tiết ở phần tiếp theo).
5. Một bảng điểm nhà cung cấp được tạo riêng biệt cho từng nhà cung cấp. Chỉ có thể tạo một bảng điểm nhà cung cấp cho mỗi nhà cung cấp.
<img class="screenshot" alt="Purchase Order" src="https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-scorecard.png">

## 2. Các tính năng
### 2.1 Thiết lập chấm điểm
Bảng điểm nhà cung cấp bao gồm một tập hợp các giai đoạn đánh giá, trong đó hiệu suất của nhà cung cấp được đánh giá. Giai đoạn này có thể là hàng tuần, hàng tháng hoặc hàng năm. Điểm hiện tại được tính từ điểm của mỗi giai đoạn đánh giá dựa trên hàm trọng số. Công thức mặc định là tính trọng số tuyến tính dựa trên 12 giai đoạn chấm điểm trước đó.
<img class="screenshot" alt="Purchase Order" src="https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-scorecard-weighing.png">
Công thức này có thể tùy chỉnh.

#### Xếp hạng Nhà cung cấp

Xếp hạng nhà cung cấp được sử dụng để nhanh chóng phân loại các nhà cung cấp dựa trên hiệu suất của họ. Những thông tin này có thể tùy chỉnh cho từng nhà cung cấp.

Xếp hạng bảng điểm của một nhà cung cấp cũng có thể được sử dụng để hạn chế nhà cung cấp không được đưa vào Yêu cầu báo giá hoặc không được xuất Đơn mua hàng. Màn hình sau có thể được xem bằng cách mở rộng một hàng trong bảng 'Scoring Standings', nhấp vào mũi tên hướng xuống.
<img class="screenshot" alt="Purchase Order" src="https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-scorecard-standing.png">

### 2.2 Thiết lập tiêu chí
Một nhà cung cấp có thể được đánh giá dựa trên nhiều tiêu chí đánh giá riêng lẻ, bao gồm (nhưng không giới hạn) thời gian phản hồi báo giá, chất lượng mặt hàng được giao và tính kịp thời của việc giao hàng. Các tiêu chí này được tính trọng số để xác định điểm giai đoạn cuối cùng.

Để tạo một Tiêu chí mới, hãy đi đến Buying > Supplier Scorecard > Supplier Scorecard Criteria:
<img class="screenshot" alt="Purchase Order" src="https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-scorecard-criteria.png">

Lưu ý: Trọng số tiêu chí cho một bảng điểm nên cộng lại bằng 100.

### 2.3 Các biến Bảng điểm Nhà cung cấp
Phương pháp tính toán cho mỗi tiêu chí được xác định thông qua trường Criteria Formula, trường này có thể sử dụng một số biến đã được thiết lập sẵn. Điều này có thể được thấy trong ảnh chụp màn hình trước đó.

Giá trị của mỗi biến này được tính toán trong giai đoạn chấm điểm cho mỗi nhà cung cấp. Ví dụ về các biến như sau:

 - Tổng số mặt hàng nhận được từ nhà cung cấp
 - Tổng số mặt hàng được chấp nhận từ nhà cung cấp
 - Tổng số mặt hàng bị từ chối từ nhà cung cấp
 - Tổng số lần giao hàng từ nhà cung cấp
 - Tổng số tiền nhận được từ một nhà cung cấp

![Supplier Scorecard variable](https://docs.erpnext.com/docs/v13/assets/img/buying/supplier-scorecard-variables.png)

Các biến đã được thiết lập sẵn, các biến bổ sung có thể được thêm thông qua tùy chỉnh phía máy chủ. Đánh dấu vào ô Custom nếu biến bạn đang tạo dành cho một trường tùy chỉnh.

Công thức tiêu chí nên được tùy chỉnh để đánh giá các nhà cung cấp trong mỗi tiêu chí theo cách phù hợp nhất với yêu cầu của công ty.

### 2.4 Công thức đánh giá
Công thức đánh giá sử dụng các biến đã được thiết lập sẵn hoặc biến tùy chỉnh để đánh giá một khía cạnh về hiệu suất của nhà cung cấp trong giai đoạn chấm điểm. Các công thức có thể sử dụng các hàm toán học sau:

* phép cộng: +
* phép trừ: -
* phép nhân: *
* phép chia: /
* min: min(x,y)
* max: max(x,y)
* if/else: (x) if (formula) else (y)
* nhỏ hơn: <
* lớn hơn: >
* biến: {variable_name}

Điều quan trọng là công thức phải có thể giải được cho tất cả các giá trị biến. Đây thường là vấn đề nếu giá trị trả về bằng 0. Ví dụ:
```
{total_accepted_items} / {total_received_items}
```

Ví dụ này sẽ trả về 0 / 0 trong các giai đoạn không có mặt hàng nào được nhận, và do đó nên có một bước kiểm tra để bảo vệ trong trường hợp này:
```
({total_accepted_items} / {total_received_items})
if {total_received_items} > 0
else 1.
```

### 2.5 Đánh giá Nhà cung cấp
Một bản đánh giá được tạo cho mỗi Giai đoạn Bảng điểm Nhà cung cấp bằng cách nhấp vào nút "Generate Missing Scorecard Periods". Có thể xem điểm hiện tại của nhà cung cấp, cũng như biểu đồ trực quan hiển thị hiệu suất của nhà cung cấp theo thời gian. Bất kỳ hành động nào chống lại nhà cung cấp cũng được ghi chú tại đây, bao gồm cả các cảnh báo khi tạo RFQ và PO hoặc ngăn chặn hoàn toàn các tính năng này đối với nhà cung cấp đó.

### 3. Các chủ đề liên quan
1. [Supplier](supplier.md)
1. [Supplier Quotation](supplier-quotation.md)

{next}