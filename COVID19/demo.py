#https://blog.csdn.net/sjjsaaaa/article/details/107129879

import requests  #导入第三方库
import json #  轻量级的数据交互格式
import jsonpath  # 类似正则表达式  提取数据，信息抽取类库

#import pyecharts
from pyecharts.charts import Map  #地图matplotlib   :静态图
from pyecharts import options as opts  #配置项
from demo1 import nameMap    #自己写的模块  引入


#爬取全球疫情数据
#数据源
url='https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
resp = requests.post(url).text  #get post  对网址post请求
# print(resp)     #字符串

data = json.loads(resp)   #string——dict  方便后期提取内容
# print(type(data))

#1提取国家名字  病死率数量
name=jsonpath.jsonpath(data,"$..name")   #从网页源代码提取名字
print(name)


#  #病死率数量
confirm=jsonpath.jsonpath(data,"$..confirm")  #提取数据
print(confirm)


# 整理数据 zip
a = list(zip(name,confirm))
print(a)

#  可视化地图分析
map_ = Map(opts.InitOpts(width='1200px',height='600px')).add(series_name="世界各国的病死率",
                                                          data_pair = a,#输入数据
                                                          maptype = "world",#设置地图类型，世界地图
                                                          name_map = nameMap,#设置地图颜色分布
                                                          is_map_symbol_show=False
                                                         )

#设置系列配置项
map_.set_series_opts(lable_opts=opts.LabelOpts(is_show=False))


#设置全局配置项
map_.set_global_opts(title_opts=opts.TitleOpts(title="国外疫情情况"),#设置标题
                    visualmap_opts=opts.VisualMapOpts(max_=3000000,is_piecewise=True))#显示图例


#展现为地图的形式
map_.render("国外疫情情况.html")#以图表方式保存
