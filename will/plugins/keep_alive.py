from bottle import route, run, template
from will.plugin_base import WillPlugin


@route("/keep-alive")
def keep_alive():
    return "Alive"