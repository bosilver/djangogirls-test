from django.contrib import admin

# Register your models here.
# trips/admin.py

from trips.models import Post

admin.site.register(Post)
