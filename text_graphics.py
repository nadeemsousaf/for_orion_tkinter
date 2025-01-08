dialogue_start_x = 400
dialogue_end_x = 1200
typing_speed = 10 #changing as editing
line_speed = 10 #---------------
button_speed = 100 #-----------------
d_new_line = "@" #signals new line in dialogue
d_action = "~" #signals action start after dialogue

#action holder- will holder the function call that is the action to be triggered after dialogue
action_holder = []

fonts = {
    '1' : ("OCR A Extended", 35),
    '2' : ("OCR A Extended", 40),
    '3' : ("OCR A Extended", 15),
    '4' : ("OCR A Extended", 25),
}

dialogue = {
    'save_name': "Processing report submission...",
    'name_submission_page': "Submission complete. Thank you,",
    'prologue': "Mission Report:@67th rotation of Earth. The solar sails have been damaged by space debris during an acute solar event. Repairs must be made to correct course and speed of ship.~",

}
