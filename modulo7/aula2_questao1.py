meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
data=input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia,mes,ano=data.split('/')
mes_index=int(mes)-1
print("{} de {} de {}".format(dia, meses[mes_index], ano))