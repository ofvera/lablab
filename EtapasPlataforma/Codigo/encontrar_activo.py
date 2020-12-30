# coding=utf-8
encontrar_pipe = "ESNUMERO(HALLAR(\"{}\";[@Pipeline]))"
encontrar_stage = "ESNUMERO(HALLAR(\"{}\";[@Deal Stage]))"
condicion = "SI({};\"{}\";{})"

def create_options(options, encontrar):
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
"PROGRAMA TERMINADO",
"VIDEO CV GRABADO",
"FREE HUNTER ACTIVO",
"CONGELADO"]

CJ_ADM_OP = [
"EN PROGRAMA",
"TALLER FINALIZADO",
"LISTA REUNIÓN CON COORDINADORA",
"PROGRAMA TERMINADO",
"VIDEO CV GRABADO",
"FREE HUNTER ACTIVO",
"CONGELADO"]

OpEj = create_options(CJ_EJECUTIVOS, encontrar_stage)
OpPr = create_options(CJ_PROFESIONALES, encontrar_stage)
OpAd = create_options(CJ_ADM_OP, encontrar_stage)


print(OpEj)
print(OpPr)
print(OpAd)