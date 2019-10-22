import frappe


@frappe.whitelist()
def filt_itemby_supplier(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql("""Select parent from `tabItem Supplier` where  supplier= %s""",(filters.get("supplier")));