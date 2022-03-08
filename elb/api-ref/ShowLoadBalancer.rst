Viewing Details of a Load Balancer
==================================

Function
^^^^^^^^

This API is used to view details of a load balancer.

URI
^^^

GET /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}

.. table:: **Table 1** Path parameters

   =============== ========= ====== ===============================
   Parameter       Mandatory Type   Description
   =============== ========= ====== ===============================
   project_id      Yes       String Specifies the project ID.
   loadbalancer_id Yes       String Specifies the load balancer ID.
   =============== ========= ====== ===============================

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

   +--------------+--------------------------------------------------+--------------------------------------------------+
   | Parameter    | Type                                             | Description                                      |
   +==============+==================================================+==================================================+
   | request_id   | String                                           | Specifies the request ID. The value is           |
   |              |                                                  | automatically generated.                         |
   +--------------+--------------------------------------------------+--------------------------------------------------+
   | loadbalancer | `LoadBalanc                                      | Specifies the load balancer.                     |
   |              | er <#ShowLoadBalancer__response_LoadBalancer>`__ |                                                  |
   |              | object                                           |                                                  |
   +--------------+--------------------------------------------------+--------------------------------------------------+

.. table:: **Table 4** LoadBalancer

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | id                                    | String                                | Specifies the load balancer ID.       |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **Automatically generated**  |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | description                           | String                                | Provides supplementary information    |
   |                                       |                                       | about the load balancer.              |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **255**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | provisioning_status                   | String                                | Specifies the provisioning status of  |
   |                                       |                                       | the load balancer. The value can only |
   |                                       |                                       | be **ACTIVE**.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | admin_state_up                        | Boolean                               | Specifies the administrative status   |
   |                                       |                                       | of the load balancer. The value can   |
   |                                       |                                       | only be **true**.                     |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **true**                     |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | provider                              | String                                | Specifies the provider of the load    |
   |                                       |                                       | balancer. The value can only be       |
   |                                       |                                       | **vlb**.                              |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **vlb**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | pools                                 | Array of                              | Lists the IDs of backend server       |
   |                                       | `PoolRef <#S                          | groups associated with the load       |
   |                                       | howLoadBalancer__response_PoolRef>`__ | balancer.                             |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | listeners                             | Array of                              | Lists the IDs of listeners added to   |
   |                                       | `ListenerRef <#ShowL                  | the load balancer.                    |
   |                                       | oadBalancer__response_ListenerRef>`__ |                                       |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | operating_status                      | String                                | Specifies the operating status of the |
   |                                       |                                       | load balancer. The value can only be  |
   |                                       |                                       | **ONLINE**.                           |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **16**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | vip_address                           | String                                | Specifies the private IPv4 address    |
   |                                       |                                       | bound to the load balancer.           |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **64**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | vip_subnet_cidr_id                    | String                                | Specifies the ID of the IPv4 subnet   |
   |                                       |                                       | where the load balancer works.        |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **36**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | name                                  | String                                | Specifies the name of the load        |
   |                                       |                                       | balancer.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **255**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | project_id                            | String                                | Specifies the project ID of the load  |
   |                                       |                                       | balancer.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **32**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | vip_port_id                           | String                                | Specifies the ID of the port bound to |
   |                                       |                                       | the virtual IP address (the value of  |
   |                                       |                                       | **vip_address**) of the load          |
   |                                       |                                       | balancer.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | When you create a dedicated load      |
   |                                       |                                       | balancer, the system automatically    |
   |                                       |                                       | creates a port for the load balancer  |
   |                                       |                                       | and associates the port with a        |
   |                                       |                                       | default security group. However,      |
   |                                       |                                       | security group rules containing the   |
   |                                       |                                       | port will not affect traffic to and   |
   |                                       |                                       | from the load balancer.               |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | tags                                  | Array of                              | Lists the tags added to the load      |
   |                                       | `Tag                                  | balancer.                             |
   |                                       |  <#ShowLoadBalancer__response_Tag>`__ |                                       |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | created_at                            | String                                | Specifies the time when the load      |
   |                                       |                                       | balancer was created.                 |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **20**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | updated_at                            | String                                | Specifies the time when the load      |
   |                                       |                                       | balancer was updated.                 |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **20**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | guaranteed                            | Boolean                               | Specifies whether the load balancer   |
   |                                       |                                       | is a dedicated load balancer.         |
   |                                       |                                       |                                       |
   |                                       |                                       | The value can be **true** or          |
   |                                       |                                       | **false**. **true** indicates a       |
   |                                       |                                       | dedicated load balancer, and          |
   |                                       |                                       | **false** indicates a shared load     |
   |                                       |                                       | balancer. When dedicated load         |
   |                                       |                                       | balancers are launched in the         |
   |                                       |                                       | **eu-de** region, either **true** or  |
   |                                       |                                       | **false** will be returned when you   |
   |                                       |                                       | use the API to query or update a load |
   |                                       |                                       | balancer.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **true**                     |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | vpc_id                                | String                                | Specifies the ID of the VPC where the |
   |                                       |                                       | load balancer works.                  |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | eips                                  | Array of                              | Specifies the EIP bound to the load   |
   |                                       | `EipInfo <#S                          | balancer.                             |
   |                                       | howLoadBalancer__response_EipInfo>`__ |                                       |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ipv6_vip_address                      | String                                | Specifies the IPv6 address bound to   |
   |                                       |                                       | the load balancer.                    |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **None**                     |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **64**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ipv6_vip_virsubnet_id                 | String                                | Specifies the ID of the IPv6 subnet   |
   |                                       |                                       | where the load balancer works.        |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ipv6_vip_port_id                      | String                                | Specifies the ID of the port bound to |
   |                                       |                                       | the IPv6 address.                     |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | availability_zone_list                | Array of strings                      | Specifies the list of AZs where the   |
   |                                       |                                       | load balancer is created.             |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | enterprise_project_id                 | String                                | Specifies the enterprise project ID.  |
   |                                       |                                       |                                       |
   |                                       |                                       | If this parameter is not passed       |
   |                                       |                                       | during resource creation, the         |
   |                                       |                                       | resource belongs to the default       |
   |                                       |                                       | enterprise project.                   |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **0**                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | l4_flavor_id                          | String                                | Specifies the Layer-4 flavor.         |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **255**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | l4_scale_flavor_id                    | String                                | Specifies the reserved Layer 4        |
   |                                       |                                       | flavor.                               |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **255**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | l7_flavor_id                          | String                                | Specifies the Layer-7 flavor.         |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **255**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | l7_scale_flavor_id                    | String                                | Specifies the reserved Layer 7        |
   |                                       |                                       | flavor.                               |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **255**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | publicips                             | Array of                              | Specifies the EIP bound to the load   |
   |                                       | `PublicIpInfo <#ShowLo                | balancer.                             |
   |                                       | adBalancer__response_PublicIpInfo>`__ |                                       |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | elb_virsubnet_ids                     | Array of strings                      | Specifies the ID of the subnet on the |
   |                                       |                                       | downstream plane. The ports used by   |
   |                                       |                                       | the load balancer dynamically occupy  |
   |                                       |                                       | IP addresses in the subnet.           |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ip_target_enable                      | Boolean                               | Specifies whether to enable cross-VPC |
   |                                       |                                       | backend.                              |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **false**                    |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | frozen_scene                          | String                                | Specifies the scenario where the load |
   |                                       |                                       | balancer is frozen. Use commas to     |
   |                                       |                                       | separate multiple scenarios.          |
   |                                       |                                       |                                       |
   |                                       |                                       | If the value is **ARREAR**, the load  |
   |                                       |                                       | balancer is frozen because your       |
   |                                       |                                       | account is in arrears.                |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ipv6_bandwidth                        | `BandwidthRef <#ShowLo                | Specifies the ID of the bandwidth.    |
   |                                       | adBalancer__response_BandwidthRef>`__ | This parameter is available only when |
   |                                       | object                                | you create or update a dedicated load |
   |                                       |                                       | balancer that has an IPv6 address     |
   |                                       |                                       | bound.                                |
   |                                       |                                       |                                       |
   |                                       |                                       | If you use a new IPv6 address and     |
   |                                       |                                       | specify a shared bandwidth, the IPv6  |
   |                                       |                                       | address will be added to the shared   |
   |                                       |                                       | bandwidth.                            |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 5** PoolRef

   ========= ====== =============================================
   Parameter Type   Description
   ========= ====== =============================================
   id        String Specifies the ID of the backend server group.
   ========= ====== =============================================

.. table:: **Table 6** ListenerRef

   ========= ====== ==========================
   Parameter Type   Description
   ========= ====== ==========================
   id        String Specifies the listener ID.
   ========= ====== ==========================

.. table:: **Table 7** Tag

   ========= ====== ========================
   Parameter Type   Description
   ========= ====== ========================
   key       String Specifies the tag key.
   value     String Specifies the tag value.
   ========= ====== ========================

.. table:: **Table 8** EipInfo

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | eip_id                                | String                                | Specifies the EIP ID.                 |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | eip_address                           | String                                | Specifies the specific IP address.    |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ip_version                            | Integer                               | Specifies the IP version. **4**       |
   |                                       |                                       | indicates IPv4, and **6** indicates   |
   |                                       |                                       | IPv6.                                 |
   |                                       |                                       |                                       |
   |                                       |                                       | IPv6 is unsupported. The value cannot |
   |                                       |                                       | be **6**.                             |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 9** PublicIpInfo

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | publicip_id                           | String                                | Specifies the EIP ID.                 |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | publicip_address                      | String                                | Specifies the IP address.             |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | ip_version                            | Integer                               | Specifies the IP version. The value   |
   |                                       |                                       | can be **4** (IPv4) or **6** (IPv6).  |
   |                                       |                                       |                                       |
   |                                       |                                       | IPv6 is unsupported. The value cannot |
   |                                       |                                       | be **6**.                             |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 10** BandwidthRef

   ========= ====== ==================================
   Parameter Type   Description
   ========= ====== ==================================
   id        String Specifies the shared bandwidth ID.
   ========= ====== ==================================

Example Requests
^^^^^^^^^^^^^^^^

Viewing details of a load balancer

.. code:: screen

   GET /v3/{project_id}/elb/loadbalancers/{loadbalancer_id}

   GET

   https://{ELB_Endpoint}/v3/060576782980d5762f9ec014dd2f1148/elb/loadbalancers/3dbde7e5-c277-4ea3-a424-edd339357eff

Example Responses
^^^^^^^^^^^^^^^^^

**Status code: 200**

Successful request.

.. code:: screen

   {
     "loadbalancer" : {
       "id" : "3dbde7e5-c277-4ea3-a424-edd339357eff",
       "project_id" : "060576782980d5762f9ec014dd2f1148",
       "name" : "elb-l4-no-delete",
       "vip_port_id" : "f079c7ee-65a9-44ef-be86-53d8927e59be",
       "vip_address" : "10.0.0.196",
       "admin_state_up" : true,
       "provisioning_status" : "ACTIVE",
       "operating_status" : "ONLINE",
       "listeners" : [ ],
       "pools" : [ {
         "id" : "1d864dc9-f6ef-4366-b59d-7034cde2328f"
       }, {
         "id" : "c0a2e4a1-c028-4a24-a62f-e721c52f5513"
       }, {
         "id" : "79308896-6169-4c28-acbc-e139eb661996"
       } ],
       "tags" : [ ],
       "created_at" : "2019-12-02T09:55:11Z",
       "updated_at" : "2019-12-02T09:55:11Z",
       "vpc_id" : "70711260-9de9-4d96-9839-0ae698e00109",
       "enterprise_project_id" : "0",
       "availability_zone_list" : [ ],
       "publicips" : [ ],
       "elb_virsubnet_ids" : [ "ad5d63bf-3b50-4e88-b4d9-e94a59aade48" ],
       "eips" : [ ],
       "guaranteed" : true,
       
       "l4_flavor_id" : "e5acacda-f861-404e-9871-df480c49d185",
       "vip_subnet_cidr_id" : "396d918a-756e-4163-8450-3bdc860109cf"
     },
     "request_id" : "1a47cfbf-969f-4e40-8c0e-c2e60b14bcac"
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

**Parent topic:** `Load Balancer <topic_300000003.html>`__
