from django.urls import path

from stale import views

urlpatterns = [

    path('', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('animals/', views.animals, name='animal'),
    path('species/', views.species, name='species'),
    path('member/<str:pk>/', views.member, name='member'),
    path('staff/', views.createstaff, name='createstaff'),

]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
