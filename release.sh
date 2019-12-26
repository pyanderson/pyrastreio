#!/bin/bash
rm -rf build/ dist/

python setup.py sdist bdist_wheel

if [ "$1" == "prod" ]
then
    twine upload dist/*
else
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
fi
