import uuid
from jinja2 import Environment
from pyl7plot.engine import Engine
from pyl7plot.helper.code import json_dump_to_js
from pyl7plot.helper.file import write_utf8_file
from pyl7plot.helper.html import HTML
from typing import Optional

L7PLOT_LIB = 'https://unpkg.com/@antv/l7plot@0'


class Plot():
    '''
    instance with plot type string
    '''

    def __init__(self, plot_type: str):
        self.plot_type = plot_type
        self.plot_id = uuid.uuid4().hex
        self.options = {}

        # page settting
        self.page_title = "PyL7Plot"

    '''
    set the L7Plot options, documents [here](https://l7plot.antv.vision/)
    '''

    def set_options(self, options: object):
        self.options = options
        return self

    '''
    get the JavaScript options of L7Plot
    '''

    def dump_js_options(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        return json_dump_to_js(self.options)

    '''
    render plot into jupyter
    '''

    def render_notebook(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> HTML:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="notebook.html",
            **kwargs
        ))

    '''
    render plot into jupyter lab
    '''

    def render_jupyter_lab(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> HTML:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="jupyter-lab.html",
            **kwargs
        ))

    '''
    render plot to html string
    '''

    def render_html(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        self.dependencies = [{
            "name": "L7Plot",
            "asset": L7PLOT_LIB,
        }]
        # get html string
        return Engine(env=env).render(
            plot=self,
            template_name="plot.html",
            **kwargs
        )

    '''
    render the plot into html file
    '''

    def render(
        self,
        path: str = "plot.html",
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        # get html string
        html = self.render_html(env, **kwargs)
        # write output into file
        write_utf8_file(path, html)
        return path
