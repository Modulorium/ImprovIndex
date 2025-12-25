import json
import logging
import os
import sys
from typing import Dict, Any

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.http import (
    get_endpoint_variables, response_success, response_failed, response_error
)

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Main Lambda handler for Improv Index API
    Currently supports: GET /activities
    """
    try:
        # Log the incoming request for debugging
        logger.info(f"Received event: {json.dumps(event, default=str)}")

        # Extract request details
        endpoint = get_endpoint_variables(event)
        logger.info(f"Processing {endpoint['method']} {endpoint['path']}")
        
        # Handle CORS preflight requests
        if endpoint['method'] == 'OPTIONS':
            return response_success(message="CORS preflight")
        
        # Route to appropriate handler based on method and path
        if endpoint['path'] == '/activities' and endpoint['method'] == 'GET':
            return handle_get_activities(event, context)
        
        else:
            logger.warning(f"No handler found for {endpoint['method']} {endpoint['path']}")
            return response_failed(f"Endpoint not found: {endpoint['method']} {endpoint['path']}")
    
    except Exception as e:
        logger.error(f"Unhandled exception in lambda_handler: {str(e)}", exc_info=True)
        return response_error("An unexpected error occurred")


def handle_get_activities(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handle GET /activities - Returns all improv activities
    """
    try:
        from lib.dynamo import get_table, scan_table
        
        # Get table name from environment
        table_name = os.environ.get('ACTIVITIES_TABLE')
        if not table_name:
            logger.error("ACTIVITIES_TABLE environment variable not set")
            return response_error("Configuration error")
        
        # Get table and scan for all activities
        table = get_table(table_name)
        activities = scan_table(table)
        
        logger.info(f"Retrieved {len(activities)} activities from DynamoDB")
        
        return response_success(data=activities, message="Activities retrieved successfully")
    
    except Exception as e:
        logger.error(f"Error in handle_get_activities: {str(e)}", exc_info=True)
        return response_error("Failed to retrieve activities")

