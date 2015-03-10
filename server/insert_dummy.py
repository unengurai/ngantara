#!/usr/bin/env python3

import sys

## python2 perlu ini nih
#import os, sys
#mbahPath = os.getcwd()
#sys.path.append(mbahPath+'/handler')
from handler.model import *

from pprint import pprint
#init()
try:
    KwType = KeywordType(kwtype='dummy',app='dummy app',note='dummy')
    KwType.save()
except:
    print("KwType err : " + str(sys.exc_info()))
    pass


try:
    KwType = KeywordType.get(KeywordType.kwtype=='dummy')
    Kw = Keyword(kwtype=KwType.ktid,kw='keyword_1')
    Kw.save()
except:
    print("Kw err : " + str(sys.exc_info()))
    pass
