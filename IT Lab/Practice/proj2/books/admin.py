from django.contrib import admin
from .models import BookModel, IssueModel

admin.site.register(BookModel)
admin.site.register(IssueModel)

# Register your models here.
