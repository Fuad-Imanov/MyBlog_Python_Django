from django.contrib import admin
from .models import Rubric,Article
from mptt.admin import DraggableMPTTAdmin
# from mptt.admin import MPTTModelAdmin
# Register your models here.
# admin.site.register( Rubric ,MPTTModelAdmin)
admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Article)