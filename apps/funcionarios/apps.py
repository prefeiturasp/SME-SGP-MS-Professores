"""Configuracao do app funcionarios."""

from django.apps import AppConfig


class FuncionariosConfig(AppConfig):
    """App do domínio Funcionários."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.funcionarios"
    label = "funcionarios"
