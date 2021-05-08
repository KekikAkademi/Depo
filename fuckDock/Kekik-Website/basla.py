from Lab import app
import os

port = int(os.environ.get("PORT", 8080))

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_AS_ASCII'] = False
    app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
    #app.run(debug = True, host = '0.0.0.0', port = port)
    from waitress import serve
    serve(app, host = "0.0.0.0", port = port)