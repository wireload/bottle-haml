import functools
import haml

from bottle import template, DEBUG, BaseTemplate

# Use two spaces for indention in generated HTML
# code instead of \t
haml.codegen.Generator.indent_str = "  "


class HamlTemplate(BaseTemplate):

    extensions = ['haml']

    def prepare(self, **options):
        from mako.template import Template
        from mako.lookup import TemplateLookup

        options.update({'input_encoding': self.encoding})
        options.setdefault('format_exceptions', bool(DEBUG))
        lookup = TemplateLookup(directories=self.lookup, **options)
        options['preprocessor'] = haml.preprocessor

        if self.source:
            self.tpl = Template(self.source, lookup=lookup, **options)
        else:
            self.tpl = Template(uri=self.name, filename=self.filename, lookup=lookup, **options)

    def render(self, *args, **kwargs):
        for dictarg in args:
            kwargs.update(dictarg)
        _defaults = self.defaults.copy()
        _defaults.update(kwargs)
        return self.tpl.render(**_defaults)

haml_template = functools.partial(template, template_adapter=HamlTemplate)
