from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("main/", view=views.main, name="main"),  # main 페이지로 가는 api
    path("main/helped/", views.helped, name="helped"),
    path("main/follow/", views.follow, name="follow"),
    path("main/my_recent/", views.my_recent, name="my_recent"),
    path(
        "<int:user_id>/<int:post_id>/detail", views.post_detail, name="post_detail"
    ),  # 처음 <int:pk> 의 pk: user의 id
    # 두번째 <int:pk> 의 pk: post의 id
    path("create/", views.post_create, name="post_create"),
    path("<int:pk>/update", views.post_update, name="post_update"),
    path("<int:pk>/delete", views.post_delete, name="post_delete"),
    path("search/", views.search, name="search"),
    # path("search_post_axios/", views.search_post_axios, name="search_post_axios"),
    # path("search_user_axios/", views.search_user_axios, name="search_user_axios"),
    
    # path("search_input/", views.search_input, name="search_input"),
    # path("search_select/", views.search_select, name="search_select"),
    
    path("search_quest/", views.search_quest, name="search_quest"),
    # path("search_quests_input/", views.search_quests_input, name="search_quests_input"),
    # path("search_quests_select/", views.search_quests_select, name="search_quests_select"),
    
    path("<int:user_id>/<int:post_id>/get_post", view=views.get_post, name="get_post"),
    path("scrap_axios/", views.scrap_axios, name="scrap_axios"),
    path("helped_axios/", views.helped_axios, name="helped_axios"),
    path("follow_axios/", views.follow_axios, name="follow_axios"),
    path("my_recent_axios/", views.my_recent_axios, name="my_recent_axios"),
    path("like/", views.post_like, name="post_like"),
    path("<int:user_id>/<int:post_id>/scrap/", views.post_scrap, name="post_scrap"),
    # 서비스 소개 페이지
    path("service_view/", views.service_view, name="service_view"),
    ]
