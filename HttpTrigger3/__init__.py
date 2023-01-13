import logging
import uuid
from azure.storage.blob import BlobServiceClient
import azure.functions as func
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')


    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=stpdemo2298;AccountKey=xKepZnmTE49iq7XJINPF6m8f6DFkG3l5QWJerAZmudz00EjRvdf00o+aEQ4DxlhRCXQtP7WDgjSP+AStTXUlFQ==;EndpointSuffix=core.windows.net")
    
    conn_str = os.getenv('DefaultEndpointsProtocol=https;AccountName=stpdemo2298;AccountKey=xKepZnmTE49iq7XJINPF6m8f6DFkG3l5QWJerAZmudz00EjRvdf00o+aEQ4DxlhRCXQtP7WDgjSP+AStTXUlFQ==;EndpointSuffix=core.windows.net')

    
    
    f = open("test.txt", "a")
    f.write(f"{name}")
    f.close()

    

    blob_client = blob_service_client.get_blob_client(

    container='pytesting', # container to write to
    blob='test.txt' # name of blob
    )

# Write file to blob
    with open("demo.txt",'rb') as f:
        blob_client.upload_blob(f)
   
    return func.HttpResponse("This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",status_code=200)


 