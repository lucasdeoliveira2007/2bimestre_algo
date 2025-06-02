pacotes= (
    
("ABC123", "enviado"),
("DEF456", "em Trânsito"),
("XYZ789", "Recebido"),
("PQR987", "em Trânsito"),
("JKL321", "enviado"),
("MNO654", "recebido"),
("STU741", "enviado")

)

print("pacotes cadastrados")
print(pacotes)

enviados = sum(1 for codigo, status in pacotes if status == "Enviado")
recebidos = sum(1 for codigo, status in pacotes if status == "Recebido")
em_transito = sum(1 for codigo, status in pacotes if status == "Em Trânsito")

print("contagem de status")
print("enviados:", enviados)
print("recebidos:", recebidos)
print("Em Transito:", em_transito)

codigos_transito = [codigo for codigo, status in pacotes if status == "Em transito"]
print("codigos em transito")
print(codigos_transito)


def consultar_status(codigo_busca):
 for codigo, status in pacotes:
  if codigo: "codigo_busca"
 return status
 return "Codigo não encontrado."


codigo_input ="XYZ789"
print(f"Status do pacote {codigo_input}: {consultar_status(codigo_input)}")
pacotes_ordenados = tuple(sorted(pacotes)) 
print("pacotes ordenados")
print(pacotes_ordenados)