from flask import Flask
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

jinjaAyar = app.jinja_options.copy()
jinjaAyar.update(dict(
    variable_start_string = '(%',
    variable_end_string = '%)',
    block_start_string='<%',
    block_end_string='%>',
    comment_start_string='<#',
    comment_end_string='#>',
))
app.jinja_options = jinjaAyar


from proje import anaSayfa