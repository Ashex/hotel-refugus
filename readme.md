# Hotel Refugus Lookup Demo

The hotel-refugus lookup demo has been designed as a python 3.7 Lambda function deployed behind API Gateway.



## Prerequisites
* Serverless Framework (minimum 1.61.3)
    * [serverless-python-requirements](https://github.com/UnitedIncome/serverless-python-requirements) plugin
* [Google Maps Python SDK](https://github.com/googlemaps/google-maps-services-python)
* AWS Account

## Quick Start

Once the prequisites are installed, configure your Places API Key in config.yaml in the following manner:

```yaml
api_key: <your_places_api_key>
```

Execute `serverless deploy` to deploy the application into your AWS Account then retrieve the POST endpoint and use it with the live demo:

http://hotel-refugus.s3-website.eu-central-1.amazonaws.com/

Contents of the live demo are located under `frontend-demo`

**Note**: The API Gateway URL contains the stage name (e.g /dev/query), a [custom domain](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) must be used to remove it.

## API Method

### Request Syntax

```
POST /query HTTP/1.1
Content-type: application/json

{
   "address": "string",
   "area": "int",
   "language": "string"
}
```

### URI Request Parameters
The request supports the following URI parameters.

**address** Postal Address (required)

**area** Radius in meters within which to return results (required)

**language**  The language code, indicating in which language the results should be returned, if possible. [List of support language codes](https://developers.google.com/maps/faq#languagesupport) (optional, default `en`)

### Response Syntax

An array of places in the requested vicinity of the address shall be returned.

```json
HTTP/1.1 200
Content-type: application/json

[
      {
         "geometry" : {
            "location" : {
               "lat" : -33.870775,
               "lng" : 151.199025
            }
         },
         "icon" : "http://maps.gstatic.com/mapfiles/place_api/icons/travel_agent-71.png",
         "id" : "21a0b251c9b8392186142c798263e289fe45b4aa",
         "name" : "Rhythmboat Cruises",
         "opening_hours" : {
            "open_now" : true
         },
         "photos" : [
            {
               "height" : 270,
               "html_attributions" : [],
               "photo_reference" : "CnRnAAAAF-LjFR1ZV93eawe1cU_3QNMCNmaGkowY7CnOf-kcNmPhNnPEG9W979jOuJJ1sGr75rhD5hqKzjD8vbMbSsRnq_Ni3ZIGfY6hKWmsOf3qHKJInkm4h55lzvLAXJVc-Rr4kI9O1tmIblblUpg2oqoq8RIQRMQJhFsTr5s9haxQ07EQHxoUO0ICubVFGYfJiMUPor1GnIWb5i8",
               "width" : 519
            }
         ],
         "place_id" : "ChIJyWEHuEmuEmsRm9hTkapTCrk",
         "reference" : "CoQBdQAAAFSiijw5-cAV68xdf2O18pKIZ0seJh03u9h9wk_lEdG-cP1dWvp_QGS4SNCBMk_fB06YRsfMrNkINtPez22p5lRIlj5ty_HmcNwcl6GZXbD2RdXsVfLYlQwnZQcnu7ihkjZp_2gk1-fWXql3GQ8-1BEGwgCxG-eaSnIJIBPuIpihEhAY1WYdxPvOWsPnb2-nGb6QGhTipN0lgaLpQTnkcMeAIEvCsSa0Ww",
         "types" : [ "travel_agency", "restaurant", "food", "establishment" ],
         "vicinity" : "Pyrmont Bay Wharf Darling Dr, Sydney"
      }
   ]
```
