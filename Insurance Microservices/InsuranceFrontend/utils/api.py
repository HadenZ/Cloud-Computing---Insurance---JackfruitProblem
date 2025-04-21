import json
import requests
import os

# Load endpoints once
with open(os.path.join(os.path.dirname(__file__), '../endpoints.json')) as f:
    ENDPOINTS = json.load(f)

def call_api(service, route, method='GET', data=None, params=None, headers=None, files=None):
    """
    Generic helper to call any service by name and route.

    Args:
        service (str): One of the keys from endpoints.json
        route (str): Relative route to call on the service (e.g., '/users')
        method (str): 'GET', 'POST', etc.
        data (dict): JSON payload for POST/PUT
        params (dict): URL params for GET
        headers (dict): Optional headers
        files (dict): For file uploads

    Returns:
        dict: JSON response or error
    """
    url = ENDPOINTS[service] + route

    try:
        response = requests.request(
            method=method,
            url=url,
            json=data,
            params=params,
            headers=headers,
            files=files,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
