Querying the Tags of All Load Balancers
=======================================

Function
^^^^^^^^

This API is used to query the tags of all the load balancers.

|image1|

You can also use this API for dedicated load balancers.

URI
^^^

GET /v2.0/{project_id}/loadbalancers/tags

.. table:: **Table 1** Parameter description

   ========== ============= ======== ======================================================
   Parameter  **Mandatory** **Type** Description
   ========== ============= ======== ======================================================
   project_id Yes           String   Specifies the ID of the project where the tag is used.
   ========== ============= ======== ======================================================

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
   |           |          | 3 <#elb_zq_bq_0004__en-us_topic_0109852828_en-us_topic_0101983303_table1878907810595>`__.   |
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
   |                                       |                                       | -  The tag key of a load balancer     |
   |                                       |                                       |    must be unique.                    |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | values                                | Array                                 | Lists the tag values.                 |
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

      GET https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/tags

Example Response
^^^^^^^^^^^^^^^^

-  Example response

   .. code:: screen

      {
          "tags": [
              {
                  "key": "key1", 
                  "values": [
                      "value1", 
                      "value2"
                  ]
              }, 
              {
                  "key": "key2", 
                  "values": [
                      "value1", 
                      "value2"
                  ]
              }
          ]
      }

Status Code
^^^^^^^^^^^

For details, see `Status Codes <elb_zq_bq_0013.html#elb_zq_bq_0013>`__.

**Parent topic:** `Tag <elb_zq_bq_0000.html>`__

.. |image1| image:: public_sys-resources/note_3.0-en-us.png
