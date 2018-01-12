PyRastreio
============

PyRastreio é uma biblioteca/cli para rastrear suas encomendas no site do correios,
criei ela só por que queria uma forma mais prática de ficar consultando minhas compras
sem ter que ir no site do correios fazer todo o procedimento de rastreio.

Instalação
------------

    $ pip install pyrastreio


Exemplos
--------
Usando como biblioteca:

```python
from pyrastreio import rastreio

eventos = rastreio('CODIGO_RASTREIO')
print(eventos)
```

A saida deve ser algo assim:

    [{"data": "data_evento", "local": "local onde ocorreu o evento", "mensagem": "evento"}]

Usando como CLI:

    $ rastreio CODIGO
    +------------+-----------------------------+---------------------+
    | data       | local                       | mensagem            |
    +============+=============================+=====================+
    | dd/mm/yyyy | local onde ocorreu o evento | descrição do evento |
    +------------+-----------------------------+---------------------+
    | dd/mm/yyyy | local onde ocorreu o evento | descrição do evento |
    +------------+-----------------------------+---------------------+
ou

    $ cade_minha_encomenda CODIGO
    mesma saida do comando rastreio ¯\_(ツ)_/¯
