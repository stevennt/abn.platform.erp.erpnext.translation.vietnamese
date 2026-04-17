<!-- add-breadcrumbs -->
#Thiết lập Giá trị hiện tại cho Naming Series

Tính năng Naming Series cho phép bạn xác định tiền tố để đặt tên cho các chứng từ. Ví dụ, nếu một Đơn bán hàng có tiền tố là "SO", thì chuỗi số sẽ được tạo ra là SO-00001, SO-00002... và tiếp tục như vậy. Nhấp vào [tại đây](/docs/v13/user/manual/en/setting-up/settings/naming-series.html) để tìm hiểu cách bạn có thể tùy chỉnh Chuỗi số cho một giao dịch/dữ liệu danh mục trong ERPNext.

### 1. Thiết lập Giá trị hiện tại

Tính năng Naming Series cũng cung cấp một công cụ nơi bạn có thể thiết lập Giá trị hiện tại cho một tiền tố cụ thể. Điều này thường cần thiết nếu bạn mới bắt đầu sử dụng ERPNext và có các giao dịch cũ từ hệ thống trước đó, và bạn muốn chuỗi số bắt đầu từ nơi nó đã kết thúc ở hệ thống cũ. Hãy xem xét một tình huống để hiểu rõ hơn về điều này.

Ví dụ, bạn có 322 Đơn bán hàng đã được tạo trong hệ thống cũ với ID Đơn bán hàng cao nhất là SO00322. Trong ERPNext, bạn cần Đơn bán hàng đầu tiên lấy số #323 khi được Lưu. Để thực hiện điều này, bạn nên thiết lập Giá trị hiện tại cho chuỗi SO theo các bước sau.

#### Đi tới Công cụ Naming Series

`Setup > System > Naming Series`

#### Phần Cập nhật Chuỗi (Update Series Section)

<img alt="Update Series Section" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/current-no-1.png">

#### Chọn Tiền tố

Xét tình huống của chúng ta, tiền tố cho Đơn bán hàng sẽ là "SO".

<img alt="Series Prefix" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/current-no-2.png">

#### Giá trị hiện tại

Nếu hiện tại bạn có 12 Đơn bán hàng đã được tạo trong tài khoản của mình, thì giá trị hiện tại được cập nhật sẽ là 12. Bạn có thể chỉnh sửa Giá trị hiện tại thành 322, sau đó nhấp vào Update Series Number.

<img alt="Series Current Value" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/current-no-3.png">

Với thiết lập này, các Đơn bán hàng Mới sẽ có số thứ tự bắt đầu từ #323.

### 2. Lỗi do Số Chuỗi

Nếu bạn nhận được lỗi Trùng tên (Duplicate Name) khi đang Lưu một giao dịch, ví dụ, khi đang Lưu Giá mặt hàng (Item Price), bạn nhận được thông báo lỗi:

`Duplicate name Item Price RFD/00016`

Thông báo lỗi này cho biết khi bạn đang Lưu Giá mặt hàng, hệ thống đang cố gắng cấp mã "RFD/00016" cho bản ghi Giá mặt hàng đó. Nhưng hệ thống nhận thấy rằng Giá mặt hàng với ID này đã tồn tại trong hệ thống của bạn.

Lỗi này có thể phát sinh do Giá trị hiện tại cho Chuỗi/Tiền tố của Giá mặt hàng bị xáo trộn và không đồng bộ với Giá trị hiện tại thực tế. Trong khi Giá trị hiện tại thực tế cho Giá mặt hàng có thể là 20 (hoặc bất kỳ số nào lớn hơn 16), thì ai đó đã thiết lập Giá trị hiện tại cho chuỗi này là 15.

Để xác nhận Giá trị hiện tại thực tế cho một Chuỗi cụ thể, bạn nên kiểm tra báo cáo của chứng từ liên quan (trong trường hợp này là Giá mặt hàng), và kiểm tra ID Giá mặt hàng có giá trị cao nhất.

Giả sử chúng ta thấy rằng Giá trị hiện tại thực tế cho Giá mặt hàng là 22, sau đó bạn vào Naming Series, thiết lập Giá trị hiện tại cho Tiền tố/Chuỗi của Giá mặt hàng thành 22, và nhấn Update Series Number.

Các hướng dẫn này áp dụng cho tất cả các chứng từ trong ERPNext mà người dùng có thể tùy chỉnh Chuỗi và Giá trị hiện tại của nó.

Hãy xem xét một tình huống khác để hiểu rõ hơn. Khi gán một chứng từ cho người dùng khác, thông báo lỗi hiển thị:

`Duplicate name ToDo TDI00014286`

Điều này cho thấy Giá trị hiện tại cho Chuỗi/Tiền tố của ToDo (TDI) đã bị xáo trộn. Bạn nên làm theo các bước sau để sửa giá trị cho Giá trị hiện tại của tiền tố TDI.

1. Kiểm tra báo cáo ToDo để tìm giá trị ID ToDo cao nhất.
1. Setup >> Settings >> Naming Series
1. Kiểm tra phần B của Update Series
1. Chọn Tiền tố cho ToDo là "TDI"
1. Đảm bảo rằng số cao nhất cho ToDo đã được cập nhật làm Giá trị hiện tại trong Naming Series. Nếu chưa, hãy sửa lại Giá trị hiện tại, và nhấp vào "Update Series Numbering".

<!-- markdown -->