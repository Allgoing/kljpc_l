# -- coding: utf-8 --
import json

import pytest
import allure

from data import data
from data.data import Case
from common.httpClient import HttpClient
from common.utils import get_check_value


class TestCase:
    casedata = data.read_case_data_to_yaml()['content/newHome']

    @allure.feature('宠物店')
    @allure.story('宠物管理')
    @allure.description('这是个描述')
    @pytest.mark.parametrize('cases', casedata)
    def test_case001(self, cases, use_checkpoint):

        client = HttpClient(url=cases[Case.URL], method=cases[Case.METHOD], bodytype=cases[Case.BODYTYPE],
                            params=cases[Case.PARAMS])
        client.headers = cases[Case.HEADERS]
        client.set_body(cases[Case.BODY])
        client.send()
        a = cases[Case.MESSAGE]
        print(type(a))
        # b = a['check']
        print(a)
        c = get_check_value(a, client.json())
        # use_checkpoint.check_status_code(cases[Case.STATUS_CODE], client.status_code)

        allure.dynamic.title(cases[Case.CASENAME])
        allure.dynamic.description(f'请求url：<font color="red">{cases[Case.URL]}</font><br/>'
                                   f'请求方法：{cases[Case.METHOD]}</br>'
                                   f'请求头：{cases[Case.HEADERS]}</br>'
                                   f'请求参数：{cases[Case.PARAMS]}</br>'
                                   f'请求body：{cases[Case.BODY]}</br>'
                                   f'检查点：</br>'
                                   f'期望code码：{cases[Case.STATUS_CODE]}, 实际状态码：{client.status_code}</br>'
                                   f'期望值：11，实际值：11')

        # allure.dynamic.description(f'期望状态码：{cases[Case.STATUS_CODE]}, 实际状态码：{client.status_code}')
        for i in c:
            use_checkpoint.check(check_type=i[0], expected_value=i[1], result=i[2], message=i[3])



        # if cases[Case.MESSAGE]:

        # assert int(cases[Case.STATUS_CODE]) == client.status_code
    
    # @pytest.mark.parametrize('cases', data)
    # def test_case002(self, cases):
    #     cases = cases[0]
    #     client = HttpClient(url=cases[Case.URL], method=cases[Case.METHOD], bodytype=cases[Case.BODYTYPE],
    #                         params=cases[Case.PARAMS])
