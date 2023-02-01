from importlib import import_module

from src.config import settings


def load_extensions(app):
    for extension in settings.EXTENSIONS:
        # Split data in form `extension.path:factory_function`
        module_name, factory = extension.split(":")
        # Dynamically import extension module.
        ext = import_module(module_name)
        # Invoke factory passing app.
        getattr(ext, factory)(app)


def init_app(app, **config):
    app.config.from_object(settings)
