encontrar = "ESNUMERO(HALLAR(\"{}\";[@Industria]))"

condicion = "SI({};\"{}\";{})"

o2 = "O({};{})"
o3 = "O({};{};{})"
o4 = "O({};{};{};{})"
o5 = "O({};{};{};{};{})"
o6 = "O({};{};{};{};{};{})"
o7 = "O({};{};{};{};{};{};{})"
o8 = "O({};{};{};{};{};{};{};{})"
o9 = "O({};{};{};{};{};{};{};{};{})"
o10 = "O({};{};{};{};{};{};{};{};{};{})"

alimento = ["Bebida", "Vino", "Licor", 
            "Restaurante", "Supermercado", "Alimentaria", 
            "Alimenticia", "Alimentos", "Alimentación"]
retail = ["Articulos", "Grandes Tiendas", "Textil", 
          "Moda", "Retail", "Venta al Por Mayor", 
          "Vidrios"]
financiera = ["Banca", "Financiera", "Inversiones", 
            "Finanzas", "Financiero"]
agricultura = ["Agrícola", "Agricultura", "Agua", 
              "Acuícola", "Pesquera", "Pesquero", 
              "Pesca", "Salmonera", "Agro"]
transporte = ["Abastecimiento", "Logística", "Aduana", 
              "Comercio Exterior", "Suministros", "Distribución", 
              "Distribuidora", "Transporte", "Carretera", 
              "Ferrocarril"]
salud = ["Medicina", "Salud", "Sanitaria", 
          "Sanitario", "Hospitalaria", "Hospitalario", 
          "Enfermería", "Isapre", "Farmacia", 
          "Farmacéutica"]
construccion = ["Arquitectura", "Construcción", "Urbanismo", 
                "Inmobiliario", "Inmobiliaria", "Propiedades", 
                "Ingeniería Civil"]
mineria = ["Minería", "Metales", "Metalurgia", 
          "Metalmécanica", "Siderurgía"]
gas_petroleo = ["Combustibles", "Gas", "Petroleo", 
          "Petróleo", "Energía", "Energético"]
telecomunicaciones = ["Telecomunicaciones", "Medios de Comunicación", "Inalámbrica"]
forestal = ["Forestal", "Papel"]
software = ["Programación", "Desarrollo Mobile", "E-learning", 
            "Informática", "Informático", "Gestión de la Información", 
            " Software", "Tecnologías de la Información", "TI"]


search = "=" + condicion.format( o9.format(
  encontrar.format(alimento[0]),
  encontrar.format(alimento[1]),
  encontrar.format(alimento[2]),
  encontrar.format(alimento[3]),
  encontrar.format(alimento[4]),
  encontrar.format(alimento[5]),
  encontrar.format(alimento[6]),
  encontrar.format(alimento[7]),
  encontrar.format(alimento[8]),
), "Alimentos y Gastronomía", condicion.format( o7.format(
  encontrar.format(retail[0]),
  encontrar.format(retail[1]),
  encontrar.format(retail[2]),
  encontrar.format(retail[3]),
  encontrar.format(retail[4]),
  encontrar.format(retail[5]),
  encontrar.format(retail[6]),
), "Retail y Venta Minorista", condicion.format( o5.format(
  encontrar.format(financiera[0]),
  encontrar.format(financiera[1]),
  encontrar.format(financiera[2]),
  encontrar.format(financiera[3]),
  encontrar.format(financiera[4])
), "Banca y Financiera", condicion.format( o9.format(
  encontrar.format(agricultura[0]),
  encontrar.format(agricultura[1]),
  encontrar.format(agricultura[2]),
  encontrar.format(agricultura[3]),
  encontrar.format(agricultura[4]),
  encontrar.format(agricultura[5]),
  encontrar.format(agricultura[6]),
  encontrar.format(agricultura[7]),
  encontrar.format(agricultura[8])
), "Agricultura/Agropecuaria y Acuícola", condicion.format( o10.format(
  encontrar.format(transporte[0]),
  encontrar.format(transporte[1]),
  encontrar.format(transporte[2]),
  encontrar.format(transporte[3]),
  encontrar.format(transporte[4]),
  encontrar.format(transporte[5]),
  encontrar.format(transporte[6]),
  encontrar.format(transporte[7]),
  encontrar.format(transporte[8]),
  encontrar.format(transporte[9])
), "Transporte y Logística", condicion.format( o10.format(
  encontrar.format(salud[0]),
  encontrar.format(salud[1]),
  encontrar.format(salud[2]),
  encontrar.format(salud[3]),
  encontrar.format(salud[4]),
  encontrar.format(salud[5]),
  encontrar.format(salud[6]),
  encontrar.format(salud[7]),
  encontrar.format(salud[8]),
  encontrar.format(salud[9])
), "Salud", condicion.format( o7.format(
  encontrar.format(construccion[0]),
  encontrar.format(construccion[1]),
  encontrar.format(construccion[2]),
  encontrar.format(construccion[3]),
  encontrar.format(construccion[4]),
  encontrar.format(construccion[5]),
  encontrar.format(construccion[6])
), "Construcción e Inmobiliaria", condicion.format( o5.format(
  encontrar.format(mineria[0]),
  encontrar.format(mineria[1]),
  encontrar.format(mineria[2]),
  encontrar.format(mineria[3]),
  encontrar.format(mineria[4])
), "Minería y Metalurgia", condicion.format( o6.format(
  encontrar.format(gas_petroleo[0]),
  encontrar.format(gas_petroleo[1]),
  encontrar.format(gas_petroleo[2]),
  encontrar.format(gas_petroleo[3]),
  encontrar.format(gas_petroleo[4]),
  encontrar.format(gas_petroleo[5])
), "Gas, Petroleo y Energía", condicion.format( o3.format(
  encontrar.format(telecomunicaciones[0]),
  encontrar.format(telecomunicaciones[1]),
  encontrar.format(telecomunicaciones[2])
), "Telecomunicaciones", condicion.format( o2.format(
  encontrar.format(forestal[0]),
  encontrar.format(forestal[1])
), "Forestal y Papelera", condicion.format( o9.format(
  encontrar.format(software[0]),
  encontrar.format(software[1]),
  encontrar.format(software[2]),
  encontrar.format(software[3]),
  encontrar.format(software[4]),
  encontrar.format(software[5]),
  encontrar.format(software[6]),
  encontrar.format(software[7]),
  encontrar.format(software[8])
), "Software y TI", "Otro")))))))))))

print(search.encode('iso-8859-1').decode('utf-8'))