PATH = "industrias.csv"

encontrar = "ESNUMERO(HALLAR(\"{}\";[@Oferta]))"

condicion = "SI({};\"{}\";{})"

def print_option(options):
  print(", ".join(options).encode('utf-8'))

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

def search_options(begin, options, names):
  eq = ""
  if begin:
    eq = "="
  if len(options) > 1:
    return eq + condicion.format(options[0], names[0], search_options(False, options[1:], names[1:]))
  if len(options) == 1:
    return eq + condicion.format(options[0], names[0], "\"otro\"")

def crear_keywords(path):
  with open(path, "r", encoding='utf-8') as file1:
    industrias = {}
    first = True
    for line in file1:
      if first:
        first = False
        line = line[1:]
      line = line.strip("\n").split(";")
      print(line[0].encode('utf-8'))
      if line[1] in industrias:
        industrias[line[1]].append(line[0])
      else:
        industrias[line[1]] = [line[0]]
  options = []
  names = []
  for category in industrias:
    names.append(category)
    options.append(industrias[category])
  return options, names

options, names = crear_keywords(PATH)
#print(names)
#print(options)
search = search_options(True, options, names)
print(search.encode('utf-8'))
