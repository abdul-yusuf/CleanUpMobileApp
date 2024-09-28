import importlib

import View.LoginScreen.login_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.LoginScreen.login_screen)




class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = View.LoginScreen.login_screen.LoginScreenView(controller=self, model=self.model)

    def get_view(self) -> View.LoginScreen.login_screen:
        return self.view

    def login(self):
        self.dialog = self.view.app.dialog
        self.dialog.open()
        payload = {
            'email': self.view.ids.email.text,
            'password': self.view.ids.password.text
        }
        print(payload)
        self.view.app.api().login(self, payload=payload)

    def get_user_details(self):
        self.view.app.api().get_user(self, headers=self.view.app.get_headers())
        
    def on_success(self, *args, **kwargs):
        print('Success: ', args, kwargs)
        self.view.app.store_token(args[1]['token'])
        print(self.view.app.get_headers())
        self.model.notify_observers('login screen')
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

    def on_user_details_failure(self, *args, **kwargs):
        print('Failure: ', args, kwargs)
        self.view.app.add_screen('otp screen')
        self.dialog.dismiss()