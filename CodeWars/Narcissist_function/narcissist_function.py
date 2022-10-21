def narcissistic( value ):
    n = len(str(value))
    sum=0
    for i in str(value):
        sum+=int(i)**n
    if sum==value:
        return True
    else:
        return False