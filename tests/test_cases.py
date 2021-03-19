# -- coding: utf-8 --
import json

import pytest
import allure

from data import data
from data.data import Case
from common.httpClient import HttpClient


class TestCase:
    casedata = data.read_case_data(sheet_name='manage')

    @allure.feature('宠物店')
    @allure.story('宠物管理')
    @allure.title('{title}')
    @allure.description('这是个描述')
    @pytest.mark.parametrize('cases, title', casedata)
    def test_case001(self, cases, title):
        # print(len(cases))
        # cases = cases[3]
        # print(cases[Case.URL])
        # print(cases[Case.BODY])
        client = HttpClient(url=cases[Case.URL], method=cases[Case.METHOD], bodytype=cases[Case.BODYTYPE],
                            params=cases[Case.PARAMS])
        client.headers = json.loads(cases[Case.HEADERS])
        client.set_body(cases[Case.BODY])
        client.send()
        a = json.loads(cases[Case.MESSAGE])
        b = a['check']
        use_checkpoint.check_status_code(cases[Case.STATUS_CODE], client.status_code)
        for i in b:
            use_checkpoint.check(check_type=i['method'], expected_value=i['exp'], json_data=client.json, node_path=i['path'], message=i['message'])

        # if cases[Case.MESSAGE]:

        # assert int(cases[Case.STATUS_CODE]) == client.status_code
    
    # @pytest.mark.parametrize('cases', data)
    # def test_case002(self, cases):
    #     cases = cases[0]
    #     client = HttpClient(url=cases[Case.URL], method=cases[Case.METHOD], bodytype=cases[Case.BODYTYPE],
    #                         params=cases[Case.PARAMS])
