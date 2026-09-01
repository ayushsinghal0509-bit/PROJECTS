"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007 

def  mod_add(a, b):
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
 # Problem 3b
dp_strategy = [[[-1 for i in range(201)] for j in range(201)] for k in range(201)]
def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).
    
    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive
    """
    payoff_matrix=[[[nb/(na+nb),0,na/(na+nb)],[7/10,0,3/10],[5/11,0,6/11]],[[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],[[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    strat=[0,0,0]
    max_points=-1
    if tot_rounds<=0:
        return strat
    if dp_strategy[int(2*na)][int(2*nb)][tot_rounds]!=-1:
        return dp_strategy[int(2*na)][int(2*nb)][tot_rounds]
    for amove in range(3):
        curr_points=0
        for bmove in range(3):
            weight=payoff_matrix[amove][bmove]
            curr_points+=weight[0]*(1+expected_points(tot_rounds-1,na+1,nb))+weight[1]*(0.5+expected_points(tot_rounds-1,na+0.5,nb+0.5))+weight[2]*(0+expected_points(tot_rounds-1,na,nb+1))
        if curr_points>max_points:
            strat=[0,0,0]
            strat[amove]=1
            max_points=curr_points 
    dp_strategy[int(2*na)][int(2*nb)][tot_rounds]=strat   #memoizing the strategy in the dp table
    return strat
            
    pass
dp_points = [[[-1 for i in range(201)] for j in range(201)] for k in range(201)]
def calculate_total_prob(conditional_prob1,conditional_prob2,conditional_prob3,p1,p2,p3):
    return conditional_prob1*p1+conditional_prob2*p2+conditional_prob3*p3
def expected_points(tot_rounds,na=1,nb=1):
    """
    Given the total number of rounds(tot_rounds), calculate the expected points that Alice can score after the tot_rounds,
    assuming that Alice plays optimally.

    Return : The expected points that Alice can score after the tot_rounds.
    """
    payoff_matrix=[[[nb/(na+nb),0,na/(na+nb)],[7/10,0,3/10],[5/11,0,6/11]],[[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],[[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    if  na>100 or nb>100:  #base case: if the points are greater than 100 we return 0 as the points of a and b are lower than the two digits of entry numbers 
        return 0
    if dp_points[tot_rounds][int(2*na)][int(2*nb)]!=-1:   # if the expected points are already calculated we return the value
        return dp_points[tot_rounds][int(2*na)][int(2*nb)] 
    if tot_rounds<=0:  #base case
        return 0
   
    exp_points=-1  #initializing the expected points to be something negative so that we can update it later
    attack,balance,defend=optimal_strategy(na,nb,tot_rounds)
    p_win_provided_attack=1/3*(payoff_matrix[0][0][0]+payoff_matrix[0][1][0]+payoff_matrix[0][2][0])  #calculating the conditional probabilities
    p_draw_provided_attack=1/3*(payoff_matrix[0][0][1]+payoff_matrix[0][1][1]+payoff_matrix[0][2][1])
    p_loss_provided_attack=1/3*(payoff_matrix[0][0][2]+payoff_matrix[0][1][2]+payoff_matrix[0][2][2])
    p_win_provided_balance=1/3*(payoff_matrix[1][0][0]+payoff_matrix[1][1][0]+payoff_matrix[1][2][0])
    p_draw_provided_balance=1/3*(payoff_matrix[1][0][1]+payoff_matrix[1][1][1]+payoff_matrix[1][2][1])
    p_loss_provided_balance=1/3*(payoff_matrix[1][0][2]+payoff_matrix[1][1][2]+payoff_matrix[1][2][2])    
    p_win_provided_defend=1/3*(payoff_matrix[2][0][0]+payoff_matrix[2][1][0]+payoff_matrix[2][2][0])
    p_draw_provided_defend=1/3*(payoff_matrix[2][0][1]+payoff_matrix[2][1][1]+payoff_matrix[2][2][1])
    p_loss_by_defend=1/3*(payoff_matrix[2][0][2]+payoff_matrix[2][1][2]+payoff_matrix[2][2][2])
    #p_win
    p_win=calculate_total_prob(p_win_provided_attack,p_win_provided_balance,p_win_provided_defend,attack,balance,defend)  #calculating the winning, losing, drawing probability using the conditional probabilities
    #p_draw
    p_draw=calculate_total_prob(p_draw_provided_attack,p_draw_provided_balance,p_draw_provided_defend,attack,balance,defend)
    #p_loss
    p_loss=calculate_total_prob(p_loss_provided_attack,p_loss_provided_balance,p_loss_by_defend,attack,balance,defend)

    exp_points=p_win*(1+expected_points(tot_rounds-1,na+1,nb))+p_draw*(0.5+expected_points(tot_rounds-1,na+0.5,nb+0.5))+p_loss*(0+expected_points(tot_rounds-1,na,nb+1))
    dp_points[tot_rounds][int(2*na)][int(2*nb)]=exp_points   #memoizing the expected points in the dp table
    return exp_points

print(expected_points(2))
