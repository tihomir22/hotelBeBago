#!/bin/bash

echo "<?xml version="1.0" encoding="utf-8"?>
<odoo>
	<data>"
i=2;

	while [ $i -gt 0 ] ; do
		echo "
		<record model="hotels_be_bago.hotel" id="hotel1">
			<field name="name">Hotel Number 9</field>
			<field name="description">Extra dip.</field>
			<!-- para Many2One-->
			<field name="ciudad" ref="hotels_be_bago.ciudad1"></field>
			<!-- para Many2Many -->

          <field name="listaServicios" eval="[(6,0,[ref('hotels_be_bago.servici1'),ref('hotels_be_bago.servici2')] )]" />

			<field name="valoraciones">5</field>
			 <field name="listaServicios" eval="[(6,0,[ref('hotels_be_bago.servici1'),ref('hotels_be_bago.servici2')] )]" />
		</record>
		";

	i=$(( $i - 1 ))
	done
echo "
		</record>
	</data>
</odoo>"
