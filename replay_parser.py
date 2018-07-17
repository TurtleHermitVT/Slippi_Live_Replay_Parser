#Experimental Live Slippi Replay Parser
#Parses the data during live gameplay
#Updates are inconsistently timed as data becomes available,
#This means that the parser won't be on the exact same frame as the live game
#but every single frame will be read.

import time

import translator
from structures import *
from general import *
from file_detection import watch_for_create

#watch for Slippi file creation
full_filename = watch_for_create("../")

#live parse the newly created file
with open(full_filename, "rb") as replay:
    #skip init routine
    replay.seek(30)
    #game start
    data = read_frame(replay, 320)
    game_start_data.parse_game_start(data)

    match.set_match_context(translator.external_character_id[game_start_data.character_ID_port1],
    translator.external_character_id[game_start_data.character_ID_port2],
    translator.stage_index[game_start_data.stage])

    #Frame update
    #This will loop until the game ends
    command = ""
    stocks = [0,0]
    while(True):
        #get command byte
        command = read_frame(replay, 1)[0]

        #parse command
        #update data for cooresponding command byte
        if(command == PRE_FRAME_UPDATE):
            data = read_frame(replay, 58)
            pre_frame_data.parse_pre_frame(data)
        elif(command == POST_FRAME_UPDATE):
            data = read_frame(replay, 33)
            post_frame_data.parse_post_frame(data)
            #Example prints
            if(post_frame_data.action_state in translator.action_state_id):
                print(translator.action_state_id[post_frame_data.action_state])
            print(vars(post_frame_data))
        elif(command == GAME_END):
            data = read_frame(replay, 1)
            game_end_data.game_end_method = hex_to_int([data[0]])
            break

    replay.close()
