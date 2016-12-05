def decimalbinário():
    continuar="sim"
    while ( continuar=="sim"):
        import time
        print('+-----------------------------------------+')
        print('|                                         |')                      
        print('|      CONVERSOR DE BINÁRIO               |')
        print('|                                         |')                      
        print('+-----------------------------------------+')
        print('\n' *2)
        numero=int(input('informe o numero que deseja converter para BINÁRIO:\n'))
        print('\n' *2)
        armazenador = []
        while numero > 0:
            resto=numero % 2
            resto=str(resto)
            armazenador.append(resto)
            numero=numero//2
        print('carregando:')
        print('\n'*1)
        print('▓▒▒▒▒▒▒▒▒▒▒▒ (0%)...')
        time.sleep(0.5)
        print('▓▓▒▒▒▒▒▒▒▒▒▒ (10%)...')
        time.sleep(0.4)
        print('▓▓▓▒▒▒▒▒▒▒▒▒ (20%)...')
        time.sleep(0.5)
        print('▓▓▓▓▒▒▒▒▒▒▒▒ (30%)...')
        time.sleep(0.5)
        print('▓▓▓▓▓▒▒▒▒▒▒▒ (40%)...')
        print('▓▓▓▓▓▓▒▒▒▒▒▒ (50%)...')
        print('▓▓▓▓▓▓▓▒▒▒▒▒ (60%)...')
        print('▓▓▓▓▓▓▓▓▒▒▒▒ (70%)...')
        print('▓▓▓▓▓▓▓▓▓▒▒▒ (80%)...')
        print('▓▓▓▓▓▓▓▓▓▓▒▒ (90%)...')
        time.sleep(0.5)
        print('▓▓▓▓▓▓▓▓▓▓▓▓(100%)...')

        print('\n'*2)
        print('        numero convertido com sucesso')
        print('\n'*2)
        print('          -------> ', "".join(armazenador)[::-1], ' <--------')
        print('\n'*4)

        print("para continuar digite 'sim', e para finalizar o programa, digite 'nao'")

        print('\n'*2)
        continuar=input('deseja continuar ? ----> ')
        
    print('\n'*3)
    if continuar != 'sim':
        import conversor_binário_completo
        menu()
decimalbinário()    
