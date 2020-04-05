import re

import requests
from bs4 import BeautifulSoup as bs4


def correios(tracking_code):
    headers = {'Referer': 'https://www2.correios.com.br/sistemas/rastreamento/'}  # noqa
    url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?' # noqa
    data = {'objetos': tracking_code, 'btnPesq': 'Buscar', 'acao': 'track'}
    res = requests.post(url, data=data, headers=headers)
    parser = bs4(res.text, 'html.parser')
    dt_events = parser.find_all('td', {'class': 'sroDtEvent'})
    lb_events = parser.find_all('td', {'class': 'sroLbEvent'})
    regex = re.compile(r'[\n\r\t]')
    eventos = []
    for dt, lb in zip(dt_events, lb_events):
        event = {}
        dt_info = regex.sub(' ', dt.text).split()
        event['data'], event['hora'] = dt_info[:2]
        event['local'] = ' '.join(dt_info[2:])
        event['mensagem'] = ' '.join(regex.sub(' ', lb.text).split())
        eventos.append(event)
    return eventos


def jadlog(tracking_code):
    url = 'http://www.jadlog.com.br/siteInstitucional/tracking_dev.jad'
    res = requests.get(url, params={'cte': tracking_code})
    parser = bs4(res.text, 'html.parser')
    events = []
    keys = ['data/hora', 'origem', 'status', 'destino', 'documento']
    for tr in parser.find_all('tr')[1:]:
        tds = tr.find_all('td')
        if len(tds) == 5:
            events.append({c: v.text.strip() for c, v in zip(keys, tds)})
    return events


def sequoia(tracking_code, cpf):
    url = 'https://portal.texlog.com.br/rastreamento/rastrear.php'
    data = {'remessa': tracking_code, 'cpf': cpf, 'pg': 'rastreamento_geral'}
    res = requests.post(url, data=data)
    parser = bs4(res.text, 'html.parser')
    big_div = parser.find('div', {'class': 'rastreamento'})
    if big_div is None:
        return []
    dt = big_div.find_all('div', {'class': 'col_dt'})[1:]
    st = big_div.find_all('div', {'class': 'col_st'})[1:]
    return [{'data/hora': d.text, 'status': s.text} for d, s in zip(dt, st)]
