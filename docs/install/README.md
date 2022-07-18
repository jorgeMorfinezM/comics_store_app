<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Microservice N-Layered Domain Driven Design Template</h3>

  <p align="center">
    Domain Driven Design Template to implement on microservice
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started 🚀

Setting up these environment constants to execute the microservice.

### Prerequisites ✔️

These are the environment constants to build and run microservice project on staging or test environment.
Production environment needed.

* Environment variables required
  ### ms Envs
  - FLASK_SECRET_KEY=The flask secret key
  - FLASK_APP=Directory to en-route the flask application and config
  - FLASK_ENV=Flask API web framework working environment
  - FLASK_RUN_PORT=Flask API port to run ms API

  - ENVIRONMENT=The environment, can be: "local", "test", "producccion"

  - CONTENT_TYPE=The content type available to response and request or response API
  - HEADERS=The dictionary to set headers of an API endpoint request

  - CORS_METHOD_GET=It's the HTTP method to accept by the CORS
  - HTTP_METHODS_ALLOW=It's the list of the methods accepted on the CORS
  - ORIGINS=It's the list of the URL host to consider by the CORS

  - MARVEL_URL_HOST=It's the API host to retrieve data from the endpoint API microservice

  - ENDPOINT_CHARACTERS_ORDERBY_NAME=Endpoint to retrieve characters data ordered by name in ascending order
  - ENDPOINT_CHARACTERS_BY_NAME=Endpoint to retrieve character data filtered by name in ascending order
  - ENDPOINT_CHARACTERS_START_NAME=Endpoint to retrieve character data filtered by some letters of the name

  - ENDPOINT_COMIC_BY_TITLE=Endpoint to retrieve comic data filtered by title of the comic
  - ENDPOINT_COMIC_START_TITLE=Endpoint to retrieve comic data filtered by some letters of the comic title

  - MARVEL_API_PUBLIC_KEY=The Public key of the Marvel API developer portal account to request on endpoints collection
  - MARVEL_API_PRIVATE_KEY=The Public key of the Marvel API developer portal account to request on endpoints collection

  - LOOKING_FOR_CRITERIA_ACCEPTANCE=The lis of words of criteria acceptance to search between comics or characters



Make with ❤️ by Jorge Morfinez Mojica
