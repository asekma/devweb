import flask
import datetime
import markupsafe
import math

app = flask.Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
    return "<h1>Hello World!</h1>Page générée le " + now

@app.route('/about/')
def about() :
    return "<p> R209 - TD1 - © Ali SEKMA </p>"

@app.route('/client/')
def client_socket() :
    return f"Socket client : {flask.request.remote_addr}:{flask.request.environ.get('REMOTE_PORT')}"

@app.route('/color/')
@app.route('/color/<color_name>')
def color(color_name='MediumSlateBlue'):
    color_name = markupsafe.escape(color_name)
    return f"""Couleur <code>{color_name}</code>
               <span style="background: {color_name}">
               &nbsp;&nbsp;&nbsp;&nbsp;</span>"""
'''
@app.route('/page/<int(signed=True):nb>')
def page(nb) :
    return f"Visualisation de la page n°{nb}"
'''

@app.route('/page/<int:nb>')
def page(nb):
    if nb > 10:
        url_dynamique = flask.url_for('page', nb=1)
        return flask.redirect(url_dynamique)
    else:
        more = nb + 1
        url_dynamique = flask.url_for('page', nb=more)
        url_statique = flask.url_for('about')
        return f"""Visualisation de la page n°{nb}<br>
            <a href="{url_dynamique}">Page suivante</a><br>
            <a href="{url_statique}">À propos...</a>"""

@app.route('/sqrt/<float:x>')
def sqrt(x) :
    return f"&#8730;{x}={math.sqrt(x)}"

#app.add_url_rule('/client/', view_func=client_socket)
#app.add_url_rule('/about/', view_func=about)

if __name__ == '__main__':
    app.run(debug=True, port=5001)