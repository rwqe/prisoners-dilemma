####
# Each team's file must define four tokens:
#     team_name: Idk
#     strategy_name: Idk either
#     strategy_description: How does it works?
#     move: A function that returns 'c' or 'b'
####

team_name = 'idk'
strategy_name = 'dig each other in'
strategy_description = 'Always betray unless they collude twice.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always Betray unless they collude twice.
    return 'b'
    num_of_c = their_history.count('c')
    if num_of_c >= 2:
        return 'c'
    num_of_b = their_history.count('b')
    if num_of_b >= 1:
        return 'b'
    
    