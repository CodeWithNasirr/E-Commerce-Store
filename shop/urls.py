from django.urls import path,reverse
from . import views
urlpatterns = [
    path("",views.index,name="Index"),
    path("product_list",views.product_list,name="product_list"),
    path("tracker",views.tracking,name="tracking"),
    path("about",views.About,name="About"),
    path("contact",views.contact_form_submit,name="contact_form_submit"),
    path("search",views.Search,name="Search"),
    path("ProductView/<int:myid>", views.Product_view, name="ProductView"),
    path("checkout",views.Checkout,name="Checkout"),
    path('order_success/<int:order_id>/', views.order_success, name='order_success')
]
