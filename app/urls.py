from django.urls import path
from . import views

# path linking
urlpatterns = [
    path("", views.index),
    path("login/", views.login),
    path("Signin/", views.Signin),
    path("Detectionscreen/", views.Detectionscreen),
    path("api2/", views.api2),
    path("contact/", views.contact),
    path("forgotpassword/", views.forgotpassword),
    path("idk/", views.idk),
    path("info2/", views.info2),
    path("myappointment/", views.myappointment),
    path("newappointment/", views.newappointment),
    path("newprofile/", views.newprofile),
    path("sup/", views.sup),
    # goes to the views.py file, looks for a function named Feedback,
    # api call urls
    path("login_api/", views.login_api),
    path("signin_api/", views.signin_api),
    path("send_otp_api/", views.send_otp_api),
    path("reset_password_api/", views.reset_password_api),
    path("predict_result_api/", views.predict_result_api),
    path("logout/", views.logout_view),
    path("drdeepak/", views.drdeepak),
    path("profile/", views.newprofile),
    path("drdinesh/", views.drdinesh),
    path("dreswari/", views.dreswari),
    path("drharish/", views.drharish),
    path("drneha/", views.drneha),
    path("drparthasarathi/", views.drparthasarathi),
    path("drsavitha/", views.drsavitha),
    path("drshashidar/", views.drshashidar),
    path("drsheelavathi/", views.drsheelavathi),
    path("drshishira/", views.drshishira),
    # miscellaneous
    path("add_doctor_dict/", views.add_doctor_dict),
]
