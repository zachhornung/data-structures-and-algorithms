# Challenge Summary
Create a function that takes in a string and determines whether or not all brackets have matching pairs.

## Whiteboard Process
* [Whiteboard](matching_brackets.jpg)

## Approach & Efficiency
The approach I took was to iterate throught the string and see if the character is a left or right bracket. If it is, a counter correlated to that bracket is incrimented by 1. After iterating through the string, corresponding left and right counters are compared, and if each corresponding pair is equal, then return True. False is returned by default.

