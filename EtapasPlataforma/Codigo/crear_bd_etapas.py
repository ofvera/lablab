# Codigo para crear la base de datos del historial de etapas de negocio desde hubspot
FECHA = '2020-12-24'

EXTRACT_PATH = 'hubspot_csvs/'
IN_PATH = 'etapa-del-negocio-2020-12-24.csv'
OUT_PATH = 'historial_etapas.csv'

CJ_EJECUTIVOS = [
"OUTPLACEMENT TERMINADO",
"EN BÚSQUEDA",
"PROCESO ACTIVO",
"CONGELADO",
"NO REALIZA ASESORÍAS",
"NEGOCIANDO ASESORÍA",
"EN ASESORIA",
"ASESORÍA TERMINADA",
"FRANQUICIAS O INDEPENDIENTES"]

CJ_PROFESIONALES = [
"EN PROGRAMA",
"TALLER FINALIZADO",
"LISTA REUNIÓN CON COORDINADORA",
"PROCESO ACTIVO",
"PROGRAMA TERMINADO", # en busqueda
"VIDEO CV GRABADO", # en busqueda
"FREE HUNTER ACTIVO", # en busqueda
"CONGELADO"]

CJ_ADM_OP = [
"EN PROGRAMA",
"TALLER FINALIZADO",
"LISTA REUNIÓN CON COORDINADORA",
"PROCESO ACTIVO",
"EMPLEO TRANSITORIO",
"PROGRAMA TERMINADO",# en buslsqueda
"VIDEO GRABADO",# en busqueda
"FREE HUNTER ACTIVO",# en busqueda
"CONGELADO"]

CJ_ONLINE = [
  "ENTRÓ AL PROGRAMA",
  "TALLER FINALIZADO",
  "VIDEO CV GRABADO",
  "FREE HUNTER ACTIVO"
]

CJ_ONLINE_PRO = [
  "ENTRÓ AL PROGRAMA",
  "TALLER FINALIZADO",
  "LISTA REUNIÓN CON COORDINADORA",
  "VIDEO CV GRABADO",
  "FREE HUNTER ACTIVO"
]

activeStages = {'CJ Ejecutivos': CJ_EJECUTIVOS, 'CJ Profesionales': CJ_PROFESIONALES, 
                'CJ Adm/Op.': CJ_ADM_OP, 'CJ Online': CJ_ONLINE, 'CJ Online Pro': CJ_ONLINE_PRO}


historic_stages = {}
with open(EXTRACT_PATH + IN_PATH, 'r', encoding='utf-8') as Input:
  with open(OUT_PATH, 'w', encoding='utf-8') as Output:
    header = Input.readline()
    headers = header.strip('\n').split(';')
    Output.write(';'.join(headers[:4])+'\n')
    for line in Input:
      content = line.strip('\n').split(';')
      dealId = content[0]
      dealName = content[1]
      historic_stages[(dealId, dealName)] = []
      for pair in [(i,j) for i,j in zip(content[2::2], content[3::2])]:
        if pair == ('',''):
          break
        else:
          Output.write('{};{};{};{}\n'.format(dealId, dealName, pair[0], pair[1]))
          historic_stages[(dealId, dealName)].append(pair)


IN_PATH = 'etapas-activas-pipeline-cj-2020-12-24.csv'
OUT_PATH = 'historial_etapas_usuario.csv'


with open(EXTRACT_PATH + IN_PATH, 'r', encoding='utf-8') as Input:
  with open(OUT_PATH, 'w', encoding='utf-8') as Output:
    header = Input.readline()
    headers = header.strip('\n').split(';')
    Output.write('Contact ID;' + ';'.join(headers[1:7]) + ';{};Deal Stage;Change Date;Active;Order\n'.format(headers[8]))
    # ['\ufeffContact ID', 'Deal ID', 'Deal Name', 'First Name', 'Last Name', 'RUT', 'Ultima empresa', 'Deal Stage', 'Pipeline']
    for line in Input:
      first_item = True
      item = 0
      content = line.strip('\n').split(';')
      contactId = content[0]
      dealId = content[1]
      dealName = content[2]
      firstName = content[3]
      lastName = content[4]
      RUT = content[5]
      last_company = content[6]
      pipeline = content[8]
      if (dealId, dealName) in historic_stages:
        for stages in historic_stages[(dealId, dealName)]:
          (stage, date) = stages
          is_active = 'NO'
          is_latest = 'SI' if first_item else 'NO'
          first_item = False
          item += 1
          if pipeline in activeStages:
            is_active = 'SI' if stage.upper() in activeStages[pipeline] else 'NO'
          Output.write(';'.join(content[:7]) +';{};{};{};{};{}\n'.format(content[8], stage, date, is_active, item))
      else:
        print("[Could not find Deal {}]: {}".format(dealId, dealName))