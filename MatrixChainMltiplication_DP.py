def mcm_Parenthesis(s, i, j):
	if(i == j):
		print(i, end ="") #end="" is to display output on the same line
	else :
		print('(', end ="")
		mcm_Parenthesis(s, i, s[i][j])
		mcm_Parenthesis(s, s[i][j]+1, j)
		print(')', end ="")

def main():
    # Get the size of matrix
    n1 = int(input())
    # Get the dimensions of the matrices
    InputValue = [int(x) for x in input().split(" ")]
    #Check if the sizes are right, else error
    if(len(InputValue)!=(n1+1)):
        print("Error", end="")
    # Convert as a dictionary for easier key value par identification
    p = {}
    for i in range(0, len(InputValue), 1):
        p[i]=InputValue[i]
    n = (len(p.keys())-1 )
    
    m = [[0 for x in range(n+1)] for x in range(n+1)]
    s = [[0 for x in range(n+1)] for x in range(n+1)]

    for l in range(2, n+1) : #l=chain length
	    for i in range(1, n-l+2) :
		    j = i+l-1
		    m[i][j] = 999999999 #infinity
		    for k in range(i, j):
			    q = (m[i][k] + m[k+1][j] + (p[i-1]*p[k]*p[j]))
			    if(q<m[i][j]) :
				    m[i][j] = q
				    s[i][j] = k
    
    print(max(m)[k+1])
    mcm_Parenthesis(s, 1, n)
    print('\n')

main()