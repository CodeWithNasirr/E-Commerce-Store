from django.urls import path,reverse,include
from . import views
urlpatterns = [
    path("",views.index,name="Index"),
    path("Blog",include('Blog.urls')),
    path("product_list",views.product_list,name="product_list"),
    path("Tracker",views.tracking,name="tracking"),
    path("About",views.About,name="About"),
    path("Faq",views.Faq,name="Faq"),
    path("contact",views.contact_form_submit,name="contact_form_submit"),
    path("search",views.Search,name="Search"),
    path("ProductView/<int:myid>", views.Product_view, name="ProductView"),
    path("checkout",views.Checkout,name="Checkout"),
    path('order_success/<int:order_id>/', views.order_success, name='order_success')
]