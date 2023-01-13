import azure.functions as func
import logging
from azure.storage.blob import BlobServiceClient


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')

    try:
        print("ok")

        #blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=stpdemo2298;AccountKey=xKepZnmTE49iq7XJINPF6m8f6DFkG3l5QWJerAZmudz00EjRvdf00o+aEQ4DxlhRCXQtP7WDgjSP+AStTXUlFQ==;EndpointSuffix=core.windows.net")
        #blob_client = blob_service_client.get_blob_client(container='pytesting',blob='demo.txt' )
 
        #f = open("demo.txt", "a")
        #f.write(f"{name}")
        #f.close()
        
        #with open("demo.txt",'rb') as f:
        #    blob_client.upload_blob(f)
    
    except:
        return "code not run "

   
    return func.HttpResponse("This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",status_code=200)
