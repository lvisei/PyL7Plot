from pyl7plot import Plot

data = [
    {
        "lng": 105.005,
        "lat": 32.349,
        "depth": 10,
        "mag": 5.2,
        "time": 1212640865530,
        "title": "M 5.2 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 104.602,
        "lat": 32.067,
        "depth": 10,
        "mag": 5,
        "time": 1212462569360,
        "title": "M 5.0 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 105.272,
        "lat": 32.451,
        "depth": 10,
        "mag": 5.2,
        "time": 1211177214760,
        "title": "M 5.2 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 105.042,
        "lat": 32.402,
        "depth": 10,
        "mag": 5,
        "time": 1211170138690,
        "title": "M 5.0 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 104.982,
        "lat": 32.24,
        "depth": 9,
        "mag": 5.8,
        "time": 1211044105480,
        "title": "M 5.8 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 103.665,
        "lat": 31.29,
        "depth": 10,
        "mag": 5,
        "time": 1210969012190,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 103.351,
        "lat": 31.355,
        "depth": 3,
        "mag": 5.6,
        "time": 1210915547320,
        "title": "M 5.6 - eastern Sichuan, China"
    },
    {
        "lng": 104.214,
        "lat": 31.66,
        "depth": 10,
        "mag": 5.1,
        "time": 1210798867000,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 104.014,
        "lat": 31.356,
        "depth": 10,
        "mag": 5.1,
        "time": 1210757203950,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 104.032,
        "lat": 31.996,
        "depth": 10,
        "mag": 5.1,
        "time": 1210744497980,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 103.518,
        "lat": 31.325,
        "depth": 18.8,
        "mag": 5.4,
        "time": 1210733679980,
        "title": "M 5.4 - eastern Sichuan, China"
    },
    {
        "lng": 105.275,
        "lat": 32.416,
        "depth": 10,
        "mag": 5,
        "time": 1210663156260,
        "title": "M 5.0 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 103.194,
        "lat": 30.89,
        "depth": 9,
        "mag": 5.8,
        "time": 1210662428500,
        "title": "M 5.8 - eastern Sichuan, China"
    },
    {
        "lng": 103.682,
        "lat": 31.205,
        "depth": 10,
        "mag": 5,
        "time": 1210647638330,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 103.53,
        "lat": 31.298,
        "depth": 10,
        "mag": 5.1,
        "time": 1210636486860,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 103.527,
        "lat": 31.282,
        "depth": 10,
        "mag": 5.2,
        "time": 1210635978970,
        "title": "M 5.2 - eastern Sichuan, China"
    },
    {
        "lng": 104.454,
        "lat": 31.746,
        "depth": 32.7,
        "mag": 5.3,
        "time": 1210625134820,
        "title": "M 5.3 - eastern Sichuan, China"
    },
    {
        "lng": 103.889,
        "lat": 31.413,
        "depth": 21.7,
        "mag": 5.6,
        "time": 1210622930430,
        "title": "M 5.6 - eastern Sichuan, China"
    },
    {
        "lng": 103.524,
        "lat": 31.178,
        "depth": 34.8,
        "mag": 5,
        "time": 1210614875910,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 103.514,
        "lat": 31.058,
        "depth": 10,
        "mag": 5,
        "time": 1210606133440,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 104.575,
        "lat": 31.952,
        "depth": 10,
        "mag": 5.1,
        "time": 1210604939660,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 103.692,
        "lat": 31.243,
        "depth": 17.4,
        "mag": 5,
        "time": 1210604731260,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 104.65,
        "lat": 32.12,
        "depth": 18.3,
        "mag": 5,
        "time": 1210601727380,
        "title": "M 5.0 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 103.511,
        "lat": 31.028,
        "depth": 10,
        "mag": 5,
        "time": 1210599654130,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 103.618,
        "lat": 31.214,
        "depth": 10,
        "mag": 6.1,
        "time": 1210590662480,
        "title": "M 6.1 - eastern Sichuan, China"
    },
    {
        "lng": 103.365,
        "lat": 30.966,
        "depth": 10,
        "mag": 5,
        "time": 1210587820080,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 104.092,
        "lat": 31.527,
        "depth": 10,
        "mag": 5.5,
        "time": 1210585344860,
        "title": "M 5.5 - eastern Sichuan, China"
    },
    {
        "lng": 103.682,
        "lat": 31.206,
        "depth": 10,
        "mag": 5,
        "time": 1210583220430,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 104.052,
        "lat": 31.503,
        "depth": 10,
        "mag": 5,
        "time": 1210580499930,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 103.53,
        "lat": 31.1,
        "depth": 10,
        "mag": 5,
        "time": 1210579858350,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 103.625,
        "lat": 31.243,
        "depth": 10,
        "mag": 5.1,
        "time": 1210577682540,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 105.134,
        "lat": 32.165,
        "depth": 10,
        "mag": 5,
        "time": 1210575905390,
        "title": "M 5.0 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 104.217,
        "lat": 31.636,
        "depth": 10,
        "mag": 5.3,
        "time": 1210575694040,
        "title": "M 5.3 - eastern Sichuan, China"
    },
    {
        "lng": 104.908,
        "lat": 32.195,
        "depth": 10,
        "mag": 5,
        "time": 1210575642660,
        "title": "M 5.0 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 103.646,
        "lat": 31.216,
        "depth": 10,
        "mag": 5,
        "time": 1210575628970,
        "title": "M 5.0 - eastern Sichuan, China"
    },
    {
        "lng": 104.638,
        "lat": 31.857,
        "depth": 10,
        "mag": 5.1,
        "time": 1210575454870,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 103.747,
        "lat": 31.146,
        "depth": 10,
        "mag": 5.3,
        "time": 1210575258100,
        "title": "M 5.3 - eastern Sichuan, China"
    },
    {
        "lng": 105.202,
        "lat": 32.372,
        "depth": 10,
        "mag": 5.1,
        "time": 1210575210090,
        "title": "M 5.1 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 104.481,
        "lat": 31.906,
        "depth": 10,
        "mag": 5.1,
        "time": 1210575036930,
        "title": "M 5.1 - eastern Sichuan, China"
    },
    {
        "lng": 105.234,
        "lat": 32.436,
        "depth": 10,
        "mag": 5.3,
        "time": 1210574939120,
        "title": "M 5.3 - Sichuan-Gansu border region, China"
    },
    {
        "lng": 104.705,
        "lat": 31.272,
        "depth": 10,
        "mag": 5.4,
        "time": 1210574637160,
        "title": "M 5.4 - eastern Sichuan, China"
    },
    {
        "lng": 103.715,
        "lat": 31.211,
        "depth": 10,
        "mag": 5.8,
        "time": 1210574594360,
        "title": "M 5.8 - eastern Sichuan, China"
    },
    {
        "lng": 104.682,
        "lat": 31.342,
        "depth": 10,
        "mag": 5.7,
        "time": 1210574528950,
        "title": "M 5.7 - eastern Sichuan, China"
    },
    {
        "lng": 104.032,
        "lat": 31.586,
        "depth": 10,
        "mag": 5.7,
        "time": 1210574516000,
        "title": "M 5.7 - eastern Sichuan, China"
    },
    {
        "lng": 104.787,
        "lat": 31.968,
        "depth": 10,
        "mag": 5.2,
        "time": 1210574486530,
        "title": "M 5.2 - eastern Sichuan, China"
    },
    {
        "lng": 103.322,
        "lat": 31.002,
        "depth": 19,
        "mag": 7.9,
        "time": 1210573681570,
        "title": "M 7.9 - eastern Sichuan, China"
    }
]

heatMap = Plot("Heatmap")

heatMap.set_options({
    "map": {
        "type": "mapbox",
        "style": "light",
        "center": [103.447303, 31.753574],
        "zoom": 7,
    },
    "autoFit": True,
    "source": {
        "data": data,
        "parser": {"type": "json", "x": "lng", "y": "lat"},
    },
    "size": {
        "field": "mag",
    },
    "style": {
        "intensity": 3,
        "radius": 20,
        "opacity": 1,
        "colorsRamp": [
            {"color": '#206C7C', "position": 0},
            {"color": '#2EA9A1 ', "position": 0.2},
            {"color": '#91EABC', "position": 0.4},
            {"color": '#FFF598', "position": 0.6},
            {"color": '#F7B74A', "position": 0.8},
            {"color": '#FF4818', "position": 1},
        ],
    },
    "legend": {"position": "bottomleft"},
    "scale": {"position": "bottomright"},
})

heatMap.render("heat-map.html")
