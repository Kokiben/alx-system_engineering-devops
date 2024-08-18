Postmortem Report: Web Stack Outage
Issue Summary:
 Duration: August 10, 2024, from 14:00 to 16:30 GMT
 Impact: The website experienced significant slowdowns and intermittent downtime.
Approximately 70% of users were unable to access the website, while the remaining 30%
experienced page load times exceeding 30 seconds.
 Root Cause: A misconfigured load balancer led to uneven traffic distribution, causing
some servers to be overwhelmed while others remained underutilized.

Timeline:
 14:00 GMT: Issue detected through a spike in 500 Internal Server Errors and slow page
load times, flagged by automated monitoring.
 14:05 GMT: Incident escalated to the on-call DevOps engineer.
 14:10 GMT: Initial investigation focused on server health and resource usage; no
anomalies were found.
 14:20 GMT: Network team was looped in to check for any potential external issues such
as DDoS attacks.
 14:35 GMT: Network analysis ruled out external threats, and attention shifted to the load
balancer.
 14:45 GMT: Misleading assumption that the database was the bottleneck due to a recent
update; database checks showed no performance degradation.
 15:00 GMT: Load balancer logs were reviewed, revealing uneven traffic distribution.
 15:20 GMT: Configuration changes were made to the load balancer to properly distribute
traffic across all servers.
 15:45 GMT: Website performance began to stabilize.
 16:30 GMT: Full service restored, and the incident was marked as resolved.

Root Cause and Resolution:
The root cause of the outage was a misconfigured load balancer. During a recent deployment, a
configuration change was made to the load balancer settings to accommodate new application
servers. However, the new configuration inadvertently set a weighted distribution that favored a
single server, leading to one server being overwhelmed with the majority of the traffic. This
caused the server to hit its resource limits, resulting in slow responses and timeouts.
The resolution involved identifying the load balancer as the bottleneck and correcting the traffic
distribution settings. The configuration was modified to ensure an even distribution of incoming
traffic across all available servers. Once the correct settings were applied, server load
normalized, and the website performance returned to expected levels.

Corrective and Preventative Measures:
To prevent a similar incident from occurring in the future, the following actions will be taken:
1. Enhance Load Balancer Configuration Review Process:
o Implement a mandatory review process for any changes to load balancer settings,
including peer reviews and automated validation checks.

2. Improve Monitoring and Alerts:
o Set up more granular monitoring and alerting specifically for load balancer traffic
distribution and server load to detect any imbalances earlier.
o Implement alerts for unusual spikes in error rates and slow page load times that
are directly tied to load balancing.
3. Training and Documentation:
o Provide additional training for DevOps and engineering teams on load balancer
configuration and management.
o Update internal documentation to include best practices for load balancer setup
and common pitfalls.
4. Simulate Load Balancer Failures:
o Regularly simulate load balancer failures and traffic misconfigurations in a
controlled environment to ensure teams are prepared to diagnose and resolve
these issues quickly.

These measures will help ensure better preparedness and quicker resolution in the event of
similar issues in the future, minimizing impact on users.
