Author: Jakub Jonczyk  
Project made: 22.03.2020  
Repository created: 28.03.2020  
________________________________  

This code is a solution to a well-known mathematical problem (but extended a little bit).
Given the triangle of numbers, I had to find a path with the smallest sum and return both the path (from the top to the bottom) and its sum itself. 
Oh, and of course you can only go one step down and one step left/right each time!

For example:  
   4  
  1 3  
 2 5 6  
3 2 1 2  

This one is easy, right?
-sum:  9
-path: 4->1->2->2 (return: '4122')

Most of you were probably searching for the solution from the top to the bottom (as given above)  
but it's not efficient with bigger data.
So I decided to start at penultimate line and go upwards, for each element comparing the sum for both elements (left and right)  
in the line below.

Step by step, it's working like this:  

1st loop:   
  
4  
1 3  
2 5 6	<- starting in this line  
3 2 1 2  
  
2: compare(3, 2), smallest sum = 2  
5: compare (2, 1), smallest sum = 1   
6: compare(1, 2), smallest sum = 1  
  
Now I can add those sums to the proper elements above.  
  
4  
1 3  
4 6 7  
  
In the 2nd loop we should go line above and so on...  
  
I needed to return the sum AND the path, so I decided to keep the data in the second structure:  
  
pyramid = list()  
-this is the list which contains a list for each line (easy to access indexes of wanted elements)  
  
pyramid_data = dictionary  
-keys: indexes from the pyramid converted to a string  
  
['00']  
['10'] ['11']   
['20'] ['21'] ['31']  
[...]  
  
-values: another dictionary, containing path in a string (easy expansion: ('2' += '2') == '22') and value in integer numbers.  
  
For example in our pyramid (when we are done):  
pyramid_data['00']  == {"elem_path": '4122', "elem_sum": 9}  

My solution was tested on a pyramid containing 100 rows of numbers,  
so I think its efficiency and scalability is quite good.  
  
I am a beginner programmer so my code may need some improvements  
but it works already and I hope it's quite clear and readable to you!
