# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from aplicacion.models import estanteria, objeto, stock
admin.site.register(estanteria)
admin.site.register(objeto)
admin.site.register(stock)