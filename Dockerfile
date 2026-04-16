# ERPNext v16 + Frappe HRMS + Vietnamese localization
#
# Extends the official frappe/erpnext image with:
#   - Frappe HRMS app installed
#   - Patch for money_in_words() to use Vietnamese convention
#     (amount in words ... đồng chẵn., first-word-capitalized)
#   - Dummy common_site_config.json so HRMS frontend PWA can build
#
# Runtime site settings (Language=vi, Number Format, VND symbol) are
# applied via scripts/setup_vn_site.py — run after site creation.

FROM frappe/erpnext:v16.13.3

USER frappe
WORKDIR /home/frappe/frappe-bench

# Dummy site config for HRMS PWA build step
RUN mkdir -p sites && echo '{"socketio_port": 9000, "default_site": "build.local"}' > sites/common_site_config.json

# Install HRMS (skip asset build; assets built later by `bench build`)
RUN bench get-app --branch version-16 hrms https://github.com/frappe/hrms.git

# Apply Vietnamese localization patches
COPY patches/money_in_words_vi.patch /tmp/money_in_words_vi.patch
RUN cd apps/frappe && patch -p2 < /tmp/money_in_words_vi.patch

# Return to default frappe workdir; image is now ready.
