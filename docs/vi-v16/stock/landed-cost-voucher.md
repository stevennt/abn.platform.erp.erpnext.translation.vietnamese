<!-- add-breadcrumbs -->
# Phiếu chi phí chuyển đến

**Chi phí chuyển đến là tổng chi phí cuối cùng liên quan đến một mặt hàng để nó đến được kho của người mua.**

Chi phí chuyển đến bao gồm giá gốc của mặt hàng, toàn bộ chi phí vận chuyển, thuế hải quan, thuế, bảo hiểm, phí chuyển đổi tiền tệ, v.v. Tất cả các thành phần này có thể không áp dụng cho mọi lô hàng, nhưng các thành phần liên quan phải được xem xét như một phần của chi phí chuyển đến.

> **Chi phí chuyển đến là gì?**

> Để hiểu rõ hơn về chi phí chuyển đến, hãy lấy một ví dụ trong đời sống hàng ngày. Bạn cần mua một chiếc máy giặt mới cho gia đình. Trước khi thực hiện mua hàng thực tế, bạn có thể sẽ tìm hiểu để biết mức giá tốt nhất. Trong quá trình này, bạn thường tìm thấy một ưu đãi tốt hơn từ một cửa hàng ở xa nhà. Nhưng bạn cũng nên xem xét chi phí vận chuyển khi mua từ cửa hàng đó. Tổng chi phí bao gồm cả vận chuyển có thể cao hơn mức giá bạn nhận được tại cửa hàng gần nhà. Trong trường hợp đó, bạn sẽ chọn mua từ cửa hàng gần nhất, vì chi phí chuyển đến của mặt hàng tại cửa hàng gần nhất rẻ hơn.

Tương tự trong kinh doanh, việc xác định chi phí chuyển đến cho một Mặt hàng là rất quan trọng, vì nó giúp quyết định giá bán của mặt hàng đó và ảnh hưởng đến khả năng sinh lời của công ty. Do đó, tất cả các khoản phí chi phí chuyển đến áp dụng nên được bao gồm trong giá trị tính giá của Mặt hàng.

Trong phiên bản v16, tính năng này được tối ưu hóa để hỗ trợ quản lý kho chính xác hơn, đặc biệt khi kết hợp với hệ thống [Quản lý tồn kho theo từng mặt hàng (Item-Level Stock Accounting)](stock-accounting.md).

Để truy cập danh sách Phiếu chi phí chuyển đến, hãy đi tới:
> Home > Stock > Tools > Landed Cost Voucher

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Phiếu chi phí chuyển đến, bạn nên tạo các chứng từ sau trước:

* [Phiếu nhập hàng](purchase-receipt.md)

    Hoặc

* [Hóa đơn mua hàng](../accounts/purchase-invoice.md)


## 2. Cách tạo Phiếu chi phí chuyển đến

1. Đi tới danh sách Phiếu chi phí chuyển đến, nhấp vào **Mới**.
1. Chọn Loại chứng từ nhập hàng là Hóa đơn mua hàng hoặc Phiếu nhập hàng. Bạn có thể chọn nhiều chứng từ.
1. Chọn Hóa đơn hoặc Phiếu nhập hàng cụ thể. Tên Nhà cung cấp và Tổng cộng sẽ được tự động lấy ra.
1. Nhấp vào nút **Lấy các mặt hàng từ Phiếu nhập hàng** để lấy chi tiết mặt hàng từ Hóa đơn mua hàng/Phiếu nhập hàng.
1. Chọn xem Phân bổ chi phí dựa trên **Số lượng** hay **Số tiền**.
1. Nhập Tài khoản chi phí và Số tiền cho Chi phí bổ sung trong bảng Thuế và phí. Số tiền sẽ được phân bổ dựa trên số lượng hoặc số tiền theo lựa chọn của bạn.
1. **Lưu** và **Xác nhận**.

    <img class="screenshot" alt="Landed Cost Voucher" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/landed-cost-voucher.png">

Trong chứng từ, bạn có thể chọn nhiều Phiếu nhập hàng/Hóa đơn mua hàng và lấy tất cả các mặt hàng từ các chứng từ đó. Sau đó, bạn nên thêm các khoản phí áp dụng vào bảng “Thuế và phí”. Bạn có thể dễ dàng xóa một mặt hàng nếu các khoản phí đã thêm không áp dụng cho mặt hàng đó.

Các khoản phí được thêm vào sẽ được phân bổ tỷ lệ cho tất cả các mặt hàng dựa trên số tiền hoặc số lượng của chúng. Nếu bạn chọn dựa trên số tiền, Mặt hàng có số tiền cao nhất sẽ được phân bổ tỷ lệ phí cao nhất. Trong trường hợp dựa trên số lượng, Mặt hàng có số lượng lớn nhất sẽ được phân bổ phần lớn các khoản phí và các Mặt hàng khác sẽ được phân bổ số tiền ít hơn.

## 3. Các hành động liên quan
### 3.1 Thêm Chi phí chuyển đến ngay trong Phiếu nhập hàng

Trong ERPNext, bạn có thể thêm các khoản phí liên quan đến chi phí chuyển đến trong bảng “Thuế và phí” khi tạo Phiếu nhập hàng (PR). Bạn nên thêm các khoản phí đó cho “Tổng và Giá trị tính giá” hoặc “Giá trị tính giá” trong trường 'Xét thuế hoặc phí cho'. Các khoản phí phải trả cho cùng một Nhà cung cấp mà bạn đang mua hàng nên được gắn thẻ là “Tổng và Giá trị tính giá”. Ngược lại, nếu các khoản phí áp dụng phải trả cho bên thứ ba, nó nên được gắn thẻ là “Giá trị tính giá”. Khi **Xác nhận** Phiếu nhập hàng, hệ thống sẽ tính toán chi phí chuyển đến của tất cả các mặt hàng, có tính đến các khoản phí đó. Chi phí chuyển đến này sẽ được xem xét để tính Giá trị tính giá của mặt hàng (dựa trên phương pháp FIFO / Giá bình quân gia quyền).

Tuy nhiên, trong thực tế, khi lập Phiếu nhập hàng, chúng ta có thể không biết tất cả các khoản phí áp dụng. Đơn vị vận chuyển có thể gửi hóa đơn sau một thời gian. Trong những trường hợp này, “Phiếu chi phí chuyển đến” trở nên hữu ích, vì nó cho phép bạn thêm các khoản phí bổ sung đó vào một ngày sau đó, và cập nhật chi phí chuyển đến của các mặt hàng đã mua mà không cần sửa đổi chứng từ gốc.

### 3.2 Điều gì xảy ra khi Xác nhận?

1. **Tính toán lại giá trị:** Giá trị tính giá của các mặt hàng được tính toán lại dựa trên chi phí chuyển đến mới. Với tính năng [Quản lý tồn kho theo từng mặt hàng](stock-accounting.md), việc phân bổ này sẽ được ghi nhận chính xác vào sổ cái cho từng mặt hàng cụ thể.
2. **Bút toán sổ cái:** Nếu bạn đang sử dụng “Kiểm kê vĩnh viễn”, hệ thống sẽ ghi **Bút toán (JE)** để điều chỉnh số dư Tồn kho. Hệ thống sẽ ghi nợ (tăng) “tài khoản kho” tương ứng và ghi có (giảm) **Tài khoản chi phí** được đề cập trong bảng Thuế và phí. 
3. **Điều chỉnh Giá vốn:** Nếu các mặt hàng đã được xuất kho, giá trị Giá vốn hàng bán (CoGS) đã được ghi nhận theo giá trị tính giá cũ. Do đó, các bút toán sổ cái sẽ được ghi lại cho tất cả các bút toán xuất kho trong tương lai của các mặt hàng liên quan để điều chỉnh giá trị CoGS một cách chính xác.

Bạn có thể kiểm tra các thay đổi này thông qua tính năng **Xem trước sổ cái (Ledger Preview)** để đảm bảo các bút toán được ghi nhận đúng theo kỳ kế toán.

## 4. Các tính năng nâng cao trong v16
* **Hệ thống Giữ chỗ Tồn kho (Stock Reservation System):** Khi chi phí chuyển đến làm thay đổi giá trị mặt hàng, hệ thống vẫn đảm bảo tính nhất quán với các lệnh giữ chỗ hàng hóa đã tạo trước đó.
* **Truy xuất nguồn gốc Lô/Số sê-ri (Serial/Batch Traceability Report):** Chi phí chuyển đến được phân bổ chính xác vào từng Lô hàng (Batch) hoặc Số sê-ri (Serial), giúp báo cáo giá trị tồn kho theo lô trở nên cực kỳ chính xác.