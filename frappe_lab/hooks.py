# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_lab"
app_title = "Frappe Lab"
app_publisher = "Gaurav Naik"
app_description = "App for experiments using the Frappe Framework"
app_icon = "fa fa-flask"
app_color = "green"
app_email = "gauravnaik6288@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_lab/css/frappe_lab.css"
# app_include_js = "/assets/frappe_lab/js/frappe_lab.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_lab/css/frappe_lab.css"
# web_include_js = "/assets/frappe_lab/js/frappe_lab.js"

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

# Website user home page (by function)
# get_website_user_home_page = "frappe_lab.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_lab.install.before_install"
# after_install = "frappe_lab.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_lab.notifications.get_notification_config"

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
# 		"frappe_lab.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_lab.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_lab.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_lab.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_lab.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_lab.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_lab.event.get_events"
# }

