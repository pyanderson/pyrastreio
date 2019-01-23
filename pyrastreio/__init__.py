import re
import requests
from bs4 import BeautifulSoup as bs4


def rastreio(codigo):
    headers = {'Referer': 'https://www2.correios.com.br/sistemas/rastreamento/'}  # noqa
    url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?' # noqa
    data = {'objetos': codigo, 'btnPesq': 'Buscar', 'acao': 'track'}
    res = requests.post(url, data=data, headers=headers)
    parser = bs4(res.text, 'html.parser')
    dt_eventos = parser.find_all('td', {'class': 'sroDtEvent'})
    lb_eventos = parser.find_all('td', {'class': 'sroLbEvent'})
    regex = re.compile(r'[\n\r\t]')
    eventos = []
    for dt, lb in zip(dt_eventos, lb_eventos):
        evento = {}
        dt_info = regex.sub(' ', dt.text).split()
        evento['data'], evento['hora'] = dt_info[:2]
        evento['local'] = ' '.join(dt_info[2:])
        evento['mensagem'] = ' '.join(regex.sub(' ', lb.text).split())
        eventos.append(evento)
    return eventos
