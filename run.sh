#!/bin/bash
sleep 2 
python3 -m venv venv
. venv/bin/activate
pip install pytest
pip install selenium
pip install allure-pytest
pip install openpyxl
pip install pytest-xdist
pytest -s -v -m "regression" testCases/ --browser chrome
