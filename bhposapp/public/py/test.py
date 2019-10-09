import frappe

@frappe.whitelist()
def get_query(item_code,warehouse): 
	#frappe.db.sql(""" SELECT * FROM `tabPOS Profile` WHERE item_code =%s""", item_code, as_dict=1);
	whouse = frappe.db.get_value('POS Profile', warehouse, 'warehouse');
	# filters = [["warehouse" ,  "=", whouse] ,["actual_qty", ">=", 0],["item_code", "=", item_code]];
	# res =  frappe.get_all("Bin", fields = ["item_code", "sum(actual_qty) as actual_qty"],
	#  			filters = filters, group_by = "item_code");	
	res = frappe.db.sql(""" SELECT  item_code,  sum(actual_qty) as actual_qty FROM `tabBin` WHERE warehouse =%s and item_code =%s GROUP BY item_code""", (whouse, item_code), as_dict=1);	
	return res; 