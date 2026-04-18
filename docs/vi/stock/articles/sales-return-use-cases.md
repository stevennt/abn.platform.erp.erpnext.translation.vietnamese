# Quản lý Trả hàng bán

Trong trường hợp Trả hàng bán, các điều chỉnh liên quan đến tồn kho và kế toán sau đây có thể được xử lý theo nhiều cách khác nhau. Hãy cùng kiểm tra việc hạch toán kho và tài khoản sẽ được ghi nhận như thế nào dựa trên việc điều chỉnh Trả hàng bán.

### Trả hàng chưa thanh toán

Nếu khách hàng yêu cầu trả hàng ngay cả trước khi xử lý thanh toán, bạn có thể đơn giản là:

1. Hủy Hóa đơn bán hàng.
2. Tạo một Phiếu trả hàng bán dựa trên Phiếu giao hàng.

Nếu luật pháp hiện hành không cho phép bạn hủy Hóa đơn bán hàng, bạn cũng có thể tạo một Giấy báo có (Credit Note) dựa trên Hóa đơn bán hàng.

### Hóa đơn bán hàng đã thanh toán - Điều chỉnh qua Giấy báo có

Đây là kịch bản mà khách hàng đã mua một mặt hàng từ bạn, Hóa đơn bán hàng đã được Xác nhận và họ cũng đã thanh toán.

1. Tạo một Giấy báo có dựa trên Hóa đơn bán hàng.
2. Trong Hóa đơn bán hàng, kiểm tra trường "Is Paid". Đảm bảo rằng Tài khoản thanh toán / Phương thức thanh toán đã được chọn trong bảng liên quan.
3. Nếu bạn cũng muốn trả lại mặt hàng thông qua chính Hóa đơn bán hàng, hãy kiểm tra trường "Update Stock".
4. Lưu và Xác nhận Giấy báo có.

<img class="screenshot" alt="Create sales return" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sales-return-against-payment.png">

Theo bút toán này, các mặt hàng đã bán sẽ được nhập lại vào Kho của bạn. Đồng thời, khoản thanh toán nhận được từ Khách hàng sẽ được đảo ngược.

Sau khi tạo Giấy báo có, Số dư còn lại của Hóa đơn bán hàng sẽ chuyển sang số âm. Điều này giúp bạn có phạm vi để điều chỉnh Hóa đơn bán hàng này (với số dư âm) để đối trừ với các Hóa đơn bán hàng còn nợ trong tương lai.

### Hóa đơn bán hàng chưa thanh toán - Giấy báo có

Trong trường hợp Trả hàng bán mà khách hàng chưa thực hiện bất kỳ khoản thanh toán nào, bạn có thể đơn giản là tạo một Giấy báo có. Khi tạo Giấy báo có, Số dư còn lại của Hóa đơn bán hàng sẽ trở nên âm.

Để điều chỉnh tồn kho, bạn có thể tạo một Phiếu trả hàng bán dựa trên Phiếu giao hàng hoặc trong chính Giấy báo có, hãy kiểm tra trường "Update Stock".