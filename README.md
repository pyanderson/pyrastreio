PyRastreio
============

PyRastreio é uma biblioteca/cli para rastrear suas encomendas em alguns sistemas (correios e jadlog),
criei ela só por que queria uma forma mais prática de ficar consultando minhas compras
sem ter que ir nesses sistemas fazer todo o procedimento de consulta.

Instalação
------------

    $ pip install pyrastreio

**obs. Se você vai instalar a biblioteca fora de um ambiente virtual, é recomendado usar a flag [--user](https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site).**

Exemplos
--------
Correios:

```python
from pyrastreio import correios

eventos = correios('CODIGO_RASTREIO')
print(eventos)
```

Caso um código válido seja usado, essa deve ser a saída:

    [{"data": "data_evento", "hora": "hora_evento", local": "local onde ocorreu o evento", "mensagem": "evento"}]

Jadlog:

```python
from pyrastreio import jadlog

eventos = jadlog('CODIGO_RASTREIO')
print(eventos)
```

Caso um código válido seja usado, essa deve ser a saída:

    [{"data/hora": "data hora", "origem": "local origem", "status": "situação", "destino": "local destino", "documento": "numero documento"}]


Usando como CLI, dois comandos estão disponíveis:

    $ rastreio correios CODIGO
    +------------+--------+----------------+---------------------+
    | data       | hora   | local          | mensagem            |
    +============+========+================+=====================+
    | 11/11/2011 | 11:11  | São Paulo / SP | descrição do evento |
    +------------+--------+----------------+---------------------+
    | 12/12/2011 | 12:12  | São Paulo / SP | descrição do evento |
    +------------+--------+----------------+---------------------+

ou

    $ cade_minha_encomenda jadlog CODIGO
    +--------------------+-----------------+---------------+-----------------+----------------+
    | data/hora          | origem          | status        | destino         | documento      |
    +====================+=================+===============+=================+================+
    | 11/11/2011   11:11 | CO SAO PAULO 01 | EMISSAO       | CO SAO PAULO 02 |                |
    +--------------------+-----------------+---------------+-----------------+----------------+
    | 12/12/2011   12:12 | CO SAO PAULO 02 | TRANSFERENCIA | CO SAO PAULO 03 | 11111111111111 |
    +--------------------+-----------------+---------------+-----------------+----------------+

Ajuda:

    $ rastreio --help
    Usage: rastreio [OPTIONS] [correios|jadlog] CODIGO

    Options:
      --help  Show this message and exit.
