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
                            116.368156824000266,
                            39.947572964936114
                        ],
                        [
                            116.36838301301448,
                            39.94766696430289
                        ],
                        [
                            116.368417291803468,
                            39.947681036715984
                        ],
                        [
                            116.368787460460396,
                            39.947833141044228
                        ],
                        [
                            116.368998156087471,
                            39.947909643995608
                        ],
                        [
                            116.370412460816695,
                            39.948359180907097
                        ],
                        [
                            116.370478927129824,
                            39.948377294805347
                        ],
                        [
                            116.370548031529694,
                            39.948394403026434
                        ],
                        [
                            116.37075004487798,
                            39.948439732250279
                        ],
                        [
                            116.370940357870779,
                            39.948479042616903
                        ],
                        [
                            116.371258392614152,
                            39.948540525680201
                        ],
                        [
                            116.371949687673265,
                            39.948628938417258
                        ],
                        [
                            116.3719543845299,
                            39.948629535827614
                        ],
                        [
                            116.373885825284404,
                            39.94874904324594
                        ],
                        [
                            116.375683379915031,
                            39.948827212159721
                        ],
                        [
                            116.376544248293598,
                            39.948838132399935
                        ],
                        [
                            116.377215783650328,
                            39.948845608711416
                        ],
                        [
                            116.379011116449078,
                            39.948865524859826
                        ],
                        [
                            116.379026486516935,
                            39.948865696046042
                        ],
                        [
                            116.37934298141748,
                            39.94886673687882
                        ],
                        [
                            116.379933211014844,
                            39.948877211200085
                        ],
                        [
                            116.379938416406915,
                            39.948877303287652
                        ],
                        [
                            116.380500724307979,
                            39.94888011518406
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
                            116.427351928182389,
                            39.846271951947919
                        ],
                        [
                            116.427191941466646,
                            39.846276626004183
                        ],
                        [
                            116.426413076385273,
                            39.84629935264978
                        ],
                        [
                            116.403873632779764,
                            40.087322148730152
                        ],
                        [
                            116.403582209955772,
                            40.087227189874326
                        ],
                        [
                            116.403486144331239,
                            40.087202201337995
                        ],
                        [
                            116.403334752451613,
                            40.08717722048528
                        ],
                        [
                            116.403098706199344,
                            40.087151016112706
                        ],
                        [
                            116.402880777013451,
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
    "tooltip": {
        "items": ["name", "code"],
    },
})

pathMap.render("path-map.html")
