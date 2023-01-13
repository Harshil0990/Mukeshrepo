
import azure.functions as func
import logging
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential



def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get("name")

    account_url = "https://stpdemo2298.blob.core.windows.net"
    default_credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient.from_connection_string("BlobEndpoint=https://stpdemo2298.blob.core.windows.net/;QueueEndpoint=https://stpdemo2298.queue.core.windows.net/;FileEndpoint=https://stpdemo2298.file.core.windows.net/;TableEndpoint=https://stpdemo2298.table.core.windows.net/;SharedAccessSignature=sv=2021-06-08&ss=bfqt&srt=c&sp=rwdlacupyx&se=2023-01-12T21:08:23Z&st=2023-01-12T13:08:23Z&spr=https&sig=MbQoqVoS18jdyJ9e4fBv5HMOOd7Mvqt%2FM8I1tTPGFRQ%3D")
    #blob_service_client = BlobServiceClient(account_url, credential=default_credential)


    try:
        f = open("demo.txt", "a")
        f.write(name)
        f.close()
        
        container_client = blob_service_client.create_container(name)

        blob_client = blob_service_client.get_blob_client(container='pytesting', blob='demo.txt' )
        with open("demo.txt",'rb') as f:blob_client.upload_blob(f)
        return func.HttpResponse("success",status_code=200)
    except Exception as e:
        return func.HttpResponse(str(e),status_code=200)

