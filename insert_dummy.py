#!/usr/bin/env python3

import sys
from handler import model


model.create_model()
try:
    KwType = model.KeywordType(kwtype='dummy', app='dummy app', note='dummy')
    KwType.save()
except:
    print("KwType err : " + str(sys.exc_info()))
    pass


try:
    KwType = model.KeywordType.get(model.KeywordType.kwtype == 'dummy')
    Kw = model.Keyword(kwtype_id=KwType.id, kw='keyword_3')
    Kw.save()
except:
    print("Kw err : " + str(sys.exc_info()))
    pass
