<!-- add-breadcrumbs -->
# Tồn kho vĩnh viễn

Theo hệ thống tồn kho vĩnh viễn, bút toán kế toán được thực hiện cho mọi giao dịch kho. Nếu không, nó sẽ được thực hiện theo các khoảng thời gian lớn hơn, ví dụ như hàng tháng hoặc hàng quý. Mỗi kho được liên kết với một tài khoản tương ứng.

Khi nhận mặt hàng vào một kho cụ thể, số dư trong Tài khoản Kho sẽ tăng lên. Tương tự, khi mặt hàng được xuất từ Kho, một khoản chi phí sẽ được ghi nhận và số dư trong Tài khoản Kho sẽ giảm xuống.

### 1. Cách kích hoạt tồn kho vĩnh viễn

1. Kích hoạt Tồn kho vĩnh viễn:

    **Home > Accounting > Company > Enable Perpetual Inventory**

    <img class="screenshot" alt="Perpetual Inventory" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/perpetual-1.png">
    Lưu ý rằng nếu bạn vô hiệu hóa tồn kho vĩnh viễn, người dùng sẽ phải quản lý các bút toán tài khoản một cách thủ công.
1. Thiết lập các tài khoản mặc định sau cho mỗi Công ty nếu chưa được thiết lập. Các tài khoản này được tạo tự động trong các tài khoản ERPNext mới.

    * Default Inventory Account (Tài sản)
    * Stock Received But Not Billed (Nợ phải trả)
    * Stock Adjustment Account (Chi phí)
    * Expenses Included In Valuation (Chi phí)
    * Cost Center (Trung tâm chi phí)

1. Nếu người dùng muốn thiết lập một tài khoản riêng biệt cho mỗi kho, hãy tạo tài khoản cho từng tài khoản đó. Đi tới:

    **Accounts > Chart of Accounts > Company > Application of Funds (Assets) > Current Asset > Stock Assets > *Tạo một tài khoản mới có cùng tên với Kho***

    Bây giờ, hãy đi tới một kho và liên kết tài khoản này với kho đó. Điều này giúp ích trong việc lọc và xem các báo cáo theo từng kho.

1. Đối với các giao dịch kho, các bút toán sổ cái được thực hiện dựa trên Tài khoản được thiết lập trên kho, nếu người dùng không thiết lập tài khoản cho kho thì hệ thống sẽ lấy tài khoản từ kho cha. Nếu Tài khoản chưa được thiết lập cho kho cha thì hệ thống sẽ lấy tài khoản (Default Inventory Account) từ danh mục công ty.

* * *

### 2. Ví dụ

Xem xét thiết lập Hệ thống tài khoản và Kho sau đây cho công ty của bạn:

Hệ thống tài khoản:

* Assets (Nợ)
    * Current Assets
        * Accounts Receivable
            * Debtors
        * Stock Assets
            * Stores
            * Finished Goods
            * Work In Progress
        * Tax Assets
            * VAT
* Liabilities (Có)
    * Current Liabilities
        * Accounts Payable
            * Creditors
        * Stock Liabilities
            * Stock Received But Not Billed
        * Tax Liabilities
            * Service Tax
* Income (Có)
    * Direct Income
        * Sales Account
* Expenses (Nợ)
    * Direct Expenses
        * Stock Expenses
            * Cost of Goods Sold
            * Expenses Included In Valuation
            * Stock Adjustment
    * Indirect Expenses
        * Shipping Charges
        * Customs Duty

#### 2.1 Cấu hình Kho - Tài khoản

  * Stores
  * Work In Progress
  * Finished Goods

#### 2.2 Phiếu nhập hàng

Giả sử bạn đã mua _10 cái_ mặt hàng "RM0001" với giá _$200_ từ nhà cung cấp "Arcu Vel Quam Fabricators". Dưới đây là chi tiết của Phiếu nhập hàng:

**Supplier:** Arcu Vel Quam Fabricators

**Items:**

<table class="table table-bordered">
    <thead>
        <tr>
            <th>Item</th>
            <th>Warehouse</th>
            <th>Qty</th>
            <th>Rate</th>
            <th>Amount</th>
            <th>Valuation Amount</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>RM0001</td>
            <td>Stores</td>
            <td>10</td>
            <td>200</td>
            <td>2000</td>
            <td>2250</td>
        </tr>
    </tbody>
</table>
<p><strong>Taxes:</strong>
</p>
<table class="table table-bordered">
    <thead>
        <tr>
            <th>Account</th>
            <th>Amount</th>
            <th>Category</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Shipping Charges</td>
            <td>100</td>
            <td>Total and Valuation</td>
        </tr>
        <tr>
            <td>VAT (10%)</td>
            <td>200</td>
            <td>Total</td>
        </tr>
        <tr>
            <td>Customs Duty</td>
            <td>150</td>
            <td>Valuation</td>
        </tr>
    </tbody>
</table>

**Sổ kho**

<img class="screenshot" alt="Perpetual Inventory" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/perpetual-receipt-sl-1.png">

**Sổ cái**

<img class="screenshot" alt="Perpetual Inventory" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/perpetual-receipt-gl-2.png">

Khi số dư tồn kho tăng lên thông qua Phiếu nhập hàng, các tài khoản "Store" sẽ được ghi nợ và một tài khoản tạm thời "Stock Receipt But Not Billed" sẽ được ghi có, để duy trì hệ thống kế toán bút toán kép. Đồng thời, một khoản chi phí âm sẽ được ghi vào tài khoản có danh mục là "Valuation" hoặc "Total and Valuation" trong bảng thuế và phí cho số tiền được cộng thêm nhằm mục đích tính giá, để tránh việc ghi nhận chi phí hai lần.

#### 2.3 Hóa đơn mua hàng

Khi nhận được Hóa đơn từ nhà cung cấp cho Phiếu nhập hàng trên, bạn sẽ lập Hóa đơn mua hàng cho cùng giao dịch đó. Các bút toán sổ cái như sau:

**Sổ cái**

<img class="screenshot" alt="Perpetual Inventory" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/perpetual-pinv-gl-3.png">

Tại đây, tài khoản "Stock Received But Not Billed" được ghi nợ và triệt tiêu ảnh hưởng của Phiếu nhập hàng.

#### 2.4 Phiếu giao hàng

Giả sử, bạn có một đơn hàng từ "Utah Automation Services" để giao 5 cái mặt hàng "RM0001" với giá $300. Dưới đây là chi tiết của Phiếu giao hàng:

**Customer:** Utah Automation Services

**Items:**
<table class="table table-bordered">
    <thead>
        <tr>
            <th>Item</th>
            <th>Warehouse</th>
            <th>Qty</th>
            <th>Rate</th>
            <th>Amount</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>RM0001</td>
            <td>Stores</td>
            <td>5</td>
            <td>300</td>