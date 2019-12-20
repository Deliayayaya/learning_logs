from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry,Pizza,Topping
from learning_logs.models import Entry
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Pizza)
admin.site.register(Topping)