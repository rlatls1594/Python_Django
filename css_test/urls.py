# urls.py
from django.urls import path
from . import views

app_name = 'css_test' # 이 앱 이름은 그대로 사용합니다.

urlpatterns = [
    path('', views.index, name='index'), # 메인 페이지 URL
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

    # 전시 상세 정보 관련 URL 패턴
    path('exhibition/<int:exhibition_id>/', views.exhibition_detail_view, name='exhibition_detail'),
    path('exhibition/<int:exhibition_id>/add_review/', views.add_review, name='add_review'), # 리뷰 작성 URL

    # 예약 관련 URL 패턴
    path('reserve/<int:exhibition_id>/', views.reserve_view, name='reserve'),
    path('reserve/success/', views.reserve_success_view, name='reserve_success'), # 예약 완료 페이지 URL 추가
]