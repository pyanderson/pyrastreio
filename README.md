# PyRastreio

PyRastreio é uma biblioteca/cli para rastrear suas encomendas em alguns sistemas,
criei ela só por que queria uma forma mais prática de ficar consultando minhas compras
sem ter que ir nesses sistemas fazer todo o procedimento de consulta.

## Sistemas

- [Correios](https://www.correios.com.br/)
- [Jadlog](https://www.jadlog.com.br/jadlog/home)
- [Sequoia](http://sequoialog.com.br/)

## Instalação

    $ pip install pyrastreio

**obs. Se você vai instalar a biblioteca fora de um ambiente virtual, é recomendado usar a flag [--user](https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site).**

## CLI
Você pode executar o CLI usando os comandos `rastreio` ou `cade_minha_encomenda`:

    $ cade_minha_encomenda --help
    Usage: cade_minha_encomenda [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      correios
      jadlog
      sequoia

### Exemplos
#### Correios

    $ rastreio correios CODIGO
    +------------+--------+----------------+---------------------+
    | data       | hora   | local          | mensagem            |
    +============+========+================+=====================+
    | 11/11/2011 | 11:11  | São Paulo / SP | descrição do evento |
    +------------+--------+----------------+---------------------+
    | 12/12/2011 | 12:12  | São Paulo / SP | descrição do evento |
    +------------+--------+----------------+---------------------+

#### Jadlog

    $ cade_minha_encomenda jadlog CODIGO
    +--------------------+-----------------+---------------+-----------------+----------------+
    | data/hora          | origem          | status        | destino         | documento      |
    +====================+=================+===============+=================+================+
    | 11/11/2011   11:11 | CO SAO PAULO 01 | EMISSAO       | CO SAO PAULO 02 |                |
    +--------------------+-----------------+---------------+-----------------+----------------+
    | 12/12/2011   12:12 | CO SAO PAULO 02 | TRANSFERENCIA | CO SAO PAULO 03 | 11111111111111 |
    +--------------------+-----------------+---------------+-----------------+----------------+

#### Sequoia

    $ cade_minha_encomenda sequoia CODIGO CPF
    +------------------+----------------------------+
    | data/hora        | status                     |
    +==================+============================+
    | 11/11/2011 11:11 | Recepção na transportadora |
    +------------------+----------------------------+
    | 12/12/2011 12:12 | Em transferência           |
    +------------------+----------------------------+

## Biblioteca
A biblioteca implementa uma busca para cada sistema:

```python
from pyrastreio import correios, jadlog, sequoia

print('Correios:')
print(correios('CODIGO_RASTREIO_CORREIOS'))
print('Jadlog:')
print(jadlog('CODIGO_RASTREIO_JADLOG'))
# sequoia precisa do cpf ou cnpj além do código de rastreio
print('Sequoia:')
print(sequoia('CODIGO_RASTREIO_SEQUOIA', '11111111111'))
```

Caso um código válido seja usado, essa deve ser a saída:

    Correios:
    [{"data": "11/11/2011", "hora": "11:11", local": "São Paulo / SP", "mensagem": "descrição do evento"}]
    Jadlog:
    [{"data/hora": "11/11/2011   11:11", "origem": "CO SAO PAULO", "status": "EMISSAO", "destino": "CO SAO PAULO 02", "documento": "11111111111111"}]
    Sequoia:
    [{"data/hora": "11/11/2011", "status": "Recepção na transportadora"}]
