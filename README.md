# AI Assignment 01 - Kids in the Yard


1. I used OpenAI's codex program. I had never tried it out and was curious to see how it would compare to other LLMs I have used
2. Prompt I gave it: `Take a look at A1 - Kids Running in the Yard (1).pdf where you will find the instructions for this project. Come up with a plan on how you would tackle this issue. List the data structures you would use. Only use data found in this folder. Use object orientation and make code reusable.` 
After seeing its plan I thought it seemed reasonable enough given the steps it stated it would take 
3. One of the main differences between my implementation and the LLMs is the readibility. The code produced did not have any comments and it was all on one file. My implementation has 3 classes whereas the LLM generated 7 classes and had around 500 lines total
4. Some of the changes I would make to my implementation based on what the LLMs generated was the use of constant variables a for the numbers used constantly like the year we start start with and year we stop at. The LLM also used a deque instead of a list which could be much faster for larger data sets
5. Changes I would refuse to make would be to keep it as one file only. I would also not have as many as 7 classes instead of the three I had and that were asked for in this assignment. It also used id's instead of object orientation which made it look very complex.