import os
from dotenv import load_dotenv
import requests
from typing import Literal, Optional

# Define the ApiClient class
class ApiClient():
    """
    base_url = "https://www.os2autoproces.eu/"
    apikey_path = "" #The path to the file containing the apikey (RAW string)
    apikey = "" #The apikeystring from the apikey_path
    client = ApiClient() #print_everything shows sucessful login and logouts, disabled by default
    """

    def __init__(self, print_everything=None) -> None:
        """Initialize default attributes needed by the other methods."""
        try:
            self.base_url = "https://www.os2autoproces.eu/"
            self.print_everything = print_everything

            load_dotenv(override=True) # Load environment variables, needed to get os.getenv() to work
            api_key_path = os.getenv("api_key_path") # Read api_key_path from .env

            # Use apikey_path to set self.apikey attribute
            if api_key_path and os.path.exists(api_key_path):
                with open(api_key_path, "r") as file:
                    file_contents = file.read()
                    if not isinstance(file_contents, str):
                        raise ValueError("File did not contain string!")
                    self.api_key = file_contents
            else:
                print("File/path does not exist: ", api_key_path)
                    

            # Set up headers with the API key
            self.headers = {
                "Accept": "application/json",
                "ApiKey": self.api_key,
            }

            # Arrays of allowed string values for testing parameter inputs
            self.PHASES = ["IDEA", "PREANALYSIS", "SPECIFICATION", "DEVELOPMENT", "IMPLEMENTATION", "OPERATION", "DECOMMISSIONED"]
            self.STATUSES = ["REJECTED", "FAILED", "PENDING", "INPROGRESS", "NOT_RATED", "NOT_RELEVANT"]

            self.set_cookie_header = None
            self.session = requests.Session()  # To maintain session cookies
            self.log_into_api()
        except Exception as e:
            print("Error during initialization of ApiClient:", str(e))

    def log_into_api(self) -> None:
        """Called upon initialization to log in to the API as a superuser."""
        try:
            url = f"{self.base_url}xapi/auth"
            if not self.session:
                self.session = requests.Session()
            response = self.session.post(url, headers=self.headers, data="")
            response.raise_for_status()  # Raise an exception for error status codes

            set_cookie_header = response.headers.get("Set-Cookie")
            if self.print_everything:
                if set_cookie_header:
                    print("Login successful, Set-Cookie header found")
                else:
                    print("Login successful, no Set-Cookie header")
        except requests.RequestException as e:
            print("Error in log_into_api: ", str(e))

    def logout_from_api(self) -> None:
        """Logs the user out of the API."""
        # FIXME: Doesn't seem to actually logout the user...
        try:
            url = f"{self.base_url}saml/logout"
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            self.set_cookie_header = None
            self.session.cookies.clear()  # FIXME: tempoary fix to logout from API
            self.session.close()
            self.session = None
            if self.print_everything:
                if not self.session:
                    print("Logout successful, cleared session cookie and closed")
        except requests.RequestException as e:
            print("Error in logout_from_api: ", str(e))

    def who_am_i(self) -> None:
        """Check and see who you are to the API."""
        try:
            url = f"{self.base_url}public/whoami"
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            print("You are:", response.json())
        except requests.RequestException as e:
            print("Error in who_am_i: ", str(e))

    # def update_process(self, process_id=None, phase=None, status=None) -> None:
    def update_process(
        self,
        process_id: int,
        phase: Optional[
            Literal[
                "IDEA",
                "PREANALYSIS",
                "SPECIFICATION",
                "DEVELOPMENT",
                "IMPLEMENTATION",
                "OPERATION",
                "DECOMMISSIONED",
            ]
        ] = None,
        status: Optional[
            Literal[
                "REJECTED",
                "FAILED",
                "PENDING",
                "INPROGRESS",
                "NOT_RATED",
                "NOT_RELEVANT",
            ]
        ] = None,
    ) -> None:
        """Update a process by ID, accepts phase and status."""
        try:
            if process_id is None:
                raise ValueError("Error in update_process: 'process_id' must be provided.")
            elif not isinstance(process_id, int):
                raise TypeError("Error in update_process: 'process_id' must be an integer.")
            else:
                url = f"{self.base_url}api/processes/{process_id}"

            # Initialize an empty JSON object
            json_dict = {}

            # Fill in the JSON object based on conditionals
            if phase and not isinstance(phase, str):
                raise TypeError("Error in update_process: 'phase' must be a string.")
            elif phase and phase not in self.PHASES:
                raise ValueError("Error in update_process: 'phase' was not a valid phase, check your spelling.")
            else:
                json_dict["phase"] = phase

            if status and not isinstance(status, str):
                raise TypeError("Error in update_process: 'status' must be a string.")
            elif status and status not in self.STATUSES:
                raise ValueError("Error in update_process: 'status' was not a valid status, check your spelling.")
            else:
                json_dict["status"] = status
            # TODO: Add more fields?

            # if json_dict contains data run patch call, else skip it
            if len(json_dict) > 0 and json_dict != {}:
                response = self.session.patch(url, headers=self.headers, json=json_dict)
                response.raise_for_status()
                data = response.json()
                print(f"Sucesfully patched process with process_id={data["id"]} with new phase/staus to: phase={data["phase"]}, status={data["status"]}")
            else:
                print("No new values was supplied, skipped update. Check if the parameters fit inside the constraints of the API")
        except Exception as e:
            print("Error in 'update_process': ", str(e))