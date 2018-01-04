from django.conf.urls import url, include
from catalog import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^books/$', views.BookListView, name='books'),
	url(r'^authors/$', views.AuthorListView, name = 'authors'),
	url(r'^book/(?P<pk>\d+)/$', views.book_detail_view, name = 'book-detail'),
	# url(r'^author/(/d+)/$', ),
]
