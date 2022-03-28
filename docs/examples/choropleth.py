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
    "source": {
        "data": [],
        "joinBy": {"sourceField": "code", "geoField": "adcode"},
    },
    "color": {
        "field": "mag",
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
        "items": ["name", "adcode"],
    },
})

choroplethMap.render("choropleth-map.html")
