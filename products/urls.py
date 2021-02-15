from django.urls import path
from .views import *
from django.contrib.auth import views as a_views

urlpatterns = [
    path('', products_page, name='products'),
    path('order/<int:product_id>/', order_page, name='order'),
    path('order_update/<int:order_id>/', update_order, name='order-update'),
    path('order_delete/<int:order_id>/', delete_order, name='order_delete'),
    path('registrasia/', registrasia_page, name='register'),
    path('user/<int:user_id>/', user_page, name='user-list'),
    path('aboutus/', aboutus_page, name='aboutus_page'),
    path('contakts/', contakts_page, name='contakts_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('profile/', account_settings, name='profile'),
    path('reset_password/', a_views.PasswordResetView.as_view(template_name='user_dir/reset_password.html'),
         name='password_reset'),
    path('reset_password_done/', a_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', a_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', a_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         activate, name='activate'),
]
