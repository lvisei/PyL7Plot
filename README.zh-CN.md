<img src="https://gw.alipayobjects.com/zos/antfincdn/R8sN%24GNdh6/language.svg" width="18"> [English](./README.md) | 简体中文

# PyL7Plot

🌍 PyL7Plot 是 [`@AntV/L7Plot`](https://github.com/antvis/L7Plot) 在 Python3 上的封装。L7Plot 是基于 L7 的地理空间可视化图表库。

[![Latest Stable Version](https://img.shields.io/pypi/v/pyl7plot.svg)](https://pypi.python.org/pypi/pyl7plot)
[![build Status](https://github.com/hustcc/pyl7plot/workflows/build/badge.svg?branch=main)](https://github.com/hustcc/pyl7plot/actions?query=workflow%3Abuild)
[![Pypi Download](https://img.shields.io/pypi/dm/pyl7plot)](https://pypi.python.org/pypi/pyl7plot)

## 安装

```bash
$ pip install pyl7plot
```

## 使用

#### **渲染成 HTML**

```py
from pyl7plot import Plot

dot = Plot("Dot")

dot.set_options({
  "map": {
    "type": "mapbox",
    "style": "light",
    "center": [103.447303, 31.753574],
    "zoom": 7,
  },
  "autoFit": True,
  "source": {
    "data": [
       { "lng": 103.715, "lat": 31.211, "depth": 10, "mag": 5.8, "title": "M 5.8 - eastern Sichuan, China" },
       { "lng": 104.682, "lat": 31.342, "depth": 10, "mag": 5.7, "title": "M 5.7 - eastern Sichuan, China" },
       # ...
    ],
    "parser": { "type": "json", "x": "lng", "y": "lat" },
  },
  "color": {
    "field": "mag",
    "value": ["#82cf9c", "#10b3b0", "#2033ab"],
    "scale": { "type": "quantize" },
  },
  "size": {
    "field": "mag",
  },
  "state": { "active": True },
  "scale": { "position": "bottomright" },
  "legend": { "position": "bottomleft" },
  "tooltip": {
    "items": ["title", "mag", "depth"],
  },
})

# 渲染成 html 文件
dot.render("dot.html")

# 或者渲染成 html 字符串
# dot.render_html()
```

![image](https://gw.alipayobjects.com/zos/antfincdn/Yn%24QslMAWP/20220326145659.jpg)

#### **在 Jupyter 中使用**

```py
from pyl7plot import Plot, JS

dot = Plot("Dot")

dot.set_options({
  "map": {
    "type": "mapbox",
    "style": "light",
    "center": [103.447303, 31.753574],
    "zoom": 7,
  },
  "autoFit": True,
  "source": {
    "data": [
       { "lng": 103.715, "lat": 31.211, "depth": 10, "mag": 5.8, "title": "M 5.8 - eastern Sichuan, China" },
       { "lng": 104.682, "lat": 31.342, "depth": 10, "mag": 5.7, "title": "M 5.7 - eastern Sichuan, China" },
       # ...
    ],
    "parser": { "type": "json", "x": "lng", "y": "lat" },
  },
  "color": {
    "field": "mag",
    "value": ["#82cf9c", "#10b3b0", "#2033ab"],
    "scale": { "type": "quantize" },
  },
  "size": {
    "field": "mag",
    "value": JS('''function({ mag }) {
        return (mag - 4.3) * 10;
      }''')
  },
  "state": { "active": True },
  "scale": { "position": "bottomright" },
  "legend": { "position": "bottomleft" },
  "tooltip": {
    "items": ["title", "mag", "depth"],
  },
})

# 渲染到 notebook
dot.render_notebook()

# 或者渲染到 jupyter lab
# dot.render_jupyter_lab()
```

## API

- **Plot**

1. _Plot(plot_type: str)_: 获取 `Plot` 对应的类实例。

2. _plot.set_options(options: object)_: 给图表实例设置一个 [L7Plot](https://l7plot.antv.vision/) 图形的配置，文档可以直接参考 L7Plot 官网，未进行任何二次数据结构包装。

3. _plot.render(path, env, \*\*kwargs)_: 渲染出一个 HTML 文件，同时可以传入文件的路径，以及 jinja2 env 和 kwargs 参数。

4. _plot.render_notebook(env, \*\*kwargs)_: 将图形渲染到 jupyter 的预览。

5. _plot.render_jupyter_lab(env, \*\*kwargs)_: 将图形渲染到 jupyter lab 的预览。

6. _plot.render_html(env, \*\*kwargs)_: 渲染出 HTML 字符串，同时可以传入 jinja2 env 和 kwargs 参数。

7. _plot.dump_js_options(env, \*\*kwargs)_: 输出 Javascript 的 option 配置结构，同时可以传入 jinja2 env 和 kwargs 参数，可以用于 Server 中的 HTTP 结构返回数据结构。

## 协议

[MIT](./LICENSE)
