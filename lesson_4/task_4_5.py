from sys import argv
from utils_task_4_5 import currency_rates_adv, currency_rates
if len(argv) == 2:
    print(currency_rates_adv(argv[1]))
elif len(argv) > 2:
    print('Передано слищком много параметров')
else:
    print('Пожалуйста передайте параметры')
