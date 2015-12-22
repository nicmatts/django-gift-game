from django.contrib import admin

from .models import Game, Person, Gift


class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'order')


class GiftAdmin(admin.ModelAdmin):
    list_display = ('gift_name',)


admin.site.register(Game, GameAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Gift, GiftAdmin)
