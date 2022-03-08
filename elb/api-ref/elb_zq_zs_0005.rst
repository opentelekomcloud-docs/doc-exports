Deleting a Certificate
======================

Function
^^^^^^^^

This API is used to delete a specific certificate.

Constraints
^^^^^^^^^^^

If the target certificate is used by a listener, the certificate cannot be deleted, and 409 code will be displayed.

URI
^^^

DELETE /v2.0/lbaas/certificates/{certificate_id}

.. table:: **Table 1** Parameter description

   ============== ========= ====== =============================
   Parameter      Mandatory Type   Description
   ============== ========= ====== =============================
   certificate_id Yes       String Specifies the certificate ID.
   ============== ========= ====== =============================

Request
^^^^^^^

-  Request parameters

   None

Response
^^^^^^^^

-  Response parameters

   None

Example Request
^^^^^^^^^^^^^^^

-  Example request: Deleting a certificate

   .. code:: screen

      DELETE https://{Endpoint}/v2.0/lbaas/certificates/23ef9aad4ecb463580476d324a6c71af

Example Response
^^^^^^^^^^^^^^^^

-  Example response 1

   None

Status Code
^^^^^^^^^^^

For details, see `Status Codes <elb_gc_1102.html#elb_gc_1102>`__.

**Parent topic:** `Certificate <elb_zq_zs_0000.html>`__
