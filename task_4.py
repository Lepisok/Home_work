import utils

if __name__ == '__main__':
    import sys

result = utils.currency_rates(sys.argv[1])
if result is not None:
    print(f"Данные от {result.get('Date')}:\n{result.get('Nominal')} {sys.argv[1]} = {result.get('Value')} RUB")
exit()
