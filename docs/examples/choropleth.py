from pyl7plot import Plot

choroplethMap = Plot("Choropleth")

choroplethMap.set_options({
    "map": {
        "type": "mapbox",
        "style": "light",
        "center": [103.447303, 31.753574],
        "zoom": 7,
    },
    "autoFit": True,
    "viewLevel": {
        "level": "world",
        "adcode": "all",
    },
    "source": {
        "data": [
            {"name": "中华人民共和国", "value": 200},
            {"name": "美国", "value": 250},
            {"name": "俄罗斯", "value": 180},
            {"name": "日本", "value": 120},
            {"name": "加拿大", "value": 130},
            {"name": "澳大利亚", "value": 130},
            {"name": "新加坡", "value": 170},
            {"name": "巴西", "value": 80},
        ],
        "joinBy": {"sourceField": "name", "geoField": "name"},
    },
    "color": {
        "field": "value",
        "value": ["#B8E1FF", "#7DAAFF", "#3D76DD", "#0047A5", "#001D70"],
    },
    "style": {
        "opacity": 1,
        "stroke": "#ccc",
        "lineWidth": 0.6,
        "lineOpacity": 1,
    },
    "label": {
        "visible": True,
        "field": "name",
        "style": {
            "fill": "#000",
            "opacity": 0.8,
            "fontSize": 10,
            "stroke": "#fff",
            "strokeWidth": 1.5,
            "textAllowOverlap": False,
            "padding": [5, 5],
        },
    },
    "chinaBorder": False,
    "state": {"active": True, "select":  True},
    "legend": {"position": "bottomleft"},
    "tooltip": {
        "items": ["name", "adcode", "value"],
    },
})

choroplethMap.render("choropleth-map.html")
