<!-- add-breadcrumbs -->
# Custom Script để lấy giá trị từ dữ liệu gốc (Master)

Để lấy giá trị từ một trường liên kết khi được chọn, hãy sử dụng phương thức `add_fetch`.

    
    
    add_fetch(link_fieldname, source_fieldname, target_fieldname)
    

### Ví dụ

Giả sử bạn đã tạo một Trường tùy chỉnh (Custom Field) là **VAT ID** (`vat_id`) trong **Khách hàng** (Customer) và **Hóa đơn bán hàng** (Sales Invoice), và bạn muốn đảm bảo rằng giá trị này được cập nhật mỗi khi bạn chọn một Khách hàng trong Hóa đơn bán hàng.

Để cấu hình việc này, trong Custom Script của Hóa đơn bán hàng, bạn có thể thêm dòng sau:

    
    
    cur_frm.add_fetch('customer','vat_id','vat_id')
    


{next}