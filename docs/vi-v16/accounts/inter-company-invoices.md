<!-- add-breadcrumbs -->

# Hóa đơn liên công ty

**Một Hóa đơn bút toán liên công ty được thực hiện giữa các tổ chức thuộc cùng một tập đoàn.**

Cùng với việc tạo Hóa đơn mua hàng hoặc Hóa đơn bán hàng cho một công ty duy nhất, bạn có thể tạo các hóa đơn liên kết với nhau cho nhiều công ty.

Ví dụ, bạn có thể tạo một Hóa đơn mua hàng cho một công ty, chẳng hạn 'Công ty ABC', và tạo một Hóa đơn bán hàng đối ứng với Hóa đơn mua hàng này cho một công ty khác, chẳng hạn 'Công ty XYZ' và liên kết chúng lại với nhau.

## 1. Cách tạo Hóa đơn liên công ty

### 1.1 Thiết lập
1. Đi đến: **Accounts > Masters > Khách hàng**.
2. Chọn Khách hàng mà bạn muốn chọn cho hóa đơn liên kết.
3. Bật hộp kiểm, **Is Internal Customer** hiển thị như sau:

![Internal Customer](https://docs.erpnext.com/docs/v16/assets/img/accounts/inter-company-customer.png)

4. Thêm công ty mà Khách hàng đó đại diện vào trường **Represents Company**. Đây là công ty mà Hóa đơn bán hàng sẽ được tạo.
5. Trong bảng **Allowed To Transact With**, thêm công ty mà bạn sẽ tạo Hóa đơn mua hàng đối ứng.
6. Bây giờ, khi bạn tạo một Hóa đơn mua hàng đối ứng với công ty A (khách hàng thuộc công ty B, người bán là công ty A), nó sẽ được liên kết với Hóa đơn bán hàng cho công ty A được tạo bằng cách sử dụng Khách hàng nội bộ này từ công ty B.
7. Bây giờ, bạn cần thực hiện quy trình tương tự để thiết lập Nhà cung cấp cho các hóa đơn liên kết.
8. Đi đến: **Accounts > Masters > *Chọn Nhà cung cấp***
9. Tích vào **Is Internal Supplier**.
10. Trong trường **Represents Company**, thêm công ty mà bạn đã thêm vào bảng **Allowed To Transact With** cho Khách hàng.
11. Trong bảng **Allowed To Transact With** của Nhà cung cấp, thêm công ty mà Khách hàng đại diện. Đây là công ty mà bạn sẽ thực hiện một Hóa đơn mua hàng liên kết.
12. Đây là ảnh chụp màn hình về công ty Nhà cung cấp để tránh bất kỳ sự nhầm lẫn nào:

![Inter Company Supplier](https://docs.erpnext.com/docs/v16/assets/img/accounts/inter-company-supplier.png)

### 1.2 Tạo Hóa đơn
1. Bây giờ, tạo một [Sales Invoice](sales-invoice.md) mới, điền đầy đủ các trường.
2. Hãy nhớ chọn Khách hàng là khách hàng nội bộ và công ty mà họ đang mua hàng.
3. **Lưu** và **Xác nhận** Hóa đơn.

 <img class="screenshot" alt="Inter company invoice" src="https://docs.erpnext.com/docs/v16/assets/img/accounts/make-inter-company-invoice.png">

1. Trước khi bạn thực hiện *Hóa đơn liên công ty*, bạn cần thực hiện các bước sau:
    1. Giá bán và giá mua giữa các công ty phải đồng bộ.
    2. Đi đến **Stock > Price List**, tạo một Bảng giá mới cho các giao dịch liên công ty.
    3. Tích chọn cả Selling và Buying trong Bảng giá mới này.
    4. Đi đến **Buying > Supplier > *internal supplier***, trong phần tiền tệ và bảng giá, hãy thiết lập bảng giá thành bảng giá mới vừa tạo.
    5. Thực hiện tương tự cho khách hàng nội bộ, tức là thiết lập bảng giá thành bảng giá mới.
    6. Bây giờ, bạn có thể thực hiện Hóa đơn mua hàng hoặc Hóa đơn bán hàng liên công ty.
2. Dưới menu thả xuống của nút **Make**, bạn sẽ thấy một liên kết **Inter Company Invoice**, khi nhấp vào liên kết, bạn sẽ được chuyển đến trang biểu mẫu Hóa đơn mua hàng mới.
3. Tại đây, nhà cung cấp và công ty sẽ được tự động lấy dữ liệu tùy thuộc vào công ty bạn đã chọn trong Hóa đơn bán hàng.

> ***Lưu ý**: Chỉ có thể có duy nhất một Nhà cung cấp hoặc Khách hàng nội bộ cho mỗi công ty.*

4. **Xác nhận** hóa đơn, hoàn tất! Bây giờ, cả hai hóa đơn đã được liên kết với nhau. *Ngoài ra, khi **Hủy** bất kỳ hóa đơn nào, liên kết cũng sẽ bị phá vỡ.*

> Ghi chú: Một hóa đơn liên công ty sẽ chỉ ảnh hưởng đến sổ cái kế toán mà không ảnh hưởng đến sổ cái tồn kho. Điều này là do các công ty thuộc cùng một tập đoàn.

Bạn có thể làm theo quy trình tương tự để tạo một Hóa đơn mua hàng và sau đó là một Hóa đơn bán hàng liên kết từ Hóa đơn mua hàng đã được **Xác nhận**.

### 2. Các chủ đề liên quan
1. [Sales Invoice](sales-invoice.md)
1. [Purchase Invoice](purchase-invoice.md)
1. [Inter Company Journal Entry](inter-company-journal-entry.md)

{next}