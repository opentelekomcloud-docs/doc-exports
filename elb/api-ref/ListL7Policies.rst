Querying Forwarding Policies
============================

Function
^^^^^^^^

This API is used to query all forwarding policies.

Constraints
^^^^^^^^^^^

Parameters **marker**, **limit**, and **page_reverse** are used for pagination query.

Parameters **marker** and **page_reverse** take effect only when they are used together with parameter **limit**.

URI
^^^

GET /v3/{project_id}/elb/l7policies

.. table:: **Table 1** Path parameters

   ========== ========= ====== =========================
   Parameter  Mandatory Type   Description
   ========== ========= ====== =========================
   project_id Yes       String Specifies the project ID.
   ========== ========= ====== =========================

.. table:: **Table 2** Query parameters

   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | Parameter                   | Mandatory                   | Type                        | Description                 |
   +=============================+=============================+=============================+=============================+
   | marker                      | No                          | String                      | Specifies the ID of the     |
   |                             |                             |                             | last record on the previous |
   |                             |                             |                             | page.                       |
   |                             |                             |                             |                             |
   |                             |                             |                             | Note:                       |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  This parameter must be   |
   |                             |                             |                             |    used together with       |
   |                             |                             |                             |    **limit**.               |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  If this parameter is not |
   |                             |                             |                             |    specified, the first     |
   |                             |                             |                             |    page will be queried.    |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  This parameter cannot be |
   |                             |                             |                             |    left blank or set to an  |
   |                             |                             |                             |    invalid ID.              |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | limit                       | No                          | Integer                     | Specifies the number of     |
   |                             |                             |                             | records on each page.       |
   |                             |                             |                             |                             |
   |                             |                             |                             | Minimum: **0**              |
   |                             |                             |                             |                             |
   |                             |                             |                             | Maximum: **2000**           |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | page_reverse                | No                          | Boolean                     | Specifies the page          |
   |                             |                             |                             | direction.                  |
   |                             |                             |                             |                             |
   |                             |                             |                             | The value can be **true**   |
   |                             |                             |                             | or **false**, and the       |
   |                             |                             |                             | default value is **false**. |
   |                             |                             |                             |                             |
   |                             |                             |                             | The last page in the list   |
   |                             |                             |                             | requested with              |
   |                             |                             |                             | **page_reverse** set to     |
   |                             |                             |                             | **false** will not contain  |
   |                             |                             |                             | the "next" link, and the    |
   |                             |                             |                             | last page in the list       |
   |                             |                             |                             | requested with              |
   |                             |                             |                             | **page_reverse** set to     |
   |                             |                             |                             | **true** will not contain   |
   |                             |                             |                             | the "previous" link.        |
   |                             |                             |                             |                             |
   |                             |                             |                             | This parameter must be used |
   |                             |                             |                             | together with **limit**.    |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | enterprise_project_id       | No                          | Array                       | Specifies the enterprise    |
   |                             |                             |                             | project ID.                 |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  If this parameter is not |
   |                             |                             |                             |    passed, resources in the |
   |                             |                             |                             |    default enterprise       |
   |                             |                             |                             |    project are queried, and |
   |                             |                             |                             |    authentication is        |
   |                             |                             |                             |    performed based on the   |
   |                             |                             |                             |    default enterprise       |
   |                             |                             |                             |    project.                 |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  If this parameter is     |
   |                             |                             |                             |    passed, its value can be |
   |                             |                             |                             |    the ID of an existing    |
   |                             |                             |                             |    enterprise project or    |
   |                             |                             |                             |    **all_granted_eps**.     |
   |                             |                             |                             |                             |
   |                             |                             |                             | If the value is a specific  |
   |                             |                             |                             | ID, resources in the        |
   |                             |                             |                             | specific enterprise project |
   |                             |                             |                             | are required. If the value  |
   |                             |                             |                             | is **all_granted_eps**,     |
   |                             |                             |                             | resources in all enterprise |
   |                             |                             |                             | projects are queried.       |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple IDs can be queried |
   |                             |                             |                             | in the format of            |
   |                             |                             |                             | *enterprise_project_id=xxx& |
   |                             |                             |                             | enterprise_project_id=xxx*. |
   |                             |                             |                             |                             |
   |                             |                             |                             | This parameter is           |
   |                             |                             |                             | unsupported. Please do not  |
   |                             |                             |                             | use it.                     |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | id                          | No                          | Array                       | Specifies the forwarding    |
   |                             |                             |                             | policy ID.                  |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple IDs can be queried |
   |                             |                             |                             | in the format of            |
   |                             |                             |                             | *id=xxx&id=xxx*.            |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | name                        | No                          | Array                       | Specifies the forwarding    |
   |                             |                             |                             | policy name.                |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple names can be       |
   |                             |                             |                             | queried in the format of    |
   |                             |                             |                             | *name=xxx&name=xxx*.        |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | description                 | No                          | Array                       | Provides supplementary      |
   |                             |                             |                             | information about the       |
   |                             |                             |                             | forwarding policy.          |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple descriptions can   |
   |                             |                             |                             | be queried in the format of |
   |                             |                             |                             | *descri                     |
   |                             |                             |                             | ption=xxx&description=xxx*. |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | admin_state_up              | No                          | Boolean                     | Specifies the               |
   |                             |                             |                             | administrative status of    |
   |                             |                             |                             | the forwarding policy. The  |
   |                             |                             |                             | default value is **true**.  |
   |                             |                             |                             |                             |
   |                             |                             |                             | This parameter is           |
   |                             |                             |                             | unsupported. Please do not  |
   |                             |                             |                             | use it.                     |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | listener_id                 | No                          | Array                       | Specifies the ID of the     |
   |                             |                             |                             | listener to which the       |
   |                             |                             |                             | forwarding policy is added. |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  If **action** is set to  |
   |                             |                             |                             |    **REDIRECT_TO_POOL**,    |
   |                             |                             |                             |    the forwarding policy    |
   |                             |                             |                             |    can be added to an HTTP  |
   |                             |                             |                             |    or HTTPS listener.       |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  If **action** is set to  |
   |                             |                             |                             |                             |
   |                             |                             |                             |   **REDIRECT_TO_LISTENER**, |
   |                             |                             |                             |    the forwarding policy    |
   |                             |                             |                             |    can be added to an HTTP  |
   |                             |                             |                             |    listener.                |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple IDs can be queried |
   |                             |                             |                             | in the format of            |
   |                             |                             |                             | *listen                     |
   |                             |                             |                             | er_id=xxx&listener_id=xxx*. |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | position                    | No                          | Array                       | Specifies the forwarding    |
   |                             |                             |                             | policy priority.            |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple priorities can be  |
   |                             |                             |                             | queried in the format of    |
   |                             |                             |                             | *                           |
   |                             |                             |                             | position=xxx&position=xxx*. |
   |                             |                             |                             |                             |
   |                             |                             |                             | This parameter is           |
   |                             |                             |                             | unsupported. Please do not  |
   |                             |                             |                             | use it.                     |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | action                      | No                          | Array                       | Specifies where requests    |
   |                             |                             |                             | will be forwarded. The      |
   |                             |                             |                             | value can be one of the     |
   |                             |                             |                             | following:                  |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  **REDIRECT_TO_POOL**:    |
   |                             |                             |                             |    Requests will be         |
   |                             |                             |                             |    forwarded to another     |
   |                             |                             |                             |    backend server group.    |
   |                             |                             |                             |                             |
   |                             |                             |                             | -                           |
   |                             |                             |                             |   **REDIRECT_TO_LISTENER**: |
   |                             |                             |                             |    Requests will be         |
   |                             |                             |                             |    redirected to an HTTPS   |
   |                             |                             |                             |    listener.                |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple values can be      |
   |                             |                             |                             | queried in the format of    |
   |                             |                             |                             | *action=xxx&action=xxx*.    |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | redirect_url                | No                          | Array                       | Specifies the URL to which  |
   |                             |                             |                             | requests are forwarded.     |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple URLs can be        |
   |                             |                             |                             | queried in the format of    |
   |                             |                             |                             | *redirect                   |
   |                             |                             |                             | _url=xxx&redirect_url=xxx*. |
   |                             |                             |                             |                             |
   |                             |                             |                             | This parameter is           |
   |                             |                             |                             | unsupported. Please do not  |
   |                             |                             |                             | use it.                     |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | redirect_pool_id            | No                          | Array                       | Specifies the ID of the     |
   |                             |                             |                             | backend server group to     |
   |                             |                             |                             | which requests are          |
   |                             |                             |                             | forwarded. This parameter   |
   |                             |                             |                             | will take effect and is     |
   |                             |                             |                             | mandatory when **action**   |
   |                             |                             |                             | is set to                   |
   |                             |                             |                             | **REDIRECT_TO_POOL**.       |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple IDs can be queried |
   |                             |                             |                             | in the format of            |
   |                             |                             |                             | *redirect_pool_id           |
   |                             |                             |                             | =xxx&redirect_pool_id=xxx*. |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | redirect_listener_id        | No                          | Array                       | Specifies the ID of the     |
   |                             |                             |                             | listener to which requests  |
   |                             |                             |                             | are redirected. This        |
   |                             |                             |                             | parameter will take effect  |
   |                             |                             |                             | and is mandatory when       |
   |                             |                             |                             | **action** is set to        |
   |                             |                             |                             | **REDIRECT_TO_LISTENER**.   |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple IDs can be queried |
   |                             |                             |                             | in the format of            |
   |                             |                             |                             | *redirect_listener_id=xxx   |
   |                             |                             |                             | &redirect_listener_id=xxx*. |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | provisioning_status         | No                          | Array                       | Specifies the provisioning  |
   |                             |                             |                             | status of the forwarding    |
   |                             |                             |                             | policy. The value can only  |
   |                             |                             |                             | be **ACTIVE**, indicating   |
   |                             |                             |                             | that the forwarding policy  |
   |                             |                             |                             | is provisioned              |
   |                             |                             |                             | successfully.               |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple provisioning       |
   |                             |                             |                             | statuses can be queried in  |
   |                             |                             |                             | the format of               |
   |                             |                             |                             | *provisioning_status=xx     |
   |                             |                             |                             | x&provisioning_status=xxx*. |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | display_all_rules           | No                          | Boolean                     | Specifies whether to        |
   |                             |                             |                             | display all information     |
   |                             |                             |                             | about the forwarding rule   |
   |                             |                             |                             | in the forwarding policy.   |
   |                             |                             |                             | The value can be **true**   |
   |                             |                             |                             | or **false**.               |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  **true** indicates all   |
   |                             |                             |                             |    information about the    |
   |                             |                             |                             |    forwarding rule is       |
   |                             |                             |                             |    displayed.               |
   |                             |                             |                             |                             |
   |                             |                             |                             | -  **false** indicates that |
   |                             |                             |                             |    only the rule ID is      |
   |                             |                             |                             |    displayed.               |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+
   | priority                    | No                          | Array                       | Specifies the forwarding    |
   |                             |                             |                             | policy priority. A smaller  |
   |                             |                             |                             | value indicates a higher    |
   |                             |                             |                             | priority.                   |
   |                             |                             |                             |                             |
   |                             |                             |                             | Multiple priorities can be  |
   |                             |                             |                             | queried in the format of    |
   |                             |                             |                             | *                           |
   |                             |                             |                             | position=xxx&position=xxx*. |
   |                             |                             |                             |                             |
   |                             |                             |                             | This parameter is           |
   |                             |                             |                             | unsupported. Please do not  |
   |                             |                             |                             | use it.                     |
   +-----------------------------+-----------------------------+-----------------------------+-----------------------------+

Request Parameters
^^^^^^^^^^^^^^^^^^

.. table:: **Table 3** Request header parameters

   ============ ========= ====== ================================================
   Parameter    Mandatory Type   Description
   ============ ========= ====== ================================================
   X-Auth-Token Yes       String Specifies the token used for IAM authentication.
   ============ ========= ====== ================================================

Response Parameters
^^^^^^^^^^^^^^^^^^^

**Status code: 200**

.. table:: **Table 4** Response body parameters

   +------------+---------------------------------------------------+---------------------------------------------------+
   | Parameter  | Type                                              | Description                                       |
   +============+===================================================+===================================================+
   | request_id | String                                            | Specifies the request ID. The value is            |
   |            |                                                   | automatically generated.                          |
   +------------+---------------------------------------------------+---------------------------------------------------+
   | page_info  | `PageInfo <#ListL7Policies__response_PageInfo>`__ | Shows pagination information.                     |
   |            | object                                            |                                                   |
   +------------+---------------------------------------------------+---------------------------------------------------+
   | l7policies | Array of                                          | Lists the forwarding policies.                    |
   |            | `L7Policy <#ListL7Policies__response_L7Policy>`__ |                                                   |
   |            | objects                                           |                                                   |
   +------------+---------------------------------------------------+---------------------------------------------------+

.. table:: **Table 5** PageInfo

   +-----------------+---------+----------------------------------------------------------------------------------------+
   | Parameter       | Type    | Description                                                                            |
   +=================+=========+========================================================================================+
   | previous_marker | String  | Specifies the ID of the first record in the pagination query result. This parameter    |
   |                 |         | will not be returned if no query result is returned.                                   |
   +-----------------+---------+----------------------------------------------------------------------------------------+
   | next_marker     | String  | Marks the start record on the next page in the pagination query result. This parameter |
   |                 |         | will not be returned if there is no next page.                                         |
   +-----------------+---------+----------------------------------------------------------------------------------------+
   | current_count   | Integer | Specifies the number of records.                                                       |
   +-----------------+---------+----------------------------------------------------------------------------------------+

.. table:: **Table 6** L7Policy

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | action                                | String                                | Specifies where requests will be      |
   |                                       |                                       | forwarded. The value can be one of    |
   |                                       |                                       | the following:                        |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **REDIRECT_TO_POOL**: Requests     |
   |                                       |                                       |    will be forwarded to another       |
   |                                       |                                       |    backend server group.              |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **REDIRECT_TO_LISTENER**: Requests |
   |                                       |                                       |    will be redirected to an HTTPS     |
   |                                       |                                       |    listener.                          |
   |                                       |                                       |                                       |
   |                                       |                                       | **REDIRECT_TO_LISTENER** has the      |
   |                                       |                                       | highest priority. If requests are to  |
   |                                       |                                       | be redirected to an HTTPS listener,   |
   |                                       |                                       | other forwarding policies of the      |
   |                                       |                                       | listener will become invalid.         |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | admin_state_up                        | Boolean                               | Specifies the administrative status   |
   |                                       |                                       | of the forwarding policy. The default |
   |                                       |                                       | value is **true**.                    |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **true**                     |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | description                           | String                                | Provides supplementary information    |
   |                                       |                                       | about the forwarding policy.          |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | id                                    | String                                | Specifies the forwarding policy ID.   |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | listener_id                           | String                                | Specifies the ID of the listener to   |
   |                                       |                                       | which the forwarding policy is added. |
   |                                       |                                       |                                       |
   |                                       |                                       | -  If **action** is set to            |
   |                                       |                                       |    **REDIRECT_TO_POOL**, the          |
   |                                       |                                       |    forwarding policy can be added to  |
   |                                       |                                       |    an HTTP or HTTPS listener.         |
   |                                       |                                       |                                       |
   |                                       |                                       | -  If **action** is set to            |
   |                                       |                                       |    **REDIRECT_TO_LISTENER**, the      |
   |                                       |                                       |    forwarding policy can be added to  |
   |                                       |                                       |    an HTTP listener.                  |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | name                                  | String                                | Specifies the forwarding policy name. |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **255**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | position                              | Integer                               | Specifies the forwarding policy       |
   |                                       |                                       | priority. This parameter cannot be    |
   |                                       |                                       | updated.                              |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **100**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | project_id                            | String                                | Specifies the project ID of the       |
   |                                       |                                       | forwarding policy.                    |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | provisioning_status                   | String                                | Specifies the provisioning status of  |
   |                                       |                                       | the forwarding policy.                |
   |                                       |                                       |                                       |
   |                                       |                                       | The value can only be **ACTIVE**.     |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **ACTIVE**                   |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | redirect_listener_id                  | String                                | Specifies the ID of the listener that |
   |                                       |                                       | requests are redirected to.           |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is valid and mandatory |
   |                                       |                                       | only when **action** is set to        |
   |                                       |                                       | **REDIRECT_TO_LISTENER**.             |
   |                                       |                                       |                                       |
   |                                       |                                       | Only HTTPS listeners are supported,   |
   |                                       |                                       | and the listener cannot be any        |
   |                                       |                                       | listener added to other load          |
   |                                       |                                       | balancers.                            |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | redirect_pool_id                      | String                                | Specifies the ID of the backend       |
   |                                       |                                       | server group that requests are        |
   |                                       |                                       | forwarded to.                         |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is valid and mandatory |
   |                                       |                                       | only when **action** is set to        |
   |                                       |                                       | **REDIRECT_TO_POOL**.                 |
   |                                       |                                       |                                       |
   |                                       |                                       | The specified backend server group    |
   |                                       |                                       | cannot be the default one associated  |
   |                                       |                                       | with the listener, or any backend     |
   |                                       |                                       | server group associated with the      |
   |                                       |                                       | forwarding policies of other          |
   |                                       |                                       | listeners.                            |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter cannot be specified    |
   |                                       |                                       | when **action** is set to             |
   |                                       |                                       | **REDIRECT_TO_LISTENER**.             |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | redirect_url                          | String                                | Specifies the URL to which requests   |
   |                                       |                                       | are forwarded.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Format:                               |
   |                                       |                                       | *protocol://host:port/path?query*     |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | rules                                 | Array of                              | Lists the forwarding rules in the     |
   |                                       | `RuleRef <                            | forwarding policy.                    |
   |                                       | #ListL7Policies__response_RuleRef>`__ |                                       |
   |                                       | objects                               |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | redirect_url_config                   | `RedirectUrlConfig <#ListL7Pol        | Specifies the URL to which requests   |
   |                                       | icies__response_RedirectUrlConfig>`__ | are forwarded.                        |
   |                                       | object                                |                                       |
   |                                       |                                       | For shared load balancers, this       |
   |                                       |                                       | parameter is not supported. If it is  |
   |                                       |                                       | passed, an error will be returned.    |
   |                                       |                                       |                                       |
   |                                       |                                       | For dedicated load balancers, this    |
   |                                       |                                       | parameter will take effect only when  |
   |                                       |                                       | advanced forwarding is enabled        |
   |                                       |                                       | (**enhance_l7policy_enable** is set   |
   |                                       |                                       | to **true**). If it is passed when    |
   |                                       |                                       | **enhance_l7policy_enable** is set to |
   |                                       |                                       | **false**, an error will be returned. |
   |                                       |                                       |                                       |
   |                                       |                                       | Format:                               |
   |                                       |                                       | *protocol://host:port/path?query*     |
   |                                       |                                       |                                       |
   |                                       |                                       | At least one of the four parameters   |
   |                                       |                                       | (**protocol**, **host**, **port**,    |
   |                                       |                                       | and **path**) must be passed, or      |
   |                                       |                                       | their values cannot be set to         |
   |                                       |                                       | **${xxx}** at the same time.          |
   |                                       |                                       | (**${xxx}** indicates that the value  |
   |                                       |                                       | in the request will be inherited. For |
   |                                       |                                       | example, **${host}** indicates the    |
   |                                       |                                       | host in the URL to be redirected.)    |
   |                                       |                                       |                                       |
   |                                       |                                       | The values of **protocol** and        |
   |                                       |                                       | **port** cannot be the same as those  |
   |                                       |                                       | of the associated listener, and       |
   |                                       |                                       | either **host** or **path** must be   |
   |                                       |                                       | passed or their values cannot be      |
   |                                       |                                       | **${xxx}** at the same time.          |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | fixed_response_config                 | `FixtedResponseConfig <#ListL7Polici  | Specifies the configuration of the    |
   |                                       | es__response_FixtedResponseConfig>`__ | page that will be returned. This      |
   |                                       | object                                | parameter will take effect when       |
   |                                       |                                       | **enhance_l7policy_enable** is set to |
   |                                       |                                       | **true**. If this parameter is passed |
   |                                       |                                       | and **enhance_l7policy_enable** is    |
   |                                       |                                       | set to **false**, an error will be    |
   |                                       |                                       | returned. For shared load balancers,  |
   |                                       |                                       | this parameter is not supported. If   |
   |                                       |                                       | it is passed, an error will be        |
   |                                       |                                       | returned.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | priority                              | Integer                               | Specifies the forwarding policy       |
   |                                       |                                       | priority. This parameter is available |
   |                                       |                                       | only for dedicated load balancers and |
   |                                       |                                       | will take effect when                 |
   |                                       |                                       | **enhance_l7policy_enable** is set to |
   |                                       |                                       | **true**.                             |
   |                                       |                                       |                                       |
   |                                       |                                       | A smaller value indicates a higher    |
   |                                       |                                       | priority. The value must be unique    |
   |                                       |                                       | for each forwarding policy of the     |
   |                                       |                                       | same listener.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | If **action** is set to               |
   |                                       |                                       | **REDIRECT_TO_LISTENER**, the value   |
   |                                       |                                       | can only be **0**, indicating that    |
   |                                       |                                       | **REDIRECT_TO_LISTENER** has the      |
   |                                       |                                       | highest priority.                     |
   |                                       |                                       |                                       |
   |                                       |                                       | -  If **enhance_l7policy_enable** is  |
   |                                       |                                       |    set to **false**, forwarding       |
   |                                       |                                       |    policies are automatically         |
   |                                       |                                       |    prioritized based on the original  |
   |                                       |                                       |    sorting logic. Forwarding policy   |
   |                                       |                                       |    priorities are independent of each |
   |                                       |                                       |    other regardless of domain names.  |
   |                                       |                                       |    If forwarding policies use the     |
   |                                       |                                       |    same domain name, their priorities |
   |                                       |                                       |    follow the order of exact match    |
   |                                       |                                       |    (**EQUAL_TO**), prefix match       |
   |                                       |                                       |    (**STARTS_WITH**), and regular     |
   |                                       |                                       |    expression match (**REGEX**). If   |
   |                                       |                                       |    prefix match is used for matching, |
   |                                       |                                       |    the longer the path, the higher    |
   |                                       |                                       |    the priority. If a forwarding      |
   |                                       |                                       |    policy contains only a domain name |
   |                                       |                                       |    without a path specified, the path |
   |                                       |                                       |    is **/**, and prefix match is used |
   |                                       |                                       |    by default.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | -  If **enhance_l7policy_enable** is  |
   |                                       |                                       |    set to **true** and this parameter |
   |                                       |                                       |    is not passed, the priority will   |
   |                                       |                                       |    set to a sum of 1 and the highest  |
   |                                       |                                       |    priority of existing forwarding    |
   |                                       |                                       |    policy in the same listener by     |
   |                                       |                                       |    default. There will be two cases:  |
   |                                       |                                       |    a) If the highest priority of      |
   |                                       |                                       |    existing forwarding policies is    |
   |                                       |                                       |    the maximum (10,000), the          |
   |                                       |                                       |    forwarding policy will fail to     |
   |                                       |                                       |    create because the final priority  |
   |                                       |                                       |    for creating the forwarding policy |
   |                                       |                                       |    is the sum of 1 and 10,000, which  |
   |                                       |                                       |    exceeds the maximum. In this case, |
   |                                       |                                       |    please specify a value or adjust   |
   |                                       |                                       |    the priorities of existing         |
   |                                       |                                       |    forwarding policies. b) If no      |
   |                                       |                                       |    forwarding policies exist, the     |
   |                                       |                                       |    highest priority of existing       |
   |                                       |                                       |    forwarding policies will set to 1  |
   |                                       |                                       |    by default.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | This parameter is unsupported. Please |
   |                                       |                                       | do not use it.                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **0**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **10000**                    |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 7** RuleRef

   ========= ====== =================================
   Parameter Type   Description
   ========= ====== =================================
   id        String Specifies the forwarding rule ID.
   ========= ====== =================================

.. table:: **Table 8** RedirectUrlConfig

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | protocol                              | String                                | Specifies the protocol for            |
   |                                       |                                       | redirection. The default value is     |
   |                                       |                                       | **${protocol}**, indicating that the  |
   |                                       |                                       | protocol of the request will be used. |
   |                                       |                                       |                                       |
   |                                       |                                       | Value options:                        |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **HTTP**                           |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **HTTPS**                          |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **${protocol}**                    |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **36**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | host                                  | String                                | Specifies the host name that requests |
   |                                       |                                       | are redirected to. The value can      |
   |                                       |                                       | contain only letters, digits, hyphens |
   |                                       |                                       | (-), and periods (.) and must start   |
   |                                       |                                       | with a letter or digit. The default   |
   |                                       |                                       | value is **${host}**, indicating that |
   |                                       |                                       | the host of the request will be used. |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **${host}**                  |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **128**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | port                                  | String                                | Specifies the port that requests are  |
   |                                       |                                       | redirected to. The default value is   |
   |                                       |                                       | **${port}**, indicating that the port |
   |                                       |                                       | of the request will be used.          |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **${port}**                  |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **16**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | path                                  | String                                | Specifies the path that requests are  |
   |                                       |                                       | redirected to. The default value is   |
   |                                       |                                       | **${path}**, indicating that the path |
   |                                       |                                       | of the request will be used. The      |
   |                                       |                                       | value can contain only letters,       |
   |                                       |                                       | digits, and special characters        |
   |                                       |                                       | \_-';@^- %#&$.*+?,=!:|/()[]{} and     |
   |                                       |                                       | must start with a slash (/).          |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **${path}**                  |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **128**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | query                                 | String                                | Specifies the query string set in the |
   |                                       |                                       | URL for redirection. The default      |
   |                                       |                                       | value is **${query}**, indicating     |
   |                                       |                                       | that the query string of the request  |
   |                                       |                                       | will be used.                         |
   |                                       |                                       |                                       |
   |                                       |                                       | For example, in the URL               |
   |                                       |                                       | **https://www.                        |
   |                                       |                                       | xxx.com:8080/elb?type=loadbalancer**, |
   |                                       |                                       | **${query}** indicates                |
   |                                       |                                       | **type=loadbalancer**. If this        |
   |                                       |                                       | parameter is set to                   |
   |                                       |                                       | **${query}&name=my_name**, the URL    |
   |                                       |                                       | will be redirected to                 |
   |                                       |                                       | **https://www.xxx.com:8080/           |
   |                                       |                                       | elb?type=loadbalancer&name=my_name**. |
   |                                       |                                       |                                       |
   |                                       |                                       | The value is case-sensitive and can   |
   |                                       |                                       | contain only letters, digits, and     |
   |                                       |                                       | special characters                    |
   |                                       |                                       | !$&'()*+,-./:;=?@^_\`                 |
   |                                       |                                       |                                       |
   |                                       |                                       | Default: **${query}**                 |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **0**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **128**                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | status_code                           | String                                | Specifies the status code returned    |
   |                                       |                                       | after the requests are redirected.    |
   |                                       |                                       |                                       |
   |                                       |                                       | Value options:                        |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **301**                            |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **302**                            |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **303**                            |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **307**                            |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **308**                            |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **16**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 9** FixtedResponseConfig

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Parameter                             | Type                                  | Description                           |
   +=======================================+=======================================+=======================================+
   | status_code                           | String                                | Specifies the HTTP status code        |
   |                                       |                                       | configured in the forwarding policy.  |
   |                                       |                                       | The value can be any integer in the   |
   |                                       |                                       | range of 200–299, 400–499, or         |
   |                                       |                                       | 500–599.                              |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **1**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **16**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | content_type                          | String                                | Specifies the format of the response  |
   |                                       |                                       | body.                                 |
   |                                       |                                       |                                       |
   |                                       |                                       | Value options:                        |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **text/plain**                     |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **text/css**                       |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **text/html**                      |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **application/javascript**         |
   |                                       |                                       |                                       |
   |                                       |                                       | -  **application/json**               |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **0**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **32**                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | message_body                          | String                                | Specifies the content of the response |
   |                                       |                                       | body.                                 |
   |                                       |                                       |                                       |
   |                                       |                                       | Minimum: **0**                        |
   |                                       |                                       |                                       |
   |                                       |                                       | Maximum: **1024**                     |
   +---------------------------------------+---------------------------------------+---------------------------------------+

Example Requests
^^^^^^^^^^^^^^^^

.. code:: screen

   GET

   https://{elb_endpoint}/v3/99a3fff0d03c428eac3678da6a7d0f24/elb/l7policies?display_all_rules=true

Example Responses
^^^^^^^^^^^^^^^^^

**Status code: 200**

Successful request.

.. code:: screen

   {
     "request_id" : "d3c67339-be91-4813-bb24-85728a5d326a",
     "l7policies" : [ {
       "redirect_pool_id" : "3b34340d-59e8-4c70-9ef5-b41b12023dc9",
       "description" : "",
       "admin_state_up" : true,
       "rules" : [ {
         "id" : "1e5f17df-feec-427e-a162-8e4e05e91085"
       } ],
       "project_id" : "99a3fff0d03c428eac3678da6a7d0f24",
       "listener_id" : "e2220d2a-3faf-44f3-8cd6-0c42952bd0ab",
       "action" : "REDIRECT_TO_POOL",
       "position" : 100,
       "provisioning_status" : "ACTIVE",
       "id" : "0d7bf316-2e03-411f-bf29-c403c04e52bf",
       "name" : "elbv3"
     }, {
       "redirect_pool_id" : "3b34340d-59e8-4c70-9ef5-b41b12023dc9",
       "description" : "",
       "admin_state_up" : true,
       "rules" : [ {
         "id" : "0f5e8c34-09d1-4588-8459-f9b9add0be05"
       } ],
       "project_id" : "99a3fff0d03c428eac3678da6a7d0f24",
       "listener_id" : "e2220d2a-3faf-44f3-8cd6-0c42952bd0ab",
       "action" : "REDIRECT_TO_POOL",
       "position" : 100,
       "provisioning_status" : "ERROR",
       "id" : "2587d8b1-9e8d-459c-9081-7bccaa075d2b",
       "name" : "elbv3"
     } ],
     "page_info" : {
       "next_marker" : "2587d8b1-9e8d-459c-9081-7bccaa075d2b",
       "previous_marker" : "0d7bf316-2e03-411f-bf29-c403c04e52bf",
       "current_count" : 2
     }
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

**Parent topic:** `Forwarding Policy <topic_300000009.html>`__
