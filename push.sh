#!/bin/bash
rm tmp_console_main.py
git add --chmod +x $1
git add *
git commit -m "$2"
git push