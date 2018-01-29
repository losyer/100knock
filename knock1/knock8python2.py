# -*- coding: utf-8 -*-
f = lambda x:"".join([unichr(219-ord(i)) if ord(u'a')<=ord(i)<=ord(u'z') else i for i in x])