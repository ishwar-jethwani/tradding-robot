from django.urls import path,include
from .views import home,signal,order_history,trade_history,signal_source,live_signal,loginwithapi
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",login_required(home),name="home"),
    path("signal/",login_required(signal),name="signal"),
    path("order_history/",login_required(order_history),name="order"),
    path("trade_history/",login_required(trade_history),name="trade"),
    path("source/",login_required(signal_source),name="source"),
    path("live_signal",login_required(live_signal),name="live"),
    path("api_login",login_required(loginwithapi),name="api"),


]