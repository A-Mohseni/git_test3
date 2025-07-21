while True:
    try:
        n=int(input('   ?  '))
        if n>=10:
            raise Exception('number greater that 9')
        a=10/n
        print({2.0:'two'}[a])
        print([9,8,6][int(a)])
        break
    except ValueError:
            print('you should enter a number')
    except ZeroDivisionError:
            print('you most not enter 0 ')
    except KeyError:
            print(a)
    except Exception as e:
            print(e)
            print('somthing went wrong')        