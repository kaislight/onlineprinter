import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/28329/Documents/WeChat Files/wxid_xh5qcr375gd112/FileStorage/File/2022-01/retail/food/result/1.CSV',encoding='gbk') #filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
print (df.head())
print (df.tail())
