# -- coding: utf-8 --
import records
import requests

from config.config import Config
from log.log import logger


class SqlClient:
    def __init__(self):
        self.db = records.Database(Config().database)

    def get_sql(self, sql_val):
        try:
            result = self.db.query(sql_val)
            return result.all(as_dict=True)
        except:
            logger.error('数据库错误')
        finally:
            self.db.close()


db = SqlClient()


if __name__ == '__main__':
    url = 'http://apidev.kunlunjue.com/Content/newHome'
    params = {
        'token':'67b146423966de2d32737634264cbef3189313'
    }
    res = requests.get(url=url, params=params)
    casedata = read_case_data_to_yaml()['content/newHome'][0]
    a = get_check_value(casedata['message'], res.json())
    print(a)
    print(casedata)
    # print(res.json())
    # result = jsonpath.jsonpath(res.json(), '$..matchLive[*]')
    # print(result)
    # c = CheckPoint()
    # a = c.check_nodes_count(11, res.json(), '$..matchLive[*]')
    # print(a)

#     b = res.json()
#     print(json.dumps(b))
#     c = json.dumps(b)
#     print(c)
#     # print(res.json())
#     print(type(c))
#     a = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', c)
#     for url in a:
#         result = requests.get(url)
#         code = result.status_code
#         print(f'url:{url},code:{code}')
# #
#
#
#
#
#
#
# db = records.Database(Config().database)
# # rows = db.query("SELECT count (match_id) FROM klj_a_match WHERE match_status IN (0, 1);")
# # print(rows)
# rows = db.query("SELECT * FROM klj_a_match WHERE match_status IN (0, 1);")
# db.close()
# print(len(rows.all(as_dict=True)))