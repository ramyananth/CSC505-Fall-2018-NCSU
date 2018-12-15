Practice Problems
1. Coin Change DP

Given a set of arbitrary denominations C =(c1,...,cd), describe an algorithm that uses dynamic programming to compute the minimum number of coins required for making change. You may assume that C contains 1 cent, that all denomination are different, and that the denominations occur in in increasing order.

2. Matrix Chain Multiplication

Reinforce your understanding of dynamic programming and the matrix-chain multiplication problem. Implement a dynamic programming version of the algorithm for solving the matrix-chain multiplication problem. Your program should take an array of integers representing the dimensions of the matrices in the matrix-chain as input, and it should produce the optimal number of scalar multiplications needed to compute the matrix-chain product as output.  In addition, your algorithm should also output an optimal parenthesization of the matrix chain.

3. Modified Djikstra

Reinforce your understanding of Dijkstra’s shortest path algorithm, learn about multiple solutions, and practice algorithm design and Implementation. In the usual formulation of Dijkstra’s algorithm, the number of edges in the shortest (= lightest) path is not a consideration. Here, we assume that there might be multiple shortest paths. Implement an algorithm that takes as input an undirected graph G = (V, E), a nonnegative cost function w on E, a source vertex s and a destination vertex t, and produces a path with the fewest edges amongst all shortest paths from s to t. If there are multiple such shortest paths with the fewest edges, your algorithm should output the unique path with the lexicographically smallest sequence of vertices amongst all such paths. Please describe (6 points) and implement your algorithm. Your implementation should follow the description of Dijkstra's algorithm given in class.

I/O Specification:

The input should be read from the console, and the output should be printed to the console.

The first line of input contains two integers separated by a space: the number of vertices |V| (1<=|V|<=50), and the number of edges |E| (0<=|E|<=100). The next |E| lines each describes an undirected edge. An edge is described by three integers separated by space: the end-points u and v (0<=u, v<=|V|-1), and the cost w(u,v) (0<=w(u,v)<=1000). The last line of input contains the source-destination s and t (0<=s, t<=|V|-1) separated by space.

Your program should print two lines. In the first line, output the cost of the optimal path computed by your algorithm. In the second line, output the sequence of vertices in the path (for details, see the problem description) separated by spaces. Do not print an extra space after the last vertex in the sequence; do print a newline after the sequence. You can assume that there will always be a solution.


4. Creature-Prolog

Here is a database of facts and rules. 

Creatures come in two types: humans and birds.
One type of human is a man.
One type of bird is a turkey.
Louis is a man.
Albert is a man.
Frank is a turkey.
a. Louis is a man, Louis is a human, and Louis is a creature.
b. Albert is a man, Albert is a human, and Albert is a creature.
c. Frank is a turkey, Frank is a bird, and Frank is a creature.
