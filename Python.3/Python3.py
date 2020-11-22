"""
【Python.3】リスト(次元と要素編)
サンプルコード
"""

data_int_list=[0,1,2,3,4,5] # int型のリスト
print(type(data_int_list))
print(data_int_list)
data_str_list=["a","b","c"] # str型のリスト
print(data_str_list)

#同じ要素のリスト#
all_zero_list=[0]*10 #要素0が10個入ったリスト
print(all_zero_list)
all_zero_list=[1]*15 #要素1が15個入ったリスト
print(all_zero_list)

empty_list1 = list() #空リスト作成
empty_list2 = [] #空リスト作成
print(type(empty_list1),type(empty_list2))

#2次元リスト#
data2_list=[["00","01"],["10","11"],["30"]]
print(data2_list)

#3次元リスト#
data3_list=[
            ["1",["2"]],
            [["3","4"],["5"]],
            ["50"]
            ]
print(data3_list)

"""実行結果
<class 'list'>
[0, 1, 2, 3, 4, 5]
['a', 'b', 'c']
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
<class 'list'> <class 'list'>
[['00', '01'], ['10', '11'], ['30']]
[['1', ['2']], [['3', '4'], ['5']], ['50']]
"""
