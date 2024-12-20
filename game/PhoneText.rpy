define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "[player_name]" ##The name of the main character, used to place them on the screen

init -1 python:
    phone_position_x = 0.5
    phone_position_y = 0.5


    ## def Phone_ReceiveSound(event, interact=True, **kwargs):
    ##     if event == "show_done":
    ##         renpy.sound.play("audio/ReceiveText.ogg")
    ## def Phone_SendSound(event, interact=True, **kwargs):
    ##     if event == "show_done":
    ##         renpy.sound.play("audio/SendText.ogg")

    def next_message(dialogue):
        """현재 메시지를 진행시킴"""
        # 현재 출력 중인 메시지를 찾음
        for idx, d in enumerate(dialogue):
            if d.current:  # 현재 출력 중인 대사 찾기
                d.current = False  # 현재 대사 비활성화
                if idx + 1 < len(dialogue):  # 다음 대사로 이동
                    dialogue[idx + 1].current = True
                break


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen phone_dialogue(dialogue, items=None):
    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            draggable True
            mousewheel True
            yinitial 1.0
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.current:
            if d.who == None: # Narrator
                text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
            else:
                if d.who == "[player_name]":
                    $ message_frame = "phone_send_frame.png"
                else:
                    $ message_frame = "phone_received_frame.png"

                hbox:
                    spacing 10
                    if d.who == "[player_name]":
                        pos (110,0)
                    
                    if previous_d_who != d.who and d.who != "[player_name]":  # 플레이어가 아니고 이전 화자와 다를 때만
                        if d.who == "세나":
                            $ message_icon = "phone_received_icon_sena.png"
                            add message_icon:
                                if d.current:
                                    at message_appear_icon()
                        elif d.who == "찬미":
                            $ message_icon = "phone_received_icon_chanmi.png"
                            add message_icon:
                                if d.current:
                                    at message_appear_icon()
                        elif d.who == "아리":
                            $ message_icon = "phone_received_icon_ari.png"
                            add message_icon:
                                if d.current:
                                    at message_appear_icon()
                    else:
                        null width 50

                    vbox:
                        yalign 1.0
                        if d.who != "[player_name]" and previous_d_who != d.who:
                            text d.who:
                                size 20
                        
                        frame:
                            padding (20,20)
                            background Frame(message_frame, 23,23,23,23)
                            xsize 300
                        
                            if d.who == "[player_name]":
                                at message_appear(1)
                            else:
                                at message_appear(-1)
                                
                            text d.what:
                                pos (0,0)
                                xsize 350
                                slow_cps False
                                
                                if d.who == "[player_name]":
                                    color "#FFF"
                                    text_align 1.0
                                else:
                                    color "#000"
                                    text_align 0.0
                                    id d.what_id
            $ previous_d_who = d.who
                    
style phoneFrame is default

style phoneFrame_frame:
    background Transform("phone_background.png", xcenter=0.5,yalign=0.5)
    foreground Transform("phone_foreground.png", xcenter=0.5,yalign=0.5)
    ysize 815
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill True
    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True
