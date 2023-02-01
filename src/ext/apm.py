from elasticapm.contrib.flask import ElasticAPM

elasticapm = ElasticAPM()


def init_app(app):
    elasticapm.init_app(app)
