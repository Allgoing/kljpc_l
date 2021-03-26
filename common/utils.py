# -- coding: utf-8 --
import jsonpath
import requests

from common.sqlClient import db
from data.data import read_case_data_to_yaml


def dict_to_result(dict_data):
    val = None
    if 'value' in dict_data:
        val = dict_data['value']
    else:
        val = db.get_sql(dict_data['sql'])
    return val


def get_value_from_path(json_data, node_path):
    '''
    获取节点数据
    :param json_data: 原始json串
    :param node_path: 节点地址
    :return:
    '''
    result = None
    if json_data:
        result = jsonpath.jsonpath(json_data, node_path)
        return result
    return result


def get_check_value(check_dict, json_data):
    result_list = []
    check_points = check_dict['check']
    for check_point in check_points:
        var = dict_to_result(check_point['exp'])
        result = get_value_from_path(json_data, check_point['path'])
        result_list.append((check_point['method'], var, result, check_point['message']))
    return result_list


# if __name__ == '__main__':
#     url = 'http://apidev.kunlunjue.com/Content/newHome'
#     params = {
#         'token':'67b146423966de2d32737634264cbef3189313'
#     }
#     res = requests.get(url=url, params=params)
#     # print(b)

    # a = get_check_value(casedata['message'], res.json())
    # print(a)


