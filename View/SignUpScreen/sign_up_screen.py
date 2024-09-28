from View.base_screen import BaseScreenView
from kivy.clock import Clock

class SignUpScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.app.add_screen('otp screen')
        # def pass_attr(self, name_screen: str, data, attr=None)
        Clock.schedule_once(lambda _:self.model.pass_attr('otp screen', self.ids.email.text, 'email'), 1)
        Clock.schedule_once(lambda _:self.model.pass_attr('otp screen', self.model.phone_last_two_digit, 'phone_last_two_digit'), 1)
        Clock.schedule_once(lambda _:self.model.notify_observers('otp screen'), 2)

