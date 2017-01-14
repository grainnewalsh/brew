# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "brew"
app_title = "Brewing"
app_publisher = "Metalman Brewing"
app_description = "App for managing brews from Prep to Package"
app_icon = "octicon octicon-beaker"
app_color = "#589494"
app_email = "admin@metalmanbrewing.com"
app_license = "TBD"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/brew/css/brew.css"
# app_include_js = "/assets/brew/js/brew.js"

# include js, css files in header of web template
# web_include_css = "/assets/brew/css/brew.css"
# web_include_js = "/assets/brew/js/brew.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "brew.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "brew.install.before_install"
# after_install = "brew.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "brew.notifications.get_notification_config"

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
# 		"brew.tasks.all"
# 	],
# 	"daily": [
# 		"brew.tasks.daily"
# 	],
# 	"hourly": [
# 		"brew.tasks.hourly"
# 	],
# 	"weekly": [
# 		"brew.tasks.weekly"
# 	]
# 	"monthly": [
# 		"brew.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "brew.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "brew.event.get_events"
# }

