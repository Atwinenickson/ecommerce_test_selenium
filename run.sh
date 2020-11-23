#!/bin/bash
sleep 2 
python3 -m venv venv
. venv/bin/activate
pip install pytest
pip install selenium
pytest -s -v -m "regression" testCases/ --browser chrome
