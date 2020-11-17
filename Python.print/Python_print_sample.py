"""
    Python】様々なprint関数
    サンプルコード
"""

hello = "Hello"  # 文字列変数
number_int = 3  # int変数
number_float = 3.141592  # float変数

print(hello, number_int, number_float)  # 出力: Hello 3 3.141592

print(hello, number_int, number_float, sep="/")  # 出力: Hello/3/3.141592

print(hello, end=":")
print(number_int, end="/")
print(number_float)  # 出力: Hello:3:3.141592

print(hello+str(number_int)+str(number_float))  # 出力: Hello33.141592
print(hello+repr(number_int)+repr(number_float))  # 出力: Hello33.141592

# 出力: Helloと3そして3.141592
print("{0}と{1}そして{2}".format(hello, number_int, number_float))

# 出力: Helloと3そして3.14
print("{0}と{1}そして{2:.3}".format(hello, number_int, number_float))

print("{0}≒{1:.2}".format(1.05, 1.05))  # 出力: 1.05≒1.1

# 出力: Helloと3そして3.14
print("{}と{}そして{:.3}".format(hello, number_int, number_float))

print("{hel}と{num_int}そして{num_float:.3}".format(
    hel=hello, num_int=number_int, num_float=number_float))  # 出力: Helloと3そして3.14

print(f"{hello}と{number_int}そして{number_float}")  # 出力: Helloと3そして3.141592

print(f"{hello}と{number_int}そして{number_float:.3}")  # 出力: Helloと3そして3.14
