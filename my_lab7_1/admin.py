from django.contrib import admin
from .models import ComputerModel, OrderModel, User


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'brand')
    search_fields = ('serial_num', 'brand')


admin.site.register(ComputerModel, ComputerAdmin)


class OrderAdmin(admin.ModelAdmin):
    def item_amount(self, obj):
        data = ComputerModel.objects.filter(ord_num=obj.id).all()
        i = len(data)
        return i
    list_display = ('order_num', 'order_date', 'item_amount')
    list_filter = ['order_date']

admin.site.register(OrderModel, OrderAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)
# Register your models here.
