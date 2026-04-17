<!-- add-breadcrumbs -->
#Cho phép Giao hàng/Lập hóa đơn vượt mức

Khi tạo Phiếu giao hàng, hệ thống sẽ kiểm tra xem số lượng mặt hàng có khớp với Đơn bán hàng hay không. Nếu số lượng mặt hàng đã tăng lên, bạn sẽ nhận được thông báo xác nhận về việc giao hàng hoặc nhập hàng vượt mức.

Trong trường hợp bán hàng, nếu bạn muốn có thể giao nhiều mặt hàng hơn so với số lượng đã nêu trong Đơn bán hàng, bạn nên cập nhật mục "Allow over delivery or receipt upto this percent" (Cho phép giao hàng hoặc nhập hàng vượt mức tối đa bao nhiêu phần trăm) trong danh mục Mặt hàng.

<img alt="Itemised Limit Percentage" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/limit-1.png">

Khi tạo hóa đơn, đơn giá của mặt hàng cũng được kiểm tra dựa trên các giao dịch trước đó như Đơn bán hàng. Điều này cũng áp dụng khi tạo Phiếu nhập hàng hoặc Hóa đơn mua hàng từ Đơn mua hàng. Việc cập nhật "Allow over delivery or receipt upto this percent" sẽ có hiệu lực trong tất cả các giao dịch mua và bán.

Ví dụ, nếu bạn đã đặt hàng 100 đơn vị của một mặt hàng, và nếu tỷ lệ phần trăm nhập hàng vượt mức của mặt hàng đó là 50, thì bạn được phép lập Phiếu nhập hàng cho tối đa 150 đơn vị.

Cập nhật giá trị chung cho "Allow over delivery or receipt upto this percent" từ Cài đặt kho. Giá trị được cập nhật tại đây sẽ áp dụng cho tất cả các mặt hàng.

1. Đi tới `Stock > Setup > Stock Settings`

2. Thiết lập `Limit Percentage`.

3. Lưu Cài đặt kho.

<img alt="Item wise Allowance percentage" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/limit-2.png">


<!-- markdown -->