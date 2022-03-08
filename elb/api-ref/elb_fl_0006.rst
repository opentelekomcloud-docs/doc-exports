Querying Versions
=================

Function
^^^^^^^^

Queries all available versions.

If there is no version added to the URL, all available versions are returned.

URI
^^^

GET /

Request
^^^^^^^

None

Response
^^^^^^^^

None

Example
^^^^^^^

-  Example request

   .. code:: screen

      GET /

-  Example response

   .. code:: screen

      {
         "versions": [
            {
                "status": "CURRENT",
                "id": "v2.0",
                "links": [
               {
                  "href": "http://192.168.82.231:9696/v2.0",
                  "rel": "self"
               }
              ]
             }
           ]
      }
