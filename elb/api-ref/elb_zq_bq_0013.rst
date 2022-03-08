Status Codes
============

.. table:: **Table 1** Normal codes

   +---------------------------------------+---------------------------------------+---------------------------------------+
   | Status Code                           | Message                               | Description                           |
   +=======================================+=======================================+=======================================+
   | 200                                   | OK                                    | Specifies the normal response code    |
   |                                       |                                       | for the GET operation.                |
   |                                       |                                       |                                       |
   |                                       |                                       | This code is returned when a response |
   |                                       |                                       | body is returned for the POST         |
   |                                       |                                       | operation.                            |
   +---------------------------------------+---------------------------------------+---------------------------------------+
   | 204                                   | No Content                            | Specifies the normal response code    |
   |                                       |                                       | for the DELETE operation.             |
   |                                       |                                       |                                       |
   |                                       |                                       | This code is returned when no         |
   |                                       |                                       | response body is returned for the     |
   |                                       |                                       | POST operation.                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+

.. table:: **Table 2** Error codes

   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | Status Code | Error Code | Description                | Error Message              | Measure                    |
   +=============+============+============================+============================+============================+
   | 400         | VPC.1801   | The ID is incorrect.       | resource id is             | Use a correct resource ID. |
   |             |            |                            | invalid/Getting id is      |                            |
   |             |            |                            | invalid.                   |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | An action error occurs.    | action is invalid.         | Ensure that the value of   |
   |             |            |                            |                            | **action** is **create**   |
   |             |            |                            |                            | or **delete**.             |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | The key length is invalid. | Tag length is invalid. The | Input a valid key.         |
   |             |            |                            | key length must be in      |                            |
   |             |            |                            | range [1,36] and value in  |                            |
   |             |            |                            | range [0,43]               |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.0007   | The project ID is          | urlTenantId is not equal   | Check the project ID.      |
   |             |            | incorrect.                 | token TenantId.            |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 401         | VPC.0008   | The token in the request   | Invalid token in the       | Check whether the token is |
   |             |            | is invalid or the request  | header./Authorization      | valid.                     |
   |             |            | does not contain the       | information is wrong.      |                            |
   |             |            | token.                     |                            |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | The value length is        | Tag length is invalid. The | Input a valid value.       |
   |             |            | invalid.                   | key length must be in      |                            |
   |             |            |                            | range [1,36] and value in  |                            |
   |             |            |                            | range [0,43]               |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | The key or value contains  | InvalidInput/Tag value xxx | Check the validity of the  |
   |             |            | invalid characters.        | is invalid.                | key or value.              |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | The key or value is left   | Tag xxx can not be null.   | Check whether the key or   |
   |             |            | blank.                     |                            | value is left blank.       |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | The tag is null.           | Tag can not be null.       | Check whether the tag is   |
   |             |            |                            |                            | null.                      |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | A resource type error      | Resource xxx is invalid.   | Ensure that the value of   |
   |             |            | occurs.                    |                            | **resource_type** is       |
   |             |            |                            |                            | **loadbalancers** or       |
   |             |            |                            |                            | **listeners**.             |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | The total number of tags   | number of tags exceeds max | Reduce the number of tags. |
   |             |            | added at a time exceeds    | unm of 10.                 |                            |
   |             |            | 10.                        |                            |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1814   | The total number of        | Invalid input for          | Reduce the number of tags. |
   |             |            | existing tags and newly    | operation: resource_id:    |                            |
   |             |            | added tags exceeds 10.     | XXXX, number of tags       |                            |
   |             |            |                            | exceed max num of 10.      |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1814   | The key values of newly    | Invalid input for          | Change the tag values.     |
   |             |            | added tags are duplicate.  | operation: tags key is     |                            |
   |             |            |                            | duplicated.                |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1814   | The resource ID does not   | Resource XXX XXX could not | Check whether the resource |
   |             |            | exist.                     | be found.                  | is available.              |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1814   | The specified key to be    | The resource could not be  | Enter a correct key and    |
   |             |            | deleted does not exist, or | found.                     | send the request again.    |
   |             |            | the key is an empty        |                            |                            |
   |             |            | string.                    |                            |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1814   | More than 10 tags are      | Invalid input for          | Each resource supports up  |
   |             |            | added to a specified       | operation:resource_id:xxx, | to 10 tags.                |
   |             |            | resource.                  | number of tags exceeds max |                            |
   |             |            |                            | num of 10.                 |                            |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 400         | VPC.1801   | Tags are duplicate.        | Tag key is repeated.       | Delete duplicate tags and  |
   |             |            |                            |                            | resend the request.        |
   +-------------+------------+----------------------------+----------------------------+----------------------------+
   | 500         | -          | The request format is      | Internal Server Error.     | Use the correct request    |
   |             |            | incorrect.                 |                            | body format.               |
   +-------------+------------+----------------------------+----------------------------+----------------------------+

**Parent topic:** `Tag <elb_zq_bq_0000.html>`__
