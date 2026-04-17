<!-- add-breadcrumbs -->

### Báo cáo GSTR3B trong ERPNext

Để tạo Báo cáo GSTR3B trong ERPNext, hãy điều hướng đến <br>
> **Accounting > Goods and Services Tax (GST India) > GSTR 3B Report** <br>

hoặc chỉ cần tìm kiếm GSTR 3B Report trong awesomebar.

Nhấp vào New để tạo một báo cáo mới hoặc chọn một báo cáo hiện có để cập nhật hoặc tải xuống JSON.

Nhập các chi tiết sau để tạo báo cáo:
1. Company Name (Tên Công ty)
2. Company Address (Địa chỉ Công ty) được liên kết với GSTIN mà báo cáo cần được tạo
3. Year (Năm)
4. Month (Tháng)

![GSTR 3B Report](https://docs.erpnext.com/docs/v13/assets/img/regional/india/gstr-3b-input.png)

Nhấp vào Lưu để tạo báo cáo. Một báo cáo hiện có cũng có thể được cập nhật/tạo lại bằng cách nhấp vào Lưu.

Sau khi lưu, bạn có thể thấy kết quả JSON trong trường văn bản bên dưới, kết quả này cũng có thể được tải xuống bằng cách sử dụng nút Download JSON ở góc trên bên phải như hiển thị trong hình dưới đây.

![GSTR 3B With JSON](https://docs.erpnext.com/docs/v13/assets/img/regional/india/gstr-3b-report.png)

Nếu bạn muốn in báo cáo, nó cũng có thể được in và xem trong GSTR3B Form bằng cách nhấp vào View Form như hiển thị bên dưới.

![Download Option in GSTR 3B](https://docs.erpnext.com/docs/v13/assets/img/regional/india/gstr-3b-download.png)

Lưu ý: Để đảm bảo báo cáo được tính toán chính xác và đúng đắn, vui lòng lưu ý những điều sau.

1. Vì GST là thuế dựa trên điểm đến, vui lòng đảm bảo tất cả Khách hàng và Nhà cung cấp tại Ấn Độ đều có gst state (ngay cả những đối tượng chưa đăng ký).

2. Đối với các mặt hàng không chịu thuế (Nil rated), được miễn thuế (exempted) hoặc không thuộc diện GST (non-gst), ô Is nill rated hoặc Is Non GST phải được tích chọn trong thông tin mặt hàng (item master).

![GST Exempted](https://docs.erpnext.com/docs/v13/assets/img/regional/india/gst-item.png)

3. Các tài khoản (account heads) phù hợp đã được nhập trong GST Settings.

4. Trường Eligibility For ITC phù hợp đã được chọn. Ví dụ: All Other ITC hoặc Ineligible

{next}