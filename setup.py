from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()


setup(
    name='pyrastreio',
    version='0.1.2',
    url='https://github.com/pyanderson/pyrastreio',
    license='MIT License',
    author='Anderson Lima',
    author_email='anderson.sl93@hotmail.com',
    keywords='rastreio encomenda correios jadlog',
    description='Biblioteca/CLI para rastreio de encomendas nos sistemas do correios e jadlog.',  # noqa
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests', 'click', 'tabulate'],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese (Brazilian)'
    ],
    entry_points='''
        [console_scripts]
        rastreio=pyrastreio.cli:main
        cade_minha_encomenda=pyrastreio.cli:main
    ''',
)
