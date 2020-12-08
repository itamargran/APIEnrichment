# ExploriumTakeHomeAssingment

This is my solution for the take home assingment, in which I was asked to create an enrichment service build on the external Overpass API.

The repo contains a REST API with single endpoint, that recieves data regarding a location (defined by latitude and lonitude) and adds the number of schools in that area.

For example:

**POST /api/enrich**
```
{
    "data": [
        {
            "Address": "9 Lynch St 3011, Melbourne, Australia",
            "Bathroom": 1,
            "Bedroom2": 3,
            "Car": 1,
            "Date": "2016-03-12",
            "Landsize": 292,
            "Latitude": -37.797,
            "Longitude": 144.9051,
            "Postcode": 3011,
            "Rooms": 3,
            "Suburb": "Footscray",
            "YearBuilt": 1900
        }
    ]
}
```

 Will return:
```
{
    "data": [
        {
            "Address": "9 Lynch St 3011, Melbourne, Australia",
            "Bathroom": 1,
            "Bedroom2": 3,
            "Car": 1,
            "Date": "2016-03-12",
            "Landsize": 292,
            "Latitude": -37.797,
            "Longitude": 144.9051,
            "Postcode": 3011,
            "Rooms": 3,
            "Schools": 5,
            "Suburb": "Footscray",
            "YearBuilt": 1900
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
 pytest -vvv
 ```
 #### Build and Run Docker Container
 ```
 docker-compose up
 ```
 
 
