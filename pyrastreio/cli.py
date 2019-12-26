import click

import pyrastreio
from tabulate import tabulate


@click.command()
@click.argument(
    'sistema', type=click.Choice(['correios', 'jadlog'], case_sensitive=False)
)
@click.argument('codigo')
def main(sistema, codigo):
    eventos = getattr(pyrastreio, sistema)(codigo)
    if len(eventos) == 0:
        message = '''
            Parece que o %s parou de funcionar
            ou você digitou um codigo invalido ¯\\_(ツ)_/¯
            ''' % sistema
        print(message)
    else:
        print(tabulate(eventos, headers="keys", tablefmt="grid"))


if __name__ == '__main__':
    main()
