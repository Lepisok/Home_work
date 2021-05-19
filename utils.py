from datetime import datetime
from decimal import Decimal

from requests import get

HTTP = "http://www.cbr.ru/scripts/XML_daily.asp"


def currency_rates(currency_code):
    response = get(HTTP)
    content = response.content.decode(encoding=response.encoding)
    date_str = content.split('<ValCurs Date="')[1].split('" ')[0]
    date = datetime.strptime(date_str, '%d.%m.%Y').date()
    temp = content.split('<CharCode>' + currency_code.upper() + '</CharCode>')
    if len(temp) > 1:
        nominal = int(temp[1].split('<Nominal>')[1].split('</Nominal>')[0])
        value = Decimal(temp[1].split('<Value>')[1].split('</Value>')[0].replace(",", "."))
        return {
            'Date': date,
            'Nominal': nominal,
            'Value': value
        }
