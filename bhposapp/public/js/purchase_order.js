/* display items based on supplier */
frappe.ui.form.on('Purchase Order', {
    supplier: function(frm) {
       me.frm.set_query("item_code", "items", function(doc, cdt, cdn){
            var values = locals[cdt][cdn];
            return {
                query: "bhposapp.public.py.purchase_order.filt_itemby_supplier",
                filters: {
                    "supplier": frm.doc.supplier
                }
            };
       });
    }
});
