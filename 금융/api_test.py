import requests
import pytest


def test_LPMAEAA_A102lc()->None:
    r=requests.get("https://m.lottecard.co.kr/app/LPMAEAA_A102.lc")
    code=r.text
    print(code)
