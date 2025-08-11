def verficar0(num):
    if  num == 0:
        return True
    else:
        return False
    

def div(num1, num2):
    if verficar0(num2):
        div = "Divisão impossivel"
    else:
        div = f"{(num1 / num2):,.3}"
    return div