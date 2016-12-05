print('''
+-------------------------------+
|Sorteio De Frases Engraçadas   |
|       E Aleatórias            |       
+-------------------------------+

''')
import random
nome = input('informe os nomes\n').split(' ')
nome = random.choice(list(nome))
print('\n')
lugar= input('informe os lugares\n').split(' ')
lugar = random.choice(list(lugar))
print('\n')
fazendo= input('informe o que estava fazendo\n  ').split(' ')
fazendo = random.choice(list(fazendo))
print('\n')
com_quem= input('com quem:\n').split(' ')
com_quem = random.choice(list(com_quem))
print('\n')
print('\n'*2)
print(nome,'estava no',lugar,fazendo,'com',com_quem, )
