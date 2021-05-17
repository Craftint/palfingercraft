# Copyright (c) 2013, Craft and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, msgprint


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_record(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Type"),
            "fieldname": "type",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Estimate"),
            "fieldname": "estimate",
            "fieldtype": "Currency",
            "width": 200
        },
        {
            "label": _("Actual"),
            "fieldname": "actual",
            "fieldtype": "Currency",
            "width": 200
        },

        {
            "label": _("Variance"),
            "fieldname": "variance",
            "fieldtype": "Currency",
            "width": 200
        },

    ]


def get_record(filters):
    data = []
    sql = """select 
                *
            from 
                `tabProject` 
            where 
                {}""".format(get_conditions(filters))
    project = frappe.db.sql(sql, as_dict=1)
    for po in project:
        if po.cost_of_raw_materials_and_stock_estimate:
            row = {
                "type": "Consumables",
                "estimate": po.cost_of_raw_materials_and_stock_estimate,
                "actual": po.cost_of_raw_material_and_stock,
                "variance": po.cost_of_raw_materials_and_stock_estimate-po.cost_of_raw_material_and_stock
            }
            data.append(row)
        if po.asset_cost_estimate:
            row = {
                "type": "Asset",
                "estimate": po.asset_cost_estimate,
                "actual": po.asset_cost,
                "variance": po.asset_cost_estimate-po.asset_cost
            }
            data.append(row)
        if po.labor_cost_estimate:
            row = {
                "type": "Labour",
                "estimate": po.labor_cost_estimate,
                "actual": po.labor_cost,
                "variance": po.labor_cost_estimate-po.labor_cost
            }
            data.append(row)
        if po.machinery_and_equipment_cost_estimate:
            row = {
                "type": "Machinery and Equipment",
                "estimate": po.machinery_and_equipment_cost_estimate,
                "actual": po.machinery_and_equipment_cost,
                "variance": po.machinery_and_equipment_cost_estimate-po.machinery_and_equipment_cost
            }
            data.append(row)
        if po.other_cost_involved_estimate:
            row = {
                "type": "Other",
                "estimate": po.other_cost_involved_estimate,
                "actual": po.other_cost_involved,
                "variance": po.other_cost_involved_estimate-po.other_cost_involved
            }
            data.append(row)

    return data


def get_conditions(filters):
    conditions = []

    if filters.get('company'):
        conditions.append("company = '{}'".format(filters.get('company')))
    if filters.get('project'):
        conditions.append("name = '{}'".format(filters.get('project')))

    conditions = (" and ").join(conditions)
    return conditions
