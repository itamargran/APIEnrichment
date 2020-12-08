# ExploriumTakeHomeAssingment

This is my solution for the take home assingment, in which I was asked to create an enrichment service build on the external Overpass API.

The repo contains a REST API with single endpoint, that recieves data regarding a location (defined by latitude and longitude) and adds the number of schools in that area.

**For example:

```
curl --location --request POST 'localhost:5000/api/enrich' \
--header 'Content-Type: text/plain' \
--data-raw '{"data": [{"Latitude":-37.797, "Longitude":144.9051}]}'
```

 Will return:
```
{
    "data": [
        {
            "Latitude": -37.797,
            "Longitude": 144.9051,
            "Schools": 5,
        }
    ]
}
``` 
 ## Setup
 ```
 git clone https://github.com/itamargran/ExploriumTakeHomeAssingment.git
 ```
 #### Run Tests
 ```
 cd ExploriumTakeHomeAssingment
 cd src
 pip install -r requirements.txt
 pytest -vvv
 ```
 #### Build and Run Docker Container
 ```
 docker-compose up
 ```
 
 
