from django.urls import path 
from . import views
urlpatterns=[
    path('dashboard/',views.index,name='dashboardindex'),
    path('staff/',views.staff,name='dashboardstaff'),
    path('product/',views.product,name='dashboardproduct'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
    path('staff/detail/<int:pk>/',views.staff_detail,name='dashboardstaffdetail'),
    path('issueditems/',views.issued_items,name='dashboardissueditems'),

]