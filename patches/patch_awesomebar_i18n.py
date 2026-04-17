#!/usr/bin/env python3
"""
Patch Frappe's Awesome Bar / Command Palette for correct Vietnamese word order.

Root cause:
  get_route_label() and get_recent_pages() concatenate translated parts:
    __(name) + " " + __(type)  →  "Người dùng Danh sách"  (wrong)
  instead of using template strings that already have correct translations:
    __("{0} List", [__(name)])  →  "Danh sách Người dùng"  (correct)

Usage:
  # Copy into container and run:
  docker cp patch_awesomebar_i18n.py erpnext-backend:/tmp/
  docker exec erpnext-backend python3 /tmp/patch_awesomebar_i18n.py
  docker exec erpnext-backend bench build --app frappe

  # IMPORTANT: After bench build, copy real files to shared volume
  # (bench build creates symlinks that don't work across containers)
  docker exec erpnext-backend bash -c '
    cd /home/frappe/frappe-bench/sites/assets
    for link in frappe erpnext hrms; do
      if [ -L $link ]; then
        target=$(readlink $link); rm $link; cp -r $target $link
      fi
    done'
  docker exec erpnext-backend bench --site SITE_NAME clear-cache

Re-run after each Frappe update.
"""
import re
import shutil
from pathlib import Path

FRAPPE_JS = Path("/home/frappe/frappe-bench/apps/frappe/frappe/public/js/frappe")


def patch_get_route_label():
    """Patch utils.js: get_route_label() to use template strings."""
    fpath = FRAPPE_JS / "utils" / "utils.js"
    text = fpath.read_text()

    # Already patched?
    if '"{0} List"' in text.split("get_route_label")[1].split("report_column_total")[0]:
        print(f"  [skip] get_route_label already patched")
        return

    shutil.copy(fpath, str(fpath) + ".bak")

    old = '''	get_route_label(route_str) {
		let route = route_str.split("/");

		if (route[2] === "Report" || route[0] === "query-report") {
			return (__(route[3]) || __(route[1])).bold() + " " + __("Report");
		}
		if (route[0] === "List") {
			return __(route[1]).bold() + " " + __("List");
		}
		if (route[0] === "modules") {
			return __(route[1]).bold() + " " + __("Module");
		}
		if (route[0] === "Workspaces") {
			return __(route[1]).bold() + " " + __("Workspace");
		}
		if (route[0] === "dashboard") {
			return __(route[1]).bold() + " " + __("Dashboard");
		}
		return __(frappe.utils.to_title_case(__(route[0]), true));
	},'''

    new = '''	get_route_label(route_str) {
		let route = route_str.split("/");

		if (route[2] === "Report" || route[0] === "query-report") {
			return __("{0} Report", [(__(route[3]) || __(route[1])).bold()]);
		}
		if (route[0] === "List") {
			return __("{0} List", [__(route[1]).bold()]);
		}
		if (route[0] === "modules") {
			return __("{0} Module", [__(route[1]).bold()]);
		}
		if (route[0] === "Workspaces") {
			return __("{0} Workspace", [__(route[1]).bold()]);
		}
		if (route[0] === "dashboard") {
			return __("{0} Dashboard", [__(route[1]).bold()]);
		}
		return __(frappe.utils.to_title_case(__(route[0]), true));
	},'''

    if old not in text:
        print(f"  [WARN] get_route_label source differs from expected — skipping")
        return

    text = text.replace(old, new)
    fpath.write_text(text)
    print(f"  [ok] get_route_label patched")


def patch_get_recent_pages():
    """Patch search_utils.js: get_recent_pages() to use template strings."""
    fpath = FRAPPE_JS / "ui" / "toolbar" / "search_utils.js"
    text = fpath.read_text()

    # Already patched?
    if "i18n-patched" in text:
        print(f"  [skip] get_recent_pages already patched")
        return

    shutil.copy(fpath, str(fpath) + ".bak")

    # Replace the switch/case block and the label/value assignment
    old_block = '''				let labelSuffix;

				switch (view_type) {
					case "List":
						labelSuffix = __("List");
						break;
					case "Tree":
						labelSuffix = __("Tree");
						break;
					case "Workspaces":
						labelSuffix = __("Workspace");
						break;
					case "query-report":
						labelSuffix = __("Report");
						break;
				}

				out.label = __(view_name.bold()) + " " + labelSuffix;
				out.value = __(view_name) + " " + labelSuffix;'''

    new_block = '''				// i18n-patched: use template strings for correct word order
				let viewTypeKey;

				switch (view_type) {
					case "List":
						viewTypeKey = "List";
						break;
					case "Tree":
						viewTypeKey = "Tree";
						break;
					case "Workspaces":
						viewTypeKey = "Workspace";
						break;
					case "query-report":
						viewTypeKey = "Report";
						break;
				}

				out.label = __("{0} " + viewTypeKey, [__(view_name).bold()]);
				out.value = __("{0} " + viewTypeKey, [__(view_name)]);'''

    if old_block not in text:
        print(f"  [WARN] get_recent_pages source differs from expected — skipping")
        return

    text = text.replace(old_block, new_block)
    fpath.write_text(text)
    print(f"  [ok] get_recent_pages patched")


def main():
    print("Patching Frappe Awesome Bar for i18n word order...")
    patch_get_route_label()
    patch_get_recent_pages()
    print("\nDone! Run: bench build --app frappe")


if __name__ == "__main__":
    main()
