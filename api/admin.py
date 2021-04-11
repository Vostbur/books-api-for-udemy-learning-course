from django.contrib import admin

from .models import (
    Isbn,
    Book,
    Character,
    Author
)


class CharacterAdmin(admin.StackedInline):
    model = Character


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'get_characters', 'get_authors', 'isbn')
    sortable_by = ['id', 'title', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title']
    inlines = [CharacterAdmin]

    def get_characters(self, obj):
        return ', '.join([c.name for c in obj.characters.all()])

    get_characters.short_description = 'Characters'

    def get_authors(self, obj):
        return ', '.join([a.name for a in obj.authors.all()])

    get_authors.short_description = 'Authors'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            'characters', 'authors'
        )


admin.site.register(Isbn)
admin.site.register(Character)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
