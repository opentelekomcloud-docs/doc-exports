Deleting a Forwarding Policy
============================

Function
^^^^^^^^

This API is used to delete a specific forwarding policy.

URI
^^^

DELETE /v2.0/lbaas/l7policies/{l7policy_id}

.. table:: **Table 1** Parameter description

   =========== ========= ====== ===================================
   Parameter   Mandatory Type   Description
   =========== ========= ====== ===================================
   l7policy_id Yes       Object Specifies the forwarding policy ID.
   =========== ========= ====== ===================================

Request
^^^^^^^

None

Response
^^^^^^^^

None

Example Request
^^^^^^^^^^^^^^^

-  Example request: Deleting a forwarding policy

   .. code:: screen

      DELETE https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586

Example Response
^^^^^^^^^^^^^^^^

-  Example response

   None

Status Code
^^^^^^^^^^^

For details, see `HTTP Status Codes of Shared Load Balancers <elb_gc_0002.html>`__.

**Parent topic:** `Forwarding Policy <elb_zq_zf_0000.html>`__
