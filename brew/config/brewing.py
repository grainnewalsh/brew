from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Production Activity"),
			"items": [

                                {
                                        "type": "doctype",
                                        "name": "Recipe"
                                },

				{
					"type": "doctype",
					"name": "Production Brew"
				},
				{
					"type": "doctype",
					"name": "Packaging Run"
				}
			]
		},
	]


