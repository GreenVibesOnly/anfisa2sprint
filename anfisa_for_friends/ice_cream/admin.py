from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper


admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (  # какие поля отображаются
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (  # какие поля можно редактировать
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)  # по каким полям можно искать запись
    list_filter = ('is_published',)  # по каким полям можно фильтровать записи
    list_display_links = ('title',)  # какие поля ведут на страницу с редакт записи
    empty_value_display = 'Не задано'  # пишется в поле, где нет значения
    filter_horizontal = ('toppings',)  # создает двойное окошко для выбора М:М


class IceCreamInline(admin.TabularInline):  # модель IceCream для вставки как связанных записей
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,  # вставка модели IceCream
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream, IceCreamAdmin)
