"""
Apply Vietnamese runtime settings to an ERPNext site.

Usage (inside erpnext-backend container):
    bench --site <site-name> execute /path/to/setup_vn_site.py

Or via docker exec:
    docker cp scripts/setup_vn_site.py erpnext-backend:/tmp/
    docker exec erpnext-backend bench --site <site> execute \\
      frappe.utils.execute_in_shell --kwargs '{"cmd":"python /tmp/setup_vn_site.py"}'

This is idempotent — safe to re-run.

Configures:
  - System Settings: language=vi, number_format=#.###,##, date_format=dd-mm-yyyy, time_zone=Asia/Ho_Chi_Minh
  - VND currency: symbol=đ, placed on right, no fraction unit
  - All LKF users' preferred_language = vi
"""

import frappe


def run():
    ss = frappe.get_single("System Settings")
    ss.language = "vi"
    ss.country = "Vietnam"
    ss.time_zone = "Asia/Ho_Chi_Minh"
    ss.first_day_of_the_week = "Monday"
    ss.number_format = "#.###,##"
    ss.date_format = "dd-mm-yyyy"
    ss.time_format = "HH:mm:ss"
    ss.currency_precision = "0"
    ss.float_precision = 2
    ss.save(ignore_permissions=True)
    print("System Settings → vi, dd-mm-yyyy, Asia/Ho_Chi_Minh")

    if frappe.db.exists("Currency", "VND"):
        vnd = frappe.get_doc("Currency", "VND")
        vnd.symbol = "đ"
        vnd.symbol_on_right = 1
        vnd.smallest_currency_fraction_value = 0
        vnd.fraction = ""
        vnd.fraction_units = 0
        vnd.number_format = "#.###,##"
        vnd.save(ignore_permissions=True)
        print("VND currency → symbol đ on right, no fraction")

    # Set Vietnamese users' language
    users = frappe.get_all(
        "User",
        filters={"enabled": 1},
        fields=["email"],
    )
    count = 0
    for u in users:
        email = u["email"]
        if email in ("Administrator", "Guest"):
            continue
        if not (email.endswith("@lkf.com.vn") or email.endswith("@lkf.vn")):
            continue
        frappe.db.set_value("User", email, "language", "vi")
        frappe.db.set_value("User", email, "time_zone", "Asia/Ho_Chi_Minh")
        count += 1
    print(f"Set vi language for {count} LKF users")

    frappe.db.commit()
    frappe.clear_cache()
    print("Done — logout/login to see Vietnamese UI.")


if __name__ == "__main__":
    run()
