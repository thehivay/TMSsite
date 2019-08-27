from django.contrib import admin
from homepage.models import Product, Brand, Item

# Почему красным подчеркивает homepage, Product, Brand, Item?
# Не помогло:
# Проект запускается, все нормально. Пакеты в viertuakenv, но почему то PyCharm не понимает
# импорты стандартных модулей Django, подсвечивает их красным. При этом все работает и запускается.
# В настройках для проекта указал Django support.
# Может кому и пригодится.. Помогло: Проверьте, что Django нашел интерпретатор и его пакеты:
# File - Settings - Project - Project Interpreter В списке пакетов должен быть Django.
# Там и так стоял Django, зашел, проверил, нажал OK и все стало нормально.

# Помогло:
# Пометить папку prosport как Sources в Project Structure (Settings | Project | Project Structure),
# так как PyCharm поймет, где именно ему стоит искать данный модуль.

# Register your models here. Здесь регистрируются созданные модели, чтоб админка их вилела и могла с ними работать.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Item)
