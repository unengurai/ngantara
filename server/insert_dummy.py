#!/usr/bin/env python3

import sys
from model import *


#create_model()
try:
    KwType = KeywordType(kwtype='dummy', app='dummy app', note='dummy')
    KwType.save()
except:
    print("KwType err : " + str(sys.exc_info()))
    pass


try:
    KwType = KeywordType.get(KeywordType.kwtype == 'dummy')
    Kw = Keyword(kwtype=KwType.ktid, kw='keyword_3')
    Kw.save()
except:
    print("Kw err : " + str(sys.exc_info()))
    pass
