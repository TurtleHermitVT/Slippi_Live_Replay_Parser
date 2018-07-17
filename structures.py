from general import *

#command bytes
EVENT_PAYLOADS = "0x35"
GAME_START = "0x36"
PRE_FRAME_UPDATE = "0x37"
POST_FRAME_UPDATE = "0x38"
GAME_END = "0x39"

#event data holders and parse methods
#constructors initialize all to defaults
class game_start_event:
    def __init__(self):
        self.command_byte = GAME_START
        self.version = [] #major.minor.build.revision
        self.game_info_block = [] #not sure what this is
        self.is_teams = 0
        self.stage = 0
        self.character_ID_port1 = 0
        self.character_ID_port2 = 0
        self.character_ID_port3 = 0
        self.character_ID_port4 = 0
        self.player_type_port1 = 0
        self.player_type_port2 = 0
        self.player_type_port3 = 0
        self.player_type_port4 = 0
        self.character_color_port1 = 0
        self.character_color_port2 = 0
        self.character_color_port3 = 0
        self.character_color_port4 = 0
        self.team_ID_port1 = 0
        self.team_ID_port2 = 0
        self.team_ID_port3 = 0
        self.team_ID_port4 = 0
        self.random_seed = 0
    #parser for game start event data
    def parse_game_start(self, data):
        self.version.append(hex_to_int([data[0]]))
        self.version.append(hex_to_int([data[1]]))
        self.version.append(hex_to_int([data[2]]))
        self.version.append(hex_to_int([data[3]]))
        self.game_info_block = data[4:11]
        self.is_teams = hex_to_int([data[11]])
        self.stage = hex_to_int(data[18:20])
        self.character_ID_port1 = hex_to_int([data[100]])
        self.character_ID_port2 = hex_to_int([data[136]])
        self.character_ID_port3 = hex_to_int([data[172]])
        self.character_ID_port4 = hex_to_int([data[208]])
        self.player_type_port1 = hex_to_int([data[101]])
        self.player_type_port2 = hex_to_int([data[137]])
        self.player_type_port3 = hex_to_int([data[173]])
        self.player_type_port4 = hex_to_int([data[209]])
        self.character_color_port1 = hex_to_int([data[103]])
        self.character_color_port2 = hex_to_int([data[139]])
        self.character_color_port3 = hex_to_int([data[175]])
        self.character_color_port4 = hex_to_int([data[211]])
        self.team_ID_port1 = hex_to_int([data[109]])
        self.team_ID_port2 = hex_to_int([data[145]])
        self.team_ID_port3 = hex_to_int([data[181]])
        self.team_ID_port4 = hex_to_int([data[217]])
        self.random_seed = hex_to_int(data[316:])

class pre_frame_event:
    def __init__(self):
        self.command_byte = PRE_FRAME_UPDATE
        self.frame_number = 0
        self.player_index = 0 #port is this +1
        self.is_follower = 0
        self.random_seed = 0
        self.action_state = 0
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.facing_direction = 0.0
        self.joystick_x = 0.0
        self.joystick_y = 0.0
        self.c_stick_x = 0.0
        self.c_stick_y = 0.0
        self.trigger = 0.0
        self.buttons = 0
        self.physical_buttons = 0
        self.physical_l = 0.0
        self.physical_r = 0.0
    #parser for pre frame update event data
    def parse_pre_frame(self, data):
        self.frame_number = hex_to_int(data[0:4])
        self.player_index = hex_to_int([data[4]])
        self.is_follower = hex_to_int([data[5]])
        self.random_seed = hex_to_int(data[6:10])
        self.action_state = hex_to_int(data[10:12])
        self.x_pos = hex_to_float(data[12:16])
        self.y_pos = hex_to_float(data[16:20])
        self.facing_direction = hex_to_float(data[20:24])
        self.joystick_x = hex_to_float(data[24:28])
        self.joystick_y = hex_to_float(data[28:32])
        self.c_stick_x = hex_to_float(data[32:36])
        self.c_stick_y = hex_to_float(data[36:40])
        self.trigger = hex_to_float(data[40:44])
        self.buttons = hex_to_int(data[44:48])
        self.physical_buttons = hex_to_int(data[48:50])
        self.physical_l = hex_to_float(data[50:54])
        self.physical_r = hex_to_float(data[54:])

class post_frame_event:
    def __init__(self):
        self.command_byte = PRE_FRAME_UPDATE
        self.frame_number = 0
        self.player_index = 0
        self.is_follower = 0
        self.internal_character_ID = 0
        self.action_state = 0
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.facing_direction = 0.0
        self.percent = 0.0
        self.shield_size = 0.0
        self.last_attack_landed = 0
        self.current_combo_count = 0
        self.last_hit_by = 0
        self.stocks_remaining = 0
    #parser for post frame update event data
    def parse_post_frame(self, data):
        self.frame_number = hex_to_int(data[0:4])
        self.player_index = hex_to_int([data[4]])
        self.is_follower = hex_to_int([data[5]])
        self.internal_character_ID = hex_to_int([data[6]])
        self.action_state = hex_to_int(data[7:9])
        x = hex_to_float(data[9:13])
        if(x <= 0.1 and x >= -0.1):
            x = 0
        self.x_pos = round(x, 2)
        y = hex_to_float(data[13:17])
        if(y <= 0.1 and y >= -0.1):
            y = 0
        self.y_pos = round(y, 2)
        self.facing_direction = hex_to_float(data[17:21])
        self.percent = hex_to_float(data[21:25])
        self.shield_size = hex_to_float(data[25:29])
        self.last_attack_landed = hex_to_int([data[29]])
        self.current_combo_count = hex_to_int([data[30]])
        self.last_hit_by = hex_to_int([data[31]])
        self.stocks_remaining = hex_to_int([data[32]])

class game_end_event:
    command_byte = GAME_END
    game_end_method = 0

class match_info:
    def __init__(self):
        self.player1_character = ""
        self.player2_character = ""
        self.current_stage = ""
    def set_match_context(self, character1, character2, stage):
        self.player1_character = character1
        self.player2_character = character2
        self.current_stage = stage

#ALL GLOBAL DATA HOLDERS -------------------
#data holders
#variable values will be updated each time one of these
#commands are encountered in the replay file
game_start_data = game_start_event()
pre_frame_data = pre_frame_event()
post_frame_data = post_frame_event()
game_end_data = game_end_event()
match = match_info()
