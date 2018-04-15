import os
from datetime import datetime
import jinja2
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(__file__)))
)

jinja_environment.globals['year'] = datetime.now().year


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template(
            'src/templates/index.html'
        )
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
