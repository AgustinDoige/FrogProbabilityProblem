# Frog Problem
#### Problem:  

> I initially found the problem from Matt Parker's [Youtube Video](https://youtu.be/ZLTyX4zL2Fc)  

There's a frog at one bank of a river, it wants to get to the other bank, and in the middle there's 9 lily pads (and with the other bank that's 10 jumps). The frog can jump any number of lily pads ahead (1 or more), even crossing the entire river in 1 jump. Every lily pad *ahead of the frog* (and the bank) have the same probability of being the next jump, and the frog cannot jump backwards.  

The question is, at one side, what is the *expected number of jumps that it will end up taking* to the to the other side? 

**Bonus Problem:** Generalize this result for n number of possible jumps, and give a non-recursive function that calculates it.  

 ### Simulation Solution:  
 
 Simply simulate with a random number generator lots of crossings, and then calculate the average of jumps the frog took.  
 
 > Simulated_Expectancy(10) = 2.92766              Calculation Time: 1.684s
 
 ### Bonus Solution:  
  ## [Image](https://raw.githubusercontent.com/AgustinDoige/FrogProbabilityProblem/master/DSC_0019c.jpg)  

A non rigorous explanation on the image DSC_0019b.  

Also implemented on the program: *frogProblemLeg.py*  

Results:  [Console Output](https://raw.githubusercontent.com/AgustinDoige/FrogProbabilityProblem/master/consoleScreenshot.jpg)  

Notes: It really starts having trouble at n=23, where the simulation actually does much better than the direct solution. There's probably some bottleneck that can be fixed there.
