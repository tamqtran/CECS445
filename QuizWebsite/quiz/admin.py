from django.contrib import admin

from .models import AgeCategory
from .models import Question

admin.site.register(AgeCategory)
admin.site.register(Question)
# Register your models here.
