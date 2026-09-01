"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    l=[[0]*101 for i in range(101)]   #dp table
    n1=alice_wins                     #alice wins
    n2=bob_wins                       #bob wins
    def solve(na,nb):
        if na==n1 and nb==n2:
            return 1  #base case
        if l[na][nb]:
            return l[na][nb]  #memoization
        if na==n1:
            l[na][nb]=mod_multiply(solve(na,nb+1),mod_divide(na,(na+nb)))
            return l[na][nb]  #returning one possible case
        if nb==n2:
            l[na][nb]=mod_multiply(solve(na+1,nb),mod_divide(nb,(na+nb)))
            return l[na][nb] #returning one possible case
        l[na][nb]=mod_add(mod_multiply(solve(na,nb+1),mod_divide(na,(na+nb))),mod_multiply(solve(na+1,nb),mod_divide(nb,(na+nb))))
        return l[na][nb] #returning the sum of two possible cases whenever they are possible
    
    return(solve(1,1))
    
# print(calc_prob(16,43)) 
# Problem 1b (Expectation)      
def calc_expectation(t):
    
    """
    Returns:
        The expected value of sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    ans=0
    for i in range(1,t):
        ans=mod_add(ans,mod_multiply((2*i-t),calc_prob(i,t-i)))  #calculating the expectation using summing the values of x*P(X=x)
    return(ans)
    # pass
# print(calc_expectation(98))
# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    ans=0
    exp=calc_expectation(t)
    for i in range(1,t):
        # print(i)
        
        ans=mod_add(ans,mod_multiply((2*i-t-exp)**2,calc_prob(i,t-i)))   #calculating the variance using the formula of variance
    # print(ans)
    return(ans)
    # pass
# (calc_variance(43))