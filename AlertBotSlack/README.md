# Building A Serverless Chatbot with AWS Lex

This bot will send notification by email and text based on an alert level: yellow, orange or red
And this bot can be interacted with in Slack after integration
My slack bot is available at:
https://fabcoworkspace.slack.com/messages/DF8R2KBU4/

This repository hosts all the example code used in this course.
It is based of 2 lambda for:
 - validation
 - fullfillment

Source: https://beta.linuxacademy.com/#/activities/take/be27d1d5-4185-4789-b4d4-71dccd2e6e45


This project makes use of:
 - Lambda (Python 3.6)
 - Lex
 - Simple Email Service
 - Simple Notification Service


Don't forget to add both SES and SNS as part of the IAM Role that is used to create the lambda to be able to send email/text


