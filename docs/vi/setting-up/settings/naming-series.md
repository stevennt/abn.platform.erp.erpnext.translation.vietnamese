<!-- add-breadcrumbs -->
# Chuỗi đặt tên (Naming Series)

**Các danh mục chính và giao dịch có thể được đặt tiền tố dưới dạng chuỗi đặt tên.**

ERPNext cho phép bạn tạo các tiền tố cho tài liệu của mình, với mỗi tiền tố sẽ tạo thành một chuỗi riêng biệt. Ví dụ, một chuỗi với tiền tố INV12#### sẽ có các số INV120001, INV120002, v.v.

Bạn có thể có nhiều chuỗi cho tất cả các giao dịch của mình. Ví dụ, các ID Hóa đơn bán hàng như sau có thể được tạo ra:

* ACC-SINV-.YYYY.-
* SINV12####
* SALESINV-00####

Bạn có thể định nghĩa hoặc chọn mẫu Chuỗi đặt tên từ:

> Home > Settings > Naming Series

## 1. Thiết lập Chuỗi đặt tên cho Tài liệu

1. Chọn giao dịch mà bạn muốn tạo chuỗi. Hệ thống sẽ cập nhật chuỗi hiện tại trong hộp văn bản.
2. Chỉnh sửa chuỗi theo yêu cầu với các tiền tố duy nhất cho mỗi chuỗi.
  Tiền tố đầu tiên sẽ là tiền tố mặc định. Mỗi Chuỗi đặt tên mới phải được thêm vào một dòng mới. Chuỗi đặt tên mới được thêm sẽ có sẵn trong tài liệu.
  ![Multiple naming series](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/settings/multiple-naming-series.gif)

3. Nếu bạn muốn người dùng phải chọn rõ ràng một chuỗi thay vì dùng mặc định, hãy tích vào ô “User must always select”.
  Sẽ không có chuỗi đặt tên mặc định nếu ô này được tích.

1. Bạn cũng có thể cập nhật điểm bắt đầu của một chuỗi bằng cách nhập tên chuỗi và điểm bắt đầu trong phần “Update Series”.

1. Nhấp vào nút Update để cập nhật bộ Chuỗi đặt tên cho tài liệu đã chọn.

> Lưu ý: Để thấy Chuỗi đặt tên mới được thêm, hãy nhấp vào Settings > Reload.

## 2. Năm tài chính trong Chuỗi đặt tên
Bạn cũng có thể hiển thị năm tài chính trong Chuỗi đặt tên. Theo mặc định, nếu bạn nhập 'YYYY' vào chuỗi đặt tên, nó sẽ lấy năm hiện tại. Để thiết lập chuỗi đặt tên dựa trên năm tài chính, hãy nhập thứ gì đó như 'ACC-SINV-.19-20.-' trong đó 19-20 là Năm tài chính hiện tại. Việc có một chuỗi riêng biệt cho mỗi năm tài chính là điều phổ biến.

Như bạn có thể thấy, trong ảnh chụp màn hình sau của một Hóa đơn bán hàng, năm 2019 được liệt kê:

![Fiscal year in Naming Series](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/settings/year-naming-series.png)


## 3. Cập nhật giá trị hiện tại cho Chuỗi đặt tên hiện có

Bạn có thể thay đổi số thứ tự bắt đầu/hiện tại của một chuỗi hiện có.

1. Trong phần Update Series, chọn tiền tố có số thứ tự cần thay đổi.
1. Giá trị hiện tại sẽ được truy xuất và hiển thị.
1. Thay đổi số thứ tự bắt đầu/hiện tại nếu cần.
1. Nhấp vào Update Series Number.

Ví dụ, nếu số chuỗi Đơn bán hàng hiện tại đang ở mức 16, và bạn muốn bắt đầu lại hoặc đặt nó thành 50, hãy nhập 0 hoặc 50 tùy thuộc vào trường hợp của bạn. Bất kỳ Đơn bán hàng mới nào được tạo sẽ bắt đầu từ số thứ tự mới.

Để biết thêm về điều này, [truy cập bài viết này](../articles/naming-series-current-value.md).

> Mẹo: Bạn có thể có một chuỗi riêng biệt cho mỗi loại Khách hàng hoặc cho mỗi cửa hàng bán lẻ của mình.

## 4. Sử dụng Giá trị trường trong Chuỗi đặt tên

Một số công ty thích sử dụng "mã ngắn" cho nhà cung cấp, ví dụ: WN cho công ty "Web Notes" mà sau đó có thể được sử dụng trong chuỗi đặt tên để nhận diện nhanh chóng.

Ví dụ:

    Một trường tùy chỉnh "Vendor ID" được tạo trong DocType: Supplier.
    Sau đó trong Naming Series, chúng ta cho phép thứ gì đó như:
        PO-.YY.MM.-.vendor_id.-.####
        Kết quả là "PO-1503-WN-00001"

## 5. Video
<div>
  <div class='embed-container'>
    <iframe src='https://www.youtube.com/embed//IGyISSfI1qU' frameborder='0' allowfullscreen>
    </iframe>
  </div>
</div>

### 6. Các chủ đề liên quan
1. [Bulk Rename](bulk-rename.md)