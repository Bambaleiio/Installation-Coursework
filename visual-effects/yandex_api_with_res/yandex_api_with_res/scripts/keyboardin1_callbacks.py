# me - This DAT
# 
# dat - The DAT that received the key event
# keyInfo - A namedtuple containing the following members:
#	key - The name of the key attached to the event.
#			This tries to be consistent regardless of which language
#			the keyboard is set to. The values will be the english/ASCII
#			values that most closely match the key pressed.
#			This is what should be used for shortcuts instead of 'character'.
#	webCode - The name of the key following web-programming standards.
#	character - The unicode character generated.
#	alt - True if the alt modifier is pressed
#	lAlt - True if the left-alt modifier is pressed
#	rAlt - True if the right-alt modifier is pressed
#	ctrl - True if the ctrl modifier is pressed
#	lCtrl - True if the left-ctrl modifier is pressed
#	rCtrl - True if the right-ctrl modifier is pressed
#	shift - True if the shift modifier is pressed
#	lShift - True if the left-shift modifier is pressed
#	rShift - True if the right-shift modifier is pressed
#	state - True if the event is a key press event
#	time - The time when the event came in milliseconds
#	cmd - True if the cmd modifier is pressed
#	lCmd - True if the left-cmd modifier is pressed
#	rCmd - True if the right-cmd modifier is pressed

def onKey(dat, keyInfo):
    if not ui.performMode: return

    if not op('select1')['done'][0]: return
    
    state = keyInfo.state
    key = keyInfo.key
    character = keyInfo.character

    if not state: return

    textOp = op('text1')

    if (key == 'esc'):
        textOp.text = ''
        return

    if (key == 'space'):
        textOp.text += ' '
        return True

    if (key == 'backspace'):
        if len(textOp.text):
            textOp.text = textOp.text[:-1]
        return
    
    if (key == 'enter'):
        debug(f'Sent message: {textOp.text}')
        op.LLMHandler.SendToLLM(textOp.text)
        textOp.clear()
        op('timer1').par.start.pulse()
        return
    
    textOp.text += character
    return
