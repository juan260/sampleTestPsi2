import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import estanteria, objeto, stock
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts populates de workflow database, no arguments needed.' \
           'Execute it with the command line python manage.py populate'
    
    def handle(self, *args, **options):
        e=estanteria.objects.get_or_create(id=1001)[0]
        e.ubicacion="pasillo_01"
        e.save()

        e=estanteria.objects.get_or_create(id=1002)[0]
        e.ubicacion="pasillo_02"
        e.save()

        e=estanteria.objects.get_or_create(id=1003)[0]
        e.ubicacion="pasillo_03"
        e.save()

        o=objeto.objects.get_or_create(id=1001)[0]
        o.nombreO="objeto_01"
        o.save()

        o=objeto.objects.get_or_create(id=1002)[0]
        o.nombreO="objeto_02"
        o.save()
        o=objeto.objects.get_or_create(id=1003)[0]
        o.nombreO="objeto_03"
        o.save()
        o=objeto.objects.get_or_create(id=1004)[0]
        o.nombreO="objeto_04"
        o.save()

        e=estanteria.objects.get(id=1001)
        o=objeto.objects.get(id=1001)
        s=stock.objects.get_or_create(id=1001)[0]
        s.objeto_id=o
        s.estanteria_id=e
        s.numerounidades=1
        s.save()

        e=estanteria.objects.get(id=1002)
        o=objeto.objects.get(id=1002)
        s=stock.objects.get_or_create(id=1002)[0]
        s.objeto_id=o
        s.estanteria_id=e
        s.numerounidades=2
        s.save()

        e=estanteria.objects.get(id=1003)
        o=objeto.objects.get(id=1003)
        s=stock.objects.get_or_create(id=1003)[0]
        s.objeto_id=o
        s.estanteria_id=e
        s.numerounidades=3
        s.save()
