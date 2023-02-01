from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    FLASK_ADMIN_NAME: str = "Admin"
    FLASK_ADMIN_TEMPLATE_MODE: str = "bootstrap3"
    FLASK_ADMIN_SWATCH: str = "cerulean"
    SQLALCHEMY_DATABASE_URI: str = (
        "postgresql://postgres:postgres@localhost:5432/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TITLE: str = "Template"
    SECRET_KEY: str = "jadkfbsdkjbfbh"
    PASSWORD_SCHEMES: list[str] = ["pbkdf2_sha512", "md5_crypt"]
    EXTENSIONS: list[str] = [
        "src.ext.appearance:init_app",
        "src.ext.database:init_app",
        "src.ext.migrations:init_app",
        "src.ext.auth:init_app",
        "src.blueprints.webui:init_app",
        "src.blueprints.restapi:init_app",
        "src.auth.blueprints.webui:init_app",
    ]

    TEMPLATES_AUTO_RELOAD: bool = True
    DEBUG_TOOLBAR_ENABLED: bool = True
    DEBUG_TB_INTERCEPT_REDIRECTS: bool = False
    DEBUG_TB_PROFILER_ENABLED: bool = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED: bool = True
    DEBUG_TB_PANELS: list[str] = [
        "flask_debugtoolbar.panels.versions.VersionDebugPanel",
        "flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel",
        "flask_debugtoolbar.panels.timer.TimerDebugPanel",
        "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
        "flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
        "flask_debugtoolbar.panels.template.TemplateDebugPanel",
        "flask_debugtoolbar.panels.route_list.RouteListDebugPanel",
        "flask_debugtoolbar.panels.logger.LoggingPanel",
        "flask_debugtoolbar.panels.profiler.ProfilerDebugPanel",
        "flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel",
    ]


settings = Settings()
