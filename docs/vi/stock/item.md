<!-- add-breadcrumbs -->
# Mặt hàng

**Mặt hàng là một sản phẩm hoặc dịch vụ được cung cấp bởi công ty của bạn.**

Thuật ngữ Mặt hàng cũng có thể áp dụng cho nguyên vật liệu hoặc các thành phần của sản phẩm chưa được sản xuất (trước khi chúng có thể được bán cho khách hàng). ERPNext cho phép bạn quản lý tất cả các loại mặt hàng như nguyên vật liệu, bán thành phẩm, thành phẩm, biến thể mặt hàng và mặt hàng dịch vụ.

ERPNext được tối ưu hóa để quản lý chi tiết từng mặt hàng trong hoạt động bán hàng và mua hàng của bạn. Nếu bạn kinh doanh dịch vụ, bạn có thể tạo một Mặt hàng cho mỗi dịch vụ mà bạn cung cấp. Việc hoàn thiện Danh mục Mặt hàng là rất thiết yếu để triển khai ERPNext thành công.

Để truy cập danh sách Mặt hàng, hãy đi đến:
> Home > Stock > Items and Pricing > Item
## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng một Mặt hàng, bạn nên tạo các mục sau trước:

* [Nhóm mặt hàng](/docs/v13/user/manual/en/stock/item-group)
* [Kho](/docs/v13/user/manual/en/stock/warehouse)
* Đơn vị tính nếu cần thiết
## 2. Cách tạo một Mặt hàng
1. Đi tới danh sách Mặt hàng, nhấn vào mới.
2. Nhập Mã mặt hàng, tên sẽ được tự động điền giống với Mã mặt hàng khi nhấp vào trường Tên mặt hàng.
1. Chọn một Nhóm mặt hàng.
1. Nhập số lượng tồn kho đầu kỳ và đơn giá bán tiêu chuẩn.
3. Lưu.
  ![Item Saved](/docs/v13/assets/img/stock/item-saved.png)

### 2.1 Thuộc tính Mặt hàng

  * **Tên mặt hàng:** Tên mặt hàng là tên thực tế của sản phẩm hoặc dịch vụ của bạn.

  * **Mã mặt hàng:** Mã mặt hàng là dạng viết tắt để biểu thị Mặt hàng của bạn. Nếu bạn có rất ít Mặt hàng, bạn nên để Tên mặt hàng và Mã mặt hàng giống nhau. Điều này giúp người dùng mới nhận diện và cập nhật chi tiết Mặt hàng trong tất cả các giao dịch. Trong trường hợp bạn có nhiều Mặt hàng với tên dài và danh sách lên đến hàng trăm, bạn nên sử dụng mã. Để hiểu về cách đặt Mã mặt hàng, hãy xem [Mã hóa mặt hàng](/docs/v13/user/manual/en/stock/articles/item-codification). Bạn cũng có thể tạo Mã mặt hàng dựa trên [Chuỗi đặt tên](/docs/v13/user/manual/en/setting-up/settings/naming-series) bằng cách bật tính năng này trong [Cài đặt kho](/docs/v13/user/manual/en/stock/stock-settings#1-item-naming-by).

  * **Nhóm mặt hàng:** Nhóm mặt hàng được sử dụng để phân loại một Mặt hàng theo các tiêu chí khác nhau như sản phẩm, nguyên vật liệu, dịch vụ, bán thành phẩm, vật tư tiêu hao hoặc tất cả các Nhóm mặt hàng. Hãy tạo danh sách Nhóm mặt hàng mặc định của bạn trong Thiết lập > Nhóm mặt hàng và chọn trước tùy chọn này khi điền chi tiết Mặt hàng mới trong [Nhóm mặt hàng](/docs/v13/user/manual/en/stock/item-group). Các nhóm mặt hàng có thể là bán thành phẩm, nguyên vật liệu, v.v., hoặc dựa trên trường hợp sử dụng kinh doanh của bạn.

  * **Đơn vị tính mặc định:** Đây là đơn vị đo lường mặc định mà bạn sẽ sử dụng cho sản phẩm của mình. Nó có thể là Cái, Kg, Mét, v.v. Bạn có thể lưu trữ tất cả các Đơn vị tính mà sản phẩm của bạn yêu cầu trong Thiết lập > Dữ liệu chính > Đơn vị tính. Những đơn vị này có thể được chọn trước khi điền Mặt hàng mới bằng cách sử dụng ký hiệu % để hiển thị danh sách Đơn vị tính. Truy cập trang [Đơn vị tính](/docs/v13/user/manual/en/stock/uom) để biết thêm chi tiết.

### 2.2 Các tùy chọn khi tạo một mặt hàng
* **Vô hiệu hóa**: Nếu bạn vô hiệu hóa một Mặt hàng, nó sẽ không thể được chọn trong bất kỳ giao dịch nào.

* **Cho phép mặt hàng thay thế**: Đôi khi khi sản xuất thành phẩm, một số nguyên vật liệu cụ thể có thể không có sẵn. Nếu bạn tích vào ô này, bạn có thể tạo và chọn một mặt hàng thay thế từ danh sách Mặt hàng thay thế. Để biết thêm, hãy truy cập trang [Mặt hàng thay thế](/docs/v13/user/manual/en/manufacturing/item-alternative).

* **Duy trì tồn kho:** Nếu bạn duy trì tồn kho của Mặt hàng này trong Kho của mình, ERPNext sẽ tạo một bút toán sổ kho cho mỗi giao dịch của mặt hàng này. Hãy đảm bảo bỏ chọn tùy chọn này khi tạo Mặt hàng không lưu kho (sản xuất theo đơn hàng/thiết kế riêng) hoặc một dịch vụ.

* **Bao gồm mặt hàng trong sản xuất**: Tùy chọn này dành cho các Mặt hàng nguyên vật liệu sẽ được sử dụng để tạo thành thành phẩm. Nếu Mặt hàng là một dịch vụ bổ sung như 'giặt ủi' được sử dụng trong BOM, hãy để trống tùy chọn này.

* **Giá trị tính giá**: Có hai tùy chọn để duy trì giá trị tồn kho. FIFO (nhập trước - xuất trước) và Giá bình quân gia quyền. Để hiểu chi tiết về chủ đề này, vui lòng truy cập [Giá trị mặt hàng, FIFO và Giá bình quân gia quyền](/docs/v13/user/manual/en/stock/articles/item-valuation-fifo-and-moving-average).

* **Đơn giá bán tiêu chuẩn**: Khi *tạo* một Mặt hàng, việc nhập giá trị cho trường này sẽ tự động tạo một [Giá mặt hàng](/docs/v13/user/manual/en/stock/item-price) ở hệ thống phía sau. Việc nhập giá trị sau khi Mặt hàng đã được Lưu sẽ không có tác dụng. Trong trường hợp đó, Giá mặt hàng được tạo từ bất kỳ giao dịch nào với Mặt hàng đó. Đây là mức giá mà bạn sẽ bán mặt hàng. Giá này sẽ được lấy vào Đơn bán hàng và Hóa đơn bán hàng.

* **Là tài sản cố định**: Tích vào ô này nếu mặt hàng này là Tài sản của công ty. Xem [Phân hệ Tài sản](/docs/v13/user/manual/en/asset) để biết thêm.

* **Tự động tạo tài sản khi mua hàng**: Nếu Mặt hàng là Tài sản của Công ty, hãy tích vào ô này nếu bạn muốn tự động tạo tài sản khi mua mặt hàng này thông qua [Chu trình mua hàng](/docs/v13/user/manual/en/buying/purchase-order). Xem [Trang Tài sản](/docs/v13/user/manual/en/asset/asset) để biết thêm.

* **Phần trăm dung sai**: Tùy chọn này sẽ chỉ khả dụng khi bạn tạo và Lưu mặt hàng. Đây là tỷ lệ phần trăm mà bạn được phép lập hóa đơn vượt mức hoặc giao hàng vượt mức cho Mặt hàng này. Nếu không được thiết lập, nó sẽ lấy từ [Cài đặt kho](/docs/v13/user/manual/en/stock/stock-settings#3-limit-percent).

* **Tải lên hình ảnh**: Để tải lên một hình ảnh làm biểu tượng sẽ xuất hiện trong tất cả các giao dịch, hãy Lưu biểu mẫu đã điền một phần. Chỉ sau khi tệp của bạn được Lưu, nút 'Thay đổi' mới xuất hiện trên biểu tượng Hình ảnh. Nhấp vào Thay đổi, sau đó nhấp vào Tải lên, và tải hình ảnh lên.

Dành cho Ấn Độ:

* **HSN/SAC**: Hệ thống hài hòa về mô tả và mã hóa hàng hóa (HSN) và Mã kế toán dịch vụ (SAC) cho GST. Các mã số này được chính phủ quy định và các Mặt hàng khác nhau sẽ thuộc các mã khác nhau. Các mã HSN mới có thể được thêm vào nếu không có trong danh sách.
* **Là mặt hàng thuế suất 0% hoặc được miễn thuế**: Dành cho Mặt hàng thuộc diện chịu thuế GST, nhưng không áp dụng thuế. Ví dụ: Ngũ cốc.
* **Không thuộc diện GST**: Dành cho mặt hàng không thuộc phạm vi điều chỉnh của GST. Ví dụ: xăng dầu.
## 3. Tính năng

### 3.1 Thương hiệu và Mô tả

* **Thương hiệu**: Nếu bạn có nhiều thương hiệu, hãy lưu chúng trong mục Bán hàng > Thương hiệu và chọn trước chúng khi tạo Mặt hàng mới.
* **Mô tả**: Mô tả của mặt hàng. Văn bản từ Mã mặt hàng sẽ được tự động lấy theo mặc định.
  ![Item brand and description](/docs/v13/assets/img/stock/item-brand-description.png)

### 3.2 Mã vạch

Mã vạch có thể được ghi lại trong Mặt hàng để quét nhanh và thêm chúng vào các giao dịch. Trong bảng Mã vạch, bạn có thể thêm [mã vạch để quét](/docs/v13/user/manual/en/stock/articles/track-items-using-barcode) của một Mặt hàng. Có hai loại mã vạch trong ERPNext:

* **EAN**: Mã số hàng hóa Châu Âu là số có 13 chữ số. EAN được sử dụng quốc tế và được nhiều hệ thống POS công nhận hơn.
* **UPC**: Mã sản phẩm phổ biến là số có 12 chữ số. UPC thường chỉ được sử dụng tại Hoa Kỳ và Canada.

### 3.3 Tồn kho

* **Hạn sử dụng (ngày)**: Dành cho sản phẩm theo [Lô hàng](/docs/v13/user/manual/en/stock/batch). Số ngày mà sau đó lô sản phẩm sẽ không còn sử dụng được nữa. Ví dụ: thuốc.
* **Kết thúc vòng đời**: Đối với một mặt hàng/sản phẩm đơn lẻ, đây là ngày mà sau đó nó sẽ hoàn toàn không thể sử dụng được. Nghĩa là, mặt hàng sẽ không thể sử dụng trong các giao dịch và sản xuất. Ví dụ: bạn đang sử dụng các hạt nhựa để sản xuất Mặt hàng trong 5 năm tới, sau đó bạn muốn chuyển sang dùng hạt nhựa khác.
* **Bảo hành**: Để theo dõi thời hạn bảo hành, Mặt hàng đó bắt buộc phải được quản lý theo số serial. Khi Mặt hàng này được giao, ngày giao hàng và thời hạn hết hạn sẽ được lưu trong danh mục Số serial. Thông qua danh mục số serial, bạn có thể theo dõi tình trạng bảo hành.

  Thời hạn bảo hành là khoảng thời gian mà một sản phẩm đã mua có thể được trả lại hoặc đổi mới.

  <img class="screenshot" alt="Item Warranty" src="{{docs_base_url}}/v13/assets/img/stock/item-inventory.png">

* **Đơn vị tính trọng lượng**: Đơn vị tính của mặt hàng. Có thể là Cái, Kilo, v.v. Đơn vị tính trọng lượng bạn sử dụng nội bộ có thể khác với đơn vị tính mua hàng.
* **Trọng lượng trên mỗi đơn vị**: Trọng lượng thực tế trên mỗi đơn vị của mặt hàng. Ví dụ: 1 kilo bánh quy hoặc 10 bánh quy mỗi gói.
* **Loại Yêu cầu vật tư mặc định**: Khi bạn tạo một Yêu cầu vật tư mới cho mặt hàng này, trường được thiết lập ở đây sẽ được chọn mặc định trong Yêu cầu vật tư mới. Điều này còn được gọi là 'indent'.
* **Phương pháp tính giá**: Chọn Phương pháp tính giá là FIFO hoặc Bình quân gia quyền. Đọc [Phương pháp tính giá Mặt hàng](/docs/v13/user/manual/en/stock/articles/item-valuation-fifo-and-moving-average) để biết thêm chi tiết.

### 3.4 Tự động đặt hàng lại
Khi tồn kho của một mặt hàng giảm xuống dưới một số lượng nhất định, bạn có thể thiết lập đặt hàng lại tự động trong phần 'Tự động đặt hàng lại'. Tính năng này phải được bật trong [Cài đặt kho](/docs/v13/user/manual/en/stock/stock-settings#9-automatic-material-request). Việc này sẽ tạo một [Yêu cầu vật tư](/docs/v13/user/manual/en/stock/material-request) cho Mặt hàng. Người dùng có vai trò Quản lý mua hàng và Quản lý kho sẽ được **thông báo** khi Yêu cầu vật tư được tạo.

* **Kiểm tra trong (nhóm)**: Các nhóm kho nào sẽ được kiểm tra số lượng của mặt hàng.
* **Yêu cầu cho**: Kho nào sẽ được nhập hàng khi đặt hàng lại mặt hàng.
* **Mức đặt hàng lại**: Khi đạt đến số lượng này, việc đặt hàng lại sẽ được kích hoạt. Mức đặt hàng lại có thể được xác định dựa trên thời gian chờ và mức tiêu thụ trung bình hàng ngày. Ví dụ, bạn có thể đặt mức đặt hàng lại của Bo mạch chủ là 10. Khi chỉ còn lại 10 Bo mạch chủ trong kho, hệ thống sẽ tự động tạo một Yêu cầu vật tư trong tài khoản ERPNext của bạn.
* **Số lượng đặt hàng lại**: Số lượng đơn vị cần được đặt hàng lại sao cho tổng chi phí đặt hàng và chi phí lưu kho là thấp nhất. Số lượng đặt hàng lại dựa trên 'Số lượng đặt hàng tối thiểu' do nhà cung cấp quy định và nhiều yếu tố khác.

  Ví dụ, Nếu mức đặt hàng lại là 100 mặt hàng, số lượng đặt hàng lại của bạn không nhất thiết phải là 100 mặt hàng. Số lượng đặt hàng lại có thể lớn hơn hoặc bằng mức đặt hàng lại. Nó có thể phụ thuộc vào thời gian chờ, chiết khấu, vận chuyển và mức tiêu thụ trung bình hàng ngày.

* **Loại Yêu cầu vật tư**: Loại [Yêu cầu vật tư](/docs/v13/user/manual/en/stock/material-request) mà kho sẽ được đặt hàng lại. Điều này phụ thuộc vào việc bạn mua Mặt hàng, tự sản xuất hay chuyển giữa các Kho.

  <img alt="Item Reorder" class="screenshot" src="{{docs_base_url}}/v13/assets/img/stock/item-reorder.png">

> **Lưu ý**: Yêu cầu vật tư được tạo vào lúc 12 giờ đêm tùy thuộc vào mức đặt hàng lại đã thiết lập.

### 3.5 Nhiều đơn vị tính
Bạn có thể thêm các Đơn vị tính thay thế cho một Mặt hàng. Nếu Đơn vị tính mặc định mà bạn bán là cái (Nos) nhưng bạn nhận hàng theo Kilo, bạn có thể thiết lập một Đơn vị tính bổ sung với hệ số chuyển đổi phù hợp. Ví dụ, 500 cái vít = 1 Kilogram, vì vậy hãy chọn Kilogram/Lít làm Đơn vị tính và đặt hệ số chuyển đổi là 500. Để biết thêm về việc bán hàng bằng các Đơn vị tính khác nhau, hãy truy cập [trang này](/docs/v13/user/manual/en/selling/articles/Selling-in-different-UOM).

### 3.6 Số serial

Với Số serial, bạn có thể theo dõi bảo hành và trả hàng. Trong trường hợp bất kỳ Mặt hàng riêng lẻ nào bị nhà cung cấp thu hồi, hệ thống đánh số sẽ giúp theo dõi từng Mặt hàng đó. Hệ thống đánh số cũng quản lý ngày hết hạn.

Lưu ý rằng nếu bạn bán hàng nghìn mặt hàng, và nếu các mặt hàng rất nhỏ như bút hoặc cục tẩy, bạn không cần phải quản lý theo số serial.

Trong ERPNext, bạn sẽ phải ghi Số serial trong một số bút toán kế toán. Nếu sản phẩm của bạn không phải là Mặt hàng tiêu dùng lâu bền lớn, nếu nó không có bảo hành và không có khả năng bị thu hồi, hãy tránh việc cấp số serial.

<img alt="Serial No modal" class="screenshot" src="{{docs_base_url}}/v13/assets/img/stock/serial_no_modal.gif">

### 3.7 Lô hàng

Một tập hợp các Mặt hàng có thể được sản xuất theo lô. Điều này hữu ích để luân chuyển lô hàng và gắn ngày hết hạn với một lô nhất định.

* **Có Số lô**: Các tùy chọn cho số lô, ngày hết hạn và lưu giữ mẫu hàng sẽ được hiển thị khi tích vào ô này. Bạn không thể kích hoạt tính năng này nếu đã có bất kỳ giao dịch nào tồn tại trước đó.
## 4. Video

<div>
  <div class='embed-container'>
    <iframe src='https://www.youtube.com/embed/FcOsV-e8ymE?end=192' frameborder='0' allowfullscreen>
    </iframe>
  </div>
</div>

### 5. Các chủ đề liên quan
1. [Giá Mặt hàng](/docs/v13/user/manual/en/stock/item-price)
1. [Mã hóa Mặt hàng](/docs/v13/user/manual/en/stock/articles/item-codification)
1. [Biến thể Mặt hàng](/docs/v13/user/manual/en/stock/item-variants)
1. [Nhóm mặt hàng](/docs/v13/user/manual/en/stock/item-group)
1. [Thuộc tính Mặt hàng](/docs/v13/user/manual/en/stock/item-attribute)
1. [Giá trị tồn kho Mặt hàng theo FIFO và Bình quân gia quyền di động](/docs/v13/user/manual/en/stock/articles//item-valuation-fifo-and-moving-average)
1. [Các giao dịch Giá trị tồn kho Mặt hàng](/docs/v13/user/manual/en/stock/articles/item-valuation-transactions)
1. [Duy trì trường Tồn kho bị khóa trong Danh mục Mặt hàng](/docs/v13/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master)
1. [Quản lý các Mặt hàng thành phẩm bị loại bỏ](/docs/v13/user/manual/en/stock/articles/managing-rejected-finished-goods-items)
1. [Trả lại Mặt hàng bị loại bỏ](/docs/v13/user/manual/en/stock/articles/return-rejected-item)
1. [Theo dõi Mặt hàng bằng Mã vạch](/docs/v13/user/manual/en/stock/articles/track-items-using-barcode)
1. [Tạo Khấu hao cho Mặt hàng](/docs/v13/user/manual/en/stock/articles/creating-depreciation-for-item)
1. [Đặt tên Số serial](/docs/v13/user/manual/en/stock/articles/serial-no-naming)
1. [Nhập số dư Tồn kho đầu kỳ cho Mặt hàng theo Số serial và Lô hàng](/docs/v13/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
1. [Số serial](/docs/v13/user/manual/en/stock/serial-no)
1. [Đặt tên Số serial](/docs/v13/user/manual/en/stock/articles/serial-no-naming)