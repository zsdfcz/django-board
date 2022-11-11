from django.urls import path
from . import views
app_name = 'board'

urlpatterns = [
    path('', views.board_list ,name='board_list'), #board's home  /// CRUD board app 
    path('write/',views.write,name='write'), #write page board contents create :CREATE
    path('write/board_write',views.board_write,name='board_write'), #write page board contents create :CREATE
    path('<int:board_id>/',views.detail, name='detail'), #detail page board contents call :READ
    path('<int:board_id>/comment', views.comment, name='comment'),
    path('<int:board_id>/update',views.update, name='update'), #update board contents :UPDATE
    path('board_update/<int:board_id>',views.board_update, name='board_update'), #update board contents :UPDATE 
    path('<int:board_id>/delete', views.delete,name='delete'), #delete board contents :DELETE
]
