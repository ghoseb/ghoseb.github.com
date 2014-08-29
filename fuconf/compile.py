#!/usr/bin/env python
import codecs
from jinja2 import Environment, FileSystemLoader

PUBLISH_ROOT = '.'
TEMPLATE_ROOT = './templates'
JINJA_ENV = Environment(loader=FileSystemLoader(TEMPLATE_ROOT))

templates = ["index.html", "about.html", "register.html", "schedule.html", "sponsor.html", "venue.html"]

for template_file in templates:
    template = JINJA_ENV.get_template("%s" % template_file)
    rendered_html = template.render()

    with codecs.open("%s/%s" % (PUBLISH_ROOT, template_file), "w", encoding="utf-8") as output_file:
        output_file.write(unicode(rendered_html))

print "Done"
