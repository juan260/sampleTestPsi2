import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import estanteria, objeto, stock

e=estanteria.objects.get_or_create(id=1001)[0]
e.ubicacion="pasillo_01"
e.save()

e=estanteria.objects.get_or_create(id=1002)[0]
e.ubicacion="pasillo_02"
e.save()

e=estanteria.objects.get_or_create(id=1003)[0]
e.ubicacion="pasillo_03"
e.save()

o=objectos.objects.get_or_create(id=1001)[0]
o.nombreO="objeto_01"
o.save()

o=objectos.objects.get_or_create(id=1002)[0]
o.nombreO="objeto_02"
o.save()
o=objectos.objects.get_or_create(id=1003)[0]
o.nombreO="objeto_03"
o.save()
o=objectos.objects.get_or_create(id=1004)[0]
o.nombreO="objeto_04"
o.save()


s=stock.objects.get_or_create(id=1001)[0]
s.objeto_id=1001
s.estanteria_id=1001
s.numerounidades=1

s=stock.objects.get_or_create(id=1002)[0]
s.objeto_id=1002
s.estanteria_id=1002
s.numerounidades=2

s=stock.objects.get_or_create(id=1003)[0]
s.objeto_id=1003
s.estanteria_id=1003
s.numerounidades=3

