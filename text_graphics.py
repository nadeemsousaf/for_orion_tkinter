#store below in object?
dialogue_start_x = 400
dialogue_end_x = 1200
typing_speed = 10 #changing as editing
line_speed = 10 #---------------
button_speed = 100 #-----------------

#store below in object?
d_new_line = "@" #signals new line in dialogue
d_action = "~" #signals action start after dialogue

#action holder- will holder the function call that is the action to be triggered after dialogue #workshopping, possible solution (typing/button-appearance order)
action_holder = []

fonts = {
    '1' : ("OCR A Extended", 35),
    '2' : ("OCR A Extended", 40),
    '3' : ("OCR A Extended", 15),
    '4' : ("OCR A Extended", 25),
}

#add d_action
dialogue = {
    'save_name': "Processing report submission...",
    'name_submission_page': "Submission complete. Thank you,",
    'prologue': "Mission Report:@67th rotation of Earth. The solar sails have been damaged by space debris during an acute solar event. Repairs must be made to correct course and speed of ship.~",
    'ship_overview_intro': "Ship overview...",
    'ship_overview_command_deck' : "Command deck",
    'ship_overview_lab' : "Lab",
    'ship_overview_cafeteria' : "Cafeteria",
    'ship_overview_sleeping_quarters' : "Sleeping quarters",
    'ship_overview_gym' : "Gym",
    'ship_overview_machine_room' : "Machine room",
    'ship_overview_airlock' : "Airlock",

}
