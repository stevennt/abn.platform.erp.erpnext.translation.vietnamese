<!-- add-breadcrumbs -->
# Trường Tỷ giá hối đoái bị đóng băng

Trong ERPNext, bạn có thể lấy Tỷ giá hối đoái giữa các loại tiền tệ trong thời gian thực, hoặc cũng có thể lưu các tỷ giá hối đoái cụ thể. Trong ERPNext, các tỷ giá hối đoái đã lưu cũng được gọi là Tỷ giá hối đoái cũ (Stale Exchange Rate).

Trong các giao dịch bán hàng và mua hàng của bạn, nếu trường Tỷ giá hối đoái bị đóng băng, đó là do tính năng cho phép sử dụng tỷ giá hối đoái cũ trong các giao dịch đã được bật. Nếu bạn muốn làm cho trường Tỷ giá hối đoái có thể chỉnh sửa được một lần nữa, hãy tắt tính năng Tỷ giá hối đoái cũ từ:

* Kế toán > Danh mục kế toán > Thiết lập kế toán (Accounting Settings)
* Bỏ chọn trường "Allow Stale Exchange Rates".

    ![Allow Stale Exchange Rates](/docs/v13/assets/img/articles/allow-stale-exchange-rates.png)
    
* Lưu Thiết lập kế toán
* Làm mới tài khoản ERPNext của bạn
* Kiểm tra lại giao dịch Bán hàng / Mua hàng

Sau thiết lập này, trường Tỷ giá hối đoái trong các giao dịch sẽ có thể chỉnh sửa được một lần nữa.

{next}