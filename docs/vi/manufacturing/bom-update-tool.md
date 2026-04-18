<!-- add-breadcrumbs -->
# Công cụ cập nhật BOM

**Từ Công cụ cập nhật BOM, bạn có thể thay thế BOM của một cụm lắp ráp phụ và cập nhật chi phí của tất cả các BOM cha.**

Sử dụng tiện ích này, bạn có thể thay thế một BOM hiện có của một mặt hàng cụm lắp ráp phụ đang được liên kết với một BOM cha. Hệ thống sẽ cập nhật BOM mới vào tất cả các BOM cha nơi nó đã được sử dụng. Trước tiên, bạn cần tạo một BOM mới.

Để sử dụng Công cụ cập nhật BOM, hãy đi đến:

> Home > Manufacturing > Tools > BOM Update Tool

## 1. Cách sử dụng Công cụ cập nhật BOM
Hãy xem xét một tình huống để hiểu rõ hơn về chức năng này.

Giả sử một công ty sản xuất máy tính, Định mức nguyên vật liệu cho máy tính sẽ trông như sau:

1. Màn hình
1. Bàn phím
1. Chuột
1. CPU

Trong số tất cả các mặt hàng trên, CPU được lắp ráp riêng biệt. Do đó, một BOM riêng sẽ được tạo cho CPU. Dưới đây là các mặt hàng từ BOM của CPU.

1. Ổ cứng 250 GB
1. Bo mạch chủ
1. Bộ vi xử lý
1. SMTP
1. Đầu đọc DVD

Nếu cần thêm nhiều mặt hàng hơn, hoặc cần chỉnh sửa các mặt hàng hiện có trong BOM của CPU, hãy tạo một BOM mới cho nó.

1. _Ổ cứng 950 GB_
1. Bo mạch chủ
1. Bộ vi xử lý
1. SMTP
1. Đầu đọc DVD

Chọn BOM hiện tại (Current BOM) và BOM mới (New BOM) của mặt hàng **cụm lắp ráp phụ (sub-assembly)**:

<img class="screenshot" alt="BOM Update Tool" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/bom-update-tool.png">

Để cập nhật BOM mới vào tất cả các BOM cha nơi CPU được chọn làm cụm lắp ráp phụ, bạn có thể sử dụng nút **Replace** (Thay thế).

Khi nhấp vào nút Replace, BOM cũ của CPU sẽ được thay thế bằng BOM mới trong BOM của mặt hàng thành phẩm (Máy tính).

**Công cụ thay thế BOM có hoạt động để thay thế các mặt hàng được phân rã (exploded Items) trong BOM cha không?**

Không, các mặt hàng được phân rã mà không có BOM riêng của chúng thì không thể được thay thế trong BOM cha. Ví dụ, hãy xem xét nếu mặt hàng Màn hình không có cụm lắp ráp phụ, nó sẽ không thể được cập nhật bằng công cụ này. Để cập nhật các mặt hàng được phân rã, bạn nên Hủy và Sửa đổi (Cancel and Amend) BOM hiện tại, hoặc tạo một BOM mới cho mặt hàng thành phẩm.

## Cập nhật chi phí BOM
Sử dụng nút **Update latest price in all BOMs** (Cập nhật giá mới nhất trong tất cả các BOM), bạn có thể cập nhật chi phí của tất cả các Định mức nguyên vật liệu, dựa trên giá mua mới nhất/giá bảng giá/giá trị tính giá của nguyên vật liệu. Điều này hữu ích nếu BOM đã cập nhật của bạn có các nguyên vật liệu với Đơn giá khác nhau.

Khi nhấp vào nút này, hệ thống sẽ tạo một tiến trình chạy ngầm để cập nhật chi phí của tất cả các BOM. Nó được xử lý thông qua các tác vụ chạy ngầm vì quá trình này có thể mất vài phút (tùy thuộc vào số lượng BOM) để cập nhật tất cả các BOM.

Chức năng này cũng có thể được thực hiện tự động hàng ngày. Để làm điều đó, bạn cần bật "Update BOM Cost Automatically" từ Manufacturing Settings.