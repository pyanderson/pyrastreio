from setuptools import setup

setup(
    name="pyrastreio",
    version='0.0.1',
    py_modules=['pyrastreio'],
    install_requires=['beautifulsoup4', 'requests', 'click', 'tabulate'],
    entry_points='''
        [console_scripts]
        rastreio=pyrastreio.cli:cli
        cade_minha_encomenda=pyrastreio.cli:cli
    ''',
)
