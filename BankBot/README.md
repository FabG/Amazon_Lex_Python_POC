# Building A Bank Serverless Chatbot with AWS Lex

This bot will send notification by email and text based on an alert level: yellow, orange or red
And this bot can be interacted with in Slack after integration
My slack bot is available at:
https://fabcoworkspace.slack.com/messages/DF8R2KBU4/

This repository hosts all the example code used in this course.
It is based of 2 lambda for:
 - validation
 - fullfillment

Source: https://beta.linuxacademy.com/#/activities/take/be27d1d5-4185-4789-b4d4-71dccd2e6e45

<h2>requirements</h2>
This project makes use of:
 - Lambda (Python 3.6)
 - Lex
 - RDS MySQL
 - PyMysql


<h2> AWS access / configuration </h2>
In lambda network section select the VPC and all subnets. Set the security group to the security group the RDS was created with / set to.
Edit said security group inbound policies and set a policy with RDS port/access settings and set the source equal to its own Group Id. It is not sufficient that they are in the same group, if it doesn't accept connections from it's own group.
Ensure the lambda function execution role has AWSLambdaVPCAccessExecutionRole and AWSLambdaBasicExecutionRole policies attached.

If you want to test from your local, add your public IP to MyQL RDS Security group for the Inbound Traffic (with a /32 if it's a single IP)
Avoid opening RDS to the public.


<h2> Uploading to AWS Lambda </h2>
Because this project mkes use of a 3rd party library (pymysql), it needs to be uploaded to Lamba as a zip file
To do so, go to the main directory and run
```
zip -r lambdaBankBotRDS.zip `ls`
```

Then upload the lambdaBankBotRDS.zip to the Lambda function
And don't forget to change the Handler info:
 - from the default: "lambda_function.handler"
 - to "create_table_handler.handler"


<h2> Testing Lambda </h2>
You can use the content of Test_Lambda_Insert_Table_Event.json and update it as need be

<h3>Useful links:</h3>
https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
https://docs.aws.amazon.com/lambda/latest/dg/vpc-rds.html
https://blog.shikisoft.com/running-aws-lambda-in-vpc-accessing-rds
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html


https://www.youtube.com/watch?v=-CoL5oN1RzQ&vl=en
https://www.youtube.com/watch?v=cGYknt3xIvM