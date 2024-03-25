# Skyscraper
Get familiar with dynamic programming design and development 

Task 1: Meet your partner at skyscraper

1.1 Problem description

You are standing at the ground floor and your partner is waiting at the top floor of a skyscraper. You
will have to use an algorithmically designed lift L to reach your partner. The lift L is designed in the
manner that if you use the lift at the floor i, you are able to reach any floor from i + 1 to i + L[i] where
L[i] is a positive integer that presents the capacity of the lift at the i-th floor. Each time you use the
lift costs $1.

Assume that the skyscraper has n floors and you are at the floor 0. Your partner is at the floor n −1
and waiting for you to see the sky view. The lift information L[i] for 0 ≤ i < n is available at the
ground floor. Write a function to return the minimum cost, i.e. the number of time using the lift, to
reach your partner.

1.2 Test case description
Your input will be a sequence of n integers, each value per line corresponding to the lift information
L[i] (e.g. the capacity of the lift) on the i-th floor. The first line is for the 0-th floor. The last line is
for the (n −1)-th floor. Your output will be an integer.

Sample Input 1:

8

1

3

1

3

Sample Output 1:

1

You only need to use the lift once since L[0] = 8 is sufficient to get you to the 4th floor.

Sample Input 2:

2

5

1

4

8

Sample Output 2:

2

You only need to use the lift twice. The first one with L[0] = 2 to the 1st floor, and L[1] = 5 is sufficient
to get you to the 4th floor.
