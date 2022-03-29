<img src="https://gw.alipayobjects.com/zos/antfincdn/R8sN%24GNdh6/language.svg" width="18"> English | [简体中文](./README.zh-CN.md)

# PyL7Plot

🌍 Python3 binding for [`@AntV/L7Plot`](https://github.com/antvis/L7Plot) Plotting Library. Geospatial Visualization Chart Library Based on `@AntV/L7`. Inspired by `PyG2Plot`.

[![Latest Stable Version](https://img.shields.io/pypi/v/pyl7plot.svg)](https://pypi.python.org/pypi/pyl7plot)
[![build Status](https://github.com/lvisei/pyl7plot/workflows/build/badge.svg?branch=main)](https://github.com/lvisei/pyl7plot/actions?query=workflow%3Abuild)
[![Pypi Download](https://img.shields.io/pypi/dm/pyl7plot)](https://pypi.python.org/pypi/pyl7plot)

<div align="center">
  <img src="https://user-images.githubusercontent.com/26923747/160286530-aec01c97-a56b-4ea9-9fc6-f245d8f7b871.png" width="800">
</div>

## Installation

```bash
$ pip install pyl7plot
```

## Usage

#### **Render to HTML**

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

# Render html file
dot.render("dot.html")

# Or render html string
# dot.render_html()
```

![image](https://gw.alipayobjects.com/zos/antfincdn/Yn%24QslMAWP/20220326145659.jpg)

#### **Render in Jupyter**

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
  "height": 400, # set a default height in jupyter preview
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
    # Use JS API, you can use JavaScript syntax for callback.
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

# Render in notebook
dot.render_notebook()

# Or render in jupyter lab
# dot.render_jupyter_lab()
```

> More Online Examples PyL7plot in [Jupyter Lab](https://colab.research.google.com/drive/11gTHsZ5Xg31jjJUJWEt5PkZv0VE9qyAG?usp=sharing).

## API

- **Plot**

1. _Plot(plot_type: str)_: get an instance of `Plot` class.

2. _plot.set_options(options: object)_: set the options of [L7Plot](https://l7plot.antv.vision/) into instance.

3. _plot.render(path, env, \*\*kwargs)_: render out html file by setting the path, jinja2 env and kwargs.

4. _plot.render_notebook(env, \*\*kwargs)_: render plot on jupyter preview.

5. _plot.render_jupyter_lab(env, \*\*kwargs)_: render plot on jupyter lab preview.

6. _plot.render_html(env, \*\*kwargs)_: render out html string by setting jinja2 env and kwargs.

## 协议

[MIT](./LICENSE)
