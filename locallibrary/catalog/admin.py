from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.


"""
# Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Language)



class BookInline(admin.TabularInline):
	model = Book


# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
# admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
	model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]



# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('id', 'status', 'due_back')
	# Add list filters
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {
			'fields':('book', 'imprint', 'id')
		}),
		('Availablity', {
			'fields':('status', 'due_back')
		}),
	)



