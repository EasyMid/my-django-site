from django.contrib import admin
from .models import Authors
from .models import Articles

admin.site.register(Authors)
admin.site.register(Articles)
# Register your models here.
