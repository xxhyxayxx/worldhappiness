from django.contrib import admin
from api.models import Country, Region, CountryRegion

class CountryRegionInline(admin.TabularInline):
    model = CountryRegion
    extra = 1  # 追加フォームを表示する数

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'regions_list')
    inlines = (CountryRegionInline,)  # CountryRegionInlineを追加

    def regions_list(self, obj):
        return ", ".join([region.name for region in obj.regions.all()])

# CountryとRegionをadminサイトに登録
admin.site.register(Country, CountryAdmin)
admin.site.register(Region)
