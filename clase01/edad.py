edad = int(input('ingrese edad: '))

if edad < 18:
    print('eres menor de edad')
else:
    if edad < 60:
        print('eres adulto')
    elif edad < 99:
        print('eres adulto mayor')
    else:
        print('no deberías estar vivo')