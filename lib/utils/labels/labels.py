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
        LabelKey.SIGN_UP: 'Cadastrar',
        LabelKey.ERROR_TEXT: 'O campo {field_name} é obrigatório.',
        LabelKey.ERROR_TEXT_PASSWORD_NOT_MATCH: 'As senhas fornecidas não coincidem.',
        # Menu
        LabelKey.MENU_HOME: 'Início',
        LabelKey.MENU_PRODUCTS: 'Produtos',
        LabelKey.MENU_CLIENTS: 'Clientes',
        LabelKey.MENU_SALES: 'Vendas',
        LabelKey.MENU_PROFILE: 'Perfil',
        LabelKey.MENU_SETTINGS: 'Configurações',
        LabelKey.MENU_LOGOUT: 'Sair',
    # Welcome page
        LabelKey.WELCOME_TITLE: 'Bem-vindo ao Sistema de Estoque!',
        LabelKey.WELCOME_INSTRUCTION: 'Use o menu lateral para navegar pelas funcionalidades.',
        # Clients
        LabelKey.NO_CLIENTS_FOUND: 'Nenhum cliente encontrado.',
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
        LabelKey.SIGN_UP: 'Sign Up',
        LabelKey.ERROR_TEXT: 'The field {field_name} is required.',
        LabelKey.ERROR_TEXT_PASSWORD_NOT_MATCH: 'The provided passwords do not match.',
        # Menu
        LabelKey.MENU_HOME: 'Home',
        LabelKey.MENU_PRODUCTS: 'Products',
        LabelKey.MENU_CLIENTS: 'Clients',
        LabelKey.MENU_SALES: 'Sales',
        LabelKey.MENU_PROFILE: 'Profile',
        LabelKey.MENU_SETTINGS: 'Settings',
        LabelKey.MENU_LOGOUT: 'Logout',
    # Welcome page
    LabelKey.WELCOME_TITLE: 'Welcome to the Inventory System!',
    LabelKey.WELCOME_INSTRUCTION: 'Use the side menu to navigate through the features.',
    # Clients
    LabelKey.NO_CLIENTS_FOUND: 'No clients found.',
    }
    _LANGS: dict[str, dict[LabelKey, str]] = {
        "pt": _LANG_PT,
        "en": _LANG_EN
    }
    @classmethod
    def t(cls, key:LabelKey, lang=None | str) -> str:
        lang = lang if isinstance(lang, str) else cls.config.default_lang
        return cls._LANGS.get(lang, cls._LANG_PT).get(key, key)