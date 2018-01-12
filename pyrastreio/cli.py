import click
from pyrastreio import rastreio
from tabulate import tabulate


@click.command()
@click.argument('codigo')
def cli(codigo):
    eventos = rastreio(codigo)
    if len(eventos) == 0:
        message = '''
            Parece que o site dos correios parou de funcionar (de novo)
            ou você digitou um codigo invalido ¯\_(ツ)_/¯
        '''
        print(message)
    else:
        print(tabulate(eventos, headers="keys", tablefmt="grid"))
