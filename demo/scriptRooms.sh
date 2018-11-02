#!/bin/bash

echo '<?xml version="1.0" encoding="utf-8"?>
<odoo>
	<data>'
i=0;
arrayString=("desagradable" "majestuosa" "primordial" "agradable" "fabulosa" "denigrante" "marginal")

	while [ $i -lt 400 ] ; do
	random=$((( RANDOM % 4 ) + 1 ))
	random2=$((( RANDOM % 5 ) + 1 ))
	random3=$((( RANDOM % 1000) + 20 ))	
	random4=$((( RANDOM % 6 ) + 0 ))
	random5=$((( RANDOM % 5 ) + 1 ))
		echo '
		<record model="hotels_be_bago.habitacion" id="habitacion'$i'">
			<field name="hotel" ref="hotels_be_bago.hotel'$random'"></field>
			<field name="name">Habitacion Number '$i'</field>
			<field name="camas">'$random2'</field>
			<field name="precios">'$random3'</field>
			<field name="descripcion">Una '${arrayString[$random4]}' habitación presidencial. Perfecta para descansar y hacer todo tipo de travesuras.</field>
<field name="fotos" eval="[(6,0,[ref('"'hotels_be_bago.roomfoto$random5'"')] )]" />
			
		</record>
		'

	i=$(( $i + 1 ))
	done
echo '
		
	</data>
</odoo>'
