from django.urls import path

from accountapp.views import hello_world

# 브라우저로 helloworld로 들어오게 된다면,
# 127.0.0.1: 8000/account/helloworld로 들어오는 매우 귀찮은 상황
# "accountapp:hello_world" 로
app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]