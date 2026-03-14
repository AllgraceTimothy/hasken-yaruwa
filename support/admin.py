from django.contrib import admin
from .models import Support, ImpactMetric, ResourceAllocation

admin.site.register(ResourceAllocation)
admin.site.register(ImpactMetric)
@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'date_received')
