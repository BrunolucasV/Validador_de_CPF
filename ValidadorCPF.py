while True:
    cpf= "16899535009"
    if  not cpf.isnumeric():
         print(f"cpf {cpf} invalido.")
         break
            
    if not len(cpf)== 11:
        print(f"cpf {cpf} invalido.") 
        break
    total=0
    multiplicador=10
    contador=9

    for i in range(len(cpf)):
        if contador !=0:
            cedula = int(cpf[i])
            total= cedula * multiplicador + total
            contador-= 1
            multiplicador-= 1
        else:
            break

    resultado= total % 11
    PrimeiroDigito=(11 - resultado)
    
    if PrimeiroDigito > 9:
        PrimeiroDigito=str(0)
    else:
        PrimeiroDigito=str(PrimeiroDigito)

    if not cpf [9] == PrimeiroDigito:
        print(f"cpf {cpf} invalido.")
        break

    Multiplicador =11
    contador = 10
    total=0
    
    for i in range(len(cpf)):
        if contador !=0: 
            cedula = int(cpf[i])
            total= cedula * Multiplicador  + total
            contador -= 1
            Multiplicador -= 1
            
        else:
            break

    resultado= total % 11
    SegundoDigito=(11 - resultado)
    if SegundoDigito >= 10:
        SegundoDigito =str(0)
    else:
        SegundoDigito =str(SegundoDigito)

 
    if not cpf [10] == SegundoDigito:
        print(f"cpf {cpf} invalido.")
        break
        
    else: 
        print(f"cpf {cpf} valido.") 
        break