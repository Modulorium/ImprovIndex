import boto3
import os
import logging
from typing import Any, Dict, Optional, List
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

# Initialize DynamoDB client and resource
dynamodb_client = boto3.client('dynamodb', region_name="us-east-2")
dynamodb_resource: Any = boto3.resource('dynamodb', region_name="us-east-2")

def get_table(table_name: Optional[str] = None):
    """
    Get a DynamoDB table resource.
    
    Args:
        table_name (str, optional): Name of the table. If None, will try to get from environment.
        
    Returns:
        boto3.dynamodb.Table: DynamoDB table resource
        
    Raises:
        ValueError: If table_name is not provided and not found in environment
    """
    if table_name is None:
        table_name = os.environ.get('DYNAMODB_TABLE_NAME')
        if not table_name:
            raise ValueError("Table name must be provided or set in DYNAMODB_TABLE_NAME environment variable")
    
    try:
        table = dynamodb_resource.Table(table_name)
        logger.info(f"Successfully connected to table: {table_name}")
        return table
    except ClientError as e:
        logger.error(f"Error accessing table {table_name}: {e}")
        raise

def put_item(table, item: Dict[str, Any]) -> Dict[str, Any]:
    """
    Put an item into a DynamoDB table.
    
    Args:
        table: DynamoDB table resource
        item (dict): Item to put into the table
        
    Returns:
        dict: Response from DynamoDB
        
    Raises:
        ClientError: If the put operation fails
    """
    try:
        response = table.put_item(Item=item)
        logger.info(f"Successfully put item into table: {table.table_name}")
        return response
    except ClientError as e:
        logger.error(f"Error putting item into table {table.table_name}: {e}")
        raise

def get_item(table, key: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Get an item from a DynamoDB table.
    
    Args:
        table: DynamoDB table resource
        key (dict): Primary key of the item to retrieve
        
    Returns:
        dict or None: Item if found, None otherwise
        
    Raises:
        ClientError: If the get operation fails
    """
    try:
        response = table.get_item(Key=key)
        item = response.get('Item')
        if item:
            logger.info(f"Successfully retrieved item from table: {table.table_name}")
        else:
            logger.info(f"Item not found in table: {table.table_name}")
        return item
    except ClientError as e:
        logger.error(f"Error getting item from table {table.table_name}: {e}")
        raise

def update_item(table, key: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update an item in a DynamoDB table.
    
    Args:
        table: DynamoDB table resource
        key (dict): Primary key of the item to update
        updates (dict): Dictionary containing update expressions and values
                       Expected format: {
                           'UpdateExpression': 'SET #attr1 = :val1, #attr2 = :val2',
                           'ExpressionAttributeNames': {'#attr1': 'attribute1', '#attr2': 'attribute2'},
                           'ExpressionAttributeValues': {':val1': 'value1', ':val2': 'value2'}
                       }
        
    Returns:
        dict: Response from DynamoDB
        
    Raises:
        ClientError: If the update operation fails
    """
    try:
        update_params = {
            'Key': key,
            'ReturnValues': 'UPDATED_NEW'
        }
        update_params.update(updates)
        
        response = table.update_item(**update_params)
        logger.info(f"Successfully updated item in table: {table.table_name}")
        return response
    except ClientError as e:
        logger.error(f"Error updating item in table {table.table_name}: {e}")
        raise

def delete_item(table, key: Dict[str, Any]) -> Dict[str, Any]:
    """
    Delete an item from a DynamoDB table.
    
    Args:
        table: DynamoDB table resource
        key (dict): Primary key of the item to delete
        
    Returns:
        dict: Response from DynamoDB
        
    Raises:
        ClientError: If the delete operation fails
    """
    try:
        response = table.delete_item(Key=key)
        logger.info(f"Successfully deleted item from table: {table.table_name}")
        return response
    except ClientError as e:
        logger.error(f"Error deleting item from table {table.table_name}: {e}")
        raise

def scan_table(table, **kwargs) -> List[Dict[str, Any]]:
    """
    Scan a DynamoDB table and return all items.
    
    Args:
        table: DynamoDB table resource
        **kwargs: Additional parameters for the scan operation (e.g., FilterExpression, Limit)
        
    Returns:
        list: List of all items in the table
        
    Raises:
        ClientError: If the scan operation fails
    """
    try:
        items = []
        
        # Perform initial scan
        response = table.scan(**kwargs)
        items.extend(response.get('Items', []))
        
        # Handle pagination
        while 'LastEvaluatedKey' in response:
            kwargs['ExclusiveStartKey'] = response['LastEvaluatedKey']
            response = table.scan(**kwargs)
            items.extend(response.get('Items', []))
        
        logger.info(f"Successfully scanned table {table.table_name}, found {len(items)} items")
        return items
    except ClientError as e:
        logger.error(f"Error scanning table {table.table_name}: {e}")
        raise

# Helper functions for common DynamoDB operations

def batch_get_items(table, keys: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Batch get multiple items from a DynamoDB table.
    
    Args:
        table: DynamoDB table resource
        keys (list): List of primary keys
        
    Returns:
        list: List of retrieved items
    """
    try:
        # DynamoDB batch_get_item has a limit of 100 items per request
        items = []
        for i in range(0, len(keys), 100):
            batch_keys = keys[i:i+100]
            response = dynamodb_resource.batch_get_item(
                RequestItems={
                    table.table_name: {
                        'Keys': batch_keys
                    }
                }
            )
            items.extend(response['Responses'].get(table.table_name, []))
        
        logger.info(f"Successfully batch retrieved {len(items)} items from table: {table.table_name}")
        return items
    except ClientError as e:
        logger.error(f"Error batch getting items from table {table.table_name}: {e}")
        raise

def query_table(table, key_condition_expression, **kwargs) -> List[Dict[str, Any]]:
    """
    Query a DynamoDB table.
    
    Args:
        table: DynamoDB table resource
        key_condition_expression: Key condition for the query
        **kwargs: Additional parameters for the query operation
        
    Returns:
        list: List of items matching the query
    """
    try:
        items = []
        
        query_params = {
            'KeyConditionExpression': key_condition_expression,
            **kwargs
        }
        
        response = table.query(**query_params)
        items.extend(response.get('Items', []))
        
        # Handle pagination
        while 'LastEvaluatedKey' in response:
            query_params['ExclusiveStartKey'] = response['LastEvaluatedKey']
            response = table.query(**query_params)
            items.extend(response.get('Items', []))
        
        logger.info(f"Successfully queried table {table.table_name}, found {len(items)} items")
        return items
    except ClientError as e:
        logger.error(f"Error querying table {table.table_name}: {e}")
        raise