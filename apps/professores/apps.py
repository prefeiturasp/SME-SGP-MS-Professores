"""Configuracao do app professores."""

from django.apps import AppConfig


class ProfessoresConfig(AppConfig):
    """App do domínio Professores."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.professores"
    label = "professores"
