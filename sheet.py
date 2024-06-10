from main import get_info
import csv
from datetime import date, datetime


def new_file(parametr):
    with open('/Users/lesia/Documents/python/parsing_currency/data_currency.csv', 'w', encoding='utf-8', newline='') as file:
        headers = ['Bank', 'USD сдать', 'USD купить', 'EUR сдать', 'EUR купить', 'RUB сдать', 'RUB купить']
        banks = [['BNB bank'], ['Paritet'], ['Alfa InSync'], ['Nembo'], ['Up'], ['Покупай выгодно'], ['Будь в курсе'], ['MyFin'], ['Alfa'], ['Belweb'], ['VTB']]
        writer = csv.writer(file, delimiter=',')
        writer.writerow(headers)
        for param in parametr:
            writer.writerow(param)


new_file(get_info())



