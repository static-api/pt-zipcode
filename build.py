import csv
import json
import os
 
output = 'build'
source = 'data/todos_cp.txt'

try:
    os.mkdir(output)
except:
    pass

# original field names from leiame.txt
fieldnames = ('DD', 'CC', 'LLLL', 'LOCALIDADE', 'ART_COD', 'ART_TIPO', 'PRI_PREP', 'ART_TITULO', 'SEG_PREP', 'ART_DESIG', 'ART_LOCAL', 'TROÇO', 'PORTA', 'CLIENTE', 'CP4', 'CP3', 'CPALF')

with open(source, encoding='latin-1') as dataset:
    csv_reader = csv.DictReader(dataset, fieldnames, delimiter=';')

    for row in csv_reader:
        zip = f'{row["CP4"]}-{row["CP3"]}'
        with open(f'{output}/{zip}.json', 'w', encoding='utf-8') as out:
            out.write(json.dumps(row, ensure_ascii=False))

# TODO the same XXXX-XXX has more than 1 result
# TODO lookup district and region
# TODO join address
# TODO cleanup end result
