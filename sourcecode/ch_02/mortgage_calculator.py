def mortgage():
    name = input('Enter your name ').capitalize()
    print(f"Time to calculate your mortgage payments {name}... ")
    principal = float(input('Enter in your principal '))
    interest_rate = float(input('Enter interest rate '))
    r = (interest_rate / 100) / 12
    n = int(input('Enter mortgage period (years) '))
    # get total number of months
    n = n * 12
    numerator = r * (1 + r) ** n
    deno = (1 + r) ** n - 1
    monthly_payment = principal * (numerator / deno)
    monthly_payment = round(monthly_payment)
    total_mortgage = monthly_payment * 30 * 12
    print(f'Monthly payment: ${monthly_payment}, total mortgage = ${total_mortgage}')


if __name__ == '__main__':
    mortgage()