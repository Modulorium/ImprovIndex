import json
from typing import Any, Dict, Optional

def create_response(status_code: int, body: Any, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    default_headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET,POST,DELETE,OPTIONS',
        'Access-Control-Allow-Headers': 'content-type'
    }
    if headers:
        default_headers.update(headers)
    # Ensure body is JSON serializable
    if body is not None:
        try:
            json_body = json.dumps(body, default=str)
        except (TypeError, ValueError) as e:
            json_body = json.dumps({"error": "Internal server error - response serialization failed"})
            status_code = 500
    else:
        json_body = json.dumps({})
    return {
        'statusCode': status_code,
        'headers': default_headers,
        'body': json_body
    }

def response_success(data: Any = None, message: str = "Success") -> Dict[str, Any]:
    body = {"message": message}
    if isinstance(data, dict):
        body.update(data)
    elif data is not None:
        body["data"] = data
    return create_response(200, body)

def response_failed(data: Any = None, message: str = "Failed") -> Dict[str, Any]:
    body = {"message": message}
    if isinstance(data, dict):
        body.update(data)
    elif data is not None:
        body["data"] = data
    return create_response(400, body)

def response_error(data: Any = None, message: str = "Error") -> Dict[str, Any]:
    body = {"message": message}
    if isinstance(data, dict):
        body.update(data)
    elif data is not None:
        body["data"] = data
    return create_response(500, body)

def parse_event_body(event: Dict[str, Any]) -> Dict[str, Any]:
    body = event.get('body')
    if not body:
        return {}
    
    try:
        return json.loads(body)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON in request body")

def get_path_parameters(event: Dict[str, Any]) -> Dict[str, str]:
    return event.get('pathParameters') or {}

def get_query_parameters(event: Dict[str, Any]) -> Dict[str, str]:
    return event.get('queryStringParameters') or {}

def get_http_method(event: Dict[str, Any]) -> str:
    return event.get('httpMethod', '').upper()

def get_resource_path(event: Dict[str, Any]) -> str:
    return event.get('resource', '')

def get_endpoint_variables(event: Dict[str, Any]) -> Dict[str, Any]:
    http_method = get_http_method(event)
    resource_path = get_resource_path(event)
    path_params = get_path_parameters(event)
    query_params = get_query_parameters(event)
    return {
        "method": http_method,
        "path": resource_path,
        "path_params": path_params,
        "query_params": query_params
    }
