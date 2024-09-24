# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.sign_up_screen import SignUpScreenModel
from Controller.sign_up_screen import SignUpScreenController
from Model.password_reset_screen import PasswordResetScreenModel
from Controller.password_reset_screen import PasswordResetScreenController
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.onboarding_screen import OnboardingScreenModel
from Controller.onboarding_screen import OnboardingScreenController
from Model.second_onboarding_screen import SecondOnboardingScreenModel
from Controller.second_onboarding_screen import SecondOnboardingScreenController
from Model.third_onboarding_screen import ThirdOnboardingScreenModel
from Controller.third_onboarding_screen import ThirdOnboardingScreenController
from Model.otp_screen import OtpScreenModel
from Controller.otp_screen import OtpScreenController

screens = {
    'home screen': {
        'model': HomeScreenModel,
        'controller': HomeScreenController,
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
    },
    'onboarding screen': {
        'model': OnboardingScreenModel,
        'controller': OnboardingScreenController,
    },
    'otp screen': {
        'model': OtpScreenModel,
        'controller': OtpScreenController,
    },
}