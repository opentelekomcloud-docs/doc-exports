Error Codes
===========

The following error code descriptions are only suitable for classic load balancers.

Overview
^^^^^^^^

If an error occurs when using an API, an error response will be returned, which contains the error code and a piece of message, as shown in the following example. The following table lists error codes and their descriptions.

Example of Returned Error Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: screen

   { 
       "error": 
       { 
       "message": "listener exist, the port repeat", 
       "code": "ELB.6101" 
       } 
   }

.. _error-codes-1:

Error Codes
^^^^^^^^^^^

.. table:: **Table 1** Error codes

   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | Status Code           | Error Code            | Message               | Description           | Solution              |
   +=======================+=======================+=======================+=======================+=======================+
   | 400                   | ELB.0002              | Api request is null.  | The request is empty. | Change the parameter  |
   |                       |                       |                       |                       | settings.             |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.0004              | Api response is null  | The response is       | Ensure that the       |
   |                       |                       | or invaild.           | empty.                | backend server is     |
   |                       |                       |                       |                       | healthy.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.0230              | Tenant_id is empty.   | The project ID is     | Correct the project   |
   |                       |                       |                       | left blank.           | ID.                   |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1000              | The loadbalancer URL  | The URL length        | Correct the URL.      |
   |                       |                       | is too long.          | exceeds the limit.    |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1010              | Query elb quota       | Failed to query the   | Contact customer      |
   |                       |                       | error.                | quota.                | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1020              | Lb ID is not correct. | Incorrect load        | Change the parameter  |
   |                       |                       |                       | balancer ID.          | settings.             |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1001              | Request parameters    | Parameter **type**,   | Change the parameter  |
   |                       |                       | error, private_key or | **name**, or          | settings.             |
   |                       |                       | certificate is nil or | **admin_status_up**   |                       |
   |                       |                       | empty.                | is left blank.        |                       |
   |                       |                       |                       |                       |                       |
   |                       |                       | Request parameters    |                       |                       |
   |                       |                       | error, lb type, name, |                       |                       |
   |                       |                       | admin_state_up one of |                       |                       |
   |                       |                       | them is empty.        |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1001              | Request parameter is  | The length of the     | Change the listener   |
   |                       |                       | not valid.            | load balancer name    | name.                 |
   |                       |                       |                       | exceeds the limit.    |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1021              | Request parameters    | Invalid load balancer | Change the parameter  |
   |                       |                       | error, name invalid.  | name.                 | settings.             |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1031              | Request parameters    | The length of the     | Change the            |
   |                       |                       | error, lb len         | load balancer         | description.          |
   |                       |                       | description too long. | description exceeds   |                       |
   |                       |                       |                       | the limit.            |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1041              | Request parameters    | Invalid load balancer | Change the parameter  |
   |                       |                       | error, lb type is not | type.                 | settings.             |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1051              | Request parameters    | Invalid load balancer | Change the parameter  |
   |                       |                       | error, lb bandwidth   | bandwidth.            | settings.             |
   |                       |                       | is not valid.         |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 4000                  | ELB.1061              | Request parameters    | The floating IP       | Change the parameter  |
   |                       |                       | error, lb vip_address | address or subnet ID  | settings.             |
   |                       |                       | and vip_subnet_id are | is left blank.        |                       |
   |                       |                       | nil.                  |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1071              | Request parameters    | Invalid floating IP   | Change the parameter  |
   |                       |                       | error, lb vip_address | address.              | settings.             |
   |                       |                       | is not valid.         |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1081              | Request parameters    | The VPC ID is left    | Change the parameter  |
   |                       |                       | error, lb vpc_id is   | blank.                | settings.             |
   |                       |                       | empty.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 403                   | ELB.1091              | Lb number larger than | The number of load    | Request a higher      |
   |                       |                       | quota.                | balancers exceeds the | quota or delete load  |
   |                       |                       |                       | quota.                | balancers that are no |
   |                       |                       |                       |                       | longer needed.        |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1101              | Vip address is exist. | The floating IP       | Enter a valid         |
   |                       |                       |                       | address exists.       | floating IP address.  |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 404                   | ELB.1002              | Find lb failed.       | The load balancer     | Change the load       |
   |                       |                       |                       | does not exist.       | balancer ID.          |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1008              | There is at least one | Failed to delete the  | Change the parameter  |
   |                       |                       | member under the lb.  | load balancer.        | settings.             |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1018              | There is at least one | The load balancer has | Change the parameter  |
   |                       |                       | member under the lb.  | backend ECSs added.   | settings.             |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1005              | Update request        | Failed to modify the  | Check the parameters. |
   |                       |                       | paramters error.      | load balancer.        |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1015              | Lb can not be         | The load balancer     | Check the parameters. |
   |                       |                       | updated.              | cannot be modified.   |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1025              | Udpate request        | The length of the     | Change the load       |
   |                       |                       | parameters error,     | load balancer name    | balancer name.        |
   |                       |                       | name is too long.     | exceeds the limit.    |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1035              | Update request        | Invalid load balancer | Change the load       |
   |                       |                       | parameters error,     | name.                 | balancer name.        |
   |                       |                       | name is not valid.    |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1045              | Update request        | The length of the     | Change the            |
   |                       |                       | parameters error,     | load balancer         | description.          |
   |                       |                       | description too long. | description exceeds   |                       |
   |                       |                       |                       | the limit.            |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1003              | Lb not exist.         | The load balancer     | Check the load        |
   |                       |                       |                       | does not exist.       | balancer ID.          |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1004              | Query condition is    | Invalid query         | Change the query      |
   |                       |                       | not valid.            | condition.            | condition.            |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6000              | Listener ID length is | The length of the     | Change the listener   |
   |                       |                       | not correct.          | listener ID exceeds   | ID.                   |
   |                       |                       |                       | the limit.            |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6010              | Listener ID content   | Invalid listener ID.  | Change the listener   |
   |                       |                       | is not correct.       |                       | ID.                   |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6030              | Listener is not       | The listener does not | Check the listener    |
   |                       |                       | associated with       | belong to any load    | ID.                   |
   |                       |                       | loadbalancer id.      | balancer.             |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6040              | The loadbalaner that  | The load balancer to  | Check the load        |
   |                       |                       | the listener belongs  | which the listener is | balancer ID.          |
   |                       |                       | to is not exist.      | added does not exist. |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6020              | Listener url is not   | Incorrect listener    | Correct the URL.      |
   |                       |                       | correct.              | URL.                  |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6001              | Request parameters    | A mandatory parameter | Specify the mandatory |
   |                       |                       | error, "..nilKey.."   | is left blank.        | parameters.           |
   |                       |                       | is nil.               |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6011              | Request parameters    | The length of the     | Change the listener   |
   |                       |                       | error, listener name  | listener name exceeds | name.                 |
   |                       |                       | too long.             | the limit.            |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6021              | Request parameters    | Invalid listener      | Change the listener   |
   |                       |                       | error, listener name  | name.                 | name.                 |
   |                       |                       | is not valid.         |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6031              | Request parameters    | The length of the     | Change the            |
   |                       |                       | error, listener len   | listener description  | description.          |
   |                       |                       | description too long. | exceeds the limit.    |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6041              | Request parameters    | Invalid port number.  | Change the port       |
   |                       |                       | error, listener port  |                       | number.               |
   |                       |                       | is not in 1 ~ 65535.  |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6051              | Request parameters    | Invalid load          | Change the load       |
   |                       |                       | error, listener lb    | balancing algorithm.  | balancing algorithm.  |
   |                       |                       | algorithm is not      |                       |                       |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6061              | Request parameters    | Invalid protocol used | Change the protocol.  |
   |                       |                       | error, listener       | by the listener.      |                       |
   |                       |                       | protocol is not       |                       |                       |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6071              | Request parameters    | Invalid backend ECS   | Change the protocol.  |
   |                       |                       | error, listener       | protocol.             |                       |
   |                       |                       | backend protocol is   |                       |                       |
   |                       |                       | not valid.            |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6081              | Request parameters    | Invalid sticky        | Check the load        |
   |                       |                       | error, listener       | session type.         | balancer ID.          |
   |                       |                       | sticky_session_type   |                       |                       |
   |                       |                       | is not valid.         |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 403                   | ELB.6091              | Request lb has more   | The number of         | No more listeners can |
   |                       |                       | than user listener    | listeners reaches the | be added.             |
   |                       |                       | quota.                | limit.                |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6101              | Listener port is      | The port exists.      | Use another port      |
   |                       |                       | repeated.             |                       | number.               |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 503                   | ELB.6002              | Delete listener       | The listener does not | Check the listener    |
   |                       |                       | failed, listener does | exist.                | ID.                   |
   |                       |                       | not exist.            |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6015              | This listener         | The property cannot   | Select a property     |
   |                       |                       | property cannot be    | be modified.          | that can be modified. |
   |                       |                       | updated               |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6025              | Udpate request        | The length of the     | Change the listener   |
   |                       |                       | parameters error,     | listener name exceeds | name.                 |
   |                       |                       | listener len name too | the limit.            |                       |
   |                       |                       | long.                 |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6035              | Udpate request        | Invalid listener      | Change the listener   |
   |                       |                       | parameters error,     | name.                 | name.                 |
   |                       |                       | listener name is not  |                       |                       |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6045              | Update request        | The length of the     | Change the            |
   |                       |                       | parameters error,     | listener description  | description.          |
   |                       |                       | listener len          | exceeds the limit.    |                       |
   |                       |                       | description too long. |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6003              | Listener query        | Invalid query         | Change the query      |
   |                       |                       | condition is not      | condition.            | condition.            |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2000              | Member url is not     | Incorrect backend ECS | Correct the URL.      |
   |                       |                       | correct.              | URL.                  |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2003              | Query member failed.  | Failed to query the   | Contact customer      |
   |                       |                       |                       | backend ECS.          | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2005              | Update member failed. | Failed to update the  | Contact customer      |
   |                       |                       |                       | backend ECS.          | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2010              | Member listener ID    | The length of the     | Change the listener   |
   |                       |                       | length is not         | listener ID exceeds   | ID.                   |
   |                       |                       | correct.              | the limit.            |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2020              | Member listener ID    | Incorrect listener    | Change the listener   |
   |                       |                       | content is not        | ID.                   | ID.                   |
   |                       |                       | correct.              |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 403                   | ELB.2001              | Create member failed, | Failed to add the ECS | Check the maximum     |
   |                       |                       | the total amount of   | because the number of | number of backend     |
   |                       |                       | members exceeds the   | backend ECSs reaches  | servers that can be   |
   |                       |                       | system setting.       | the limit.            | added.                |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2011              | Add member listener   | The listener does not | Ensure that the       |
   |                       |                       | is not exist.         | exist.                | listener exists.      |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2021              | Request parameters    | Invalid address.      | Check the IP address. |
   |                       |                       | error, member address |                       |                       |
   |                       |                       | is null.              |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2002              | Delete member input   | Incorrect parameters. | Change the parameter  |
   |                       |                       | param error.          |                       | settings.             |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.2012              | This member is not    | The backend ECS does  | Ensure that the       |
   |                       |                       | exist.                | not exist.            | backend server        |
   |                       |                       |                       |                       | exists.               |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7000              | Listener_id must not  | The listener ID is    | Change the listener   |
   |                       |                       | be null.              | left blank.           | ID and deliver the    |
   |                       |                       |                       |                       | request again.        |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7010              | Healthcheck listener  | The listener with     | Change the listener   |
   |                       |                       | is not exist.         | which the health      | ID and deliver the    |
   |                       |                       |                       | check is associated   | request again.        |
   |                       |                       |                       | does not exist.       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7020              | This healthcheck is   | The health check does | Change the health     |
   |                       |                       | not exist.            | not exist.            | check ID and deliver  |
   |                       |                       |                       |                       | the request again.    |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7001              | Healthcheck_interval  | Invalid health check  | Change the interval.  |
   |                       |                       | is illegal.           | interval.             |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7002              | Healthcheck delete    | Invalid query         | Change the query      |
   |                       |                       | condition is not      | condition.            | condition.            |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7001              | Healthcheck update    | Invalid query         | Change the query      |
   |                       |                       | condition is not      | condition.            | condition.            |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7004              | Healthcheck query     | Invalid query         | Change the query      |
   |                       |                       | condition is not      | condition.            | condition.            |
   |                       |                       | valid.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.7014              | Healthcheck           | The health check does | Check the health      |
   |                       |                       | configuration not     | not exist.            | check ID.             |
   |                       |                       | exist.                |                       |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.8001              | Create a SG error.    | Failed to create the  | Contact customer      |
   |                       |                       |                       | security group.       | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.8101              | Create VPC error.     | Failed to create the  | Contact customer      |
   |                       |                       |                       | VPC.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.8102              | Delete VPC error.     | Failed to delete the  | Contact customer      |
   |                       |                       |                       | VPC.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.8103              | Query VPC error.      | Failed to query the   | Contact customer      |
   |                       |                       |                       | VPC.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.8201              | Create subnet error.  | Failed to create the  | Contact customer      |
   |                       |                       |                       | subnet.               | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.8202              | Delete subnet error.  | Failed to delete the  | Contact customer      |
   |                       |                       |                       | subnet.               | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.8203              | Query subnet error.   | Failed to query the   | Contact customer      |
   |                       |                       |                       | subnet.               | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9001              | Interval ELB create   | Failed to add the     | Contact customer      |
   |                       |                       | VM error.             | ECS.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9002              | Internal ELB delete   | Failed to delete the  | Contact customer      |
   |                       |                       | VM error.             | ECS.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9003              | Internal ELB query VM | Failed to query ECS   | Contact customer      |
   |                       |                       | error.                | details.              | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9006              | Internal ELB update   | Failed to update the  | Contact customer      |
   |                       |                       | port fail.            | port configured on    | service.              |
   |                       |                       |                       | the ECS data plane.   |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9007              | Intenal ELB bind port | Failed to bind the    | Contact customer      |
   |                       |                       | fail.                 | port configured on    | service.              |
   |                       |                       |                       | the ECS data plane.   |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9061              | Internal ELB query    | Failed to query the   | Contact customer      |
   |                       |                       | topic fail.           | SMN topic.            | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9062              | Internal ELB create   | Failed to create the  | Contact customer      |
   |                       |                       | topic fail.           | SMN topic.            | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9063              | Internal ELB query    | Failed to query the   | Contact customer      |
   |                       |                       | subscription fail.    | SMN subscription.     | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9064              | Internal ELB create   | Failed to create the  | Contact customer      |
   |                       |                       | subscription fail.    | SMN subscription.     | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9023              | Internal ELB get      | Failed to query the   | Contact customer      |
   |                       |                       | image error.          | image.                | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9033              | Internal ELB get      | Failed to query ECS   | Contact customer      |
   |                       |                       | flavour error.        | specifications.       | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.9043              | Internal ELB get      | Failed to query the   | Contact customer      |
   |                       |                       | interface error.      | API bound to the ECS. | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1007              | Query internal ELB    | Failed to query       | Contact customer      |
   |                       |                       | error.                | details of the        | service.              |
   |                       |                       |                       | private network load  |                       |
   |                       |                       |                       | balancer.             |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1012              | Create tenant         | Failed to create the  | Contact customer      |
   |                       |                       | resource relation     | relationship between  | service.              |
   |                       |                       | error.                | resources and the     |                       |
   |                       |                       |                       | user.                 |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1013              | Update resource       | Failed to modify the  | Contact customer      |
   |                       |                       | tenant allocation     | quota of a resource   | service.              |
   |                       |                       | failed, cloud eye     | because the quota set |                       |
   |                       |                       | warning rule exceeds. | in the Cloud Eye      |                       |
   |                       |                       |                       | alarm rule is too     |                       |
   |                       |                       |                       | large.                |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1014              | Query resouce tenant  | Failed to query the   | Contact customer      |
   |                       |                       | relation failed.      | relationship between  | service.              |
   |                       |                       |                       | resources and the     |                       |
   |                       |                       |                       | user.                 |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1102              | Token invalid         | Invalid token.        | Contact customer      |
   |                       |                       |                       |                       | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1103              | Token invalid         | Invalid token.        | Contact customer      |
   |                       |                       |                       |                       | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1104              | Token invalid         | Invalid token.        | Contact customer      |
   |                       |                       |                       |                       | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1105              | Token invalid         | Invalid token.        | Contact customer      |
   |                       |                       |                       |                       | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1109              | Authentication        | Real-name             | Contact customer      |
   |                       |                       | failed.               | authentication        | service.              |
   |                       |                       |                       | failed.               |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.1201              | Get Token failed      | Failed to obtain the  | Contact customer      |
   |                       |                       |                       | token.                | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.3001              | Create floating IP    | Failed to assign the  | Contact customer      |
   |                       |                       | failed.               | floating IP address.  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.3002              | Delete floating IP    | Failed to release the | Contact customer      |
   |                       |                       | failed.               | floating IP address.  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.3003              | Query floating IP     | Failed to query the   | Contact customer      |
   |                       |                       | failed.               | floating IP address.  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.3004              | Query floating IP     | Failed to query       | Contact customer      |
   |                       |                       | list failed.          | floating IP           | service.              |
   |                       |                       |                       | addresses.            |                       |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.3005              | Update floating IP    | Failed to update the  | Contact customer      |
   |                       |                       | failed.               | floating IP address.  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.4001              | Create elastic IP     | Failed to assign the  | Contact customer      |
   |                       |                       | failed.               | EIP.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.4002              | Delete elastic IP     | Failed to release the | Contact customer      |
   |                       |                       | failed.               | EIP.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.4003              | Query elastic IP      | Failed to query the   | Contact customer      |
   |                       |                       | failed.               | EIP.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.4004              | Query elastic IP list | Failed to query EIPs. | Contact customer      |
   |                       |                       | failed.               |                       | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.4005              | Update elastic IP     | Failed to update the  | Contact customer      |
   |                       |                       | failed.               | EIP.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.5003              | Query bandwidth       | Failed to query the   | Contact customer      |
   |                       |                       | failed.               | bandwidth.            | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.5005              | Update bandwidth      | Failed to update the  | Contact customer      |
   |                       |                       | failed.               | bandwidth.            | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6004              | Query listeners list  | Failed to query       | Contact customer      |
   |                       |                       | failed.               | listeners.            | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
   | 400                   | ELB.6006              | Query ECS failed.     | Failed to query the   | Contact customer      |
   |                       |                       |                       | ECS.                  | service.              |
   +-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+

**Parent topic:** `Common Parameters <elb_gc_0000.html>`__
