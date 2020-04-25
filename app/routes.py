import json
from app import app
import random
from flask import render_template
from pyecharts import options as opts
from pyecharts.charts import Bar



def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [random.randint(10, 100) for _ in range(6)])
        .add_yaxis("商家B", [random.randint(10, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""))
    )
    return c


@app.route("/")
def index():
    return render_template("echart.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


@app.route("/stars")
def star():
    return render_template("stars.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/study")
def study():
    return render_template("study.html")

import pandas as pd
@app.route("/data")
def data():
    cvsdata = pd.read_csv("/static/text/data.csv")
    return cvsdata

