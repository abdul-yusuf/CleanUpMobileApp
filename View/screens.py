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
        'kv': 'View/HomeScreen/home_screen.kv'
    },
    'otp screen': {
        'model': OtpScreenModel,
        'controller': OtpScreenController,
        'kv': 'View/OtpScreen/otp_screen.kv'
    },
    'sign up screen': {
        'model': SignUpScreenModel,
        'controller': SignUpScreenController,
        'kv': 'View/SignUpScreen/sign_up_screen.kv'
    },
    'password rest screen': {
        'model': PasswordResetScreenModel,
        'controller': PasswordResetScreenController,
        'kv': 'View/PasswordResetScreen/password_rest_screen.kv'
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
        'kv': 'View/LoginScreen/login_screen.kv'
    },
    'onboarding screen': {
        'model': OnboardingScreenModel,
        'controller': OnboardingScreenController,
        'kv': 'View/OnboardingScreen/onboarding_screen.kv'
    },
    'second onboarding screen': {
        'model': SecondOnboardingScreenModel,
        'controller': SecondOnboardingScreenController,
        'kv': 'View/SecondOnboardingScreen/second_onboarding_screen.kv'
    },
    'third onboarding screen': {
        'model': ThirdOnboardingScreenModel,
        'controller': ThirdOnboardingScreenController,
        'kv': 'View/ThirdOnboardingScreen/third_onboarding_screen.kv'
    },
}