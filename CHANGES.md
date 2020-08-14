
---

- Created a Sensor to get hosts that have not responded
- Created a Trigger sending the server_name and last_checkin time for the server if the server has not responded
- Added a rule to match the trigger and link with the remediation workflow
- Created an orquesta workflow to remote run commands to troubleshoot satellite servers


NOTE:

- need to figure out way to not trigger virt-who hosts 
