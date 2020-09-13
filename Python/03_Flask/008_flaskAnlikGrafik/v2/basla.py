from proje import app
import os
from flask import send_from_directory

port = int(os.environ.get("PORT", 5000))

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), filename='img/favicon.ico', mimetype='image/x-icon')

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_AS_ASCII'] = False
    app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
    app.run(debug = True, host = '0.0.0.0', port = port)
    # from waitress import serve
    # serve(app, host = "0.0.0.0", port = port)