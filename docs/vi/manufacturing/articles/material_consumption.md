# Tiêu hao nguyên vật liệu

Chức năng Tiêu hao nguyên vật liệu cho phép bạn thực hiện nhiều `Stock Entry` tiêu hao đối với một Lệnh sản xuất. Để kích hoạt chức năng này, hãy đi tới Manufacturing > Manufacturing Settings.

<img class="screenshot" alt="Item Alternative" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/allow-material-consumption.png">

Sau khi được kích hoạt, nút `Material Consumption` sẽ xuất hiện trong Lệnh sản xuất khi đã bắt đầu.

<img class="screenshot" alt="Item Alternative" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/material-consumption-button.png">

Khi nhấn nút, hệ thống sẽ thực hiện các bước sau:

1.  Nó sẽ tạo một Stock Entry với mục đích là `Material Consumption for Manufacture`.

<img class="screenshot" alt="Item Alternative" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/material-consumption-for-manufacture.png">

2.  Nếu mục "Backflush Raw Materials Based On" trong Manufacturing Settings được đặt là `BOM`, hệ thống sẽ đề xuất tiêu hao tất cả số lượng cần thiết để sản xuất.
3.  Nếu mục "Backflush Raw Materials Based On" trong Manufacturing Settings được đặt là `Material Transferred for Manufacture`, hệ thống sẽ đề xuất tiêu hao tất cả số lượng đã chuyển cho sản xuất.
4.  Sau khi được Xác nhận, nó sẽ cập nhật cột `Consumed Qty` trong Lệnh sản xuất.

<img class="screenshot" alt="Item Alternative" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/consumed-qty.png">

5.  Trong các lần Tiêu hao nguyên vật liệu tiếp theo, hệ thống sẽ gợi ý số lượng chưa tiêu hao.
6.  Khi nhấn nút "Finish" trong Lệnh sản xuất, hệ thống sẽ tính toán dựa trên số lượng đã tiêu hao.

### Kiểm tra tính hợp lệ

* Nếu "Allow Multiple Material Consumption" không được thiết lập trong Manufacturing Settings nhưng "Material Consumption for Manufacture" được sử dụng trong Stock Entry.

<img class="screenshot" alt="Item Alternative" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/material-consumption-stock-entry.gif">

* Không thể Hủy "Material Consumption for Manufacture" đối với Lệnh sản xuất đã hoàn thành.

<img class="screenshot" alt="Item Alternative" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/cancel-material-consumption-stock-entry.gif">