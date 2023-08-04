from . import __version__ as app_version

app_name = "gaxisdynamic"
app_title = "gaxis_dynamic"
app_publisher = "shubham"
app_description = "sss"
app_email = "aa"
app_license = "ss"


doctype_js = {
    "Customer": "my_customization/client_scripts/customer.js",
    "Company":"my_customization/client_scripts/company.js",
    "Address":"my_customization/client_scripts/address.js",
    "Supplier":"my_customization/client_scripts/supplier.js",
    "Supplier Quotation":"my_customization/client_scripts/supplier_quotation.js",
    "User":"my_customization/client_scripts/user.js",
    "Quotation":"my_customization/client_scripts/quotation.js",
    "Sales Order":"my_customization/client_scripts/sales_order.js",
    "Batch":"my_customization/client_scripts/batch.js",
    "Item":"my_customization/client_scripts/item.js",
    "Stock Entry":"my_customization/client_scripts/stock_entry.js",
    "Stock Reconciliation":"my_customization/client_scripts/stock_reconciliation.js",
    "Sales Invoice":"my_customization/client_scripts/sales_invoice.js",
    "Warehouse":"my_customization/client_scripts/warehouse.js",
    "Material Request":"my_customization/client_scripts/material_request.js"
}

after_install = "gaxisdynamic.install.after_install"
after_migrate="gaxisdynamic.install.after_install"


doc_events = {
    "Quotation": {
        "autoname": [
            "gaxisdynamic.my_customization.constants.quotation.autoname",
        ],
    },
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gaxisdynamic/css/gaxisdynamic.css"
# app_include_js = "/assets/gaxisdynamic/js/gaxisdynamic.js"

# include js, css files in header of web template
# web_include_css = "/assets/gaxisdynamic/css/gaxisdynamic.css"
# web_include_js = "/assets/gaxisdynamic/js/gaxisdynamic.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gaxisdynamic/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "gaxisdynamic.utils.jinja_methods",
#	"filters": "gaxisdynamic.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gaxisdynamic.install.before_install"
# after_install = "gaxisdynamic.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gaxisdynamic.uninstall.before_uninstall"
# after_uninstall = "gaxisdynamic.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gaxisdynamic.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"gaxisdynamic.tasks.all"
#	],
#	"daily": [
#		"gaxisdynamic.tasks.daily"
#	],
#	"hourly": [
#		"gaxisdynamic.tasks.hourly"
#	],
#	"weekly": [
#		"gaxisdynamic.tasks.weekly"
#	],
#	"monthly": [
#		"gaxisdynamic.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "gaxisdynamic.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gaxisdynamic.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gaxisdynamic.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gaxisdynamic.utils.before_request"]
# after_request = ["gaxisdynamic.utils.after_request"]

# Job Events
# ----------
# before_job = ["gaxisdynamic.utils.before_job"]
# after_job = ["gaxisdynamic.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gaxisdynamic.auth.validate"
# ]
# fixtures=[
#     "Workspace"
# ]