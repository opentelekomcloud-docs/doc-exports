Viewing Details of a Backend Server Group
=========================================

Function
^^^^^^^^

This API is used to view details of a backend server group.

URI
^^^

GET /v3/{project_id}/elb/pools/{pool_id}

.. table:: **Table 1** Path parameters

   ========== ========= ====== =============================================
   Parameter  Mandatory Type   Description
   ========== ========= ====== =============================================
   project_id Yes       String Specifies the project ID.
   pool_id    Yes       String Specifies the ID of the backend server group.
   ========== ========= ====== =============================================

Request Parameters
^^^^^^^^^^^^^^^^^^

.. table:: **Table 2** Request header parameters

   ============ ========= ====== ================================================
   Parameter    Mandatory Type   Description
   ============ ========= ====== ================================================
   X-Auth-Token Yes       String Specifies the token used for IAM authentication.
   ============ ========= ====== ================================================

Response Parameters
^^^^^^^^^^^^^^^^^^^

**Status code: 200**

.. table:: **Table 3** Response body parameters

   ========== ========================================== ===============================================================
   Parameter  Type                                       Description
   ========== ========================================== ===============================================================
   request_id String                                     Specifies the request ID. The value is automatically generated.
   pool       `Pool <#ShowPool__response_Pool>`__ object Specifies the backend server group.
   ========== ========================================== ===============================================================

.. table:: **Table 4** Pool

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | admin_state_up                        | Boolean                               | Specifies the administrative status   |
   |                                       |                                       | of the backend server group. The      |
   |                                       |                                       | value can only be updated to          |
   |                                       |                                       | **true**.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **true**                     |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | description                           | String                                | Provides supplementary information    |
   |                                       |                                       | about the backend server group.       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | healthmonitor_id                      | String                                | Specifies the ID of the health check  |
   |                                       |                                       | configured for the backend server     |
   |                                       |                                       | group.                                |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | id                                    | String                                | Specifies the backend server group    |
   |                                       |                                       | ID.                                   |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | lb_algorithm                          | String                                | Specifies the load balancing          |
   |                                       |                                       | algorithm used by the load balancer   |
   |                                       |                                       | to route requests to backend servers  |
   |                                       |                                       | in the backend server group.          |
   |                                       |                                       |                                       |
   |                                       |                                       | The value can be **ROUND_ROBIN**      |
   |                                       |                                       | (weighted round robin),               |
   |                                       |                                       | **LEAST_CONNECTIONS** (weighted least |
   |                                       |                                       | connections), or **SOURCE_IP**        |
   |                                       |                                       | (source IP hash).                     |
   |                                       |                                       |                                       |
   |                                       |                                       | When the value is **SOURCE_IP**, the  |
   |                                       |                                       | **weight** parameter is invalid.      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | listeners                             | Array of                              | Lists the listeners associated with   |
   |                                       | `ListenerRef                          | the backend server group.             |
   |                                       |  <#ShowPool__response_ListenerRef>`__ |                                       |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | loadbalancers                         | Array of                              | Lists the IDs of load balancers       |
   |                                       | `LoadBalancerRef <#S                  | associated with the backend server    |
   |                                       | howPool__response_LoadBalancerRef>`__ | group.                                |
   |                                       | objects                               |                                       |
   |                                       |                                       | If only **listener_id** is specified  |
   |                                       |                                       | during the creation of the backend    |
   |                                       |                                       | server group, the ID of the           |
   |                                       |                                       | **loadbalancers** parameter in the    |
   |                                       |                                       | response is the ID of the load        |
   |                                       |                                       | balancer to which the listener is     |
   |                                       |                                       | added.                                |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | members                               | Array of                              | Lists the backend servers in the      |
   |                                       | `MemberR                              | backend server group.                 |
   |                                       | ef <#ShowPool__response_MemberRef>`__ |                                       |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | name                                  | String                                | Specifies the backend server group    |
   |                                       |                                       | name.                                 |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | project_id                            | String                                | Specifies the project ID.             |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | protocol                              | String                                | Specifies the protocol used by the    |
   |                                       |                                       | backend server group to receive       |
   |                                       |                                       | requests. The protocol can be TCP,    |
   |                                       |                                       | UDP, or HTTP.                         |
   |                                       |                                       |                                       |
   |                                       |                                       | -  For UDP listeners, the protocol of |
   |                                       |                                       |    the backend server group must be   |
   |                                       |                                       |    UDP.                               |
   |                                       |                                       |                                       |
   |                                       |                                       | -  For TCP listeners, the protocol of |
   |                                       |                                       |    the backend server group must be   |
   |                                       |                                       |    TCP.                               |
   |                                       |                                       |                                       |
   |                                       |                                       | -  For HTTP or HTTPS listeners, the   |
   |                                       |                                       |    protocol of the backend server     |
   |                                       |                                       |    group must be HTTP.                |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | session_persistence                   | `SessionPersistence <#Show            | Specifies the sticky session.         |
   |                                       | Pool__response_SessionPersistence>`__ |                                       |
   |                                       | object                                |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ip_version                            | String                                | Specifies the IP version supported by |
   |                                       |                                       | the backend server group.             |
   |                                       |                                       |                                       |
   |                                       |                                       | -  Shared load balancers: The default |
   |                                       |                                       |    value is **v4**.                   |
   |                                       |                                       |                                       |
   |                                       |                                       | -  Dedicated load balancers: The      |
   |                                       |                                       |    value can be **dualstack**,        |
   |                                       |                                       |    **v4**, or **v6**.                 |
   |                                       |                                       |                                       |
   |                                       |                                       | When the protocol of the backend      |
   |                                       |                                       | server group is TCP or UDP,           |
   |                                       |                                       | **ip_version** is set to              |
   |                                       |                                       | **dualstack**, indicating that both   |
   |                                       |                                       | IPv4 and IPv6 are supported.          |
   |                                       |                                       |                                       |
   |                                       |                                       | When the protocol of the backend      |
   |                                       |                                       | server group is HTTP, **ip_version**  |
   |                                       |                                       | is set to **v4**.                     |
   |                                       |                                       |                                       |
   |                                       |                                       | IPv6 is unsupported. Only **v4** is   |
   |                                       |                                       | returned.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **dualstack**                |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | slow_start                            | `SlowSta                              | Specifies whether to enable slow      |
   |                                       | rt <#ShowPool__response_SlowStart>`__ | start. After you enable slow start,   |
   |                                       | object                                | new backend servers added to the      |
   |                                       |                                       | backend server group are warmed up,   |
   |                                       |                                       | and the number of requests they can   |
   |                                       |                                       | receive increases linearly during the |
   |                                       |                                       | configured slow start duration.       |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter can be used when the   |
   |                                       |                                       | protocol of the backend server group  |
   |                                       |                                       | is HTTP or HTTPS. An error will be    |
   |                                       |                                       | returned if the protocol is not HTTP  |
   |                                       |                                       | or HTTPS.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 5** ListenerRef

   ========= ====== ==========================
   Parameter Type   Description
   ========= ====== ==========================
   id        String Specifies the listener ID.
   ========= ====== ==========================

.. table:: **Table 6** LoadBalancerRef

   ========= ====== ===============================
   Parameter Type   Description
   ========= ====== ===============================
   id        String Specifies the load balancer ID.
   ========= ====== ===============================

.. table:: **Table 7** MemberRef

   ========= ====== ================================
   Parameter Type   Description
   ========= ====== ================================
   id        String Specifies the backend server ID.
   ========= ====== ================================

.. table:: **Table 8** SessionPersistence

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | cookie_name                           | String                                | Specifies the cookie name.            |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter will take effect only  |
   |                                       |                                       | when **type** is set to               |
   |                                       |                                       | **APP_COOKIE**.                       |
   |                                       |                                       |                                       |
   |                                       |                                       | The value can contain only letters,   |
   |                                       |                                       | digits, hyphens (-), underscores (_), |
   |                                       |                                       | and periods (.).                      |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **0**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **1024**                     |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | type                                  | String                                | Specifies the sticky session type.    |
   |                                       |                                       | The value can be **SOURCE_IP**,       |
   |                                       |                                       | **HTTP_COOKIE**, or **APP_COOKIE**.   |
   |                                       |                                       |                                       |
   |                                       |                                       | -  If the protocol of the backend     |
   |                                       |                                       |    server group is TCP or UDP, only   |
   |                                       |                                       |    **SOURCE_IP** takes effect.        |
   |                                       |                                       |                                       |
   |                                       |                                       | -  For dedicated load balancers, if   |
   |                                       |                                       |    the protocol of the backend server |
   |                                       |                                       |    group is HTTP or HTTPS, the value  |
   |                                       |                                       |    can only be **HTTP_COOKIE**.       |
   |                                       |                                       |                                       |
   |                                       |                                       | -  For shared load balancers, if the  |
   |                                       |                                       |    protocol of the backend server     |
   |                                       |                                       |    group is HTTP or HTTPS, the value  |
   |                                       |                                       |    can be **HTTP_COOKIE** or          |
   |                                       |                                       |    **APP_COOKIE**.                    |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | persistence_timeout                   | Integer                               | Specifies the stickiness duration, in |
   |                                       |                                       | minutes. This parameter will not take |
   |                                       |                                       | effect when **type** is set to        |
   |                                       |                                       | **APP_COOKIE**.                       |
   |                                       |                                       |                                       |
   |                                       |                                       | -  If the protocol of the backend     |
   |                                       |                                       |    server group is TCP or UDP, the    |
   |                                       |                                       |    value ranges from **1** to **60**, |
   |                                       |                                       |    and the default value is **1**.    |
   |                                       |                                       |                                       |
   |                                       |                                       | -  If the protocol of the backend     |
   |                                       |                                       |    server group is HTTP or HTTPS, the |
   |                                       |                                       |    value ranges from **1** to         |
   |                                       |                                       |    **1440**, and the default value is |
   |                                       |                                       |    **1440**.                          |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 9** SlowStart

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | enable                                | Boolean                               | Specifies whether to enable slow      |
   |                                       |                                       | start.                                |
   |                                       |                                       |                                       |
   |                                       |                                       | **true** indicates that this function |
   |                                       |                                       | is enabled, and **false** indicates   |
   |                                       |                                       | this function is disabled.            |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **false**                    |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | duration                              | Integer                               | Specifies the slow start duration, in |
   |                                       |                                       | seconds.                              |
   |                                       |                                       |                                       |
   |                                       |                                       | The value ranges from **30** to       |
   |                                       |                                       | **1200**, and the default value is    |
   |                                       |                                       | **30**.                               |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **30**                       |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **1200**                     |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **30**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+

Example Requests
^^^^^^^^^^^^^^^^

.. code:: screen

   GET

   https://{elb_endpoint}/v3/99a3fff0d03c428eac3678da6a7d0f24/elb/pools/36ce7086-a496-4666-9064-5ba0e6840c75

Example Responses
^^^^^^^^^^^^^^^^^

**Status code: 200**

Successful request.

.. code:: screen

   {
     "pool" : {
       "lb_algorithm" : "LEAST_CONNECTIONS",
       "protocol" : "TCP",
       "description" : "My pool",
       "admin_state_up" : true,
       "loadbalancers" : [ {
         "id" : "098b2f68-af1c-41a9-8efd-69958722af62"
       } ],
       "project_id" : "99a3fff0d03c428eac3678da6a7d0f24",
       "session_persistence" : "",
       "healthmonitor_id" : "",
       "listeners" : [ {
         "id" : "0b11747a-b139-492f-9692-2df0b1c87193"
       }, {
         "id" : "61942790-2367-482a-8b0e-93840ea2a1c6"
       }, {
         "id" : "fd8f954c-f0f8-4d39-bb1d-41637cd6b1be"
       } ],
       "members" : [ ],
       "id" : "36ce7086-a496-4666-9064-5ba0e6840c75",
       "name" : "My pool.",
       "ip_version" : "dualstack"
     },
     "request_id" : "c1a60da2-1ec7-4a1c-b4cc-73e1a57b368e"
   }

Status Codes
^^^^^^^^^^^^

=========== ===================
Status Code Description
=========== ===================
200         Successful request.
=========== ===================

Error Codes
^^^^^^^^^^^

See `Error Codes <errorcode.html>`__.

**Parent topic:** `Backend Server Group <topic_300000006.html>`__
