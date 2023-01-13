import logging
import uuid
from azure.storage.blob import BlobServiceClient
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
   
    service = BlobServiceClient(account_url="https://stpdemo2298.blob.core.windows.net", 
    credential={"account_name": "stpdemo2298", "account_key":"xKepZnmTE49iq7XJINPF6m8f6DFkG3l5QWJerAZmudz00EjRvdf00o+aEQ4DxlhRCXQtP7WDgjSP+AStTXUlFQ=="})

    # Create a unique name for the container
    container_name = str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(name)
   
    return func.HttpResponse("This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",status_code=200)


 