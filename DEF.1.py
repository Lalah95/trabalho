def calcular_conceito(nota1, nota2, nota3):
    if (nota1 >=0 and nota1 <= 100) and (nota2 >=0 and nota2 <= 100) and (nota3 >=0 and nota3 <= 100) :
      media = (nota1 + nota2 + nota3) / 3
      if media <= 50:
        return "D"
      elif media <= 70:
        return "C"
      elif media <= 90:
        return "B"
      elif media == 100:
        return "A"
    else:
      return "NULO"
      

# Exemplo de uso
#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#nota3 = float(input("Digite a terceira nota: "))

#conceito = calcular_conceito(nota1, nota2, nota3)
#print("Conceito: ", conceito)


def relatorio_de_erros():
  errors = []

  if not calcular_conceito(50, 50, 50) == "D":
    errors.append("Erro: Está nota não e equivalente ao valor D")
  if not calcular_conceito(70, 70, 70) == "C":
    errors.append("Erro: Está nota não e equivalente ao valor C")
  if not calcular_conceito(90, 90, 90) == "B":
    errors.append("Erro: Está nota não e equivalente ao valor B")
  if not calcular_conceito(100, 100, 100) == "A":
    errors.append("Erro: Está nota não e equivalente ao valor A")
  if not calcular_conceito(0, 0, 0) == "D":
    errors.append("Erro: Está nota não e equivalente ao valor D")
  if not calcular_conceito(-1, 0, 0) == "NULO":
    errors.append("Erro: Está nota não e equivalente pois é negativa")
  if not calcular_conceito(0, -1, 0) == "NULO":
    errors.append("Erro: Está nota não e equivalente pois é negativa")
  if not calcular_conceito(0, 0, -1) == "NULO":
    errors.append("Erro: Está nota não e equivalente pois é negativa")
  if not calcular_conceito(110,30,90) == "NULO":
    errors.append("Erro: Está nota não e equivalente pois é maior que 100")
  if not calcular_conceito(50, 40, 110) == "NULO":
    errors.append("Erro: Está nota não e equivalente pois é negativa")
  if not calcular_conceito(50, 110, 30) == "NULO":
    errors.append("Erro: Está nota não e equivalente pois é negativa")
  # assert no error message has been registered, else print messages
  assert not errors, "errors occured:\n{}".format("\n".join(errors))


relatorio_de_erros()
print("Success, test ran 100% without errors")