from rest_framework.routers import DefaultRouter as DR

from mainapp.views import InnerTraidDashboardView

router = DR()

router.register('inner_traids_dashboard', InnerTraidDashboardView, basename='inner_traids_dashboard')

urlpatterns = []

urlpatterns += router.urls