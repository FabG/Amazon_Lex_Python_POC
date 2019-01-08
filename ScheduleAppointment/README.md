### Lex POC for Making appointment

#### Sources:
https://docs.aws.amazon.com/lex/latest/dg/ex1-sch-appt.html


This code sample demonstrates an implementation of the Lex Code Hook Interface
in order to serve a bot which manages dentist appointments.
Bot, Intent, and Slot models which are compatible with this sample can be found in the Lex Console
as part of the 'MakeAppointment' template.

Lambda is created using the blue print: lex-make-appointment-python
 - runtime: Python 2.8
 - Handler: lambda_function.lambda_handler

CloudFormation Stack
Leveraging Template url:
```
https://s3.amazonaws.com/aws-bigdata-blog/artifacts/aws-lex-web-ui/artifacts/templates/master.yaml
```

Website exposed at:
```
https://lex-web-ui-codebuilddeploy-17lkkemhb-webappbucket-1dfb1pkcapycr.s3.amazonaws.com/parent.html
```

To test the Lambda, use the "Lambda_Test_Event.json" Lambda_Test_Event
More info on the Lambda used as code hooks for Lex:
https://docs.aws.amazon.com/lex/latest/dg/using-lambda.html


Input Event Format:
```
{
  "currentIntent": {
    "name": "intent-name",
    "slots": {
      "slot name": "value",
      "slot name": "value"
    },
    "slotDetails": {
      "slot name": {
        "resolutions" : [
          { "value": "resolved value" },
          { "value": "resolved value" }
        ],
        "originalValue": "original text"
      },
      "slot name": {
        "resolutions" : [
          { "value": "resolved value" },
          { "value": "resolved value" }
        ],
        "originalValue": "original text"
      }
    },
    "confirmationStatus": "None, Confirmed, or Denied (intent confirmation, if configured)"
  },
  "bot": {
    "name": "bot name",
    "alias": "bot alias",
    "version": "bot version"
  },
  "userId": "User ID specified in the POST request to Amazon Lex.",
  "inputTranscript": "Text used to process the request",
  "invocationSource": "FulfillmentCodeHook or DialogCodeHook",
  "outputDialogMode": "Text or Voice, based on ContentType request header in runtime API request",
  "messageVersion": "1.0",
  "sessionAttributes": {
     "key": "value",
     "key": "value"
  },
  "requestAttributes": {
     "key": "value",
     "key": "value"
  }
}
```

Response format
```
{
    "sessionAttributes": {
    "key1": "value1",
    "key2": "value2"
    ...
  },
  "dialogAction": {
    "type": "ElicitIntent, ElicitSlot, ConfirmIntent, Delegate, or Close",
    Full structure based on the type field. See below for details.
  }
}
```

