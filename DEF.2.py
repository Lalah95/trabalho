def realizar_operacoes(valor1, valor2):
    resultado_soma = valor1 + valor2
    resultado_subtracao = valor1 - valor2
    resultado_multiplicacao = valor1 * valor2

     # Divisão
    if valor2 != 0:
      divisao = valor1 / valor2
    else:
      divisao = None
      if valor1 == 0:
        divisao = "indefinido"
      elif valor1 > 0:
        divisao = "infinito positivo"
      else:
        divisao = "infinito negativo"


    return [resultado_soma, resultado_subtracao, resultado_multiplicacao, divisao]

# Exemplo de uso
#valor1 = float(input("Digite o primeiro valor: "))
#valor2 = float(input("Digite o segundo valor: "))

#resultados = realizar_operacoes(valor1, valor2)
#print("Resultados:", resultados)

def relatorio_de_erros():
  errors = []
  lista_aux=[]
  lista_aux=realizar_operacoes(2,2)
  if not lista_aux[0]==4:
    errors.append("Erro: Função realizar_operacoes somou incorretamente dois valores positivos")
  if not lista_aux[1]==0:
    errors.append("Erro: Função realizar_operacoes subtraiu incorretamente dois valores positivos")
  if not lista_aux[2]==4:
    errors.append("Erro: Função realizar_operacoes multiplicou incorretamente dois valores positivos")
  if not lista_aux[3]==1:
    errors.append("Erro: Função realizar_operacoes dividiu incorretamente dois valores positivos")
  lista_aux=realizar_operacoes(2,0)
  if not lista_aux[3]=="infinito positivo":
    errors.append("Erro: Função realizar_operacoes dividiu incorretamente um valor positivo por zero")
  lista_aux=realizar_operacoes(-2,0)
  if not lista_aux[3]=="infinito negativo":
    errors.append("Erro: Função realizar_operacoes dividiu incorretamente um valor negativo por zero")
  lista_aux=realizar_operacoes(0,0)
  if not lista_aux[3]=="indefinido":
    errors.append("Erro: Função realizar_operacoes dividiu incorretamente um valor zero por zero")
  # assert no error message has been registered, else print messages
  assert not errors, "errors occured:\n{}".format("\n".join(errors))


relatorio_de_erros()
print("Success, test ran 100% without errors")
