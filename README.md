# ERPNext Vietnam Localization

**Drop-in package** to turn a fresh ERPNext v16 install into a Vietnam-compliant deployment in one image build + one script run.

Bộ bản địa hoá ERPNext v16 cho doanh nghiệp Việt Nam — build image một lần, chạy script một lần, xong.

## What it includes

### Source patches (baked into the Docker image)

- **`patches/money_in_words_vi.patch`** — modifies `frappe.utils.money_in_words()` so Vietnamese sites render monetary amounts correctly:
  - Before: `VND Tám Trăm Hai Mươi Bảy Triệu ... chỉ.`
  - After:  `Tám trăm hai mươi bảy triệu ... chín trăm đồng chẵn.`
  - Places currency word at end (VN convention), uses sentence case, and uses proper "đồng chẵn." suffix.
  - English sites are unaffected (patch is locale-conditioned on `vi`).

### Runtime settings (applied once per site)

- **`scripts/setup_vn_site.py`** — sets:
  - **System Settings**: `language=vi`, `number_format=#.###,##`, `date_format=dd-mm-yyyy`, `time_zone=Asia/Ho_Chi_Minh`, first day of week Monday, VND precision=0
  - **VND currency**: symbol `đ` on right, no fractional unit
  - **Any LKF user** (email ending `@lkf.com.vn`): default language `vi`

### Integration with translations

Full Vietnamese translations for Frappe / ERPNext / HRMS are in a sibling repo:
**https://github.com/nguyenhuuduong-lkf/erpnext-vi-translations**

Deploy that repo's `.po` files alongside this one for full VN UI coverage.

## Usage

### 1. Build image

```bash
git clone https://github.com/nguyenhuuduong-lkf/erpnext-vietnam-localization
cd erpnext-vietnam-localization
docker build -t lkf/erpnext-vi:v16.13.3 .
```

### 2. Use in docker-compose

Replace `frappe/erpnext:v16-hrms` (or whatever tag) with `lkf/erpnext-vi:v16.13.3` in your `docker-compose.yml`, then `docker compose up -d`.

### 3. Apply VN site settings after site exists

```bash
docker cp scripts/setup_vn_site.py erpnext-backend:/tmp/setup_vn_site.py
docker exec erpnext-backend bench --site <your-site> execute setup_vn_site.run
```

(You need to adjust the import — see script docstring for details. The simplest form is to `cat` the file into bench console.)

### 4. Optional: load Vietnamese translations

See https://github.com/nguyenhuuduong-lkf/erpnext-vi-translations for instructions.

## Design notes

- Patch is **additive** and guarded by `lang.startswith('vi')`. It does not change behaviour for any other locale.
- `Dockerfile` preserves the exact image structure of the official Frappe image, so it plays nicely with `frappe_docker` compose files.
- Site settings script is **idempotent** — safe to re-run after upgrades.
- When Frappe upstream releases a better VN handling, drop the patch and keep the rest.

## License

- `patches/*` — derived from Frappe Framework, same license (MIT)
- `scripts/*`, `Dockerfile`, `README.md` — MIT (LKF Cold Chain)

## Credits

- Frappe Technologies Pvt. Ltd. — upstream ERPNext
- LKF Cold Chain — patch authoring and Vietnam-specific settings
