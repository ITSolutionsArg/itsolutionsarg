from django.conf.urls.defaults import patterns, include, url
from itsolutions.vista import menu

urlpatterns = patterns('',

	(r'^main$',menu),

)