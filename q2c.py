import numpy as np
import random
# random.seed(42)
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
        Decide Alice's play style for the current round. Implement your strategy for 2a here.

        Returns:
            0 : attack
            1 : balanced
            2 : defence

        """
        na=self.points
        nb=len(self.results)-na
        if self.results[-1]==1:
            if (nb)/(na+nb)>6/11:
                return 0
            else:
                return 2
        if self.results[-1]==0.5:
            return 0
        return 1
        pass


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
        pass

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
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:
            return 0



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
    amove=alice.play_move()
    bmove=bob.play_move()
    weight=payoff_matrix[amove][bmove]
    result=random.choices([1,0.5,0],weights=weight)
    result=result[0]
    alice.observe_result(amove,bmove,result)
    bob.observe_result(bmove,amove,1-result)
    return result
    pass


def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    num_rounds=5000
    sumT=0
    for i in range(1,num_rounds+1):
        # sumT=T*(i-1)
        a=Alice() #initializing an instance of Alice
        b=Bob()   #initializing an instance of Bob
        cnt=2     #initializing the count of total rounds
        cnt2=1    #initializing the count of rounds won by alice
        while cnt2<T:
            cnt+=1   #incrementing the count of total rounds
            payoff_matrix=[[[b.points/(a.points+b.points),0,a.points/(a.points+b.points)],[7/10,0,3/10],[5/11,0,6/11]],[[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],[[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
            result=simulate_round(a,b,payoff_matrix)  #simulating the round
            if result==1:
                cnt2+=1   #incrementing the count of rounds won by alice
            
        sumT+=cnt
    return sumT/num_rounds   #returning the average number of rounds taken for alice to win T rounds
    pass

print(estimate_tau(93))   #calculating tau for T=93