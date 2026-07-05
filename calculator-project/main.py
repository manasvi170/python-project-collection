import art
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul (n1,n2):
    return n1*n2
def div(n1,n2):
    return n1 / n2

arithmatic_operations={
    "+":add ,
    "-":sub ,
    "*":mul ,
    "/":div ,
}
def calculator():
    print(art.logo)
    should_continue=True
    first_no = float(input("Type the first number :"))

    while should_continue:
        for symbol in arithmatic_operations:
            print(symbol)
        operation_symbol=input("Pick a operation:\t")
        second_no=float(input("Type the second number :"))
        result=arithmatic_operations[operation_symbol](first_no,second_no)
        print(f"{first_no} {operation_symbol} {second_no} = {result}")
        user_action=input(f"Type 'y' to continue with the {result} , or 'n' to start a new calculations : ")

        if user_action=="y":
            first_no=result
        else:
            should_continue=False
            print("\n" * 20)
            calculator()


calculator()




