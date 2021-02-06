# Unit Test Practice

This is an area to practice unit-testing in times of high dependency.

## The Opportunity

With all the reuse possible today, a little code can achieve a lot.
Of course, this comes with a lot of dependency on the re-used code.
Unit tests focus on isolating our code from dependencies.
However,
the functionality can feel 'empty' after removing dependencies.
The resulting unit-tests may not give confidence about real-life behavior.

The opportunity is to sustain confidence in small pieces of code
with fast feedback from unit tests.

## Our Playground

Let's say our product needs to read [this excel](emails-to-send.xlsx):

![excel-sample](email-sample.png)

...then send email information to employees about their hike.

Is it easy to read this excel file?
See [this file](read_excel_poc.py) for an implementation.
It reads `emails-to-send.xlsx` and prints the data -
it's a couple of lines of code.

### Code-driven play

[This file](test_read_isolated.py) is an attempt
to test the functionality without dependencies.
It uses mocking to remove the dependency on pandas, excel and the filesystem.
The mock returns predefined sample data.

The implementation is changed to make it testable -
Notice that the function now returns the result instead of printing it.
This makes the behavior 'observable' by a test.

The [sample data](...) in the file is interesting.
It gives readable percentages, like in the excel.
That was not the case when real data came in from the excel!

Did the unit test deviate from reality? Does this give us confidence?

### Consumer-driven play

What can upset a customer...

Separate reading from processing. Pure function...

## Finishing up

[This file](...) implements emails. [Here are the instructions](...)
to test it manually.

How can you catch all consumer-relevant functionality early?
Design unit-tests for that.
