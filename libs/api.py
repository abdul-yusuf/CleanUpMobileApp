"""
API Wrapper
---------------------

"""

# imports
import certifi as cfi
from json import dumps
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
from kivy.storage.jsonstore import JsonStore


class API:
    BASE_URL = 'https://cleanupbackend-production.up.railway.app/'
    def signup(self, 
                init_func,
                on_success_method=None,
                on_error_method=None,
                on_failure_method=None,
                method: str = 'POST',
                payload: dict = None,
                headers: dict = {"Content-Type": "application/json"} 
               ):
        
        url = f'{self.BASE_URL}api/accounts/signup/'
        UrlRequest(
            url,
            req_body=dumps(payload),
            method=method,
            req_headers=headers,
            on_success=init_func.on_success if on_success_method is None else on_success_method,
            on_error=init_func.on_error if on_error_method is None else on_error_method,
            on_failure=init_func.on_failure if on_failure_method is None else on_failure_method,
            ca_file=cfi.where(),
            verify=True
        )


    def login(self, 
                init_func,
                on_success_method=None,
                on_error_method=None,
                on_failure_method=None,
                method: str = 'POST',
                payload: dict = None,
                headers: dict = {"Content-Type": "application/json"} 
               ):
        """
        Login Request
        This function gets user token.
        Args:
            init_func (class): The instance that initiate the request
        Kwargs:
            on_success_method (meth)
            on_error_method=None (meth)
            on_failure_method (meth):
            method (str): Request method type ['POST', 'GET', 'DELETE', 'PATCH']
            payload (dict): The payload to be passed  
        Returns: 
            UrlRequest
        """
        
        url = f'{self.BASE_URL}api/accounts/login/'
        UrlRequest(
            url,
            req_body=dumps(payload),
            method=method,
            req_headers=headers,
            on_success=init_func.on_success if on_success_method is None else on_success_method,
            on_error=init_func.on_error if on_error_method is None else on_error_method,
            on_failure=init_func.on_failure if on_failure_method is None else on_failure_method,
            ca_file=cfi.where(),
            verify=True
        )
    
    def get_user(self, 
                init_func,
                on_success_method=None,
                on_error_method=None,
                on_failure_method=None,
                method: str = 'GET',
                payload: dict = None,
                headers: dict = {"Content-Type": "application/json"} 
               ):
        
        url = f'{self.BASE_URL}api/accounts/user/'
        UrlRequest(
            url,
            # req_body=dumps(payload),
            # method=method,
            req_headers=headers,
            on_success=init_func.on_user_details if on_success_method is None else on_success_method,
            on_error=init_func.on_error if on_error_method is None else on_error_method,
            on_failure=init_func.on_user_details_failure if on_failure_method is None else on_failure_method,
            ca_file=cfi.where(),
            verify=True
        )
    
    def resend_otp(self, 
                init_func,
                on_success_method=None,
                on_error_method=None,
                on_failure_method=None,
                method: str = 'POST',
                payload: dict = None,
                headers: dict = {"Content-Type": "application/json"} 
               ):
        
        url = f'{self.BASE_URL}signup/'
        UrlRequest(
            url,
            req_body=dumps(payload),
            method=method,
            req_headers=headers,
            on_success=init_func.resend_success if on_success_method is None else on_success_method,
            on_error=init_func.on_error if on_error_method is None else on_error_method,
            on_failure=init_func.on_failure if on_failure_method is None else on_failure_method,
            ca_file=cfi.where(),
            verify=True
        )
    
    def verify_phone_number(self, 
                init_func,
                on_success_method=None,
                on_error_method=None,
                on_failure_method=None,
                method: str = 'POST',
                payload: dict = None,
                headers: dict = {"Content-Type": "application/json"} 
               ):
        
        url = f'{self.BASE_URL}signup/'
        UrlRequest(
            url,
            req_body=dumps(payload),
            method=method,
            req_headers=headers,
            on_success=init_func.on_success if on_success_method is None else on_success_method,
            on_error=init_func.on_error if on_error_method is None else on_error_method,
            on_failure=init_func.on_failure if on_failure_method is None else on_failure_method,
            ca_file=cfi.where(),
            verify=True
        )

    def send_image_to_api(self,
                            init_func,
                            image_path,
                            on_success_method=None,
                            on_error_method=None,
                            on_failure_method=None,
                            method: str = 'POST',
                            payload: dict = None,
                            headers: dict = {"Content-Type": "application/json"} 
                            ):
        import base64

        # Read image as bytes
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

        # Prepare API URL and headers
        url = f"{self.BASE_URL}upload-image/"

        # Prepare data payload
        data = {
            "image": encoded_image,  # Send base64 encoded image
            "filename": "captured_image.png"
        }

        UrlRequest(
            url, 
            req_body=dumps(data), 
            # method=method,
            req_headers=headers,
            on_success=init_func.on_success if on_success_method is None else on_success_method,
            on_error=init_func.on_error if on_error_method is None else on_error_method,
            on_failure=init_func.on_failure if on_failure_method is None else on_failure_method,
            ca_file=cfi.where(),
            verify=True
            )
