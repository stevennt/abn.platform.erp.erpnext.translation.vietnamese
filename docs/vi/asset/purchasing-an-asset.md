<!-- add-breadcrumbs -->
# Mua Tài sản

Để mua một tài sản mới:

1. Tạo Nhóm tài sản (Asset Category)
1. Tạo một Mặt hàng (Item) liên quan và bật tùy chọn 'Is Fixed Asset' để tạo tài sản.
1. Bạn cũng có thể bật 'Auto Create Assets on Purchase' để tự động tạo tài sản. (Tùy chọn)

  <img class="screenshot" alt="Purchasing Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-auto-create.png">

1. Sau đó, cần tuân thủ [quy trình mua hàng](/docs/v13/user/manual/en/buying/purchase-order) để mua tài sản.
1. Nhập Vị trí tài sản (Asset Location) trong bảng Mặt hàng của [Phiếu nhập hàng](/docs/v13/user/manual/en/stock/purchase-receipt) hoặc [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice) mà bạn đang dùng để nhận mặt hàng.
1. Khi Xác nhận Phiếu nhập hàng, dựa trên ô đánh dấu tự động tạo, các bản ghi Tài sản sẽ được tạo tự động. Sau đó, bạn có thể nhập các chi tiết khác của Tài sản một cách thủ công từ biểu mẫu Tài sản.

<img class="screenshot" alt="Purchasing Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-auto-create-on-purchase.png">

Các bút toán kế toán sau đây sẽ được ghi sổ khi Xác nhận phiếu nhập hàng nếu tính năng Kế toán Chi phí xây dựng cơ bản dở dang (Capital Work In Progress Accounting) được bật trong Nhóm tài sản của tài sản được mua.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-purchase-receipt-gl-entries.png">

Tại đây cần lưu ý rằng, thay vì tài khoản tài sản tương ứng, tài khoản Chi phí xây dựng cơ bản dở dang (CWIP) đã được ghi nợ. Điều này là do tài sản mới chỉ được mua và vẫn chưa sẵn sàng để sử dụng. Cho đến khi tài sản sẵn sàng để sử dụng, giá trị tài sản sẽ được duy trì đối với tài khoản này. Vào ngày tài sản sẵn sàng để sử dụng, tài khoản CWIP sẽ được ghi có và tài khoản tài sản tương ứng sẽ được ghi nợ.

Trong trường hợp tính năng 'Capital Work In Progress Accounting' bị tắt trong Nhóm tài sản, phiếu nhập hàng sẽ được ghi nhận đối với các tài khoản tài sản tương ứng đã được thiết lập trong Nhóm tài sản.

ERPNext cũng sử dụng một tài khoản tạm thời "Asset Received But Not Billed" (tài khoản nợ phải trả), tài khoản này sẽ được ghi có khi Xác nhận phiếu nhập hàng. Sau đó, khi Xác nhận Hóa đơn mua hàng, tài khoản này sẽ được ghi nợ/đảo ngược.

#### Các chủ đề liên quan
1. [Tài sản](/docs/v13/user/manual/en/asset/asset)
1. [Phiếu nhập hàng](/docs/v13/user/manual/en/stock/purchase-receipt)
1. [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice)

{next}