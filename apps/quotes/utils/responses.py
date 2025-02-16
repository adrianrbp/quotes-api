from rest_framework.response import Response

def api_response(status_code, message, data=None):
    """
    Standardized API response format.
    
    Args:
        status_code (int): HTTP status code.
        message (str): Description of the response.
        data (dict or None): Payload data (if applicable).

    Returns:
        rest_framework.response.Response: Structured JSON response.
    """
    return Response(
        {
            "status": status_code,
            "message": message,
            "data": data
        },
        status=status_code
    )
