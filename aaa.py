# -- coding: utf-8 --

# d = {
#     "store": {
#         "book": [
#             {
#                 "category": "reference",
#                 "author": "Nigel Rees",
#                 "title": "Sayings of the Century",
#                 "price": 11
#             },
#             {
#                 "category": "fiction",
#                 "author": "Evelyn Waugh",
#                 "title": "Sword of Honour",
#                 "price": 12.99
#             },
#             {
#                 "category": "fiction",
#                 "author": "Herman Melville",
#                 "title": "Moby Dick",
#                 "isbn": "0-553-21311-3",
#                 "price": 8.99
#             },
#             {
#                 "category": "fiction",
#                 "author": "J. R. R. Tolkien",
#                 "title": "The Lord of the Rings",
#                 "isbn": "0-395-19395-8",
#                 "price": 22.99
#             }
#         ],
#         "bicycle": {
#             "color": "red",
#             "price": 19.95
#         }
#     },
#     "expensive": 10
# }
#
var = {'id': 2,
       'category':
           {
               'id': 10,
               'name': 'test2'
           },
       'name': 'doggie',
       'photoUrls': ['newegg.com'],
       'tags': [{
           'id': 0,
           'name': 'lcnc'
       }],
       'status': 'available'
       }
import jsonpath
path = '$.category.id'
res1 = jsonpath.jsonpath(var, path) #嵌套n层也能取到所有学生姓名信息,$表示最外层的{}，..表示模糊匹配
print(res1) #输出结果是list：['小白', '小黑']
