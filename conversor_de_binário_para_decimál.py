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
                print("Numero Convertido Com Sucesso")
                print('\n'*1)
                print('---------->', somador, '<-------------')
                continuar=input("deseja continuar ? \n")
                print('\n'*1)
decimalbinario()	
