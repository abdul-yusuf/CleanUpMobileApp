import importlib

import View.OtpScreen.otp_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.OtpScreen.otp_screen)




class OtpScreenController:
    """
    The `OtpScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.otp_screen.OtpScreenModel
        self.view = View.OtpScreen.otp_screen.OtpScreenView(controller=self, model=self.model)

    def get_view(self) -> View.OtpScreen.otp_screen:
        return self.view
