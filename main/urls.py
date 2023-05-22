from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='home'),
    path('book_detail/<int:id>/', book_detail, name='book_detail'),
    path('book_detail/<int:id>/update', update, name='update_book'),
    path('add_book/', add_book),
    path('login/', login_view, name='login'),
    path("add_author/", add_author),
    path("add_publisher/", add_publisher),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
