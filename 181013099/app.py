import pandas as pd
from flask import Flask
from flask import render_template, request, redirect
from pyecharts.charts import EffectScatter, Bar, Line, WordCloud, Map, Grid, Pie
from pyecharts.charts import Scatter
import numpy as np
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline
from pyecharts.faker import Faker

app = Flask(__name__)


@app.route('/')
def index_bar():
    df = pd.read_csv("./static/data/laji.csv")
    tl = Timeline()
    for i in range(2009, 2018):
        pie = (
            Pie()
                .add(
                "数值",
                list(zip(list(df.地区), list(df["{}".format(i)]))),
                rosetype="radius",
                radius=["30%", "55%"],
            )
                .set_global_opts(title_opts=opts.TitleOpts())
        )
        tl.add(pie, "{}".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text=''' 由上可见，人口的确是垃圾产量的一大原因。人口越多的地方，垃圾清运量越高，如广州，而西藏等人少的地方垃圾清运量很低''', text1='''我对影响垃圾无害化处理的因素的猜测如下：
                        1.高纬度的地方天气寒冷，卫生填埋在地下分解的时间很长，因此导致无害化处理的进度缓慢。
                        2.西藏等地区，并不进行农业，堆肥的无害化处理方式并不适合此些地区，也将导致其无法无害化处理垃圾
                        3.人口密度高的地区无法进行焚烧、填埋，因为人类生活用地面积就极大''')


@app.route('/people_laji')
def index_bar_every_1_tp():
    df = pd.read_csv("./static/data/renkou.csv")
    x = list(df.地区)
    tl = Timeline()
    for i in range(2009, 2018):
        bar = (
            Bar()
                .add_xaxis(x)
                .add_yaxis("各省垃圾清运量", list(df["{}".format(i)]))
                .add_yaxis("各省人口", list(df["{}".format(i)]))
                .reversal_axis()
                .set_global_opts(title_opts=opts.TitleOpts("{}年各省产生垃圾与人口对比".format(i)),
                                 datazoom_opts=opts.DataZoomOpts(orient="vertical"))
                .set_series_opts(
                label_opts=opts.LabelOpts(is_show=False),
            )
        )
        tl.add(bar, "{}".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text='''
                           由上可见，人口的确是垃圾产量的一大原因。人口越多的地方，垃圾清运量越高，如广州，而西藏等人少的地方垃圾清运量很低
                           ''', text1='''我对影响垃圾无害化处理的因素的猜测如下：
                        1.高纬度的地方天气寒冷，卫生填埋在地下分解的时间很长，因此导致无害化处理的进度缓慢。
                        2.西藏等地区，并不进行农业，堆肥的无害化处理方式并不适合此些地区，也将导致其无法无害化处理垃圾
                        3.人口密度高的地区无法进行焚烧、填埋，因为人类生活用地面积就极大''')


@app.route('/people_laji_map')
def index_bar_every():
    df = pd.read_csv("./static/data/renkou.csv")
    tl = Timeline()
    for i in range(2009, 2018):
        map0 = (
            Map()
                .add(
                "垃圾清运量（单位：万吨）", list(zip(list(df.地区), list(df["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}各省垃圾清运量".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=min(list(df["{}".format(i)])),
                                                  max_=max(list(df["{}".format(i)]))),

            )
        )
        tl.add(map0, "{}".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text='''
                           由上可见，广东的垃圾清运量十分巨大，在2009-2018期间，广东的垃圾清运量始终是占比最高的。
                            除此之外，随着年份的增加，其他省份的垃圾清运量也在上升，如浙江、山东，已经从绿色变成了黄色
                           ''', text1='''我对影响垃圾无害化处理的因素的猜测如下：
                        1.高纬度的地方天气寒冷，卫生填埋在地下分解的时间很长，因此导致无害化处理的进度缓慢。
                        2.西藏等地区，并不进行农业，堆肥的无害化处理方式并不适合此些地区，也将导致其无法无害化处理垃圾
                        3.人口密度高的地区无法进行焚烧、填埋，因为人类生活用地面积就极大''')


@app.route('/wuhai')
def index_bar_every_4():
    df = pd.read_csv("./static/data/wuhai.csv")
    tl = Timeline()
    for i in range(2009, 2018):
        map0 = (
            Map()
                .add(
                "垃圾无害化清理率（单位：百分比）", list(zip(list(df.地区), list(df["{}".format(i)]))), "china",
                is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}各省垃圾无害化清理率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=min(list(df["{}".format(i)])),
                                                  max_=max(list(df["{}".format(i)]))),

            )
        )
        tl.add(map0, "{}".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text='''
                           垃圾无害化处理的工艺主要有:卫生填埋、堆肥和焚烧三种。
                由垃圾无害化处理率地图可见，一开始，各省的处理率都十分不平均，高的高达97，低的低达29，西藏在2016年之前甚至没有数据。直到2016年后，全国的垃圾无害化处理都基本达到了90%。
                          ''', text1='''我对影响垃圾无害化处理的因素的猜测如下：
                        1.高纬度的地方天气寒冷，卫生填埋在地下分解的时间很长，因此导致无害化处理的进度缓慢。
                        2.西藏等地区，并不进行农业，堆肥的无害化处理方式并不适合此些地区，也将导致其无法无害化处理垃圾
                        3.人口密度高的地区无法进行焚烧、填埋，因为人类生活用地面积就极大''')


if __name__ == '__main__':
    app.run(debug=True)
