from View.base_screen import BaseScreenView


class LoginScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.controller.get_user_details()

    def user_is_changed(self):
        self.app.add_screen('home screen')
