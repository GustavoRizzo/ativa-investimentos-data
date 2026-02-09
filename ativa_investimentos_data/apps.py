from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoMyLib(AppConfig):
    name = 'ativa_investimentos_data'

    verbose_name = _('Django My Lib')
