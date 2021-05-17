// Copyright (c) 2016, Craft and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Estimation and Variance"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		{
			"fieldname":"project",
			"label": __("Project"),
			"fieldtype": "Link",
			"options": "Project",
			"reqd": 1
		},
	]
};
