print('this is first commit by nikita 2')
a=4
b=5
print(a+b)

if __name__ == '__main__':
    print('this is main code')
    val1=int(input('entre first number='))
    val2=int(input('entre second number='))
    op=input('which math op you want to do?')

    if op.lower()=='add':
        a1=addvalue(val1,val2)
        print(f'addition ={a1}')
    elif op.lower()=='sub':
        a2=subValue(val1,val2)

        print('subtract',a2)
    else:
        print('please choose correct operation,add,sub')