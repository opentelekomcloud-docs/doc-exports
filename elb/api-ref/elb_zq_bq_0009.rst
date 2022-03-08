Querying All Tags of a Listener
===============================

Function
^^^^^^^^

This API is used to query all tags of one listener.

|image1|

You can also use this API for dedicated load balancers.

Constraints
^^^^^^^^^^^

None

URI
^^^

GET /v2.0/{project_id}/listeners/{listener_id}/tags

.. table:: **Table 1** Parameter description

   =========== ============= ======== ==============================================================
   Parameter   **Mandatory** **Type** Description
   =========== ============= ======== ==============================================================
   project_id  Yes           String   Specifies the ID of the project where the tag is used.
   listener_id Yes           String   Specifies the ID of the listener whose tags are to be queried.
   =========== ============= ======== ==============================================================

Request
^^^^^^^

None

Response
^^^^^^^^

.. table:: **Table 2** Response parameters

   +-----------+----------+---------------------------------------------------------------------------------------------+
   | Parameter | **Type** | Description                                                                                 |
   +===========+==========+=============================================================================================+
   | tags      | Array    | Lists the tags. For details, see `Table                                                     |
   |           |          | 3 <#elb_zq_bq_0009__en-us_topic_0112614717_table9829182310517>`__.                          |
   +-----------+----------+---------------------------------------------------------------------------------------------+

.. table:: **Table 3** **tags** parameter description

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | **Type**                              | Description                           |
   +=======================================+=======================================+=======================================+
   | key                                   | String                                | Specifies the tag key.                |
   |                                       |                                       |                                       |
   |                                       |                                       | -  Cannot be left blank.              |
   |                                       |                                       | -  Can contain a maximum of 36        |
   |                                       |                                       |    characters.                        |
   |                                       |                                       | -  Can contain only the following     |
   |                                       |                                       |    character types:                   |
   |                                       |                                       |                                       |
   |                                       |                                       |    -  Uppercase letters               |
   |                                       |                                       |    -  Lowercase letters               |
   |                                       |                                       |    -  Digits                          |
   |                                       |                                       |    -  Special characters, including   |
   |                                       |                                       |       hyphens (-) and underscores (_) |
   |                                       |                                       |                                       |
   |                                       |                                       | -  The tag key of a listener must be  |
   |                                       |                                       |    unique.                            |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | value                                 | String                                | Specifies the tag value.              |
   |                                       |                                       |                                       |
   |                                       |                                       | -  Can contain a maximum of 43        |
   |                                       |                                       |    characters.                        |
   |                                       |                                       | -  Can contain only the following     |
   |                                       |                                       |    character types:                   |
   |                                       |                                       |                                       |
   |                                       |                                       |    -  Uppercase letters               |
   |                                       |                                       |    -  Lowercase letters               |
   |                                       |                                       |    -  Digits                          |
   |                                       |                                       |    -  Special characters, including   |
   |                                       |                                       |       hyphens (-) and underscores (_) |
   +---------------------------------------+---------------------------------------+---------------------------------------+

Example Request
^^^^^^^^^^^^^^^

-  Example request

   .. code:: screen

      GET https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/7add33ad-11dc-4ab9-a50f-419703f13163/tags

Example Response
^^^^^^^^^^^^^^^^

-  Example response

   .. code:: screen

      {
          "tags": [
              {
                  "key": "key1", 
                  "value": "value1"
              }, 
              {
                  "key": "key2", 
                  "value": "value2"
              }
          ]
      }

Status Code
^^^^^^^^^^^

For details, see `Status Codes <elb_zq_bq_0013.html#elb_zq_bq_0013>`__.

**Parent topic:** `Tag <elb_zq_bq_0000.html>`__

.. |image1| image:: public_sys-resources/note_3.0-en-us.png
