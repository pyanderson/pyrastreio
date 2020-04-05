import click

import pyrastreio
from tabulate import tabulate


def run_tracking(system, *args):
    events = system(*args)
    if len(events) == 0:
        return '''
            Parece que o %s parou de funcionar
            ou você digitou alguma informação inválida ¯\\_(ツ)_/¯
            ''' % system.__name__
    return tabulate(events, headers="keys", tablefmt="grid")


@click.group()
def main():
    pass


@main.command()
@click.argument('tracking_code')
def correios(tracking_code):
    print(run_tracking(pyrastreio.correios, tracking_code))


@main.command()
@click.argument('tracking_code')
def jadlog(tracking_code):
    print(run_tracking(pyrastreio.jadlog, tracking_code))


@main.command()
@click.argument('tracking_code')
@click.argument('cpf')
def sequoia(tracking_code, cpf):
    print(run_tracking(pyrastreio.sequoia, tracking_code, cpf))


if __name__ == '__main__':
    main()
