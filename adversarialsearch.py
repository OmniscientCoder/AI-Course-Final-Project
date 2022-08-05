from typing import Callable

from numpy import minimum

from adversarialsearchproblem import (
    Action,
    AdversarialSearchProblem,
    State as GameState,
)

import numpy as np

def minimax(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    Implement the minimax algorithm on ASPs, assuming that the given game is
    both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
    """
    player = asp.get_start_state().player_to_move()
    if player == 0:
        return MaxValue(asp, asp.get_start_state())
    elif player == 1:
        return MinValue(asp, asp.get_start_state())
    

def MaxValue(asp: AdversarialSearchProblem, state):
    output = [None, np.NINF]
    if asp.is_terminal_state(state):
        output[1] = asp.evaluate_terminal(state)[0]
        return output
    else:
        for action in asp.get_available_actions(state):
            successor = asp.transition(state, action)
            curr_eval = MinValue(asp, successor)[1]
            if curr_eval > output[1]:
                output = [action, curr_eval]
        return output

def MinValue(asp: AdversarialSearchProblem, state):
    output = [None, np.inf]
    if asp.is_terminal_state(state):
        output[1] = asp.evaluate_terminal(state)[0]
        return output
    else:
        for action in asp.get_available_actions(state):
            successor = asp.transition(state, action)
            curr_eval = MaxValue(asp, successor)[1]
            if curr_eval > output[1]:
                output = [action, curr_eval]
        return output


        
    """

    import numpy as np

    player = game.player_to_move(GameState)
    
    def maxPlayer(GameState):
        if asp.is_terminal_state(GameState):
            score = asp.evaluate_terminal(GameState)

        if player == 0:
            value = -np.inf
            for action in asp.get_available_actions(GameState):
                value = max(value, minPlayer(asp.transition(GameState, action)))
            return value

    def minPlayer(GameState):
        if asp.is_terminal_state(GameState):
            return asp.evaluate_terminal(GameState)

        if player == 1:
            value = +np.inf
            for action in asp.get_available_actions(GameState):
                value = min(value, maxPlayer(asp.transition(GameState, action)))
            return value

    maxPlayer(asp.get_start_state())

    """



    # FUCKKKKKKK!
    
    """

    import numpy as np

    player=game.player_to_move(GameState)
    
    def maximumPlayer(GameState):
        if asp.is_terminal_state(GameState):
            return asp.evaluate_terminal(GameState)

        if player == 0:
            value = -np.inf
            for action in asp.get_available_actions(GameState):
                value2, action2 = minimumPlayer(asp.transition(GameState, action))
                if value2 > value:
                    value = value2
                    move = action2
                    return value, move

    def minimumPlayer(GameState):
        if asp.is_terminal_state(GameState):
            return asp.evaluate_terminal(GameState)

        if player == 1:
            value = +np.inf
            for action in asp.get_available_actions(GameState):
                value2, action2 = maximumPlayer(asp.transition(GameState, action))
                if value2 > value:
                    value = value2
                    move = action2
                    return value, move

    maximumPlayer(asp.get_start_state())

    """



    # import numpy as np

    # player=game.player_to_move(GameState)

    # def maximumPlayer(GameState):
    #     if asp.is_terminal_state(GameState):
    #         return asp.evaluate_terminal(GameState)

    #     if player == 0:
    #         value = -np.inf
    #         for action in asp.get_available_actions(GameState):
    #             value2 = max(value, minimumPlayer(asp.transition(GameState, action)))
    #             if value2 > value:
    #                 return action
    #         # return value

    # def minimumPlayer(GameState):
    #     if asp.is_terminal_state(GameState):
    #         return asp.evaluate_terminal(GameState)

    #     if player == 1:
    #         value = -np.inf
    #         for action in asp.get_available_actions(GameState):
    #             value2 = min(value, maximumPlayer(asp.transition(GameState, action)))
    #             if value2 > value:
    #                 return action
    #         # return value

    # maximumPlayer(asp.get_start_state())






    # if asp.is_terminal_state(GameState):
    #     return asp.evaluate_terminal(GameState)

    # if GameState == asp.get_start_state():
        

    # if game.player_to_move() == 0:
    #     value = -np.inf
    #     for action in asp.get_available_actions(GameState):
    #         value2 = max(value, asp.heuristic_func(asp.transition(GameState, action), 0))
    #         if value2 > value:
    #             return action  


    # if game.player_to_move() == 1:
    #     value = +np.inf
    #     for action in asp.get_available_actions(GameState):
    #         value2 = min(value, asp.heuristic_func(asp.transition(GameState, action), 0))
    #         if value2 > value:
    #             return action


    # import numpy as np
 
    # if asp.is_terminal_state(GameState):
    #     return asp.heuristic_func(GameState)
    # value = -np.inf
    # for action in asp.get_available_actions(GameState):
    #     value2 = max(value, minimax(action, depth - 1, False))
 
    # if value2 > value:
    #     return value2

    # else:
    #     value = np.inf
    #     for action in asp.get_available_actions:
    #         value = min(value, minimax(action, depth - 1 ,True))
    #     return value



def alpha_beta(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    Implement the alpha-beta pruning algorithm on ASPs,
    assuming that the given game is both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...


def alpha_beta_cutoff(
    asp: AdversarialSearchProblem[GameState, Action],
    cutoff_ply: int,
    # See AdversarialSearchProblem:heuristic_func
    heuristic_func: Callable[[GameState], float],
) -> Action:
    """
    This function should:
    - search through the asp using alpha-beta pruning
    - cut off the search after cutoff_ply moves have been made.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_ply - an Integer that determines when to cutoff the search and
            use heuristic_func. For example, when cutoff_ply = 1, use
            heuristic_func to evaluate states that result from your first move.
            When cutoff_ply = 2, use heuristic_func to evaluate states that
            result from your opponent's first move. When cutoff_ply = 3 use
            heuristic_func to evaluate the states that result from your second
            move. You may assume that cutoff_ply > 0.
        heuristic_func - a function that takes in a GameState and outputs a
            real number indicating how good that state is for the player who is
            using alpha_beta_cutoff to choose their action. You do not need to
            implement this function, as it should be provided by whomever is
            calling alpha_beta_cutoff, however you are welcome to write
            evaluation functions to test your implemention. The heuristic_func
            we provide does not handle terminal states, so evaluate terminal
            states the same way you evaluated them in the previous algorithms.
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...
