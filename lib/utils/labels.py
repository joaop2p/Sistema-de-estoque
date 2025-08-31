from lib.src.config.app_config import AppConfig
from .label_keys import LabelKey

class Labels:
    config = AppConfig.get_instance()
    _LANG_PT = {
        LabelKey.APP_TITLE: "Sistema de Estoque",
        LabelKey.WELCOME: "Bem-vindo",
        LabelKey.LOGIN_MESSAGE: "Entrar",
        LabelKey.LOGIN_FIELD: 'Usuário',
        LabelKey.PASSWORD_FIELD: 'Senha',
        LabelKey.MAIL_FIELD: 'E-mail',
        LabelKey.COFIRM_PASSWORD: 'Confirmar Senha',
        LabelKey.SIGN_IN: 'Entrar',
        LabelKey.SIGN_UP: 'Cadastrar'
    }
    _LANG_EN = {
        LabelKey.APP_TITLE: "Inventory System",
        LabelKey.WELCOME: "Welcome",
        LabelKey.LOGIN_MESSAGE: "Login",
        LabelKey.LOGIN_FIELD: 'User',
        LabelKey.PASSWORD_FIELD: 'Password',
        LabelKey.MAIL_FIELD: 'E-mail',
        LabelKey.COFIRM_PASSWORD: 'Confirm password',
        LabelKey.SIGN_IN: 'Sign In',
        LabelKey.SIGN_UP: 'Sign Up'
    }
    _LANGS: dict[str, dict[LabelKey, str]] = {
        "pt": _LANG_PT,
        "en": _LANG_EN
    }
    @classmethod
    def t(cls, key:LabelKey, lang=None | str) -> str:
        lang = lang if isinstance(lang, str) else cls.config.default_lang
        return cls._LANGS.get(lang, cls._LANG_PT).get(key, key)