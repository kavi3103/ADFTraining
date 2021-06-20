# Program to Convert Decimal to Binary, Octal and Hexadecimal

1. Get the decimal number as input.
2. Set base as 2 for binary conversion or 8 for octal conversion or 16 for hexadecimal conversion.
3. Initialise an empty string for output.
4. if num != 0 then do the following, find reminder when number is divided by base.if reminder < 9 concatenate reminder to the output. Otherwise find the character coresponding to rem+55 and concat to output.(For Hexa decimal since 10 is considered as 'A' in hexadecimal). divide the num by base and set as num. Repeate the process
5. Otherwise print the output.

