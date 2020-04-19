from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^home/',views.HomePageView.as_view()),
	url(r'^$',views.login),
    url(r'^validateUser',views.validateUser),
    url(r'^inserttimetable',views.insert_timetable),
	url(r'^studentwisepage',views.timetable_class),
	url(r'^subjectwisepage',views.timetable_subject),
	url(r'^facultywisepage',views.timetable_faculty)
]