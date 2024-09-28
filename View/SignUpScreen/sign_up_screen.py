from View.base_screen import BaseScreenView


class SignUpScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.app.add_screen('otp screen')

    def user_is_changed(self):
        self.app.add_screen('otp screen')
