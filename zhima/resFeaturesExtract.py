#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
# prerequisite:py3.x
# Author:mk
# usage:Zhima Credit anti fraud API call and handle data for analysis
'''

import numpy as np
import pandas as pd
import datetime as dt
import private.dict as di
from bokeh.plotting import figure, output_file, show
import seaborn
from numpy import cos, linspace




if __name__ == '__main__':
    # print(di.CodeMap.resourceCodeMap['CN'])
    # print(di.CodeMap.targetCodeMap['PH'])
    # print(di.CodeMap.matchCodeMap['UM'])
    # print(di.CodeMap.validateCodeMapPhone['UL180D'])
    # print(di.CodeMap.validateCodeMap['UL360D'])
    # print(di.OutputHeader.raw_dict)

    out_path = 'output/kkd_apply_his_zhima_out.data'
    df_out = pd.read_csv(out_path, na_filter=False,sep='|')

    print(df_out.res_ori_data_verifyCode)
    print(df_out.res_ori_data_riskCode)


    # print(di.OutputHeader.arr_all_verify, di.OutputHeader.raw_dict)

    # x = linspace(-6, 6, 100)
    # y = cos(x)
    # p = figure(width=500, height=500)
    # p.circle(x, y, size=7, color="firebrick", alpha=0.5)
    # show(p)