#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
# prerequisite:py3.x
# Author:mk
# usage:Zhima Credit anti fraud API call and handle data for analysis
'''

import requests
import numpy as np
import pandas as pd
import private.zhimaurl as zm

def callZhiMaApi(apiname,**params):
    '''
        欺诈信息验证 fraudInfoVerification
        实名认证接口服务 realNameVerification
        欺诈关注清单接口服务 antifraudRiskList
        申请欺诈评分接口服务 antifraudScore
    '''
    params['token'] = zm.token.token
    api = eval('zm.'+apiname)
    print('调用芝麻信用['+api.chinesename+']，传入参数：' + str(params))
    r = requests.post(api.url, data=params)
    return r.json()

'''
变量展开处理
'''
def variableExpand():
    pass

'''
哑变量处理
'''
def processDummyVariables(**args):
    print(zm.antifraudRiskList.url)


if __name__ == '__main__':


    #欺诈信息验证
    # fraudInfoVerification_results = callZhiMaApi('fraudInfoVerification', certNo='640202199007164686', name='牛德华')
    #实名认证接口服务
    # realNameVerification_results = callZhiMaApi('realNameVerification', certNo='640202199007164686', name='牛德华',mobile='15843991158',bankCard='20110602436748024138')
    #欺诈关注清单接口服务
    # antifraudRiskList_results = callZhiMaApi('antifraudRiskList',certNo='640202199007164686',name='牛德华')
    #申请欺诈评分接口服务
    # antifraudScore_results = callZhiMaApi('antifraudScore', certNo='640202199007164686', name='牛德华')


    '''
    实名认证接口
    {'code': 0, 'message': None, 'data': {'success': True, 'code': '[V_CN_NA, V_PH_NM_UM, V_BC_PH_UK]', 'msg': '查询不到身份证号信息;手机号码与姓名信息不匹配;银行号码与手机号码信息匹配未知;', 'acrossVerify': False}, 'stackTrace': None, 'errMsg': None}
    '''


    # print(realNameVerification_results)

    # print(antifraudRiskList_results['code'])
    # print(antifraudRiskList_results['message'])
    # print(antifraudRiskList_results['data']['success'])
    # print(antifraudRiskList_results['data']['errorCode'])
    # print(antifraudRiskList_results['data']['errorMessage'])
    # print(antifraudRiskList_results['data']['body'])
    # print(antifraudRiskList_results['data']['params'])
    # print(antifraudRiskList_results['data']['bizNo'])
    # print(antifraudRiskList_results['data']['hit'])
    # print(antifraudRiskList_results['data']['verifyCode']) #欺诈信息验证
    # print(antifraudRiskList_results['data']['riskCode']) #欺诈关注清单接口服务
    # print(antifraudRiskList_results['data']['score'])   #申请欺诈评分接口服务
    # print(antifraudRiskList_results['stackTrace'])
    # print(antifraudRiskList_results['errMsg'])


    # df = pd.DataFrame()
    # df.append({'code':'0',
    #            ''
    # })
    # print(url.)




# ZM201709213000000797900019294796


