# Trang chủ Website

Trong ERPNext, bạn hoàn toàn có thể thiết lập một trang tiêu chuẩn nhất định làm Trang chủ Website mặc định. Dưới đây là các bước để thiết lập trang chủ website mặc định.

#### **Bước 1: Tạo một Trang Web (Web Page)**
Để tạo một trang web, hãy đi tới: `Website > Web Site > Web Page` và sau đó nhấp vào nút `New` ở góc trên bên phải.

* Điền tiêu đề trang.
* Đặt đường dẫn (route) cho trang (viết chữ thường).
* Thêm nội dung vào phần `Main Content`. Nếu muốn, bạn có thể sử dụng markdown để tạo một trang phức tạp hơn.
* Tích (Check) vào ô `Published`.
* Nhấp vào nút `Lưu`.

#### **Bước 2: Mở Trang Cài đặt Website (Website Settings)**
Để mở trang cài đặt website, hãy đi tới: `Website > Setup > Website Settings`

#### **Bước 3: Thiết lập Trang chủ (Home page)**

Nhập cùng một giá trị mà bạn đã nhập cho trường `route` ở phần trước vào trường `Home Page`. ERPNext sẽ thiết lập đường dẫn này tương đương với `/index` cho trang của bạn.

![Website Setting Home](https://docs.erpnext.com/docs/v16/assets/img/articles/Selection_021.png)

#### **Bước 4: Lưu Biểu mẫu Cài đặt Website.**

Sau khi thiết lập Trang chủ, hãy nhấn nút `Lưu` từ trang cài đặt website và làm mới (refresh) hệ thống từ menu Help. Bằng cách này, bạn có thể thiết lập bất kỳ trang tiêu chuẩn nào làm trang chủ website mặc định của mình. Khi có ai đó truy cập vào website của bạn, họ sẽ thấy trang chủ là trang đích mặc định trên website của bạn.