<!-- add-breadcrumbs -->
# Hạn chế Mục đích của Phiếu kho


    frappe.ui.form.on("Material Request", "validate", function(frm) {
        if(frappe.user=="user1@example.com" && frm.doc.purpose!="Material Receipt") {
            frappe.msgprint("Bạn chỉ được phép thực hiện Nhận vật tư");
            frappe.throw(__("Không được phép"));
        }
    }


{next}