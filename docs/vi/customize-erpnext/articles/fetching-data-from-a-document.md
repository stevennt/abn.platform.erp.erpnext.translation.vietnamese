<!-- add-breadcrumbs -->
# Lấy dữ liệu từ một DocType

**Câu hỏi:** Chúng tôi theo dõi trường Số Đơn mua hàng (PO Number) và Ngày Đơn mua hàng (PO Date) của Khách hàng trong Đơn bán hàng. Để các giá trị này cũng được lấy sang Hóa đơn bán hàng, chúng tôi đã thêm Trường tùy chỉnh (Custom Field) vào Hóa đơn bán hàng. Tuy nhiên, khi chúng tôi tạo Hóa đơn bán hàng từ Đơn bán hàng, các chi tiết Đơn mua hàng của Khách hàng không được lấy sang.

**Trả lời:** Khi dữ liệu được lấy từ giao dịch này sang giao dịch khác, việc ánh xạ dữ liệu được thực hiện dựa trên tên trường. Nếu hai giao dịch có các trường với tên hoàn toàn giống nhau, thì các giá trị của chúng sẽ được ánh xạ.

Ví dụ, nếu bạn muốn Số Đơn mua hàng và Ngày Đơn mua hàng của Khách hàng được lấy từ Đơn bán hàng sang Hóa đơn bán hàng, bạn nên đảm bảo rằng các Trường tùy chỉnh được thêm vào trong Hóa đơn bán hàng có tên trường hoàn toàn giống với tên trường trong Đơn bán hàng.

Đơn bán hàng (các trường tiêu chuẩn)

<img class="screenshot" alt="Standard fields in Sales Order" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-fetch-data-1.png">

Hóa đơn bán hàng (các trường tùy chỉnh)

<img class="screenshot" alt="Custom Field in Sales Invoice" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-fetch-data-2.png">

Vì tên của các trường liên quan đến Đơn mua hàng của Khách hàng giống nhau trong Đơn bán hàng và Hóa đơn bán hàng, nên khi tạo Hóa đơn bán hàng từ Đơn bán hàng, các giá trị trong các trường này sẽ được tự động lấy sang.

<img class="screenshot" alt="Values fetching from Sales Order to Sales Invoice" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-fetch-data-3.png">

<img class="screenshot" alt="Values fetching from Sales Order to Sales Invoice" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-fetching-data.gif">

{next}