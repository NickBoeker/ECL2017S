3 - The code iterates through a number of operations from 1 to 59 and sqrts and squares starting with 2.  The number loses its original value due to the excessive manipulation and loss of precision.  
4 - The code is running while eps is not 0 and dividing it by two each time.  When the loop exits that means that python considers the eps value to be close to zero.
5 - The code is odd in that it rounds down on the odd numbers.  Other than that it seems to output exactly what one would expect  
6B - recursive is faster with a time of 834 microseconds, loops comes in at 1.39 milliseconds  