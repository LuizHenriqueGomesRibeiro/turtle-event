import turtle

tela = turtle.Screen()
tela.title("Planejador de Eventos")
tela.bgcolor("white")

caneta = turtle.Turtle()
caneta.hideturtle()
caneta.penup()

caneta.goto(-150, 200)
caneta.write("PLANEJADOR DE EVENTOS", font=("Arial", 16, "bold"))

tipo_evento = tela.textinput("Entrada", "Qual o tipo do evento? (ex: Churrasco, Festa, Jantar)")
num_convidados = int(tela.numinput("Entrada", "Quantos convidados?", minval=1))
duracao_horas = int(tela.numinput("Entrada", "Duração do evento (em horas)?", minval=1))

carne_total = num_convidados * 0.4
bebida_total = num_convidados * 0.5 * duracao_horas
acompanhamento_total = num_convidados * 0.2

caneta.goto(-150, 100)
caneta.write(f"Evento: {tipo_evento}", font=("Arial", 12, "normal"))

caneta.goto(-150, 70)
caneta.write(f"Para {num_convidados} pessoas durante {duracao_horas}h, sugerimos:", font=("Arial", 12, "italic"))

caneta.goto(-150, 30)
caneta.write(f"1. Carne/Principal: {carne_total:.1f} kg", font=("Arial", 12, "bold"))

caneta.goto(-150, 0)
caneta.write(f"2. Bebidas: {bebida_total:.1f} litros", font=("Arial", 12, "bold"))

caneta.goto(-150, -30)
caneta.write(f"3. Acompanhamentos: {acompanhamento_total:.1f} kg", font=("Arial", 12, "bold"))

caneta.goto(-150, -100)
caneta.write("Planejamento concluído com sucesso!", font=("Arial", 10, "normal"))

print("Planejamento de Evento Finalizado!")
print(f"Tipo: {tipo_evento} | Convidados: {num_convidados} | Duração: {duracao_horas}h")
print(f"Sugestões: {carne_total:.1f}kg carne, {bebida_total:.1f}L bebidas, {acompanhamento_total:.1f}kg acompanhamentos")

tela.mainloop()