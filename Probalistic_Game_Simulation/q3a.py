import numpy as np
import random
class Alice:
    def __init__(self):
        # self.past_play_styles = np.array([1,1])  
        # self.results = np.array([1,0])           
        # self.opp_play_styles = np.array([1,1])  
        self.past_play_styles=[1,1]
        self.results=[1,0]
        self.opp_play_styles=[1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        na=self.points                  # points of Alice
        nb=len(self.results)-na         # points of Bob
        temp1=nb/(na+nb)
        if temp1+7/10+5/11>6/11+0.95:   # if the expectation of alice'attack is greater than 6/11+0.95 then alice will attack else defend
            return 0
        return 2
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.opp_play_styles.append(opp_style)
        self.results.append(result)
        self.points+=result

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        # self.past_play_styles = np.array([1,1]) 
        # self.results = np.array([0,1])          
        # self.opp_play_styles = np.array([1,1])   
        self.past_play_styles=[1,1]
        self.results=[0,1]
        self.opp_play_styles=[1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        # move = np.random.choice([0, 1, 2])
        move=random.choice([0,1,2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    amove=alice.play_move()              # alice's move
    bmove=bob.play_move()                # bob's move
    weight=payoff_matrix[amove][bmove]   # payoff matrix
    result=random.choices([1,0.5,0],weights=weight)  # random result of the round using weights
    result=result[0]
    alice.observe_result(amove,bmove,result) # updating alice's knowledge
    bob.observe_result(bmove,amove,1-result) # updating bob's knowledge
    pass
    
def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    a=Alice()    # intialize alice object
    b=Bob()      # initialize bob object
    for i in range(3,num_rounds+1):
        payoff_matrix=[[[b.points/(a.points+b.points),0,a.points/(a.points+b.points)],[7/10,0,3/10],[5/11,0,6/11]],[[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],[[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
        simulate_round(a,b,payoff_matrix)   # simulate a round
    return(a.points,b.points)         # return the points of alice and bob

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    print(monte_carlo(num_rounds=10**5))
    sum=0
    for i in range(10000//93):    # finding the average value for approx. 10**5 cumulative rounds.
        sum+=monte_carlo(num_rounds=93)[0]  # sum of Alice's points
    print(sum/(10000//93))
