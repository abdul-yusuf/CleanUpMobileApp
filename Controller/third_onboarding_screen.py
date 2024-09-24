import importlib

import View.ThirdOnboardingScreen.third_onboarding_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.ThirdOnboardingScreen.third_onboarding_screen)




class ThirdOnboardingScreenController:
    """
    The `ThirdOnboardingScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.third_onboarding_screen.ThirdOnboardingScreenModel
        self.view = View.ThirdOnboardingScreen.third_onboarding_screen.ThirdOnboardingScreenView(controller=self, model=self.model)

    def get_view(self) -> View.ThirdOnboardingScreen.third_onboarding_screen:
        return self.view
