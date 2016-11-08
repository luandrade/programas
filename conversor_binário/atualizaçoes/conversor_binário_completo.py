def menu():
    print('+-----------------------------------------+')
    print('|   ESCOLHA UMA DAS OPÇÕES:               |')
    print('|     a)DECIMAL ----->BINÁRIO             |')
    print('|     b)BINÁRIO ---> DECIMAL              |')
    print('+-----------------------------------------+')
    print('\n'*1)
    opção = input('informe a opção desejada -->')
    print('\n'*1)
    if opção=='a':
        import decimalbinario
        decimalbinario.decimalbinario()
    
  
    elif opção=='b':
        import binariodecimal
        binariodecimal.bináriodecimal()
        

menu()
