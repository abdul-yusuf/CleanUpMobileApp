from View.base_screen import BaseScreenView


class OtpScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.phone_last_two_digit = self.model.phone_last_two_digit

    def next_screen(self):
        self.app.add_screen('home screen')
        
