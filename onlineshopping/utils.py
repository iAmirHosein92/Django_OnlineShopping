from django.contrib.auth.mixins import UserPassesTestMixin


class IsAdminUserMixin(UserPassesTestMixin):

    def test_func(self):
       return  self.request.user.is_authenticated and self.request.user.is_admin



def send_otp_code(phone_number, code):
    pass