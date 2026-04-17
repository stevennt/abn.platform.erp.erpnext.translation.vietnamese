<!-- add-breadcrumbs -->
# Số lượng trường tối đa trong một Biểu mẫu

Đôi khi trong quá trình tạo các trường tùy chỉnh, bạn có thể gặp phải thông báo lỗi như sau:

> Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs.

### Điều này có nghĩa là gì?

Nói một cách đơn giản, điều này có nghĩa là bạn đã chạm đến giới hạn số lượng trường tối đa cho biểu mẫu/DocType cụ thể đó. Vậy, giới hạn tối đa của các trường là bao nhiêu?

Trong MySQL, có một giới hạn cứng là 4096 cột cho mỗi bảng, nhưng giới hạn tối đa thực tế có thể thấp hơn đối với một bảng nhất định. Giới hạn chính xác phụ thuộc vào nhiều yếu tố tương tác với nhau.

Mỗi bảng (bất kể công cụ lưu trữ nào) đều có kích thước hàng tối đa là 65.535 byte. Các công cụ lưu trữ có thể đặt thêm các ràng buộc bổ sung lên giới hạn này, làm giảm kích thước hàng tối đa thực tế.

Kích thước hàng tối đa sẽ giới hạn số lượng (và có thể là kích thước) của các cột vì tổng độ dài của tất cả các cột không được vượt quá kích thước này (65.535 byte). Ví dụ, các ký tự `utf8mb3` yêu cầu tối đa 3 byte cho mỗi ký tự, vì vậy đối với một cột `VARCHAR(140)`, máy chủ phải phân bổ `140 × 3 = 420` byte cho mỗi giá trị. Do đó, một bảng không thể chứa quá `65.535 / 420 = 156` cột như vậy.

Trong framework Frappe, các cột kiểu `VARCHAR(140)` được tạo dựa trên các loại trường "Data", "Link", "Select", "Dynamic Link", "Password" và "Read Only". Do đó, bạn có thể tạo khoảng 156 cột như vậy trong hệ thống.

### Giải pháp:

Để thêm nhiều trường hơn vào hệ thống, bạn có thể thực hiện một số thay đổi sau.

1. Chuyển đổi một số trường sang loại trường "Text", "Small Text", "Text Editor" hoặc "Code". Trong MySQL, các cột BLOB và TEXT chỉ tính từ một đến bốn cộng thêm tám byte cho mỗi cột vào giới hạn kích thước hàng vì nội dung của chúng được lưu trữ riêng biệt với phần còn lại của hàng. Vì vậy, việc chuyển đổi sang các loại trường đó sẽ giải phóng một phần không gian và cho phép thêm một số trường khác.
2. Đặt giá trị nhỏ hơn trong thuộc tính "Length" khi tạo các trường, giá trị mặc định là 140. Hệ thống sẽ thiết lập độ dài của `VARCHAR` dựa trên thuộc tính này và phân bổ kích thước cho các cột đó. Do đó, "Length" nhỏ hơn sẽ giúp thêm được nhiều trường hơn.

{next}