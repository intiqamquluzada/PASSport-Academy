from django.contrib import admin
from .models import Students, Blog, Consultation


class ConsultAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "interest_country", "meet_date", "is_met")


admin.site.register(Students)
admin.site.register(Blog)
admin.site.register(Consultation, ConsultAdmin)
