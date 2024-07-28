import os
import requests
from datetime import datetime


class Tools:
    def __init__(self):
        self._session = requests.Session()
        pass

    def get_congress_summaries(self) -> str:
        """
        Get the a Summary of Congress Bills for a given date and number of days.
        :return: Summaries of Congress Bills
        """
        api_key = os.getenv("CONGRESS_API_KEY")
        if not api_key:
            return (
                "API key is not set in the environment variable 'CONGRESS_API_KEY'."
            )

        base_url = "https://api.congress.gov/v3/summaries?fromDateTime=2022-04-01T00:00:00Z&toDateTime=2022-04-03T00:00:00Z&sort=updateDate+asc"

        params = {
            "format": "json",
        }

        headers = {
            "x-api-key": api_key,
        }

        self._session.params = params
        self._session.headers.update(headers)


        try:
            response = self._session.get(f"{base_url}/{date}")
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            
            data = response.json()

            return str(data)
        except requests.RequestException as e:
            return f"Error fetching weather data: {str(e)}"
