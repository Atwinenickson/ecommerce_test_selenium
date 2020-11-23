#!/bin/bash
sleep 2 
. venv/bin/activate
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
