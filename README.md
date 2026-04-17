# ERPNext Vietnam Localization

**Drop-in Vietnam localization pack for ERPNext v16** — Vietnamese translations, Docker image with code patches, and runtime settings. Clone one repo, deploy, done.

Bộ bản địa hoá ERPNext v16 đầy đủ cho doanh nghiệp Việt Nam. Clone một repo, deploy, xong.

## What you get

| Component | What it fixes |
|---|---|
| **translations/** | Vietnamese `.po` files for Frappe, ERPNext, HRMS (~17,600 strings, near-complete) |
| **Dockerfile** | Builds ERPNext v16.13.3 + Frappe HRMS with Vietnamese patches baked in |
| **patches/money_in_words_vi.patch** | Fixes "amount in words" for Vietnamese convention (e.g. `"Tám trăm hai mươi bảy triệu... đồng chẵn."` instead of `"VND Eight Hundred Twenty-Seven Million... only."`) |
| **scripts/setup_vn_site.py** | Idempotent script: sets System Settings, VND symbol, user language defaults |
| **scripts/fix_grammar.py** | Grammar-flip helper for Vietnamese (swaps `{placeholder} <noun>` → `<noun> {placeholder}`) |
| **scripts/translate_po.py** | Auto-translate untranslated msgids via local LLM (gemma-4, Claude, or any OpenAI-compatible API) |

## Quick start

### 1. Clone

```bash
git clone https://github.com/nguyenhuuduong-lkf/erpnext-vietnam-localization
cd erpnext-vietnam-localization
```

### 2. Build the Docker image (with HRMS + patches)

```bash
docker build -t lkf/erpnext-vi:v16.13.3 .
```

### 3. Deploy translations into your running ERPNext

```bash
docker cp translations/frappe.vi.po  erpnext-backend:/home/frappe/frappe-bench/apps/frappe/frappe/locale/vi.po
docker cp translations/erpnext.vi.po erpnext-backend:/home/frappe/frappe-bench/apps/erpnext/erpnext/locale/vi.po
docker cp translations/hrms.vi.po    erpnext-backend:/home/frappe/frappe-bench/apps/hrms/hrms/locale/vi.po

docker exec erpnext-backend bench --site <your-site> compile-po-to-mo
docker exec erpnext-backend bench --site <your-site> clear-cache
docker restart erpnext-backend
```

### 4. Apply VN runtime settings

```bash
docker cp scripts/setup_vn_site.py erpnext-backend:/tmp/setup_vn_site.py
docker exec erpnext-backend bench --site <your-site> execute /tmp/setup_vn_site.py
```

This sets: `language=vi`, `number_format=#.###,##`, `date_format=dd-mm-yyyy`, `time_zone=Asia/Ho_Chi_Minh`, VND currency with `đ` symbol on the right, etc.

### 5. Log out / log in to your ERPNext — UI now speaks Vietnamese.

## Translation coverage

| App | msgid | Translated | Coverage |
|---|---|---|---|
| frappe | ~6,100 | ~6,100 | ≈100% |
| erpnext | ~9,300 | ~9,300 | ≈100% |
| hrms | ~2,200 | ~2,200 | ≈100% |

**Total: ~17,600 translated strings.**

Base translations pulled from Frappe's `develop` branch (community-contributed). Remaining ~11,000 empty `msgstr` filled via local LLM (gemma-4-26B) with business/ERP-oriented prompts. Grammar-flipped 64+ common phrases (`{0} List` → `Danh sách {0}` etc.).

## Patch: `money_in_words_vi.patch`

Modifies `frappe.utils.money_in_words()` so Vietnamese sites render monetary amounts correctly:

**Before:** `VND Tám Trăm Hai Mươi Bảy Triệu Năm Trăm Tám Mươi Ba Nghìn Chín Trăm chỉ.`

**After:** `Tám trăm hai mươi bảy triệu năm trăm tám mươi ba nghìn chín trăm đồng chẵn.`

Changes:
- Drops "VND" English prefix
- Uses Vietnamese sentence case (only first word capitalized)
- Uses `đồng chẵn.` suffix (standard VN invoice convention)
- Places currency word at the END (VN convention) instead of prefix (EN convention)
- **Only active when `lang='vi'`** — no effect on other locales

## Updating translations

When Frappe releases new `vi.po` (e.g. from Crowdin sync):

```bash
# Pull latest source po files
for app in frappe erpnext hrms; do
  curl -sL "https://raw.githubusercontent.com/frappe/$app/develop/$app/locale/vi.po" -o "translations/${app}.vi.po"
done

# Find new empty msgstrs, auto-translate via LLM
export LLM_URL=http://your-llm:8002/v1/chat/completions
python3 scripts/translate_po.py translations/frappe.vi.po --batch 80
python3 scripts/translate_po.py translations/erpnext.vi.po --batch 80
python3 scripts/translate_po.py translations/hrms.vi.po --batch 80

# Apply VN grammar rules (flip placeholder order)
python3 scripts/fix_grammar.py translations/frappe.vi.po translations/erpnext.vi.po translations/hrms.vi.po

# Redeploy (same as step 3 above)
```

## Quality note

Translations are predominantly LLM-generated. They are **usable but not professionally curated**. For production deployments where UI correctness is critical, have a Vietnamese speaker review and override specific terms via ERPNext's `Translation` doctype.

Official contributions should go through https://crowdin.com/project/frappe (Vietnamese team).

Bản dịch phần lớn do LLM sinh. Dùng được nhưng chưa được review chuyên nghiệp. Muốn chuẩn chỉ hơn, cần người Việt review qua doctype Translation trong ERPNext, hoặc đóng góp qua Crowdin.

## License

- Translations (`.po` files) — derived from Frappe upstream; license follows each upstream app:
  - `frappe.vi.po` → MIT (Frappe Framework)
  - `erpnext.vi.po` → GPL v3 (ERPNext)
  - `hrms.vi.po` → GPL v3 (Frappe HRMS)
- `patches/money_in_words_vi.patch` → MIT (derivative of Frappe, which is MIT)
- Scripts & Dockerfile → MIT (LKF Cold Chain)

See `LICENSE`.

## Credits

- Frappe Technologies Pvt. Ltd. — upstream ERPNext
- Crowdin Vietnamese translators — base translations
- gemma-4-26B (local vLLM) — gap-filling auto-translation
- LKF Cold Chain (Vietnam) — curation, patches, grammar fixes, deployment glue

## Related

- Bot Thảo Linh — conversational ERPNext assistant in Vietnamese (internal LKF project, will be open-sourced later)
