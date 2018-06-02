from django.contrib import admin

from .models import News
from .models import NewsType
from .models import Category
from .models import Author
from .models import Status
from .models import MediaType
from .models import Media
from .models import FeatureMedia
from .models import Tags
from .models import NewsTags
from .models import Gallery
from .models import Cover
from .models import CoverNews
# Register your models here.

admin.site.register(News)
admin.site.register(NewsType)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Status)
admin.site.register(MediaType)
admin.site.register(Media)
admin.site.register(FeatureMedia)
admin.site.register(Tags)
admin.site.register(NewsTags)
admin.site.register(Gallery)
admin.site.register(Cover)
admin.site.register(CoverNews)