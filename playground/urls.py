from django.urls import path
from . import views

# url configration
urlpatterns = [
	path('login/', views.logInPage, name="login"),
	path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),
	path('', views.intro, name='intro'),
	path('FAQs', views.FAQs, name='FAQs'),
	path('contact', views.contact, name='contact'),
    path('home', views.homePage, name='home'),
    path('car/<str:pk>', views.car, name='car'),
    path('add-car/', views.addCar, name="add-car"),
    path('edit-car/<str:pk>', views.updateCar, name="edit-car"),
	path('manager-view', views.managerPage, name='manager-view'),
	path('order-list', views.ordersListView, name='order-list-view'),
    path('delete-car/<str:pk>', views.deleteCar, name="delete-car"),
	path('delete-order/<str:pk>', views.deleteOrder, name="delete-order"),
	path('order-car/<str:pk>', views.orderCar, name="order-car"),

]