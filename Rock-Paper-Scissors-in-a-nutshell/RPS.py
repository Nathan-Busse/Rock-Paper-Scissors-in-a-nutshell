# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play,
            opponent_history=[],
            my_player_history=[],
            play_order=[{
                "RR": 0,
                "RP": 0,
                "RS": 0,
                "PR": 0,
                "PP": 0,
                "PS": 0,
                "SR": 0,
                "SP": 0,
                "SS": 0,
            }]):

    if prev_play != '':
        opponent_history.append(prev_play)
    # if a new player joins the game, discard history and the  play_order
    else:
        del opponent_history[:]
        del my_player_history[:]
        del play_order[:]
        play_order.append({
                "RR": 0,
                "RP": 0,
                "RS": 0,
                "PR": 0,
                "PP": 0,
                "PS": 0,
                "SR": 0,
                "SP": 0,
                "SS": 0,
            })
    
    #   response constants
    basic_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    #       Let us give the other bots a hand
    next_response = {'P': 'R', 'R': 'S', 'S': 'P'}
    

    #  No matter what happens, fill in "play_order" to beat our arch nemasis, abbey
    if len(my_player_history) < 1:
        last_played = "R"
        my_player_history.append(last_played)
    else:
        last_played = my_player_history[-1]
    
    last_two = ''.join(my_player_history[-2:])    
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        last_played + "R",
        last_played + "P",
        last_played + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]
    abbey_response = next_response[prediction]

    # check and beat quincy
    #   since quincy plays a set response of length 5, after 5 plays verify that it is in fact quincy
    if len(opponent_history) > 4:
        last_five = ''.join(opponent_history[-5:])
        verify_quincy = ''.join(["R", "R", "P", "P", "S"]*2)
        index = verify_quincy.find(last_five)

      #   if "my_player_history" is equally matched to our opponent which will be quincy where we will go against her next move.
        if index > -1:
            response = basic_response[verify_quincy[index + 5]]
            my_player_history.append(response)
            return response
        
    # check and beat kris
    if len(opponent_history) > 4:
        #   create a list following the same rules as kris
        verify_kris = [basic_response[x] for x in my_player_history[-5:-1]]

        #   if "my_player_history" is equally matched to our opponent which will be kris where he will make the first move.
      
        if verify_kris == opponent_history[-4:]:
            response = next_response[my_player_history[-1]]
            my_player_history.append(response)
            return response
    
    # Now our player will check and beat mrugesh
    if len(opponent_history) > 3:
        
        if len(opponent_history) < 10:
            run = len(opponent_history)
        else:
            run = 10

        #  Like the end of all games there is always a boss battle and our boss is the dreaded mrugesh who has the power of learning patterns of its victims and uses their powers against them.
          
        #   check if opponent history follows mrugesh's rules
        mrugesh = True
        for x in range(run-2):
            x = x + 1
            last_ten = my_player_history[-10-x:-x]
            most_frequent = max(set(last_ten), key=last_ten.count)
            if opponent_history[-x] != basic_response[most_frequent]:
                mrugesh = False
        
        #   When our next opponent is the dreaded mrugesh, play based on player's history
        if mrugesh:
            last_own_ten = my_player_history[-10:]
            most_frequent = max(set(last_own_ten), key=last_own_ten.count)
            response = next_response[most_frequent]
            my_player_history.append(response)
            return response
    
    #   Now it is our turn to play against abbey
    my_player_history.append(abbey_response)
    return abbey_response
