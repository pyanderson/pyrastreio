from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()


setup(
    name='pyrastreio',
    version='0.1.0',
    url='https://github.com/pyanderson/pyrastreio',
    license='MIT License',
    author='Anderson Lima',
    author_email='anderson.sl93@hotmail.com',
    keywords='correios rastreio encomenda',
    description='Biblioteca de rastreio de encomendas no site do correios',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pyrastreio'],
    install_requires=['beautifulsoup4', 'requests', 'click', 'tabulate'],
    entry_points='''
        [console_scripts]
        rastreio=pyrastreio.cli:main
        cade_minha_encomenda=pyrastreio.cli:main
    ''',
)
