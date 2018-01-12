from setuptools import setup

setup(
    name="pyrastreio",
    version='0.0.3',
    url='https://github.com/pyanderson/pyrastreio',
    license='MIT License',
    author='Anderson Lima',
    author_email='anderson.sl93@hotmail.com',
    keywords='correios rastreio encomenda compra',
    description='Biblioteca de rastreio de encomendas no site do correios',
    packages=['pyrastreio'],
    install_requires=['beautifulsoup4', 'requests', 'click', 'tabulate'],
    entry_points='''
        [console_scripts]
        rastreio=pyrastreio.cli:cli
        cade_minha_encomenda=pyrastreio.cli:cli
    ''',
)
