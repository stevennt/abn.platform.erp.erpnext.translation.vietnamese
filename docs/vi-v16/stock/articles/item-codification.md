<!-- add-breadcrumbs -->
# Mã hóa Mặt hàng

Nếu bạn đã có một doanh nghiệp hoàn chỉnh với một số lượng mặt hàng vật lý nhất định, có lẽ bạn đã mã hóa các mặt hàng của mình. Nếu chưa, bạn có quyền lựa chọn. Chúng tôi khuyên bạn nên thực hiện mã hóa nếu bạn có nhiều sản phẩm với tên dài hoặc phức tạp. Trong trường hợp bạn có ít sản phẩm với tên ngắn, tốt hơn là nên giữ Mã Mặt hàng giống với Tên Mặt hàng.

Mã hóa mặt hàng là một chủ đề nhạy cảm và đã có những cuộc tranh luận nảy lửa về vấn đề này (không nói đùa đâu). Theo kinh nghiệm của chúng tôi, khi bạn có số lượng mặt hàng vượt quá một quy mô nhất định, cuộc sống mà không có mã hóa sẽ là một cơn ác mộng.

### 1. Lợi ích

  * Cách đặt tên mọi thứ một cách tiêu chuẩn.
  * Ít có khả năng bị trùng lặp.
  * Định nghĩa rõ ràng.
  * Giúp nhanh chóng tìm thấy nếu có một mặt hàng tương tự tồn tại.
  * Tên mặt hàng sẽ ngày càng dài hơn khi có thêm nhiều loại mới được đưa vào. Mã thì ngắn hơn.

### 2. Thách thức

  * Bạn phải ghi nhớ các mã!
  * Thành viên mới trong nhóm sẽ khó tiếp thu hơn.
  * Bạn phải tạo mã mới liên tục.

### 3. Ví dụ

Bạn nên có một bản hướng dẫn đơn giản / bảng tra cứu để mã hóa các Mặt hàng của mình thay vì chỉ đánh số chúng theo thứ tự. Mỗi chữ cái nên mang một ý nghĩa nào đó. Dưới đây là một ví dụ:

Nếu doanh nghiệp của bạn liên quan đến đồ nội thất gỗ, bạn có thể mã hóa như sau:

**Bảng tóm tắt mã hóa mặt hàng (MẪU)**

| Chữ cái đầu tiên: "Chất liệu" | Chữ cái thứ ba: "Kích thước" |
| :--- | :--- |
| - W - Gỗ (Wood) | - 0 - dưới 1mm |
| - H - Phụ kiện (Hardware) | - 1 - 1mm - 5mm |
| - G - Thủy tinh (Glass) | - 2 - 5mm - 10mm |
| - U - Đệm bọc (Upholstery) | - 3 - 10mm - 10cm |
| - P - Nhựa (Plastic) | |

**Chữ cái thứ hai: "Loại"**

| Đối với Gỗ: | Đối với Phụ kiện: |
| :--- | :--- |
| - S - Tấm (Sheet) | - S - Vít (Screw) |
| - B - Thanh (Bar) | - N - Đai ốc (Nut) |
| - L - Thép góc (L-section) | - W - Long đền (Washer) |
| - M - Đúc (Molded) | - B - Giá đỡ (Bracket) |
| - R - Tròn (Round) | |

Vài chữ cái cuối cùng có thể là số thứ tự. Vì vậy, khi nhìn vào mã **WM304** - bạn biết đó là một loại khuôn gỗ có kích thước nhỏ hơn 10cm.

### 4. Tiêu chuẩn hóa

Nếu có nhiều hơn một người đặt tên cho các mặt hàng, phong cách đặt tên sẽ thay đổi tùy theo mỗi người. Đôi khi, ngay cả với một người, họ cũng có thể quên cách mình đã đặt tên cho mặt hàng và có thể tạo ra một tên trùng lặp *"Wooden Sheet 3mm" hay "3mm Sheet of Wood"?*

### 5. Hợp lý hóa

Một thói quen tốt là nên có số lượng biến thể mặt hàng tối thiểu để bạn có thể duy trì mức tồn kho tối thiểu, việc quản lý kho bãi đơn giản hơn, v.v. Khi bạn đang lập kế hoạch cho một sản phẩm mới và muốn biết liệu mình đã đang mua một linh kiện nào đó cho một sản phẩm khác hay chưa, các mã mặt hàng sẽ giúp bạn nhanh chóng xác định xem bạn có đang sử dụng một loại nguyên vật liệu tương tự trong một sản phẩm khác hay không.

Chúng tôi tin rằng nếu bạn thực hiện khoản đầu tư nhỏ này, nó sẽ giúp bạn hợp lý hóa mọi thứ khi doanh nghiệp phát triển, mặc dù việc không mã hóa cũng không sao nếu bạn có ít mặt hàng.

### 6. Các tính năng mới trong v16 (Nâng cao)

Trong phiên bản v16, việc quản lý mặt hàng và tồn kho đã được nâng cấp mạnh mẽ để hỗ trợ các doanh nghiệp phức tạp:

* **Hệ thống Giữ hàng Tồn kho (Stock Reservation System):** Cho phép giữ trước mặt hàng cho các Đơn bán hàng (SO) hoặc các yêu cầu khác, giúp đảm bảo tính sẵn có của hàng hóa.
* **Báo cáo Truy xuất nguồn gốc Lô hàng/Số sê-ri (Serial/Batch Traceability Report):** Theo dõi chi tiết lịch sử của từng Lô hàng (Batch) hoặc Số sê-ri từ khi nhập kho đến khi xuất kho.
* **Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry):** Tự động phân bổ các chi phí mua hàng (vận chuyển, thuế, phí...) vào giá trị tồn kho của mặt hàng khi thực hiện Phiếu nhập hàng hoặc Phiếu kho.
* **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Cung cấp sự chính xác tuyệt đối trong việc hạch toán giá trị tồn kho cho từng mặt hàng cụ thể.
* **Xem trước Sổ cái (Ledger Preview):** Cho phép kiểm tra nhanh các bút toán (JE) liên quan trực tiếp đến mặt hàng và giao dịch kho ngay tại màn hình quản lý.

#### 7. Các chủ đề liên quan
1. [Nhóm mặt hàng](../item-group.md)
1. [Thuộc tính mặt hàng](../item-attribute.md)
1. [Giá mặt hàng](../item-price.md)
1. [Biến thể mặt hàng](../item-variants.md)