# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet

# router = DefaultRouter()
# router.register(r'students', StudentViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# from django.urls import path
# from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

# urlpatterns = [
#     path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
#     path('students/<uuid:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
# ]

from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<uuid:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
]
