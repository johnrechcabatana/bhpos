# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bhposapp"
app_title = "bhposapp"
app_publisher = "johndef"
app_description = "app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "cabatan@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/bhposapp/css/custom.css"
# app_include_js = "/assets/bhposapp/js/bhposapp.js"

# include js, css files in header of web template
web_include_css = "/assets/bhposapp/css/style.css"
# web_include_js = "/assets/bhposapp/css/custom.css"

# include js in page
page_js = {"point-of-sale" : "public/js/pos.js",
           "pos":"public/js/pos.js"
           }

# include js in doctype views
doctype_js = {
        "Sales Invoice" : "public/js/sales_invoice.js",
        "Purchase Order": "public/js/purchase_order.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
#fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
            'name', 'in',[
               "Item-item_type" ,
               "Item-shelf_area"
            ]]
        ]
    },
     {
        "doctype":"Property Setter",
        "filters":[
            [
                'name','in',[
                  "Item-standard_rate-hidden",
                  "Item-valuation_rate-hidden",
                  "Item-opening_stock-hidden"
                ]]
          ]
      }
];

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bhposapp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bhposapp.install.before_install"
# after_install = "bhposapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bhposapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bhposapp.tasks.all"
# 	],
# 	"daily": [
# 		"bhposapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"bhposapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bhposapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bhposapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bhposapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bhposapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bhposapp.task.get_dashboard_data"
# }

