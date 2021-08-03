from django.contrib import admin
from .models import Review


class ReviewsAdmin(admin.ModelAdmin):

    readonly_fields = ('added_by', )

    list_display = (
        'review',
        'added_by',
        'rating',
    )


admin.site.register(Review, ReviewsAdmin)
