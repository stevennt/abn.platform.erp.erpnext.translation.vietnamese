<!-- add-breadcrumbs -->
# Truyền dữ liệu sự kiện (Event Streaming)

Truyền dữ liệu sự kiện cho phép giao tiếp liên trang giữa hai hoặc nhiều trang web. Bạn có thể **đăng ký (subscribe)** các DocType và **truyền (stream)** các Tài liệu giữa các trang web khác nhau.

Ví dụ: Giả sử bạn có nhiều Công ty được lưu trữ trên các trang web khác nhau, một trong số đó là trang chính nơi bạn muốn thực hiện bút toán sổ cái và ở các trang khác, các Hóa đơn bán hàng được tạo ra. Bạn có thể sử dụng Truyền dữ liệu sự kiện trong trường hợp này. Để làm việc này, các trang web công ty con có thể đăng ký với trang web công ty chính cho các DocType như Mặt hàng, Khách hàng và Nhà cung cấp. Ngược lại, Công ty chính có thể đăng ký với các công ty con để nhận Hóa đơn bán hàng.

Để truy cập Truyền dữ liệu sự kiện, hãy đi tới:
> Trang chủ > Tự động hóa > Truyền dữ liệu sự kiện (Event Streaming)

## 1. Điều kiện tiên quyết
Trước khi tạo một Bên sản xuất sự kiện (Event Producer), một người dùng chung cần được tạo trên cả hai trang web sẽ được sử dụng để truy cập trang web và sẽ đóng vai trò là Bên đăng ký sự kiện (Event Subscriber). Hãy đảm bảo người dùng đó là Quản trị viên hệ thống (System Manager) và có các quyền cần thiết để tạo, cập nhật và xóa các DocType đã đăng ký.

## 2. Cách thiết lập Truyền dữ liệu sự kiện

Hãy lấy hai trang web để giải thích quy trình này. http://test_site:8000 (Trang web Người tiêu dùng - Consumer site) và http://test_site_producer:8000 (Trang web Bên sản xuất - Producer site)

### 2.1 Lấy khóa của Bên đăng ký sự kiện từ Trang web Bên sản xuất

1. Trên http://test_site_producer:8000 (trang web bên sản xuất), đi tới danh sách Người dùng (User).
2. Mở tài liệu người dùng mà bạn định sử dụng làm Bên đăng ký sự kiện. Cuộn xuống phần có nhãn "API Access". Trong phần đó, tạo khóa cho người dùng bằng cách nhấp vào nút **Tạo khóa (Generate Keys)**. Bạn sẽ nhận được một thông báo chứa mã bí mật của người dùng (user secret), hãy sao chép mã bí mật này và lưu lại. Hệ thống cũng sẽ tạo một khóa API (API key).

### 2.2 Tạo khóa cho Bên đăng ký sự kiện trên Trang web Người tiêu dùng

1. Trên http://test_site:8000 (trang web người tiêu dùng), đi tới danh sách Người dùng và thực hiện quy trình tương tự như bước trước.

### 2.3 Tạo Bên sản xuất sự kiện trên Trang web Người tiêu dùng

1. Trang web mà bạn muốn đăng ký được gọi là Bên sản xuất sự kiện (Event Producer). Hãy tạo một tài liệu Bên sản xuất sự kiện cho trang web mà bạn muốn nhận các bản cập nhật.
2. Trên http://test_site:8000 (trang web người tiêu dùng), đi tới **Trang chủ > Tự động hóa > Truyền dữ liệu sự kiện > Bên sản xuất sự kiện (Event Producer)**.
3. Nhập URL của trang web bạn muốn đăng ký (trong trường hợp này là http://test_site_producer:8000) vào trường URL của Bên sản xuất (Producer URL).
4. Thêm tất cả các DocType mà bạn muốn đăng ký vào bảng DocType của Bên sản xuất sự kiện.
5. Nếu bạn muốn các tài liệu được tạo có cùng tên như trên trang web Bên sản xuất sự kiện từ xa, hãy tích vào ô 'Use Same Name' trong bảng tương ứng với DocType yêu cầu.
6. Thiết lập trường Bên đăng ký sự kiện (Event Subscriber) thành người dùng sẽ được sử dụng để tạo các tài liệu được lấy từ Bên sản xuất sự kiện. Bạn cần tạo cùng một người dùng ở cả hai phía, tức là trên cả trang web Bên tiêu dùng sự kiện (Event Consumer) cũng như trang web Bên sản xuất sự kiện (Event Producer) trước khi tạo Bên sản xuất sự kiện.
7. Dán khóa API (API key) và Mã bí mật API (API Secret) mà bạn đã tạo ở bước đầu tiên (2.1) lần lượt vào các trường API key và API secret.
8. **Lưu**.
9. Sau khi lưu, một Bên tiêu dùng sự kiện (Event Consumer) sẽ được tạo trên trang web bên sản xuất (http://test_site_producer:8000). Trong quy trình này, các khóa của người dùng trên trang web người tiêu dùng sẽ tự động được sao chép vào tài liệu Bên tiêu dùng sự kiện trên trang web bên sản xuất.

    ![Event Producer](https://docs.erpnext.com/docs/v16/assets/img/automation/event-producer-doc.png)

>**Lưu ý**: Nếu Mã bí mật API (API Secret) của người dùng trên bất kỳ trang web nào trong số này bị thay đổi, bạn sẽ phải cập nhật thủ công các khóa trong Bên sản xuất sự kiện cũng như Bên tiêu dùng sự kiện trên cả hai trang web.

### 2.4 Phê duyệt Bên tiêu dùng sự kiện trên trang web Bên sản xuất

1. Sau khi Bên sản xuất sự kiện đã được tạo, một Bên tiêu dùng sự kiện sẽ tự động được tạo trên trang web bên sản xuất. Theo mặc định, tất cả các DocType đã đăng ký đều có trạng thái là 'Chờ duyệt' (Pending). Để cho phép Bên tiêu dùng sự kiện tiêu thụ các tài liệu của các DocType này, Trạng thái của chúng cần được cập nhật thành 'Đã phê duyệt' (Approved).
2. Đi tới: **Trang chủ > Tự động hóa > Truyền dữ liệu sự kiện > Bên tiêu dùng sự kiện (Event Consumer)**.
3. Khi bạn mở tài liệu Bên tiêu dùng sự kiện, bạn sẽ thấy tất cả các DocType mà bên tiêu dùng đã đăng ký. Thay đổi trạng thái từ 'Chờ duyệt' (Pending) sang 'Đã phê duyệt' (Approved) cho tất cả các DocType mà bạn muốn phê duyệt để tiêu thụ. Bạn có thể thay đổi trạng thái thành 'Từ chối' (Rejected) nếu bạn không muốn các tài liệu của DocType đó được tiêu thụ.
4. **Lưu**.

    ![Event Consumer](https://docs.erpnext.com/docs/v16/assets/img/automation/event-consumer-doc.png)

>**Lưu ý**: Các bản cập nhật tài liệu cho các DocType đã đăng ký sẽ không được đồng bộ hóa trừ khi chúng được Phê duyệt.

### 2.5 Truy cập ngoại tuyến với một trang web duy nhất
Nếu bạn có một số nơi có kết nối internet yếu, ví dụ như một cửa hàng ở vùng sâu vùng xa nơi các Hóa đơn bán hàng được tạo ra và bạn muốn đồng bộ hóa các hóa đơn này từ cửa hàng đến tài khoản được lưu trữ, bạn có thể thiết lập đồng bộ hóa ngoại tuyến bằng các bước sau:

1. Thiết lập một bản cài đặt ERPNext cục bộ. Bạn có thể tham khảo [hướng dẫn này](https://github.com/frappe/bench) để thiết lập cục bộ.
2. Bạn cần có một tài khoản được lưu trữ với công ty của mình đã được thiết lập.
3. Bây giờ, hãy tạo một Bên sản xuất sự kiện trên tài khoản được lưu trữ.