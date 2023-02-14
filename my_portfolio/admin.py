from django.contrib import admin
# from .models import All
from .models import Photoshop
from .models import Art
from .models import Web
from .models import Contact

# Register your models here.

# admin.site.register(All)
admin.site.register(Photoshop)
admin.site.register(Art)
admin.site.register(Web)
admin.site.register(Contact)
