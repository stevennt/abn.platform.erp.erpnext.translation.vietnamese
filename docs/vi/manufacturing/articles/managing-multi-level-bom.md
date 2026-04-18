<!-- add-breadcrumbs -->
#Quản lý BOM nhiều cấp

Hãy xem xét một kịch bản trong đó quy trình sản xuất của bạn bao gồm việc sản xuất các mặt hàng lắp ráp phụ trước khi tạo ra thành phẩm cuối cùng. Trong trường hợp này, bạn nên quản lý BOM như thế nào?

Trước hết, bạn cần có các BOM cho các cụm lắp ráp phụ, sau đó các BOM này sẽ được liên kết với BOM của thành phẩm cuối cùng. Trong ảnh chụp màn hình sau, bạn có thể thấy rằng BOM cho Brush Bristles (lắp ráp phụ) được liên kết với BOM của Shaving Brush (thành phẩm). Điều này được hiển thị trong bảng Vật tư (Materials) trong danh mục Định mức nguyên vật liệu.

![Multi-level BOM](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/multi-bom.png)

Bảng 'Materials' sẽ chỉ hiển thị các cụm lắp ráp phụ, trong khi bảng 'Materials Required (Exploded)' sẽ hiển thị tất cả các nguyên vật liệu thô cần thiết để sản xuất thành phẩm cuối cùng.

Bảng vật tư BOM nơi hiển thị cụm lắp ráp phụ:
![Multi-level BOM](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/bom-materials.png)

Trong chế độ xem phân rã (exploded view), chỉ các nguyên vật liệu thô được hiển thị:
![Multi-level BOM](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/bom-materials-exploded.png)


Để sử dụng BOM nhiều cấp trong Lệnh sản xuất, hãy bật hộp kiểm 'Use Multi-Level BOM'. Tùy chọn này được bật theo mặc định. Nếu bạn muốn lập kế hoạch vật tư cho các cụm lắp ráp phụ của Mặt hàng mà bạn đang sản xuất, hãy để tùy chọn này được bật. Nếu bạn lập kế hoạch và sản xuất các cụm lắp ráp phụ một cách riêng biệt, hãy bỏ chọn hộp kiểm này.

<!-- <img alt="Nested BOM" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/nested-bom-1.png"> -->

Hãy xem xét một ví dụ khác để hiểu rõ hơn về trường hợp một chiếc máy tính đang được lắp ráp. Ổ cứng và ổ đĩa DVD cũng đang được sản xuất và chúng là các cụm lắp ráp phụ. BOM nhiều cấp hoặc BOM lồng nhau sẽ trông như thế này:

    
- Personal Computer (Mặt hàng thành phẩm)
    - Mother Board
    - SMTP
    - Accessories and wires
    - Hard Disk (lắp ráp phụ)
        - Item A
        - Item B
        - Item C
    - DVD Drive (lắp ráp phụ)
        - Item X
        - Item Y
        - Item Z