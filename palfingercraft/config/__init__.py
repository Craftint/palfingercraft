from __future__ import unicode_literals
import frappe
from frappe import _
__version__ = '0.0.1'


from erpnext.config import buying,selling,projects,crm
data = buying.get_data()
datasell = selling.get_data()
dataproj = projects.get_data()
datacrm = crm.get_data()


#selling module desktop
def get_data_sell(datasell=datasell):
    for row in datasell:
        if row['label'] == 'Items and Pricing':
            datasell.remove(row)      #Remove Items and Pricing Section
        if row['label'] == 'Key Reports':
            for rowitem in row['items']:
                if 'Customer Acquisition and Loyalty' in rowitem['name']:
                    row['items'].remove(rowitem)
                if 'Inactive Customers' in rowitem['name']:
                    row['items'].remove(rowitem)
                if 'Ordered Items To Be Delivered' in rowitem['name']:
                    row['items'].remove(rowitem)
                if 'Sales Person-wise Transaction Summary' in rowitem['name']:
                    row['items'].remove(rowitem)
                if 'Item-wise Sales History' in rowitem['name']:
                    row['items'].remove(rowitem)
                if 'Quotation Trends' in rowitem['name']:
                    row['items'].remove(rowitem)
                if 'Sales Order Trends' in rowitem['name']:
                    row['items'].remove(rowitem)
            
        if row['label'] == 'Other Reports':
            datasell.remove(row)      #Remove other reports Section
        if row['label'] == 'Sales':
            for rowitem in row['items']:
                if 'Sales Partner' in rowitem['name']:
                    row['items'].remove(rowitem)
                if 'Blanket Order' in rowitem['name']:
                    row['items'].remove(rowitem)
            

                    row['items'].append({
                                       "type": "doctype",
                                       "name": "Estimation Sheet",
                                       "description": _("Estimation Sheet"),
                                       "onboard": 1,
                               })
    return datasell
selling.get_data = get_data_sell

# buying module desktop
def get_data(data=data):
    for row in data:
        if row['label'] == 'Items and Pricing':
           for rowitem in row['items']:
               if rowitem['name'] == "Product Bundle":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Item Group":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Promotional Scheme":
                   row['items'].remove(rowitem)
        if row['label'] == 'Supplier Scorecard':
            data.remove(row)      #Remove Supplier Scorecard


    return data
buying.get_data = get_data
# crm module desktop
def get_data_crm(datacrm = datacrm):
    for row in datacrm:
        if row['label'] == 'Sales Pipeline':
           for rowitem in row['items']:
               if rowitem['name'] == "Lead":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Communication":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Lead Source":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Contract":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Appointment":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Newsletter":
                   row['items'].remove(rowitem)
        if row['label'] == 'Settings':
           for rowitem in row['items']:
               if rowitem['name'] == "Sales Person":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Campaign":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Email Campaign":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "SMS Center":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "SMS Log":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "SMS Settings":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Email Group":
                   row['items'].remove(rowitem)
        if row['label'] == 'Reports':
            datacrm.remove(row)      #Remove Reports
        if row['label'] == 'Maintenance':
            datacrm.remove(row)      #Remove Maintenance

    return datacrm
crm.get_data = get_data_crm


# projects module desktop
def get_data_proj(dataproj=dataproj):
    for row in dataproj:
        if row['label'] == 'Projects':
           for rowitem in row['items']:
               if rowitem['name'] == "Project Template":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Project Type":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Project Update":
                   row['items'].remove(rowitem)
                   row['items'].append({                                
                                        "type": "doctype",
                                        "name": "Machinery and Other Cost",
                                        "description": _("Machinery and Other Cost"),
                                        "onboard": 1,
                                })
                   row['items'].append({
                                        "type": "doctype",
                                        "name": "Project Timesheet",
                                        "label": _("Project Time Sheet"),
                                        "onboard": 1,
                                })
                   row['items'].append({                                
                                        "type": "doctype",
                                        "name": "Employee Allocation",
                                        "label": _("Employee Allocation")
                     
                                })
                   row['items'].append({                                
                                        "type": "doctype",
                                        "name": "Employee Allocation Tool",
                                        "label": _("Employee Allocation Tool")
                                })




        if row['label'] == 'Reports':
           for rowitem in row['items']:
               if rowitem['name'] == "Project wise Stock Tracking":
                   row['items'].remove(rowitem)
               if rowitem['name'] == "Project Billing Summary":
                   row['items'].remove(rowitem)




    return dataproj
projects.get_data = get_data_proj

