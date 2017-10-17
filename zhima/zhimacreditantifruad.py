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
import itertools
import datetime as dt


def callZhiMaApi(apiname,params):
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

if __name__ == '__main__':
    source_file = 'input/kkd_apply_his_all.csv'
    out_path = 'output/kkd_apply_his_zhima_out.data'
    kkd_apply_records = pd.read_csv(source_file,na_filter=False)
    # row = ['查询时间', '查询类型', '数据来源', '行号', '原始返回数据']

    with open(out_path, 'w') as out_file:
        out_file.write('query_time|query_type|source|rowid|mcht_cd|mcht_name|certNo|name|mobile|email|bankCard|address|ip|mac|wifimac|imei|res_ori_json|res_ori_code|res_ori_message|res_ori_data_success|res_ori_data_errorCode|res_ori_data_errorMessage|res_ori_data_body|res_ori_data_params|res_ori_data_bizNo|res_ori_data_hit|res_ori_data_verifyCode|res_ori_data_riskCode|res_ori_data_score|res_ori_stackTrace|res_ori_errMsg'+'\n')
        for idx,data in kkd_apply_records.iterrows():
            res = callZhiMaApi('fraudInfoVerification', data.to_dict())
            row = []
            row.append(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))  #query_time
            row.append('fraudInfoVerification欺诈信息验证')             #query_type
            row.append(source_file)             #source
            row.append(idx)             #rowid
            row.append(data['mcht_cd'])            #mcht_cd
            row.append(data['mcht_name'])       #mcht_name
            row.append(data['certNo'])      #certNo
            row.append(data['name'])        #name
            row.append(data['mobile'])      #mobile
            row.append(data['email'])       #email
            row.append(data['bankCard'])    #bankCard
            row.append(data['address'])     #address
            row.append(data['ip'])          #ip
            row.append(data['mac'])         #mac
            row.append(data['wifimac'])     #wifimac
            row.append(data['imei'])  # imei
            row.append(res)         #res_ori_json
            row.append(res["code"])  # res_ori_code
            row.append(res["message"]) # res_ori_message
            row.append(res["data"]["success"])  # res_ori_message
            row.append(res["data"]["errorCode"])  # res_ori_data_errorCode
            row.append(res["data"]["errorMessage"]) # res_ori_data_errorMessage
            row.append(res["data"]["body"]) # res_ori_data_body
            row.append(res["data"]["params"])  #  res_ori_data_params
            row.append(res["data"]["bizNo"]) # res_ori_data_bizno
            row.append(res.get("data").get("hit",'key not exists'))   # hit
            row.append(res.get("data").get("verifyCode",'key not exists')) # verifyCode
            row.append(res.get("data").get("riskCode",'key not exists')) # res_ori_data_riskCode
            row.append(res.get("data").get("score",'key not exists'))    # res_ori_data_score
            row.append(res["stackTrace"])   # stackTrace
            row.append(res["errMsg"])       # errMsg
            out_file.write('|'.join(map(str, row))+'\n')

            res = callZhiMaApi('antifraudRiskList', data.to_dict())
            row = []
            row.append(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))  # query_time
            row.append('antifraudRiskList欺诈关注清单接口服务')  # query_type
            row.append(source_file)  # source
            row.append(idx)  # rowid
            row.append(data['mcht_cd'])  # mcht_cd
            row.append(data['mcht_name'])  # mcht_name
            row.append(data['certNo'])  # certNo
            row.append(data['name'])  # name
            row.append(data['mobile'])  # mobile
            row.append(data['email'])  # email
            row.append(data['bankCard'])  # bankCard
            row.append(data['address'])  # address
            row.append(data['ip'])  # ip
            row.append(data['mac'])  # mac
            row.append(data['wifimac'])  # wifimac
            row.append(data['imei'])  # imei
            row.append(res)  # res_ori_json
            row.append(res["code"])  # res_ori_code
            row.append(res["message"])  # res_ori_message
            row.append(res["data"]["success"])  # res_ori_message
            row.append(res["data"]["errorCode"])  # res_ori_data_errorCode
            row.append(res["data"]["errorMessage"])  # res_ori_data_errorMessage
            row.append(res["data"]["body"])  # res_ori_data_body
            row.append(res["data"]["params"])  # res_ori_data_params
            row.append(res["data"]["bizNo"])  # res_ori_data_bizno
            row.append(res.get("data").get("hit", 'key not exists'))  # hit
            row.append(res.get("data").get("verifyCode", 'key not exists'))  # verifyCode
            row.append(res.get("data").get("riskCode", 'key not exists'))  # res_ori_data_riskCode
            row.append(res.get("data").get("score", 'key not exists'))  # res_ori_data_score
            row.append(res["stackTrace"])  # stackTrace
            row.append(res["errMsg"])  # errMsg
            out_file.write('|'.join(map(str, row))+'\n')

            res = callZhiMaApi('antifraudScore', data.to_dict())
            row = []
            row.append(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))  # query_time
            row.append('antifraudScore申请欺诈评分接口服务')  # query_type
            row.append(source_file)  # source
            row.append(idx)  # rowid
            row.append(data['mcht_cd'])  # mcht_cd
            row.append(data['mcht_name'])  # mcht_name
            row.append(data['certNo'])  # certNo
            row.append(data['name'])  # name
            row.append(data['mobile'])  # mobile
            row.append(data['email'])  # email
            row.append(data['bankCard'])  # bankCard
            row.append(data['address'])  # address
            row.append(data['ip'])  # ip
            row.append(data['mac'])  # mac
            row.append(data['wifimac'])  # wifimac
            row.append(data['imei'])  # imei
            row.append(res)  # res_ori_json
            row.append(res["code"])  # res_ori_code
            row.append(res["message"])  # res_ori_message
            row.append(res["data"]["success"])  # res_ori_message
            row.append(res["data"]["errorCode"])  # res_ori_data_errorCode
            row.append(res["data"]["errorMessage"])  # res_ori_data_errorMessage
            row.append(res["data"]["body"])  # res_ori_data_body
            row.append(res["data"]["params"])  # res_ori_data_params
            row.append(res["data"]["bizNo"])  # res_ori_data_bizno
            row.append(res.get("data").get("hit", 'key not exists'))  # hit
            row.append(res.get("data").get("verifyCode", 'key not exists'))  # verifyCode
            row.append(res.get("data").get("riskCode", 'key not exists'))  # res_ori_data_riskCode
            row.append(res.get("data").get("score", 'key not exists'))  # res_ori_data_score
            row.append(res["stackTrace"])  # stackTrace
            row.append(res["errMsg"])  # errMsg
            out_file.write('|'.join(map(str,row))+'\n')
