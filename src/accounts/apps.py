from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
