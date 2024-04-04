import azure.functions as func
import uuid

app = func.FunctionApp()

@app.function_name(name="registerDog")
@app.route(route="registerDog", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(arg_name="dogDocument", database_name="waqqly_database", container_name="waqqly_container", connection="CosmosDbConnectionSetting")
def add_dog_to_database(req: func.HttpRequest, dogDocument: func.Out[func.Document]) -> func.HttpResponse:
    
    dog_id = str(uuid.uuid4())
    dogs_name = req.params.get('dogsname')
    dogs_breed = req.params.get('dogsbreed')
    dogs_age = req.params.get('dogsage')
    dogs_gender = req.params.get('dogsgender')
    owners_forename = req.params.get('ownersforename')
    owners_surname = req.params.get('ownerssurname')
    owners_phone_number = req.params.get('ownersphonenumber')
    owners_email_address = req.params.get('ownersemailaddress') 

    if dogs_name and dogs_breed and dogs_age and dogs_gender and owners_forename and owners_surname and owners_phone_number and owners_email_address:
        dogDocument.set(func.Document.from_dict({"id": dog_id, "dogs_name": dogs_name, "dogs_breed": dogs_breed, "dogs_breed": dogs_breed, "dogs_age": dogs_age, "dogs_gender": dogs_gender, "owners_forename": owners_forename, "owners_surname": owners_surname, "owners_phone_number": owners_phone_number, "owners_email_address": owners_email_address})) 
        return func.HttpResponse(status_code=204)
    else:
        return func.HttpResponse(status_code=400)


@app.function_name(name="registerWalker")
@app.route(route="registerWalker", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(arg_name="walkerDocument", database_name="waqqly_database", container_name="waqqly_container", connection="CosmosDbConnectionSetting")
def add_walker_to_database(req: func.HttpRequest, walkerDocument: func.Out[func.Document]) -> func.HttpResponse:
    
    walker_id = str(uuid.uuid4())
    walkers_forename = req.params.get('forename')
    walkers_surname = req.params.get('surname')
    walkers_city = req.params.get('city')
    walkers_county = req.params.get('county')
    walkers_phone_number = req.params.get('phonenumber')
    walkers_email_address = req.params.get('emailaddress')

    if walkers_forename and walkers_surname and walkers_city and walkers_county and walkers_phone_number and walkers_email_address:
        walkerDocument.set(func.Document.from_dict({"id": walker_id, "walkers_forename": walkers_forename, "walkers_surname": walkers_surname, "walkers_city": walkers_city, "walkers_county": walkers_county, "walkers_phone_number": walkers_phone_number, "walkers_email_address": walkers_email_address})) 
        return func.HttpResponse(status_code = 204)
    else:
        return func.HttpResponse(status_code=400)