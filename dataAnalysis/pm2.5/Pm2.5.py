#!/usr/bin/env python3
# -*- coding: utf-8 -*-




import csv #csv 文件处理
import numpy as np #线性代数库
import pandas as pd # 处理数据
import matplotlib.pyplot as plt#可视化绘制
import seaborn #可视化绘制
#Jupyter book 图片内嵌入网页
# %matplotlib inline



# #读取数据
# Shanghai_data = pd.read_csv('ShanghaiPM20100101_20151231.csv')
#
# # 显示上海数据头五行
# Shanghai_data.head()
#
#
# #显示读取数据的概况
# Shanghai_data.info()
#
#
# # print type of python object
# print(type(Shanghai_data['cbwd'][0]))
#
#
# # 处理数据 将列名规范化：下划线代替原来的空格
# Shanghai_data.columns = [c.replace(' ', '_') for c in Shanghai_data.columns]
# Shanghai_data.head()
#
#
#
#
# #将 season 列完成从分类数据到数值型数据的转换
# Shanghai_data['season'] = Shanghai_data['season'].map({1:'Spring', 2:'Summer', 3:'Autumn', 4: 'Winter'})
# Shanghai_data.head()
#
#
#
# # print the length of data
# print("The number of row in this dataset is ",len(Shanghai_data.index))
#
# # calculating the number of records in column "PM_Jingan"
# print("The number of missing data records in PM_Jingan is: ",
#       len(Shanghai_data.index) - len(Shanghai_data['PM_Jingan'].dropna()))
#
#
# # TO DO: fill in blanks below to load the city's data
# city_data = pd.read_csv('ShanghaiPM20100101_20151231.csv')
#
# city_data.head()
#
#
# city_data.info()



import os

# 打印当前目录下的信息
print(os.listdir('./'))
#
# files = ['BeijingPM20100101_20151231.csv',
#        'ChengduPM20100101_20151231.csv',
#        'GuangzhouPM20100101_20151231.csv',
#        'ShanghaiPM20100101_20151231.csv',
#        'ShenyangPM20100101_20151231.csv']


files = os.listdir('./')

out_columns = ['No', 'year', 'month', 'day', 'hour', 'season', 'PM_US Post']


# create a void dataframe
df_all_cities = pd.DataFrame()


# iterate to write diffrent files
for inx, val in enumerate(files):
    df = pd.read_csv(val)
    df = df[out_columns]
    # create a city column
    df['city'] = val.split('P')[0]
    # map season
    df['season'] = df['season'].map({1:'Spring', 2:'Summer', 3:'Autumn', 4: 'Winter'})
    # append each file and merge all files into one
    df_all_cities = df_all_cities.append(df)

# replace the space in variable names with '_'
df_all_cities.columns = [c.replace(' ', '_') for c in df_all_cities.columns]


df_all_cities.head()


def filter_data(data, condition):
    """
    Remove elements that do not match the condition provided.
    Takes a data list as input and returns a filtered list.
    Conditions should be a list of strings of the following format:
      '<field> <op> <value>'
    where the following operations are valid: >, <, >=, <=, ==, !=

    Example: "duration < 15", "start_city == 'San Francisco'"
    """

    # Only want to split on first two spaces separating field from operator and
    # operator from value: spaces within value should be retained.
    field, op, value = condition.split(" ", 2)

    # check if field is valid
    if field not in data.columns.values:
        raise Exception("'{}' is not a feature of the dataframe. Did you spell something wrong?".format(field))

    # convert value into number or strip excess quotes if string
    try:
        value = float(value)
    except:
        value = value.strip("\'\"")

    # get booleans for filtering
    if op == ">":
        matches = data[field] > value
    elif op == "<":
        matches = data[field] < value
    elif op == ">=":
        matches = data[field] >= value
    elif op == "<=":
        matches = data[field] <= value
    elif op == "==":
        matches = data[field] == value
    elif op == "!=":
        matches = data[field] != value
    else:  # catch invalid operation codes
        raise Exception("Invalid comparison operator. Only >, <, >=, <=, ==, != allowed.")

    # filter data and outcomes
    data = data[matches].reset_index(drop=True)
    return data


def reading_stats(data, filters=[], verbose=True):
    """
    Report number of readings and average PM2.5 readings for data points that meet
    specified filtering criteria.


    Example: ["duration < 15", "start_city == 'San Francisco'"]
    """

    n_data_all = data.shape[0]

    # Apply filters to data
    for condition in filters:
        data = filter_data(data, condition)

    # Compute number of data points that met the filter criteria.
    n_data = data.shape[0]

    # Compute statistics for PM 2.5 readings.
    pm_mean = data['PM_US_Post'].mean()
    pm_qtiles = data['PM_US_Post'].quantile([.25, .5, .75]).as_matrix()

    # Report computed statistics if verbosity is set to True (default).
    if verbose:
        if filters:
            print('There are {:d} readings ({:.2f}%) matching the filter criteria.'.format(n_data,
                                                                                           100. * n_data / n_data_all))
        else:
            print('There are {:d} reading in the dataset.'.format(n_data))

        print('The average readings of PM 2.5 is {:.2f} ug/m^3.'.format(pm_mean))
        print('The median readings of PM 2.5 is {:.2f} ug/m^3.'.format(pm_qtiles[1]))
        print('25% of readings of PM 2.5 are smaller than {:.2f} ug/m^3.'.format(pm_qtiles[0]))
        print('25% of readings of PM 2.5 are larger than {:.2f} ug/m^3.'.format(pm_qtiles[2]))
        seaborn.boxplot(data['PM_US_Post'], showfliers=False)
        plt.title('Boxplot of PM 2.5 of filtered data')
        plt.xlabel('PM_US Post (ug/m^3)')

    # Return three-number summary
    return data



df_test = reading_stats(df_all_cities, ["city == 'Shanghai'", "year >= 2012"])
df_test.info()






df2 = reading_stats(df_all_cities, ["city == 'Chengdu'", "year >= 2010"])
df3 = reading_stats(df_all_cities, ["city == 'Guangzhou'", "year >= 2010"])
df4 = reading_stats(df_all_cities, ["city == 'Shanghai'", "year >= 2010"])
df5 = reading_stats(df_all_cities, ["city == 'Beijing'", "year >= 2010"])
df6 = reading_stats(df_all_cities, ["city == 'Shenyang'", "year >= 2010"])






