import importlib
import os
import uni_esse3api

from pathlib import Path

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from ... anagrafica_service_v2.settings import SERVICE as anagrafica_service_v2
from ... carriere_service_v1.settings import SERVICE as carriere_service_v1
from ... utenti_service_v1.settings import SERVICE as utenti_service_v1
from ... settings import ESSE3_PREFIX


class Command(BaseCommand):
    help = "Crea i gruppi per l'accesso alle API basati sui servizi di Esse3"

    def handle(self, *args, **options):
        # Lista gruppi e permessi (codename) da creare e assegnare

        # ~ EXCLUDED_DIRS = {"management", "__pycache__"}

        all_settings = {}
        # self.stdout.write(str(Path(uni_esse3api.__file__).parent))
        for folder in Path(uni_esse3api.__file__).parent.iterdir():
            if (
                folder.is_dir()
                and '_service_' in folder.name
                #not in EXCLUDED_DIRS
                and (folder / "settings.py").exists()
            ):
                settings_path = f'{folder}/settings.py'
                # 1. Assegna un nome al modulo (può essere arbitrario, serve a Python internamente)
                module_name = f'{folder.name}_settings'
                # 2. Crea le specifiche di caricamento
                spec = importlib.util.spec_from_file_location(module_name, settings_path)
                # 3. Crea il modulo dalle specifiche
                app_settings_module = importlib.util.module_from_spec(spec)
                # 4. Esegui il modulo (questo popola il modulo con le variabili/classi)
                spec.loader.exec_module(app_settings_module)

                service_name = getattr(app_settings_module, 'SERVICE', '')

                if service_name:
                    group_name = f'{ESSE3_PREFIX}-{service_name}'
                    group, created = Group.objects.get_or_create(name=group_name)
                    if created:
                        self.stdout.write(f"Creato gruppo {group_name}")
                    else:
                        self.stdout.write(f"Gruppo {group_name} già esistente")
                    
