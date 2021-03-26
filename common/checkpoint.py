# -- coding: utf-8 --
import jsonpath

from common.utils import dict_to_result


class CheckPoint:

    def __init__(self):
        pass

    def check_status_code(self, e_code, code, message=None):
        '''
        判断status_code是否相同
        :param e_code: 期望code
        :param code: 实际code
        :param message:
        :return:
        '''
        assert e_code == code, f'{message} 预期结果：{e_code}，实际结果{code}'

    def  check_contain_str(self, e_str, s_str, message=None):
        '''
        判断是否包含字符串
        :param e_str: 期望字符串
        :param s_str: 实际字符串
        :param message:
        :return:
        '''
        assert e_str in s_str, f'{message} 预期结果：{e_str}，实际结果：{s_str}'

    def __get_value_from_path(self, json_data, node_path):
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

    def check_node_exist(self, exp, result, message=None):
        '''
        判断节点数据是否存在
        :param json_data: 原始json串
        :param node_path:节点地址
        :return:
        '''
        # val = dict_to_result(exp)
        # result = self.__get_value_from_path(json_data, node_path)
        assert result is not None, f'{message} 预期结果：节点不存在'

    def check_nodeText_equal(self, exp, json_data, node_path, message=None):
        '''
        判断期望的text和实际的字符串是否相等
        :param exp: 期望的字符值
        :param json: 原始json串
        :param node_path: 节点地址
        :param message:
        :return:
        '''
        result = self.__get_value_from_path(json_data, node_path)
        assert exp == result, f'{message} 期望结果：{exp}, 不等于实际结果：{result}'

    def check_nodeText_notequal(self, exp, json_data, node_path, message=None):
        '''
        判断期望的text和实际的字符串是否相等
        :param exp: 期望的字符值
        :param json: 原始json串
        :param node_path: 节点地址
        :param message:
        :return:
        '''
        result = self.__get_value_from_path(json_data, node_path)
        assert exp != result, f'{message} 期望结果：{exp}, 实际结果：{result}'

    def check_nodeText_startwith(self, exp, json_data, node_path, message=None,):
        '''
        判断期望结果以**开始
        :param text: 期望的字符值
        :param json_data: 原始json串
        :param node_path: 节点地址
        :param message:
        :param num:
        :return:
        '''
        result = self.__get_value_from_path(json_data, node_path)
        assert result.startwith(exp) == True, f'{message} 实际结果：{result}，不是以期望结果：{exp}开头'

    def check_nodeText_contains(self, exp, json_data, node_path, message=None):
        '''
        判断期望结果是否包含在结果中
        :param text:
        :param json_data:
        :param node_path:
        :param message:
        :param num:
        :return:
        '''
        val = dict_to_result(exp)
        result = self.__get_value_from_path(json_data, node_path)
        assert val in result, f'{message} 实际结果：{result}，不包含期望结果{val}'

    def check_nodes_count(self, exp, result, message=None):
        '''
        判断实际总数是否符合期望
        :param count_num: 期望总数
        :param json_data:
        :param node_path:
        :param message:
        :param num:
        :return:
        '''
        # result = self.__get_value_from_path(json_data, node_path)

        val = len(exp)
        if result:
            assert len(result) == val, f'{message} 实际结果{len(result)},不符合期望结果{val}'
        else:
            assert False, f'没有节点数据'

    def check(self, check_type=None, expected_value=None, result=None, json_data=None, node_path=None, message=None):
        '''
        根据检查点类型判断结果
        :param check_type:检查点类型,同CheckType
        :param expected_value: 期望值
        :param json_data:
        :param node_path:
        :param message:
        :param num:
        :return:
        '''
        c_type = check_type.lower().strip()
        # print(c_type)
        # print(expected_value)
        # print(self.__get_value_from_path(json_data, node_path))
        # if c_type == CheckType.Status_Code:
        #     self.check_status_code(expected_value, code=code, message=message)
        # elif c_type == CheckType.CS:
        #     self.check_contain_str(expected_value, s_str=s_str, message=message)
        if c_type == CheckType.EXIST:
            self.check_node_exist(expected_value, result, message=message)
        elif c_type == CheckType.EQUAL:
            self.check_nodeText_equal(expected_value, json_data=json_data, node_path=node_path, message=message)
        elif c_type == CheckType.NOTEQUAL:
            self.check_nodeText_notequal(expected_value, json_data=json_data, node_path=node_path, message=message)
        elif c_type ==CheckType.STARTWITH:
            self.check_nodeText_startwith(expected_value, json_data=json_data, node_path=node_path, message=message)
        elif c_type == CheckType.CONTAINS:
            self.check_nodeText_contains(expected_value, json_data=json_data, node_path=node_path, message=message)
        elif c_type == CheckType.COUNT:
            self.check_nodes_count(expected_value, result, message=message)


class CheckType:
    Status_Code = 'status_code'
    CS = 'c_str'
    EXIST = 'exist'
    EQUAL = 'equal'
    NOTEQUAL = 'notequal'
    STARTWITH = 'startwith'
    CONTAINS = 'contains'
    COUNT = 'count'
