# security-group-handler

### What is the purpose of this "security-group-handler"
- The goal in creating this was to create a line of code to notify a manager if an EC2 instance was being launched/terminated/pending thorugh the approved security group.

### How does it does it work?
- To start, i created a lambda which is triggered by a cloudwatch event such as if the EC2 is being started or stoped/ anytime its put into a "pending" state. the Lambda will then check the security group that is triggering the initiation of the start of the EC2. if its an approved security group (verified by grabbing paremeter of approved security group from SSM) then the EC2 instance will start with no issue and nothing will happen. However, If it has been initiated via anything other tha the approved security group it will notify someone. This someone can be defined by whatever contact you want to use, for example: a managers phone number via text or a security developers email. this will overall ensure extra safety and proper steps for deployment or termination of a server like an EC2.
