from django.urls import path,include
from .views import home,signal,order_history,trade_history,symbol_setting,trade_book,brder_book
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",login_required(home),name="home"),
    path("symbol_setting/",login_required(symbol_setting),name="symbol_setting"),
    path("signal/",login_required(signal),name="signal"),
    path("order_history/",login_required(order_history),name="order"),
    path("trade_history/",login_required(trade_history),name="trade"),
    path("trade_book/",login_required(trade_book),name="trade_book"),
    path("brder_book/",login_required(brder_book),name="brder_book"),

]