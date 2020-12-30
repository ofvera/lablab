with open("ofertas_marzo_filtro.csv", "r", encoding="utf-8") as ofertas:
  counter = 0
  for oferta in ofertas:
    offer_data = oferta.strip("\n").split(";")
    counter += 1
    if offer_data[-1] == "SI" or offer_data[-1] == "NO":
      print(offer_data[-1])
    if counter == 10:
      break