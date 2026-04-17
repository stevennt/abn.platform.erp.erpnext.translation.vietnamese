<!-- add-breadcrumbs -->
# Hạn chế quyền Hủy

Thêm một trình xử lý vào sự kiện `custom_before_cancel`:



    cur_frm.cscript.custom_before_cancel = function(doc) {
        if (frappe.user_roles.indexOf("Accounts User")!=-1 && frappe.user_roles.indexOf("Accounts Manager")==-1
                && user_roles.indexOf("System Manager")==-1) {
            if (flt(doc.grand_total) > 10000) {
                frappe.msgprint("Bạn không thể hủy giao dịch này, vì tổng cộng \
                    lớn hơn 10000");
                frappe.validated = false;
            }
        }
    }


{next}