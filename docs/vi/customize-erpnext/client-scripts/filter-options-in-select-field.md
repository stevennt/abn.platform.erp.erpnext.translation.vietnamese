<!-- add-breadcrumbs -->
# Lọc các tùy chọn trong trường Select

Giả sử bạn có hai trường thả xuống (drop-down) tên là State và City. State có hai giá trị là Karnataka và Maharashtra, còn City có bốn giá trị là Bangalore, Mysore, Mumbai và Pune. Nếu bạn muốn lọc các tùy chọn trong City dựa trên giá trị đã chọn trong State, bạn có thể viết một script tùy chỉnh như dưới đây.

    frappe.ui.form.on("Lead", "state", function(frm) {
      if(frm.doc.state == "Karnataka")
      {
        set_field_options("city", ["Bangalore","Mysore"])
      }
      else if(frm.doc.state == "Maharashtra")
      {
        set_field_options("city", ["Mumbai","Pune"])
      }
      else if(frm.doc.state == "")
      {
        set_field_options("city", ["","Bangalore","Mysore","Mumbai","Pune"])
      }
      });

  <img class="screenshot" alt="Opening Account" src="https://docs.erpnext.com/docs/v13/assets/img/customize/filter_dropdown.gif">


  {next}