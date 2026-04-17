<!-- add-breadcrumbs -->
# Gia công ngoài

**Trong gia công ngoài, bạn thuê một bên thứ ba thực hiện các công việc cho tổ chức của mình, đặc biệt là trong sản xuất.**

Gia công ngoài là một loại hợp đồng công việc nhằm thuê ngoài một số loại công việc nhất định cho các công ty khác. Nó cho phép các công việc ở nhiều giai đoạn khác nhau của dự án được thực hiện cùng một lúc, thường giúp hoàn thành nhanh hơn.

Gia công ngoài được áp dụng bởi nhiều ngành công nghiệp khác nhau. Ví dụ, các nhà sản xuất tạo ra một số sản phẩm từ các linh kiện phức tạp sẽ thuê ngoài một số linh kiện nhất định và đóng gói chúng tại cơ sở của họ.

Nếu doanh nghiệp của bạn liên quan đến việc thuê ngoài một số quy trình nhất định cho một Nhà cung cấp bên thứ ba, nơi bạn cung cấp nguyên vật liệu thô và bên thứ ba thực hiện nhân công/sản xuất, bạn có thể theo dõi việc này bằng cách sử dụng tính năng gia công ngoài của ERPNext.

## 1. Cách thiết lập Gia công ngoài

1. Tạo các Mặt hàng riêng biệt cho sản phẩm chưa qua chế biến và sản phẩm đã qua chế biến. Ví dụ, nếu bạn cung cấp X chưa sơn cho Nhà cung cấp và Nhà cung cấp trả lại X cho bạn, bạn có thể tạo hai Mặt hàng: “X-chưa sơn” và “X”.
2. Tạo một Kho cho Nhà cung cấp của bạn để bạn có thể theo dõi các Mặt hàng đã cung cấp. (bạn có thể cung cấp lượng Mặt hàng cho cả tháng trong một lần).
3. Đối với Mặt hàng đã qua chế biến, trong danh mục Mặt hàng, hãy bật “Is Sub Contracted Item”.

  <img class="screenshot" alt="Sub-Contracting" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/subcontract.png">

### 1.1 Tạo BOM
Tạo [Định mức nguyên vật liệu](/docs/v16/user/manual/vi/manufacturing/bill-of-materials) cho Mặt hàng đã qua chế biến, với các Mặt hàng chưa qua chế biến là các mặt hàng con. Hãy xem xét một ví dụ đơn giản, nơi bạn sản xuất một cây bút. Cây bút đã qua chế biến sẽ được đặt tên theo Định mức nguyên vật liệu (BOM), trong khi ngòi bút, nhựa, mực, v.v. sẽ được phân loại là các mặt hàng con.

BOM này sẽ không có các Công đoạn (Operations) nếu tất cả công việc sản xuất được thực hiện bởi bên thứ ba. Hãy xem ví dụ đơn giản về một chiếc cán nhựa:

<img class="screenshot" alt="Sub-Contracting" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/subcontract2.png">

### 1.2 Tạo Đơn mua hàng
Tạo một Đơn mua hàng cho Mặt hàng đã qua chế biến, loại mà bạn đã tạo BOM. Khi bạn “Lưu”, trong phần “Nguyên vật liệu đã cung cấp”, tất cả các Mặt hàng chưa qua chế biến của bạn sẽ được cập nhật dựa trên Định mức nguyên vật liệu của bạn. Bạn cũng có thể chọn Kho nơi nguyên vật liệu sẽ được giữ lại để gia công ngoài tại mục Reserve Warehouse.

1. Các chi phí liên quan đến quy trình gia công ngoài nên được ghi lại trong trường Đơn giá của bảng Mặt hàng trong Đơn mua hàng như sau:

  <img class="screenshot" alt="Sub-Contracting" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/subcontract3.png">

1. Trong hình ảnh trước, chúng tôi đang cung cấp cho bên gia công 2 hộp cho mỗi loại trong số 3 loại vật liệu để sản xuất 240 cây bút. Chi phí liên quan với một cây bút là 27 và tổng chi phí cho tất cả các cây bút do đó là 6,480

1. Bạn cần đặt 'Supply Raw Materials' thành Yes vì Đơn mua hàng này là để gia công ngoài.

1. Từ một Đơn mua hàng, chọn nguyên vật liệu để chuyển cho bên gia công:
  ![Sub-Contracting](https://docs.erpnext.com/docs/v16/assets/img/buying/subcontract-transfer-materials.gif)

1. Sau khi [Đơn mua hàng](/docs/v16/user/manual/vi/buying/purchase-order#35-raw-materials-supplied) được Xác nhận, bạn cũng có thể xem số lượng dự trữ của mặt hàng từ trang tổng quan mặt hàng.

  <img class="screenshot" alt="Sub-Contracting" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/subcontract3-reserved-material.png">

### 1.3 Tạo Phiếu kho để chuyển Nguyên vật liệu
Bây giờ nguyên vật liệu đã được dự trữ, hãy tạo một Phiếu kho để giao các Mặt hàng nguyên vật liệu cho Nhà cung cấp của bạn.

Trong Đơn mua hàng, nhấp vào Transfer > Material to Supplier. Thiết lập Kho Nguồn (Source) và Kho Đích (Target). Phiếu kho sẽ có loại là 'Send to Subcontractor' nơi bạn chuyển từ Kho này sang Kho khác. Tích vào 'From BOM' và chọn BOM, nhập số lượng, và nhấp vào nút Get Items.

<img class="screenshot" alt="Sub-Contracting" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/subcontract4.png">

### 1.4 Tạo Phiếu nhập hàng để nhận các mặt hàng thành phẩm
Nhận các Mặt hàng từ Nhà cung cấp của bạn bằng cách sử dụng [Phiếu nhập hàng](/docs/v16/user/manual/vi/stock/purchase-receipt). Bạn cần nhập Kho của Nhà cung cấp nơi nguyên vật liệu sẽ được lấy ra và thành phẩm sẽ được nhận tại Kho Chấp nhận (Accepted Warehouse). Hãy coi việc này giống như một quy trình backflush cho gia công ngoài.

Nhấp vào Create > Purchase Receipt từ Đơn mua hàng. Thiết lập Kho Chấp nhận và Kho Nhà cung cấp. Đảm bảo kiểm tra “Consumed Quantity” trong bảng “Raw Materials” để lượng tồn kho tại phía Nhà cung cấp được duy trì chính xác. Bạn cần chọn Kho của Nhà cung cấp nơi bạn sẽ nhận thành phẩm.

<img class="screenshot" alt="Sub-Contracting" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/subcontract5.png">

### 1.5 Nguyên vật liệu do Nhà cung cấp cung cấp
Khi tạo BOM để gia công ngoài, có thể có một vài nguyên vật liệu như đai ốc và bu lông mà các Nhà cung cấp sẽ phải tự thu mua.

Khi tạo Phiếu kho để "Chuyển" từ Đơn mua hàng, các mặt hàng này có thể được loại trừ từng cái một, nhưng điều này là không thể nếu bạn có hơn 100 mặt hàng.

Nếu một số nguyên vật liệu được Nhà cung cấp cung cấp trực tiếp, thì những nguyên vật liệu đó phải được đưa vào BOM.

* Nó sẽ có giá trị bằng không trong BOM
* Trong Đơn mua hàng, nguyên vật liệu này sẽ không xuất hiện trong Mục đã cung cấp vì nó không được cung cấp
* Ngoài ra, khi tạo một lệnh "Chuyển", các mặt hàng như vậy sẽ bị loại trừ khỏi Phiếu kho

<img class="screenshot" alt="Supplier Sourced Raw Material" src="https://docs.erpnext.com/docs/v16/assets/img/manufacturing/supplier_sourced_material.png">