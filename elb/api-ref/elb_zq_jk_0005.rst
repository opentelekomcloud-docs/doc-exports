Deleting a Health Check
=======================

Function
^^^^^^^^

This API is used to delete a health check.

Constraints
^^^^^^^^^^^

If **provisioning_status** of the load balancer for which the health check is configured is not **ACTIVE**, the health check cannot be deleted.

URI
^^^

DELETE /v2.0/lbaas/healthmonitors/{healthmonitor_id}

.. table:: **Table 1** Parameter description

   ================ ========= ====== ==============================
   Parameter        Mandatory Type   Description
   ================ ========= ====== ==============================
   healthmonitor_id Yes       String Specifies the health check ID.
   ================ ========= ====== ==============================

Request
^^^^^^^

None

Response
^^^^^^^^

None

Example Request
^^^^^^^^^^^^^^^

-  Example request: Deleting a health check

   .. code:: screen

      DELETE https://{Endpoint}/v2.0/lbaas/healthmonitors/b7633ade-24dc-4d72-8475-06aa22be5412

Example Response
^^^^^^^^^^^^^^^^

-  Example response

   None

Status Code
^^^^^^^^^^^

For details, see `Status Codes <elb_gc_1102.html#elb_gc_1102>`__.

**Parent topic:** `Health Check <elb_zq_jk_0000.html>`__
