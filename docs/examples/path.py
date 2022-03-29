from pyl7plot import Plot

data = {
    "type": "FeatureCollection",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "地铁二号线",
                "code": 430101,
                "time": "2010/08/14",
                "SHAPE_LENG": 23177.029881900002,
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            116.365500625550737,
                            39.946474524850942
                        ],
                        [
                            116.366077356117799,
                            39.946706210181567
                        ],
                        [
                            116.380500724307979,
                            39.94888011518406
                        ],
                        [
                            116.400500724307979,
                            39.99888011518406
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "地铁五号线",
                "code": 430101,
                "time": "2010/08/14",
                "SHAPE_LENG": 28448.9320391,
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            116.428898570981829,
                            39.846238382938388
                        ],
                        [
                            116.428135384651128,
                            39.846249956793876
                        ],
                        [
                            116.503098706199344,
                            40.087151016112706
                        ],
                        [
                            116.702880777013451,
                            40.087135944114152
                        ]
                    ]
                ]
            }
        },
    ]
}
pathMap = Plot("Path")

pathMap.set_options({
    "map": {
        "type": "mapbox",
        "style": "light",
        "center": [103.447303, 31.753574],
        "zoom": 7,
    },
    "autoFit": True,
    "source": {
        "data": data,
    },
    "color": {
        "field": "name",
        "value": ["#5B8FF9", "#5CCEA1", "#5D7092"],
    },
    "size": 2,
    "style": {
        "opacity": 0.8,
        "lineType": "dash",
    },
    "state": {"active": {"color": "#FFF684"}},
    "scale": {"position": "bottomright"},
    "legend": {"position": "bottomleft"},
    "tooltip": {
        "items": ["name", "code"],
    },
})

pathMap.render("path-map.html")
