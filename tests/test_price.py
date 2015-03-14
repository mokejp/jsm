# coding=utf-8
#---------------------------------------------------------------------------
# Copyright 2011 utahta
#---------------------------------------------------------------------------
import jsm
from jsm.pricebase import PriceData
from tests import CCODE

def test_get():
    q = jsm.Quotes()
    d = q.get_price(CCODE)
    assert isinstance(d, PriceData)
    assert isinstance(d.open, float)
    assert isinstance(d.close, float)
    assert isinstance(d.high, float)
    assert isinstance(d.low, float)
    assert isinstance(d.volume, int)
