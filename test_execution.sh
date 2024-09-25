#!/bin/sh

set encoding=utf-8

(DATE=$(date+"%Y%m%d")
cd /Users/yujin/PycharmProjects/Android_automation/인증
python -m pytest -v -s 인증_공동인증서.py > $DATE+ "_공동인증서로그인결과.txt" )
