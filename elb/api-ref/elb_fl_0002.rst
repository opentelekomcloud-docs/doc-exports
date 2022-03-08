ELB Metrics
===========

Introduction
^^^^^^^^^^^^

This section describes the metrics that can be monitored by Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of a monitored object and the generated alarms.

Namespace
^^^^^^^^^

SYS.ELB

Metrics
^^^^^^^

+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Metric                | Metric Name           | Description           | Value Range           | Remarks               |
+=======================+=======================+=======================+=======================+=======================+
| m1_cps                | Concurrent            | Total number of       | ≥ 0                   | Monitored object: an  |
|                       | Connections           | concurrent            |                       | elastic load          |
|                       |                       | connections processed |                       | balancer, elastic     |
|                       |                       | by the monitored      |                       | load balancer         |
|                       |                       | object per second     |                       | listener, or classic  |
|                       |                       |                       |                       | load balancer         |
|                       |                       | Unit: count           |                       |                       |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m2_act_conn           | Active Connections    | Total number of       | ≥ 0                   | Monitored object: an  |
|                       |                       | active connections    |                       | elastic load          |
|                       |                       | processed by the      |                       | balancer, elastic     |
|                       |                       | monitored object per  |                       | load balancer         |
|                       |                       | second                |                       | listener, or classic  |
|                       |                       |                       |                       | load balancer         |
|                       |                       | Unit: count           |                       |                       |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m3_inact_conn         | Inactive Connections  | Total number of       | ≥ 0                   | Monitored object: an  |
|                       |                       | inactive connections  |                       | elastic load          |
|                       |                       | processed by the      |                       | balancer, elastic     |
|                       |                       | monitored object per  |                       | load balancer         |
|                       |                       | second                |                       | listener, or classic  |
|                       |                       |                       |                       | load balancer         |
|                       |                       | Unit: count           |                       |                       |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m4_ncps               | New Connections       | Total number of new   | ≥ 0                   | Monitored object: an  |
|                       |                       | connections processed |                       | elastic load          |
|                       |                       | by the monitored      |                       | balancer, elastic     |
|                       |                       | object per second     |                       | load balancer         |
|                       |                       |                       |                       | listener, or classic  |
|                       |                       | Unit: count           |                       | load balancer         |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m5_in_pps             | Incoming Packets      | Incoming packets      | ≥ 0                   | Monitored object: an  |
|                       |                       | received by the       |                       | elastic load          |
|                       |                       | monitored object per  |                       | balancer, elastic     |
|                       |                       | second                |                       | load balancer         |
|                       |                       |                       |                       | listener, or classic  |
|                       |                       | Unit: count           |                       | load balancer         |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m6_out_pps            | Outgoing Packets      | Outgoing packets sent | ≥ 0                   | Monitored object: an  |
|                       |                       | from the monitored    |                       | elastic load          |
|                       |                       | object per second     |                       | balancer, elastic     |
|                       |                       |                       |                       | load balancer         |
|                       |                       | Unit: count           |                       | listener, or classic  |
|                       |                       |                       |                       | load balancer         |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m7_in_Bps             | Inbound Rate          | Incoming bytes        | ≥ 0                   | Monitored object: an  |
|                       |                       | received by the       |                       | elastic load          |
|                       |                       | monitored object per  |                       | balancer, elastic     |
|                       |                       | second                |                       | load balancer         |
|                       |                       |                       |                       | listener, or classic  |
|                       |                       | Unit: Byte/s          |                       | load balancer         |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m8_out_Bps            | Outbound Rate         | Outgoing bytes sent   | ≥ 0                   | Monitored object: an  |
|                       |                       | from the monitored    |                       | elastic load          |
|                       |                       | object per second     |                       | balancer, elastic     |
|                       |                       |                       |                       | load balancer         |
|                       |                       | Unit: Byte/s          |                       | listener, or classic  |
|                       |                       |                       |                       | load balancer         |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| m9_abnormal_servers   | Unhealthy Servers     | Number of backend     | ≥ 0                   | Monitored object: an  |
|                       |                       | servers considered    |                       | elastic load balancer |
|                       |                       | unhealthy             |                       | or classic load       |
|                       |                       |                       |                       | balancer              |
|                       |                       | Unit: count           |                       |                       |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| ma_normal_servers     | Healthy Servers       | Number of backend     | ≥ 0                   | Monitored object: an  |
|                       |                       | servers considered    |                       | elastic load balancer |
|                       |                       | healthy               |                       | or classic load       |
|                       |                       |                       |                       | balancer              |
|                       |                       | Unit: count           |                       |                       |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+

Dimensions
^^^^^^^^^^

================= =======================================
Key               Value
================= =======================================
lb_instance_id    ID of a classic load balancer
lbaas_instance_id ID of an elastic load balancer
lbaas_listener_id ID of an elastic load balancer listener
================= =======================================

**Parent topic:** `Appendix <elb_fl_0000.html>`__
