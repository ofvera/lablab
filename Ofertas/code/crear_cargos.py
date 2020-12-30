# coding=utf-8
encontrar = "ESNUMERO(HALLAR(\"{}\";[@Oferta]))"

condicion = "SI({};{};{})"

def create_options(options):
  l = len(options)
  string = "O("
  counter = 0
  for i in options:
    counter += 1
    if l == counter:
      string += "{})".format(encontrar.format(i))
    else:
      string += "{};".format(encontrar.format(i))
  return string

gerente_options = ["Gerente", "Subgerente", "Superintendente", "Vicepresidente", "Gerencia", "Director"]

o1 = create_options(gerente_options)


jefatura_options = ["Jefe", "Jefatura", "Jefa", "Manager", "Supervisor",
  "Coordinador", "Ingeniero", "Ingeniera", "programador", "abogado", "engineer",
  "enfermera", "arquitecto", "matrona", "medico", "soporte TI", "contador", "devops",
  "enfermeria", "constructor civil", "arquitectura", "psiquiatra", "ing comercial",
  "consultor SAP", "developer", "enfermero", "data scientist", "auditor", "psicologo",
  "consultor BI", "informatica", "agile coach", "profesional", "business analyst",
  "contabilidad", "lider de proyecto", "nutricionista", "prevencionista", "informático"
  "kinesiólogo", "médico", "farmacéutico", "diseñador", "enfermería", "geólogo",
  "Psicólogo", "psicóloga", "psicología","ingeniería", "educadora de párvulo", "agrónomo",
  "Soporte Informático", "Laboratorista", "Asesor Comercial", "Previsión de riesgo", 
  "Profesor", "Veterinario", "Terapeuta Ocupacional", "analista", "consultor", "planner",
  "fonoaudiólogo", "chef", "topografo", "rector", "informático", "traumatólogo", "encargado de rrhh",
  "encargado de recursos humano", "periodista", "product owner", "kinesiólogo", "scrum master",
  "analyst", "automatizador", "consultant", "architect", "agronomo", "dentista", "specialist",
  "head", "kam", "tecnólogo", "tecnóloga", "PM", "Docente", "Quimico Farmaceutico", "Reclutador",
  "Relator","Psicooncólogo", "Cocinero", "Encargado Selección", "Data Analytics", 
  "Líder de proyectos", "Líder de ventas", "Dibujante", "Animador digital", "Decorador", 
  "Pastelero", "Proyectista", "Procurador", "Economista", "Prof", "Académico", "Generalista", 
  "Project Management", "Comprador", "Senior", "Procuradores", "Psicopedagoga", "Sociologo", 
  "Engineer", "Kinesióloga", "Fonoaudióloga", "Químico Farmaceútico", "Kinesiologa", "Ing.", 
  "Technologist", "Psicologia", "Kinesiologo", "Topógrafo"] 

o2 = create_options(jefatura_options)

admin_operativo_options = ["asistente", "secretaria", "ejecutivo",
  "ejecutiva", "operaria", "vendedor", "auxiliar", "operador", "operario",
  "desarrollador", "administrativo", "administrador", "guardia", "bodeguero",
  "cajero", "conductor", "aseador", "sushero", "chofer", "recepcionista",
  "promotor", "mecanico", "conserje", "barista", "soldador", "instructor",
  "maquinista", "secretario", "secretaria", "bartender", "reponedor", "carrocero",
  "gasfiter", "garzon", "jardinero", "pizzero", "captador de tarjetas", "digitador",
  "inspector", "cajera", "tecnico", "capataz", "anfitrion", "ayudante de bodega",
  "telefonista",  "call center", "maestro", "maquillador", "bombero", "repartidor",
  "ayudante de bodega", "Vulcanizador", "administrativa", "Oxicortista", "Pintor",
  "cosmetóloga", "mecánico", "técnico", "anfitrión", "Ayudante de Cocina",
  "Junior de tienda", "Vigilante privado", "Garzón", "electricista", "TENS", 
  "portero", "Encargado de sala", "portero", "albañil", "ayudante", "mayordomo", 
  "guardia", "jornal", "nochero", "peoneta", "pañol", "empalmador", "mucama", 
  "costurera", "despachador", "tornero", "peluquero", "peluquera", "manipulador",
  "cuidador", "obrero", "carpintero", "Botones", "Vigilante", "Revisador", "Mensajero", 
  "Práctica", "Asesor de seguros", "Asesor de inversiones", "Agendador", "Captadores", 
  "Asesores de seguros", "Encargado de tienda", "Movilizador", "Captador", "Personal de apoyo", 
  "Empaque", "Cobradror", "Chófer", "Copero", "Apiladores", "Horneador", "Imprentero", "Asignador", 
  "Apiladores", "Estafeta", "Agente Sucursal", "Facilitador", "Clasificador", "Guardabosque", 
  "Representante", "Apoyo", "Encargado bodega", "Podologa", "Manicurista", "Perforista", 
  "Agente de ventas", "Encargado de patio", "Encargado de perecibles", "Practica", "Transportista", 
  "Archivero", "Gruero", "Encargado de soldadura", "Administrativos", "Reponerdor", "Grua", 
  "Asesora de hogar", "Personal para supermercado", "Podador", "Monitor", "Tuberos", "Yesero", 
  "Junior", "Calderero", "Personal aseo", "Motorista", "Atención de mesón", "Aseo", "Estilista", 
  "Masajista", "Meson", "Gásfiters", "Operator", "Mantenedor"]


o3 = create_options(admin_operativo_options)

gerente = "=" + condicion.format(o1,"1","0")
jefatura = "=" + condicion.format(o2,"1","0")
admin = "=" + condicion.format(o3,"1","0")
print("==== CARGOS ===")
print(gerente)
print("==== CARGOS ===")
print(jefatura)
print("==== CARGOS ===")
print(admin)

search = "=" + condicion.format(o1, "Gerencial", condicion.format(o2, "Profesional y/o Jefatura",condicion.format(o3, "Administrativo y/o Operativo","\"Otro\"")))


#print("==== CARGOS ===")
#print(search)

def print_option(options):
  print(", ".join(options))

#print_option(gerente_options)
#print_option(jefatura_options)
#print_option(admin_operativo_options)
#lugares = ["Santiago",	"Rancagua",	"Antofagasta",	"Copiapo",	"Calama",
#  "Metropolitana",	"Iquique",	"Temuco",	"San Felipe",	"Coquimbo"	,"Valparaiso",
#  "Linares",	"Aysen",	"Magallanes",	"La Serena"]

lugar_search = "SI(ESNUMERO(HALLAR(\"Santiago\";[@Lugar]));\"Santiago\";SI(ESNUMERO(HALLAR(\"Rancagua\";[@Lugar]));\"Rancagua\";SI(ESNUMERO(HALLAR(\"Antofagasta\";[@Lugar]));\"Antofagasta\";SI(ESNUMERO(HALLAR(\"Copiapo\";[@Lugar]));\"Copiapo\";SI(ESNUMERO(HALLAR(\"Calama\";[@Lugar]));\"Calama\";SI(ESNUMERO(HALLAR(\"Metropolitana\";[@Lugar]));\"Metropolitana\";SI(ESNUMERO(HALLAR(\"Iquique\";[@Lugar]));\"Iquique\";SI(ESNUMERO(HALLAR(\"Temuco\";[@Lugar]));\"Temuco\";SI(ESNUMERO(HALLAR(\"San Felipe\";[@Lugar]));\"San Felipe\";SI(ESNUMERO(HALLAR(\"Coquimbo\";[@Lugar]));\"Coquimbo\";SI(ESNUMERO(HALLAR(\"Valparaiso\";[@Lugar]));\"Valparaiso\";SI(ESNUMERO(HALLAR(\"Linares\";[@Lugar]));\"Linares\";SI(ESNUMERO(HALLAR(\"Aysen\";[@Lugar]));\"Aysen\";SI(ESNUMERO(HALLAR(\"Magallanes\";[@Lugar]));\"Magallanes\";SI(ESNUMERO(HALLAR(\"La Serena\";[@Lugar]));\"La Serena\";\"Otro\")"

print("=== LUGARES ===")
print(lugar_search)
