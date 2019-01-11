### Lex POC for Booking a Trip

#### Sources:
https://docs.aws.amazon.com/lex/latest/dg/ex-book-trip.html

This code sample demonstrates an implementation of the Lex Code Hook Interface
in order to serve a bot which manages trip booking.
Bot, Intent, and Slot models which are compatible with this sample can be found in the Lex Console
as part of the 'MakeAppointment' template.

Lambda is created using the blue print: lex-book-trip-python
 - runtime: Python 2.8
 - Handler: lambda_function.lambda_handler


CloudFormation Stack
Leveraging Template url:
```
```

Website exposed at:
```
```

To test the Lambda, use the "Lambda_Test_Event.json" Lambda_Test_Event
More info on the Lambda used as code hooks for Lex:
https://docs.aws.amazon.com/lex/latest/dg/using-lambda.html


Input Event Format:
```

```

Response format
```


```

