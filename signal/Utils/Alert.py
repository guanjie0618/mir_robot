from playsound import playsound

_select = 'Utils/Sounds/select.mp3'
_mission_completed = 'Utils/Sounds/mission_completed.mp3'


# 撥放踩點聲
def PLAY_select():
    playsound(_select)


# 撥放任務完成聲
def PLAY_mission_completed():
    playsound(_mission_completed)
