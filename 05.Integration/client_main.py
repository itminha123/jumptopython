#!/usr/bin/etc python
# -*- coding: utf-8 -*-

#lib import ====================================
from client import DBdata_Trans

if __name__== "__main__":   
        tr=DBdata_Trans()
        result= tr.dbdata_trans_run()
