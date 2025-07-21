from math import sqrt
while True:
    try:
        z1=int(input('enter a number1:  '))
        z2=int(input('enter a number2:  '))
        z3=int(input('enter a number3:  '))
        if z1<= 0 or z2<= 0 or z3 <= 0:
            print('adad vared shode manfi ast')
            continue
    
        azla=[z1,z2,z3]
        p=(sum(azla))/2
        a=p*(p-z1)*(p-z2)*(p-z3)
        if a<0:
            print('hasel jazr manfi ast')
            continue
        masahat=sqrt(a)

        if (z1<z2+z3 and z2<z1+z3 and z3<z1+z2) :
            print('mosallas sakhte mishavad')
            print(f'masahat barabar ast ba {round(masahat,2)}')
        else:
            print('mosallas sakhte nemishavad')
    
    except ValueError:
        print('moteghayer eshtebah vared kardid')
    except Exception: 
        print('moshkeli pish amad!!!! ')

         
                
         
    