import time
def decimalbinario():
        continuar='sim'
        while (continuar=='sim'):
                print('+------------------------------+')
                print('| CONVERTER BINÁRIO EM DECIMAL |')
                print('+------------------------------+')
                print('\n'*1)      
                binario = input('Informe o Numero Binario--> ')
                binario = str(binario[::-1])
                contador=0
                somador=0
                for c in str(binario):
                        multiplicador=2**contador
                        contador = contador+1
                        if c != '0':
                                somador=multiplicador+somador
                print('\n'*1)                    
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
                print('\n'*1)		
                print("Numero Convertido Com Sucesso")
                print('\n'*1)
                print('---------->', somador, '<-------------')
                continuar=input("deseja continuar ? \n")
                print('\n'*1)
        else:
                import conversor_binário_completo
                conversor_binário_completo.menu()
                
decimalbinario()

