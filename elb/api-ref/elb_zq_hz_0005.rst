Deleting a Backend Server Group
===============================

Function
^^^^^^^^

This API is used to delete a backend server group.

Constraints
^^^^^^^^^^^

Before deleting a backend server group, remove all backend servers, delete the health check, and disassociate forwarding policies from the backend server group by changing the value of **redirect_pool_id** to **null**. For details, see `Updating a Forwarding Policy <elb_zq_zf_0004.html#elb_zq_zf_0004>`__.

URI
^^^

DELETE /v2.0/lbaas/pools/{pool_id}

.. table:: **Table 1** Parameter description

   ========= ========= ====== =============================================
   Parameter Mandatory Type   Description
   ========= ========= ====== =============================================
   pool_id   Yes       String Specifies the ID of the backend server group.
   ========= ========= ====== =============================================

Request
^^^^^^^

None

Response
^^^^^^^^

None

Example Request
^^^^^^^^^^^^^^^

-  Example request: Deleting a backend server group

   .. code:: screen

      DELETE  /v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332

Example Response
^^^^^^^^^^^^^^^^

-  Example response

   None

Status Code
^^^^^^^^^^^

For details, see `Status Codes <elb_gc_1102.html#elb_gc_1102>`__.

**Parent topic:** `Backend Server Group <elb_zq_hz_0000.html>`__
