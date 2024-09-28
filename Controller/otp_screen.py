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
    
    def signup(self):
        if self.view.ids.password.text == self.view.ids.password2.text:  
            self.dialog = self.view.app.dialog
            self.dialog.open()
            payload = {
                'email': self.view.ids.email.text,
                'full_name': self.view.ids.full_name.text,
                'phone_number': self.view.ids.phone_number.text,
                'password': self.view.ids.password.text
            }
            print(payload)
            self.view.app.api().signup(self, payload=payload)
        else:
            self.view.app.snackbar_notification("Password didn't match")

    def resend_otp(self):
        self.view.app.api().resend_otp(self, headers=self.view.app.get_headers())


    def on_success(self, *args, **kwargs):
        print('Success: ', args, kwargs)
        self.view.app.store_token(args[1]['token'])
        print(self.view.app.get_headers())
        self.model.notify_observers('signup screen')
        # self.dialog.dismiss()

    def on_user_details(self, *args, **kwargs):
        print('Success: ', args, kwargs)
        self.model.notify_user_observers('login screen')
        self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        print('ERROR: ', args, kwargs)
        self.view.app.snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        print('Failure: ', args, kwargs)
        try:
            if isinstance(args[1].values(), list):
                msg = args[1]
            else:
                msg = args[1][list(args[1])[0]]
            self.view.app.snackbar_notification(f"{msg}")
        except Exception as e:
            print(e)
        self.dialog.dismiss()
        
