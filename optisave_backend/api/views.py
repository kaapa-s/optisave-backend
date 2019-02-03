from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import urllib.request
import json

banks = (
    'Powszechna Kasa Oszczędności Bank Polski',
    'Bank Polska Kasa Opieki',
    'Santander Bank Polska',
    'mBank',
    'ING Bank Śląski',
    'Bank BGŻ BNP Paribas',
    'Bank Millennium',
    'Getin Noble Bank',
    'Alior Bank',
    'Raiffeisen Bank Polska',
    'Bank Handlowy w Warszawie',
    'Deutsche Bank Polska',
    'Idea Bank',
    'Bank Ochrony Środowiska',
    'Credit Agricole Bank Polska',
    'Bank Polskiej Spółdzielczości',
    'Santander Consumer Bank',
    'SGB-Bank',
    'Euro Bank',
    'DNB Bank Polska',
    'Bank Pocztowy',
    'Plus Bank',
    'BPI Bank Polskich Inwestycji',
    'Nest Bank',
    'Toyota Bank Polska',
    'T-Mobile Usługi Bankowe',
    'Inbank'
)

bank_names_mappings = {
    'BGŻOptima': banks[5],
    'Alior Bank': banks[8],
    'BOŚ': banks[12],
    'Bank BGŻ BNP Paribas S.A': banks[5],
    'Bank BPS': banks[15],
    'Bank Pekao': banks[1],
    'Citi Handlowy': banks[10],
    'Crédit Agricole': banks[14],
    'Eurobank': banks[18],
    'ING Bank Śląski': banks[4],
    'IdeaBank': banks[12],
    'Inbank': banks[26],
    'Millennium': banks[6],
    'Nest Bank': banks[23],
    'Noble Bank': banks[7],
    'PKO Bank Polski': banks[0],
    'PLUS BANK': banks[21],
    'Raiffeisen Polbank': banks[9],
    'T-Mobile Usługi Bankowe': banks[25],
    'Toyota Bank': banks[24]
}

baseurl = 'https://www.comperialead.pl/apicl/?api=dd1d214b8f36557d0d&host=api.optisave.pl'

def deposits(request):
    url = 'https://www.comperialead.pl/apicl/?api=dd1d214b8f36557d0d&host=api.optisave.pl&polecenie=wyniki&produkt=lb&format=json&ilosc=30&strona=1'

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

        for offer in data['odpowiedz']['oferty']:
            offer['bank'] = bank_names_mappings.get(offer['bank'], offer['bank'])

        result = {'offers': data['odpowiedz']['oferty']}

        return JsonResponse(result)


def promotions(request):
    url = 'https://www.comperialead.pl/apicl/?api=dd1d214b8f36557d0d&host=api.optisave.pl&polecenie=wyniki&produkt=ko&format=json&ilosc=20&strona=1'

    with urllib.request.urlopen(url) as url:
        return HttpResponse(url.read().decode(), content_type='application/json')