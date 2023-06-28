from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("reg/",views.reg,name="reg"),
    path("wel/",views.wel,name="wel"),
    path("loguser/",views.loguser,name="loguser"),
    path("about/",views.about,name="about"),
    path("ser/",views.ser,name="ser"),
    path("adm/",views.adm,name="adm"),
    path("view/",views.view,name="view"),
    path("add/<int:pk>/",views.add,name="add"),
    path("delete/<int:pk>/",views.delete,name="delete"),
    path("aduser/",views.aduser,name="aduser"),
    path("admm/",views.admm,name="admm"),
    path("custaff/",views.custaff,name="custaff"),
    path("logout/",views.logout,name="logout"),
    path("update/<int:pk>/",views.update,name="update"),
    path("detail/<int:pk>/",views.detail,name="detail"),
    path("jead/",views.jead,name="jead"),
    path("jwd/",views.jwd,name="jwd"),
    path("dele/<int:pk>/",views.dele,name="dele"),
    path("show/",views.show,name="show"),
    path("usreg/",views.usreg,name="usreg"),
    path("uslog/",views.uslog,name="uslog"), 
    path("ususer/",views.ususer,name="ususer"),
    path("buy/<int:pk>/",views.buy,name="buy"),
    path("pay/",views.pay,name="pay"), 
    path("card/",views.card,name="card"),
    path("ord/",views.ord,name="ord"),
    path('search/',views.search,name="search"),
    path("cart/<int:pk>/",views.cart,name='cart'),
    path('button_view/',views.button_view,name='button_view'),
    path("delcart/<int:pk>/",views.delcart,name="delcart"),
    
]