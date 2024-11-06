#!/bin/bash

# Define file paths
ORIGINAL_FILE="/usr/lib/python3/dist-packages/odoo/addons/web/static/src/public/database_manager.qweb.html.origi"
UPDATED_FILE="/usr/lib/python3/dist-packages/odoo/addons/web/static/src/public/database_manager.qweb.html"
PATCH_FILE="/usr/lib/python3/dist-packages/odoo/addons/odoo_alcohol_excise/core_file_diffs/database_manager_qweb_html.diff"

# Compare the original and updated files
if diff -q $ORIGINAL_FILE $UPDATED_FILE > /dev/null; then
    echo "No differences found. Applying patch..."
    # Apply the patch if no differences
    patch -p1 < $PATCH_FILE
    # Restart Odoo service
    systemctl restart odoo
else
    echo "Differences found between the original and updated file."
    echo "Please manually review the changes before applying the patch."
fi