def convert_currency(dollar):
    peso = dollar * 57.17
    yen = dollar * 146.67
    return peso, yen

usd_input = input("Enter currency in ($): ")

usd_values = []

for val in usd_input.split(","):
    usd_values.append(float(val))

print("\nDollar($)\tPhil Peso(P)\tJpn Yen(¥)")
for usd in usd_values:
    peso, yen = convert_currency(usd)
    print(f"{usd:<12}{peso:<15.2f}{yen:.2f}")
