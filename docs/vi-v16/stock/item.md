<!-- add-breadcrumbs -->
# Mặt hàng

**Mặt hàng là một sản phẩm hoặc dịch vụ được cung cấp bởi công ty của bạn.**

Thuật ngữ Mặt hàng cũng có thể áp dụng cho nguyên vật liệu hoặc các thành phần của sản phẩm chưa được sản xuất (trước khi chúng có thể được bán cho khách hàng). ERPNext cho phép bạn quản lý tất cả các loại mặt hàng như nguyên vật liệu, bán thành phẩm, thành phẩm, biến thể mặt hàng và mặt hàng dịch vụ.

ERPNext được tối ưu hóa để quản lý chi tiết từng mặt hàng trong hoạt động bán hàng và mua hàng của bạn. Nếu bạn kinh doanh dịch vụ, bạn có thể tạo một Mặt hàng cho mỗi dịch vụ mà bạn cung cấp. Việc hoàn thiện Danh mục Mặt hàng là rất thiết yếu để triển khai ERPNext thành công.

Để truy cập danh sách Mặt hàng, hãy đi đến:
> Home > Stock > Items and Pricing > Item

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng một Mặt hàng, bạn nên tạo các mục sau trước:

* [Nhóm mặt hàng](item-group.md)
* [Kho](warehouse.md)
* Đơn vị tính nếu cần thiết

## 2. Cách tạo một Mặt hàng
1. Đi tới danh sách Mặt hàng, nhấn vào mới.
2. Nhập Mã mặt hàng, tên sẽ được tự động điền giống với Mã mặt hàng khi nhấp vào trường Tên mặt hàng.
3. Chọn một Nhóm mặt hàng.
4. Nhập số lượng tồn kho đầu kỳ và đơn giá bán tiêu chuẩn.
5. **Lưu**.
  ![Item Saved](https://docs.erpnext.com/docs/v16/assets/img/stock/item-saved.png)

### 2.1 Thuộc tính Mặt hàng

* **Tên mặt hàng:** Tên mặt hàng là tên thực tế của sản phẩm hoặc dịch vụ của bạn.

* **Mã mặt hàng:** Mã mặt hàng là dạng viết tắt để biểu thị Mặt hàng của bạn. Nếu bạn có rất ít Mặt hàng, bạn nên để Tên mặt hàng và Mã mặt hàng giống nhau. Điều này giúp người dùng mới nhận diện và cập nhật chi tiết Mặt hàng trong tất cả các giao dịch. Trong trường hợp bạn có nhiều Mặt hàng với tên dài và danh sách lên đến hàng trăm, bạn nên sử dụng mã. Để hiểu về cách đặt Mã mặt hàng, hãy xem [Mã hóa mặt hàng](articles/item-codification.md). Bạn cũng có thể tạo Mã mặt hàng dựa trên [Chuỗi đặt tên](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/settings/naming-series) bằng cách bật tính năng này trong [Cài đặt kho](stock-settings.md#1-item-naming-by).

* **Nhóm mặt hàng:** Nhóm mặt hàng được sử dụng để phân loại một Mặt hàng theo các tiêu chí khác nhau như sản phẩm, nguyên vật liệu, dịch vụ, bán thành phẩm, vật tư tiêu hao hoặc tất cả các Nhóm mặt hàng. Hãy tạo danh sách Nhóm mặt hàng mặc định của bạn trong Thiết lập > Nhóm mặt hàng và chọn trước tùy chọn này khi điền chi tiết Mặt hàng mới trong [Nhóm mặt hàng](item-group.md). Các nhóm mặt hàng có thể là bán thành phẩm, nguyên vật liệu, v.v., hoặc dựa trên trường hợp sử dụng kinh doanh của bạn.

* **Đơn vị tính mặc định:** Đây là đơn vị đo lường mặc định mà bạn sẽ sử dụng cho sản phẩm của mình. Nó có thể là Cái, Kg, Mét, v.v. Bạn có thể lưu trữ tất cả các Đơn vị tính mà sản phẩm của bạn yêu cầu trong Thiết lập > Dữ liệu chính > Đơn vị tính. Những đơn vị này có thể được chọn trước khi điền Mặt hàng mới bằng cách sử dụng ký hiệu % để hiển thị danh sách Đơn vị tính. Truy cập trang [Đơn vị tính](uom.md) để biết thêm chi tiết.

### 2.2 Các tùy chọn khi tạo một mặt hàng

* **Vô hiệu hóa**: Nếu bạn vô hiệu hóa một Mặt hàng, nó sẽ không thể được chọn trong bất kỳ giao dịch nào.

* **Cho phép mặt hàng thay thế**: Đôi khi khi sản xuất thành phẩm, một số nguyên vật liệu cụ thể có thể không có sẵn. Nếu bạn tích vào ô này, bạn có thể tạo và chọn một mặt hàng thay thế từ danh sách Mặt hàng thay thế. Để biết thêm, hãy truy cập trang [Mặt hàng thay thế](https://docs.erpnext.com/docs/v16/user/manual/en/manufacturing/item-alternative).

* **Duy trì tồn kho:** Nếu bạn duy trì tồn kho của Mặt hàng này trong Kho của mình, ERPNext sẽ tạo một bút toán sổ kho cho mỗi giao dịch của mặt hàng này. Hãy đảm bảo bỏ chọn tùy chọn này khi tạo Mặt hàng không lưu kho (sản xuất theo đơn hàng/thiết kế riêng) hoặc một dịch vụ.

* **Bao gồm mặt hàng trong sản xuất**: Tùy chọn này dành cho các Mặt hàng nguyên vật liệu sẽ được sử dụng để tạo thành thành phẩm. Nếu Mặt hàng là một dịch vụ bổ sung như 'giặt ủi' được sử dụng trong BOM, hãy để trống tùy chọn này.

* **Giá trị tính giá**: Có hai tùy chọn để duy trì giá trị tồn kho. FIFO (nhập trước - xuất trước) và Giá bình quân gia quyền. Để hiểu chi tiết về chủ đề này, vui lòng truy cập [Giá trị mặt hàng, FIFO và Giá bình quân gia quyền](articles/item-valuation-fifo-and-moving-average.md).

* **Đơn giá bán tiêu chuẩn**: Khi *tạo* một Mặt hàng, việc nhập giá trị cho trường này sẽ tự động tạo một [Giá mặt hàng](item-price.md) ở hệ thống phía sau. Việc nhập giá trị sau khi Mặt hàng đã được **Lưu** sẽ không có tác dụng. Trong trường hợp đó, Giá mặt hàng được tạo từ bất kỳ giao dịch nào với Mặt hàng đó. Đây là mức giá mà bạn sẽ bán mặt hàng. Giá này sẽ được lấy vào Đơn bán hàng và Hóa đơn bán hàng.

* **Là tài sản cố định**: Tích vào ô này nếu mặt hàng này là Tài sản của công ty. Xem [Phân hệ Tài sản](https://docs.erpnext.com/docs/v16/user/manual/en/asset) để biết thêm.

* **Tự động tạo tài sản khi mua hàng**: Nếu Mặt hàng là Tài sản của Công ty, hãy tích vào ô này nếu bạn muốn tự động tạo tài sản khi mua mặt hàng này thông qua [Chu trình mua hàng](../buying/purchase-order.md). Xem [Trang Tài sản](https://docs.erpnext.com/docs/v16/user/manual/en/asset/asset) để biết thêm.

* **Phần trăm dung sai**: Tùy chọn này sẽ chỉ khả dụng khi bạn tạo và **Lưu** mặt hàng. Đây là tỷ lệ phần trăm mà bạn được phép lập hóa đơn vượt mức hoặc giao hàng vượt mức cho Mặt hàng này. Nếu không được thiết lập, nó sẽ lấy từ [Cài đặt kho](stock-settings.md#3-limit-percent).

* **Tải lên hình ảnh**: Để tải lên một hình ảnh làm biểu tượng sẽ xuất hiện trong tất cả các giao dịch, hãy **Lưu** biểu mẫu đã điền một phần. Chỉ sau khi tệp của bạn được **Lưu**, nút 'Thay đổi' mới xuất hiện trên biểu tượng Hình ảnh. Nhấp vào Thay đổi, sau đó nhấp vào Tải lên, và tải hình ảnh lên.

### 2.3 Các tính năng nâng cao trong v16

* **Hệ thống Giữ hàng (Stock Reservation System):** Trong phiên bản v16, bạn có thể thiết lập để giữ hàng cho các Đơn bán hàng (SO) hoặc các yêu cầu khác, giúp đảm bảo lượng tồn kho luôn sẵn sàng cho các đơn hàng ưu tiên.

* **Báo cáo Truy xuất nguồn gốc theo Số sê-ri/Lô hàng (Serial/Batch Traceability Report):** Tăng cường khả năng kiểm soát chất lượng (QI) bằng cách cho phép theo dõi chi tiết lịch sử của một mặt hàng dựa trên Lô hàng (Batch) hoặc Số sê-ri từ khi nhập kho (PR) cho đến khi xuất kho hoặc bán hàng.

* **Tính giá vốn hàng bán cho Phiếu kho (Landed Cost cho Stock Entry):** Cho phép phân bổ các chi phí mua hàng bổ sung (như vận chuyển, thuế nhập khẩu) trực tiếp vào giá trị của Mặt hàng khi thực hiện các giao dịch nhập kho, giúp phản ánh chính xác giá trị tồn kho.

* **Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting):** Cung cấp khả năng quản lý chi tiết hơn các bút toán (JE) liên quan đến giá trị tồn kho cho từng mặt hàng cụ thể, giúp việc đối soát sổ cái trở nên chính xác tuyệt đối.

* **Xem trước Sổ cái (Ledger Preview):** Cho phép người dùng xem nhanh các bút toán (JE) liên quan trực tiếp từ giao dịch mặt hàng mà không cần phải chuyển sang phân hệ Kế toán, giúp tăng tốc độ kiểm tra dữ liệu.