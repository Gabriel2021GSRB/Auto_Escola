idade = 0
cnh = 'abilitacao'
exame1 = 'vista'
exame2 = 'psicotecnico'
aula1 = 'teorica'
prova1 = 'escrita'
aula2 = 'pratica'
prova2 = 'exame_prtico'
print("*********************************************************************")
print("Digite somente sim, não ou reprovei para a perguntas sobre a abilitação.")
input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
if idade >= 18:
    print("Você é maior e sua idade esta ok!!!")
else: 
    print("Você ainda é menor de idade e não pode ter CNH!!!")
cnh = str(input("Você deseja tirar sua carteira de habilitação?"))
if cnh == 'sim':
    print("Vamos verificar os exames.")
else:
    print("O que voce deseja?")
exame1 = str(input("Você ja fez o exame de vista?"))
if exame1 == 'sim':
    print("Vamos para o proximo exame.")
else:
    print("Você precisa fazer o exame de vista primeiro.")    
exame2 = str(input("Você ja fez o exame psicotécnico:"))
if exame2 == 'sim':
    print("Vou te encaminhar para o cursinho teorico.")
else:
    print("Vou te passar o enderoço para você ir fazer seu exame psicotequinico.")     
aula1 = str(input("Você ja fez o cursinho teorico?"))
if aula1 == 'sim':
    print("OK. sua prova teorica é segunda feira as 7:00 no detran.")
else:
    print("Suas aulas começa nesta segunda feira as 18:00.")
prova1 = str(input("Você ja fez a prova teorica?"))
if prova1 == 'sim':
    print("PARABENS. Escolha um dos nossos Instrutores para fazer as aulas praticas. ")  
elif prova1 == 'reprovei':
    print("Vou marca uma outra prova. Estude um pouco mais.")
else:
    print("Você preciza fazer a prova teorica ainda.")  
aula2 = str(input("Você ja fez as aulas praticas?"))
if aula2 == 'sim':
    print("A prova sera na segunda feira que vem, tome cuidado para não reprovar.")    
else:
    print("Você precisa concluir as aulas pratica ainda.")
prova2 = str(input("Você ja fez a prova pratica?"))
if prova2 == 'sim':
    print("Sua CNH chega em duas semanas.")
elif prova2 == 'reprovei':
    print("Vou reagendar uma segunda tentativa.")
else:
    print("Voce precisa fazer sua prova pratica ainda.")

print("Obrigado pela preferencia.")
print("********************************************************************")




    