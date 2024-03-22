from django.urls import path
from . import views 

urlpatterns = [
    # path("",views.api_home),
    # path("api_post",views.api_post),
    path("product",views.get_all_product),
    path("product/<int:id>/",views.get_product),
    path("product_add",views.add_product),
    path("prodcut_delete/<int:product_id>/",views.delete_prodcut_by_id),
    path("product_update/<int:id>/",views.product_update),
    path("getdata",views.getdata),
    path("add_data",views.add_data),
    path("delete_data/<int:id>/",views.delete_data)

]
