from django.contrib import admin
from .models import Blog, Section, Dish, PartyService, DishGallery, Impressum


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_file', 'text')


class PartyServiceAdmin(admin.ModelAdmin):
    list_display = ('title_p', 'media_file_p', 'text_p')


class DishAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'name', 'price')
    list_filter = ('section',)  # Добавляем фильтр по разделам

    def section_name(self, obj):
        return obj.section.name

    section_name.admin_order_field = 'section__name'  # Добавляем возможность сортировки по разделам


class DishInline(admin.TabularInline):
    model = Dish
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    inlines = [DishInline]
    list_display = ('name', 'description', 'custom_index', 'order')
    ordering = ('order',)

    actions = ['move_section_up', 'move_section_down']

    def move_section_up(modeladmin, request, queryset):
        for section in queryset:
            # Уменьшаем порядок на 1 для перемещения вверх
            section.order -= 1
            section.save()

    def move_section_down(modeladmin, request, queryset):
        for section in queryset:
            # Увеличиваем порядок на 1 для перемещения вниз
            section.order += 1
            section.save()


class DishGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


class ImpressumAdmin(admin.ModelAdmin):
    list_display = ('responsible', 'contact_us', 'internet', 'telephone')
    search_fields = ('responsible', 'contact_us', 'internet', 'telephone')


admin.site.register(Section, SectionAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(PartyService, PartyServiceAdmin)
admin.site.register(DishGallery, DishGalleryAdmin)
admin.site.register(Impressum, ImpressumAdmin)
