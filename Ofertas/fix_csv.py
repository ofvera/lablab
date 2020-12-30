
FOLDER = "csvs/"
INPUT = "extraccionOfertas2.csv"
OUTPUT = "fixedExtraccionOfertas.csv"

with open(FOLDER + INPUT, "r", encoding='utf-8') as ErrorFile:
  headers = ErrorFile.readline().strip('\n').split(';')
  columns = len(headers)
  with open(FOLDER + OUTPUT, "w", encoding='utf-8') as FixedFile:
    last_line = ""
    FixedFile.write(';'.join(headers) + '\n')
    is_complete = False
    for line in ErrorFile:
      splitLine = line.strip('\n').split(';')
      #if len(splitLine) > 8:
      # existen ; en su interior
      fixedLine = ";".join(splitLine)
      if len(splitLine) < 10:
        # Pertenece a la linea anterior
        last_line += fixedLine
        #print(last_line.encode('utf-8'))
        is_complete = False
      else:
        #if len(splitLine) == 9:
        #  print("--------------")
        #  print(fixedLine.encode('utf-8'))
        #  # existe un ; en el campo de title
        #  index1 = fixedLine.find(';')
        #  index2 = fixedLine[index1+1:].find(';') + index1 + 1
        #  index3 = fixedLine[index2+1:].find(';') + index2 + 1
        #  index4 = fixedLine[index3+1:].find(';') + index3 + 1
        #  totalIndex = index4
        #  print(totalIndex)
        #  fixedLine = fixedLine[:totalIndex] + fixedLine[totalIndex + 1:]
        #  print(fixedLine.encode('utf-8'))
        if last_line != "":
          # es una nueva linea por lo que escribimos la anterior y decimos que es la nueva ultima linea
          FixedFile.write(last_line + '\n')
        last_line = fixedLine
        is_complete = True
    if not is_complete:
      FixedFile.write(last_line + '\n')
