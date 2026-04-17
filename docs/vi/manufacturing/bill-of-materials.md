<!-- add-breadcrumbs -->
# Định mức nguyên vật liệu

**Định mức nguyên vật liệu là danh sách các mặt hàng và cụm lắp ráp cùng với số lượng cần thiết để sản xuất một Mặt hàng.**

Một BOM cũng có thể bao gồm các công đoạn sản xuất cần thiết để sản xuất Mặt hàng đó.

**Định mức nguyên vật liệu** (BOM) là trung tâm của hệ thống Sản xuất và là tài liệu quan trọng nhất giúp tạo ra các loại tài liệu khác như Lệnh sản xuất và Thẻ công việc. ERPNext hỗ trợ BOM đa cấp. Để biết thêm, hãy truy cập [trang này](/docs/v13/user/manual/en/manufacturing/articles/managing-multi-level-bom).

**BOM** là danh sách tất cả các vật tư (mua ngoài hoặc tự làm) và các công đoạn được sử dụng để sản xuất một thành phẩm hoặc cụm lắp ráp. Trong ERPNext, mỗi mặt hàng (cụm lắp ráp) có thể có BOM riêng, từ đó tạo thành một cây các Mặt hàng với nhiều cấp độ.

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/manufacturing-flow-bom.png">

Để tạo các Yêu cầu mua hàng chính xác, bạn phải luôn duy trì các BOM chính xác.

Để truy cập danh sách BOM, hãy đi tới:
> Trang chủ > Sản xuất > Định mức nguyên vật liệu > Định mức nguyên vật liệu
<p></p>
> Lưu ý rằng một khi BOM đã được Xác nhận, nó không thể chỉnh sửa. Bạn chỉ có thể Hủy bản hiện tại, sao chép nó và Xác nhận một bản khác. Một BOM cũng được liên kết với nhiều nơi trong phân hệ Sản xuất, vì vậy việc thay đổi nó có thể tốn thời gian và mệt mỏi. Do đó, tốt nhất bạn nên suy nghĩ kỹ và điền đầy đủ thông tin vào BOM trước khi Xác nhận.

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng BOM, bạn nên tạo các mục sau trước:

* [Mặt hàng](/docs/v13/user/manual/en/stock/item)
* [Công đoạn](/docs/v13/user/manual/en/manufacturing/operation)
* [Máy móc/Trạm làm việc](/docs/v13/user/manual/en/manufacturing/workstation)
* [Quy trình công nghệ](/docs/v13/user/manual/en/manufacturing/routing)

## 2. Cách tạo Định mức nguyên vật liệu
1. Đi tới danh sách Định mức nguyên vật liệu, nhấn vào Mới.
1. Chọn Mặt hàng cần sản xuất. Tên Mặt hàng, Đơn vị tính, công ty và tiền tệ sẽ được tự động lấy ra.
1. Nhập số lượng của Mặt hàng sẽ được sản xuất từ Định mức nguyên vật liệu này.
1. Trong bảng Mặt hàng, chọn các nguyên vật liệu (Mặt hàng) cần thiết để sản xuất Mặt hàng. Sau đó tiến hành:
 1. Chọn số lượng Nguyên vật liệu sử dụng.
 1. Thiết lập một công đoạn Mặt hàng tại đây để được lấy vào Lệnh sản xuất sau này.
 1. Nếu Mặt hàng này là một cụm lắp ráp, BOM mặc định của nó sẽ được lấy ra.
 1. Chọn Kho nguồn để theo dõi tồn kho.
 1. Nhập tỷ lệ phế phẩm sẽ còn lại sau khi nguyên vật liệu này được sử dụng.
  ![BOM Materials](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/bom-materials.png)

1. Trong phần Phế phẩm, chọn Mặt hàng phế phẩm sẽ được tạo ra khi sản xuất và số lượng của nó. Mặt hàng phế phẩm cũng có thể có Đơn giá nếu nó là sản phẩm phụ chứ không phải là chất thải. Bỏ qua phần này nếu 100% nguyên vật liệu được sử dụng hết hoàn toàn.
  ![BOM Scrap](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/bom-scrap.png)

1. Lưu và Xác nhận.

Trong bảng Mặt hàng, bạn sẽ thấy tùy chọn 'Include Item in Manufacturing' (Bao gồm Mặt hàng trong Sản xuất). Các Nguyên vật liệu cần được tích chọn ô này. Trong trường hợp có các Công đoạn hoặc dịch vụ bạn cần đưa vào BOM mà không nhất thiết là một Mặt hàng dùng để sản xuất, hãy bỏ tích ô này. Ví dụ, việc xử lý nhựa với hóa chất đòi hỏi một số chi phí nhưng nó không phải là một Mặt hàng và chi phí đó cần được theo dõi.

  <img class="screenshot" alt="Task" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/bom-item-include.png">

### 2.1 Định mức nguyên vật liệu có Công đoạn
Để thêm [Công đoạn](/docs/v13/user/manual/en/manufacturing/operation), hãy tích vào ô 'With Operations' (Có Công đoạn). Bây giờ, một bảng Công đoạn có thể được nhìn thấy. Tùy chọn này hữu ích để theo dõi chi phí của các Công đoạn khác nhau được thực hiện để sản xuất [Mặt hàng](/docs/v13/user/manual/en/stock/item). Các Công đoạn có thể được thêm dễ dàng bằng cách thiết lập một mẫu với [Quy trình công nghệ](/docs/v13/user/manual/en/manufacturing/routing) chính.

<img class="screenshot" alt="Task" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/bom-operations.png">

1. Trong bảng “Operations” (Công đoạn), thêm các công đoạn cần được thực hiện để sản xuất Mặt hàng cụ thể này.
1. Đối với mỗi công đoạn, bạn sẽ được yêu cầu nhập [Máy móc/Trạm làm việc](/docs/v13/user/manual/en/manufacturing/workstation) nơi Công đoạn sẽ được thực hiện. Một Máy móc/Trạm làm việc mặc định có thể được thiết lập từ tài liệu [Công đoạn](/docs/v13/user/manual/en/manufacturing/operation).
1. Nhập Đơn giá vận hành theo giờ, Thời gian công đoạn tính bằng phút, và Quy mô lô (Batch Size) được tạo với Công đoạn. Chi phí vận hành sẽ được tính toán dựa trên các giá trị này.

> Lưu ý: Các Máy móc/Trạm làm việc chỉ được định nghĩa cho mục đích tính giá thành sản phẩm và lập lịch Công đoạn của Lệnh sản xuất, không phải để theo dõi tồn kho. Tồn kho được theo dõi trong các [Kho](/docs/v13/user/manual/en/stock/warehouse) được thiết lập trong bảng Mặt hàng của BOM.

Transfer Material Against (Chuyển vật tư theo) cần được thiết lập cho một BOM có Công đoạn. Vật tư có thể được chuyển theo một [Lệnh sản xuất](/docs/v13/user/manual/en/manufacturing/work-order) theo lô hoặc theo từng [Thẻ công việc](/docs/v13/user/manual/en/manufacturing/job-card) riêng lẻ. Việc thay đổi này ảnh hưởng đến việc 'Chuyển vật tư để sản xuất' được thực hiện theo Lệnh sản xuất cùng một lúc hay thực hiện nhiều lần theo từng Thẻ công việc riêng lẻ. Việc thiết lập tùy chọn này phụ thuộc vào các yếu tố như thời gian sản xuất mặt hàng, giá trị của các mặt hàng được sản xuất, số lượng linh kiện được sử dụng trong sản xuất, kỹ năng của nhân công tham gia, v.v.

![BOM transfer materials against](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/bom-transfer-materials.png)

### 2.2 Các tùy chọn bổ sung khi tạo Định mức nguyên vật liệu

* **Is Active (Đang hoạt động)**: Một Mặt hàng cũng có thể được sản xuất bằng một bộ vật tư/công đoạn thay thế. Trong trường hợp đó, hãy bỏ tích ô này để vô hiệu hóa BOM này và sử dụng một BOM khác.
* **Is Default (Mặc định)**: BOM này sẽ được chọn mặc định trong Lệnh sản xuất, v.v. khi Mặt hàng đó được chọn.
* **Inspection Required (Yêu cầu kiểm tra)**: Tùy chọn này sẽ làm cho việc 'Kiểm tra chất lượng' trở thành bắt buộc đối với nguyên vật liệu và thành phẩm. Chọn...