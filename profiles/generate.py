# coding: cp1252
import csv

def generate_xml(filename, names, data):
    # header
    xml_data = '<?xml version="1.0" encoding="UTF-8"?>\n\
<LEDSpicer\n\
	version="1.0"\n\
	type="Profile"\n\
	backgroundColor="Black"\n\
>\n\
	<alwaysOnElements>\n\
'
    for i in range(len(names)):
        if data[i] != '':  # skip empty fields
            xml_data += '\t\t<element name="{}" color="{}\" />\n\
'.format(names[i], data[i])
	# footer
    xml_data += '	</alwaysOnElements>\n\
</LEDSpicer>\n\
'

    xml_filename = '{}.xml'.format(filename)
    with open(xml_filename, 'w') as xml_file:
        xml_file.write(xml_data)

def create_xml_files(csv_filename):
    with open(csv_filename, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        header = next(csv_data)
        names = header[1:]  # element name starting second row

        for row in csv_data:
            filename = row[0]
            if filename != '':
                data = row[1:]  # color information starting second row
                generate_xml(filename, names, data)

# define filename csv
csv_filename = 'systems_ledspicer.csv'

create_xml_files(csv_filename)

