from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Production Activity"),
			"items": [

                                {
                                        "type": "doctype",
                                        "name": "Recipe",
					"label": "All Recipes"
                                },

				{
					"type": "doctype",
					"name": "Production Brew",
					"label": "Beer Batches"
				},
				{
					"type": "doctype",
					"name": "Packaging Run",
					"label": "Packaging Batch Info"
				}
			]
		},
	{
			"label": _("Stock"),
			"items": [

                                {
                                        "type": "report",
					"is_query_report": True,
					"doctype": "Item",
                                        "name": "Beer Stock",
					"label": "Current Beer in Stock"
                                },

				{
					"type": "doctype",
					"name": "Delivery Note",
					"label": "Delivery Docket"
				}
			]
		},

	]


