﻿################################################################################
## 초기화
################################################################################

init offset = -1


################################################################################
## 스타일
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 게임내 스크린
################################################################################


## Say 스크린 #####################################################################
##
## Say 스크린은 플레이어에게 대사를 출력할 때 씁니다. 화자 who와 대사 what, 두
## 개의 매개변수를 받습니다. (화자 이름이 없으면 who는 None일 수 있음)
##
## 이 스크린은 id "what"을 가진 텍스트 디스플레이어블을 생성해야 합니다. (이 디
## 스플레이어블은 렌파이의 대사 출력에 필요합니다.) id "who" 와 id "window" 디스
## 플레이블이 존재할 경우 관련 스타일 속성이 적용됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 사이드 이미지가 있는 경우 글자 위에 표시합니다. 휴대폰 환경에서는 보이지
    ## 않습니다.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Character 객체를 통해 스타일을 지정할 수 있도록 namebox를 사용할 수 있게 만듭
## 니다.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input 스크린 ###################################################################
##
## 플레이어 입력을 받는 renpy.input을 출력할 때 쓰이는 스크린입니다. prompt 매개
## 변수를 통해 입력 지문을 표시할 수 있습니다.
##
## 이 스크린은 id "input"을 가진 input 디스플레이어블을 생성해야 합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice 스크린 ##################################################################
##
## menu 명령어로 생성된 게임내 선택지를 출력하는 스크린입니다. 한 개의 매개변수
## items를 받고, 이는 선택지 내용(caption)과 선택지 결과(action)이 있는 오브젝트
## 가 들어있는 리스트입니다.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu 스크린 ##############################################################
##
## 퀵메뉴는 게임 외 메뉴 접근성을 높여주기 위해 게임 내에 표시됩니다.

screen quick_menu():

    ## 다른 화면 위에 표시되는지 확인합니다.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.97
            #yoffset 0
            spacing 5

            textbutton _("되감기") action Rollback() text_size 25
            # textbutton _("대사록") action ShowMenu('history') 
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True) text_size 25
            textbutton _("자동진행") action Preference("auto-forward", "toggle") text_size 25
            # textbutton _("저장하기") action ShowMenu('save')
            # textbutton _("Q.저장하기") action QuickSave()
            # textbutton _("Q.불러오기") action QuickLoad()
            textbutton _("메뉴") action ShowMenu() text_size 25

## 플레이어가 UI(스크린)을 일부러 숨기지 않는 한 퀵메뉴가 게임 내에 오버레이로
## 출력되게 합니다.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main과 Game Menu 스크린
################################################################################

## Navigation 스크린 ##############################################################
##
## 이 스크린은 메인메뉴와 게임외 메뉴에 포함되어 다른 메뉴로 이동하거나 게임을
## 시작/종료할 수 있게 합니다.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if not main_menu:

            ##textbutton _("시작하기") action Start()

            textbutton _("대사록") action ShowMenu("history")

            # textbutton _("저장하기") action ShowMenu("save")

        ##textbutton _("불러오기") action ShowMenu("chapter_select")

        # textbutton _("환경설정") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("리플레이 끝내기") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("환경설정") action ShowMenu("preferences")
            textbutton _("메인 메뉴") action [Function(save_game_state), MainMenu()]

        ##textbutton _("캐릭터 프로필") action ShowMenu("character_profiles")

        ##if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## 도움말 메뉴는 모바일 디바이스와 맞지 않아 불필요합니다.
            ##textbutton _("게임 설명") action ShowMenu("game_help")

        ##if main_menu and renpy.variant("pc"):

            ## iOS에서는 종료 버튼이 금지되어 있으며 Android 및 웹에서는 불필요
            ## 합니다.
            ##textbutton _("종료하기") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu 스크린 ###############################################################
##
## 렌파이가 시작할 때 메인메뉴를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 이렇게 하면 다른 메뉴 화면이 모두 교체됩니다.
    tag menu

    add gui.main_menu_background

    ## 이 빈 프레임은 기본 메뉴를 어둡게 만듭니다.
    frame:
        style "main_menu_frame"

    vbox:

        # 세로로 나열
        align (0.08, 0.5)
        spacing 60  # 버튼 간 간격 (필요에 따라 조정)

        ## "시작하기" 버튼
        imagebutton:
            idle "main_button/images_start_idle.png"
            hover "main_button/images_start_hover.png"
            action CheckNewGame()
            
    
        ## "돌아가기" 버튼
        imagebutton:
            idle "main_button/images_chapter_idle.png"
            hover "main_button/images_chapter_hover.png"
            action ShowMenu("chapter_select")

        ## "게임 설명" 버튼
        imagebutton:
            idle "main_button/images_info_idle.png"
            hover "main_button/images_info_hover.png"
            action ShowMenu("game_help")

        ## "호감도 확인" 버튼
        ##imagebutton:
            ##idle "images_favor_idle.png"
            ##hover "images_favor_hover.png"
            ##action ShowMenu("affection_status")  
            ##xsize 80
            ##ysize 40  

        ## 환경설정 버튼
        imagebutton:
            idle "main_button/images_settings_idle.png"
            hover "main_button/images_settings_hover.png"
            action ShowMenu("preferences")    

        ## 프로필 버튼
        imagebutton:
            idle "main_button/images_profile_idle.png"
            hover "main_button/images_profile_hover.png"
            action ShowMenu("character_profiles") 

        ## "게임 종료" 버튼
        imagebutton:
            idle "main_button/images_quit_idle.png"
            hover "main_button/images_quit_hover.png"
            action Quit(confirm=True)
            

    ## use 명령어로 스크린 내에 다른 스크린을 불러옵니다. 메인 메뉴 스크린의 내
    ## 용물은 navigation 스크린에 있습니다.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"
        vbox:
            xalign 0.97
            yalign 0.01
            text "{size=-16}© 2024 두근두근 충북대 by 옥수수수염차 All rights reserved{/size}":
                style "main_menu_version"
            text "[config.version]":
                style "main_menu_version"
    
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

## 메인 메뉴 화면 왼쪽 검은 바탕 삭제
## style main_menu_frame:
    ##xsize 420
    ##yfill True

    ##background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    font "KCC-Ganpan.ttf"
    color "#ffffff"

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

init python:
    def CheckNewGame():
        # 저장된 데이터가 있는지 확인
        if  persistent.chanmi_affection != 20 or \
            persistent.ari_affection != 20 or \
            persistent.sena_affection != 20 or \
            (hasattr(persistent, 'player_name') and persistent.player_name is not None):
            return Show("confirm_new_game")
        else:
            return [SetField(persistent, "is_new_game", True), Start()]

screen confirm_new_game():
    modal True
    zorder 200  # 다른 화면보다 위에 표시되도록 설정
    
    frame:
        style_prefix "confirm"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 30
            text "데이터가 존재합니다.\n새 게임을 시작하시겠습니까?\n모든 진행 상황이 초기화됩니다."
            hbox:
                spacing 100
                textbutton "예":
                    action [Function(reset_persistent_data), SetField(persistent, "is_new_game", True), Start()]
                textbutton "아니오":
                    action Hide("confirm_new_game")




## Game Menu 스크린 ###############################################################
##
## 게임 메뉴의 기본 틀입니다. 매개변수 title로 스크린 제목을 정하고, 배경, 제목,
## 그리고 navigation 스크린을 출력합니다.
##
## scroll 매개변수는, None, "viewport" 혹은 "vpgrid" 중 하나여야 합니다.
## transclude 명령어를 통해 다른 스크린을 이 스크린 내부에 불러옵니다.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 탐색 섹션을 위한 공간 예약.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("돌아가기"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45



##캐릭터 이름 글자 크기를 키우고 색을 입히기 위함
style character_name_text is menu_text:
    size gui.interface_text_size + 4  # 기본 크기보다 4포인트 크게 설정
    color "#ffffff"

style character_identity_text is menu_text:
    color "#ffffff" 

##캐릭터 설명 글자 크기를 줄이기 위함
style character_description_text is menu_text:
    size gui.interface_text_size - 4  # 기본 크기보다 4포인트 작게 설정
    color "#ffffff"

init python:
    if persistent.chapter1_cleared is None:
        persistent.chapter1_cleared = False
    if persistent.chapter2_cleared is None:
        persistent.chapter2_cleared = False
    if persistent.chapter3_cleared is None:
        persistent.chapter3_cleared = False
    if persistent.chapter4_cleared is None:
        persistent.chapter4_cleared = False
    if persistent.player_name is None:
        persistent.player_name = None

# 먼저 persistent 변수들을 초기화
default persistent.chapter_selected = 0
default persistent.chapter1_cleared = False
default persistent.chapter2_cleared = False
default persistent.chapter3_cleared = False

# 챕터 선택 스크린
screen chapter_select():
    tag menu
    modal True

    vbox:
        align (0.5, 0.5)
        spacing 10

        text "챕터 선택 화면" size 40

        if not persistent.player_name:
            text "새 게임을 시작하세요." size 20 color "#ff0000"

        if persistent.player_name:
            textbutton "Chapter 1" action [SetField(persistent, "chapter_selected", 1), Function(save_game_state), Hide("chapter_select"), Start()]
        else:
            textbutton "Chapter 1 (Locked)" action NullAction()

        if persistent.chapter1_cleared:
            textbutton "Chapter 2" action [SetField(persistent, "chapter_selected", 2), Function(save_game_state), Hide("chapter_select"), Start()]
        else:
            textbutton "Chapter 2 (Locked)" action NullAction()

        if persistent.chapter2_cleared:
            textbutton "Chapter 3" action [SetField(persistent, "chapter_selected", 3),Function(save_game_state),  Hide("chapter_select"), Start()]
        else:
            textbutton "Chapter 3 (Locked)" action NullAction()

        if persistent.chapter3_cleared:
            textbutton "Chapter 4" action [SetField(persistent, "chapter_selected", 4), Function(save_game_state), Hide("chapter_select"), Start()]
        else:
            textbutton "Chapter 4 (Locked)" action NullAction()

        textbutton "돌아가기" action Return()


## 캐릭터 프로필 스크린 ############################################################
screen character_profiles():
    tag menu
    
    use game_menu(_("Character Profiles"), scroll="viewport"):
        style_prefix "character_profiles"
        
        vbox:
            spacing 20
            for char in all_characters:
                textbutton char.char.name action Show("character_detail", character=char)

## 개별 캐릭터 상세 정보 화면
screen character_profiles():
    tag menu
    
    use game_menu(_("캐릭터 프로필")):
        vbox:
            spacing 20
            
            for char in all_characters:
                hbox:
                    spacing 20
                    add char.profile_image size (200, 200)
                    vbox:
                        text char.name style "character_name_text" color char.color
                        text char.personality style "character_identity_text"
                        text char.description style "character_description_text"


#     tag menu

#     ## 이 use 명령어로 game_menu 스크린을 이 스크린 내에 불러옵니다. use 명령어
#     ## 하위블럭(vbox 내용)은 game_menu 스크린 내 transclude 명령어가 있는 곳에
#     ## 다시 불려집니다.
#     use game_menu(_("버전정보"), scroll="viewport"):

#         style_prefix "about"

#         vbox:

#             label "[config.name!t]"
#             text _("버전 [config.version!t]\n")

#             ## gui.about 의 내용은 보통 options.rpy에 있습니다.
#             if gui.about:
#                 text "[gui.about!t]\n"

#             text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임.\n\n[renpy.license!t]")


# style about_label is gui_label
# style about_label_text is gui_label_text
# style about_text is gui_text

# style about_label_text:
#     size gui.label_text_size


## Load 그리고 Save 스크린 ###########################################################
##
## 이 스크린은 세이브/로드에 쓰입니다. 거의 동일하기 때문에, file_slots 스크린을
## 불러와서 씁니다.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    use game_menu(_("일시정지")):
        use affection_status

screen load():
    tag menu
    use game_menu(_("불러오기")):
        use affection_status


style vbar:
    bar_vertical True  # 세로 방향 바
    bar_invert False    # 아래에서 위로 차오르도록 설정

screen affection_status():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            
            if persistent.player_name:  # 이름이 입력된 경우에만 표시
                text "플레이어 이름 : [persistent.player_name]" size 20 xalign 0.5 color "#000000" outlines [(2, "#ffffff")]
                text "캐릭터 호감도" size 40 xalign 0.5 color "#000000" outlines [(2, "#ffffff")]
                
                null height 40
                
                hbox:
                    spacing 50
                    xalign 0.5
                        
                    # 찬미 호감도
                    vbox:
                        spacing 10
                        text "찬미" size 30 xalign 0.5 color "#000000" outlines [(1, "#ffffff")]
                        bar:
                            xsize 150
                            ysize 150
                            value chanmi_affection
                            range 100
                            right_bar Frame("gui/heart_full.png")
                            left_bar Frame("gui/heart_empty.png")
                            style "vbar"
                        text "[chanmi_affection]/100" xalign 0.5 color "#000000" outlines [(1, "#ffffff")]
                        
                    # 아리 호감도
                    vbox:
                        spacing 10
                        text "아리" size 30 xalign 0.5 color "#000000" outlines [(1, "#ffffff")]
                        bar:
                            xsize 150
                            ysize 150
                            value ari_affection
                            range 100
                            right_bar Frame("gui/heart_full.png")
                            left_bar Frame("gui/heart_empty.png")
                            style "vbar"
                        text "[ari_affection]/100" xalign 0.5 color "#000000" outlines [(1, "#ffffff")]
                        
                    # 세나 호감도
                    vbox:
                        spacing 10
                        text "세나" size 30 xalign 0.5 color "#000000" outlines [(1, "#ffffff")]
                        bar:
                            xsize 150
                            ysize 150
                            value sena_affection
                            range 100
                            right_bar Frame("gui/heart_full.png")
                            left_bar Frame("gui/heart_empty.png")
                            style "vbar"
                        text "[sena_affection]/100" xalign 0.5 color "#000000" outlines [(1, "#ffffff")]
            # else:  # 이름이 입력되지 않은 경우
            #     text "게임을 시작하고 이름을 입력해주세요." size 30 xalign 0.5 color "#000000" outlines [(2, "#000000")]


## Preferences 스크린 #############################################################
##
## Preferences 스크린에서는 각종 환경설정을 플레이어가 지정할 수 있습니다.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("환경설정"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("화면 모드")
                        textbutton _("창 화면") action Preference("display", "window")
                        textbutton _("전체 화면") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("넘기기")
                    textbutton _("읽지 않은 지문") action Preference("skip", "toggle")
                    textbutton _("선택지 이후") action Preference("after choices", "toggle")
                    textbutton _("화면 전환 효과") action InvertSelected(Preference("transitions", "toggle"))

                ## "radio_pref" 나 "check_pref" 를 추가하여 그 외에도 환경설정
                ## 항목을 추가할 수 있습니다.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("텍스트 속도")

                    bar value Preference("text speed")

                    label _("자동 진행 시간")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("배경음 음량")

                        hbox:
                            bar value Preference("music volume") changed log_scale

                    if config.has_sound:

                        label _("효과음 음량")

                        hbox:
                            bar value Preference("sound volume") changed log_scale

                            if config.sample_sound:
                                textbutton _("테스트") action Play("sound", config.sample_sound)


                    # if config.has_voice:
                    #     label _("음성 음량")

                    #     hbox:
                    #         bar value Preference("voice volume")

                    #         if config.sample_voice:
                    #             textbutton _("테스트") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("모두 음소거"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

init python:
    import math

    def log_scale(value, min_db=-40, max_db=0):
        if value <= 0:
            return 0
        min_amp = 10 ** (min_db / 20)
        max_amp = 10 ** (max_db / 20)
        return min_amp * (max_amp/min_amp) ** value


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History 스크린 #################################################################
##
## 지난 대사록을 출력합니다. _history_list 에 저장된 대사 기록을 확인합니다.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 이 스크린은 내용이 아주 많을 수 있으므로 prediction을 끕니다.
    predict False

    use game_menu(_("대사록"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## history_height 이 None일 경우 레이아웃이 틀어지지 않게 합니
                ## 다.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 화자 Character에 화자 색깔이 지정되어 있으면 불러옵니
                        ## 다.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("대사가 없습니다.")


## 이것은 대사록 화면에 표시할 수 있는 태그를 결정합니다.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5



screen game_help():
    tag menu
    
    use game_menu(_("게임 설명")):
        side "c r":
            viewport id "help_vp":
                draggable True
                mousewheel True
                vbox:
                    spacing 20
                    xsize 800
                    vbox:
                        spacing 10
                        xalign 1.0
                        hbox:
                            textbutton _("조작 방법") action ShowMenu('help') style "gui_button"
                    vbox:
                        spacing 10
                        text "게임 진행 방법" size 30 color "#ffffff"
                        null height 20
                        text "• 화면의 대화를 클릭하거나 스페이스바를 눌러 진행할 수 있습니다." color "#ffffff"
                        text "• 우클릭이나 ESC를 눌러 게임 메뉴를 열 수 있습니다." color "#ffffff"
                    
                    vbox:
                        null height 40
                        spacing 10
                        text "호감도 시스템" size 30 color "#ffffff"
                        null height 20
                        text "• 각 캐릭터와 상호작용하면서 호감도가 변화합니다." color "#ffffff"
                        text "• 호감도는 0에서 100 사이의 값을 가지며, 게임 시작 시 20으로 시작합니다." color "#ffffff"
                        text "• 특정 선택지는 호감도에 영향을 미칩니다." color "#ffffff"
                        text "• 만약 특정 캐릭터의 호감도가 70이상일 시 그 캐릭터의 엔딩을 볼 수 있습니다." color "#ffffff"
                    
                    vbox:
                        spacing 10
                        null height 40
                        if gui.about:
                            text "[gui.about!t]\n" color "#ffffff"

                        text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임.\n\n[renpy.license!t]") color "#ffffff"
                        null height 20
                        text _("게임 버전 [config.version!t]\n") color "#ffffff"
                    vbox:
                        spacing 10
                        xalign 1.0
                        hbox:
                            textbutton _("크레딧 보기"):
                                action Call("credits")

            vbar value YScrollValue("help_vp")

style help_frame:
    background "#000000CC"
    padding (50, 50)

style help_label_text:
    color "#FFFFFF"
    size 40
    outlines [(2, "#000000")]

style help_text:
    color "#FFFFFF"
    size 25
    outlines [(1, "#000000")]

style help_button:
    xpadding 50
    ypadding 10

style help_button_text:
    color "#FFFFFF"
    hover_color "#CCCCCC"
    size 30
    outlines [(1, "#000000")]

style help_frame:
    background "#000000CC"
    padding (50, 50)

style help_label_text:
    color "#FFFFFF"
    size 40
    outlines [(2, "#000000")]

style help_text:
    color "#FFFFFF"
    size 25
    outlines [(1, "#000000")]

style help_button:
    xpadding 50
    ypadding 10

style help_button_text:
    color "#FFFFFF"
    hover_color "#CCCCCC"
    size 30
    outlines [(1, "#000000")]


## Help 스크린 ####################################################################
##
## 입력장치의 기능을 설명합니다. 각 입력장치별 설정은 keyboard_help, mouse_help,
## gamepad_help 스크린을 각각 불러와서 출력합니다.


screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("조작방법"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
        
        vbox:
                spacing 20
                xalign 1.0
                hbox:
                    textbutton _("돌아가기") action ShowMenu('game_help')



screen keyboard_help():

    hbox:
        label _("엔터(Enter)")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("스페이스(Space)")
        text _("대사를 진행하되 선택지는 선택하지 않음.")

    hbox:
        label _("화살표 키")
        text _("UI 이동.")

    hbox:
        label _("이스케이프(Esc)")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("컨트롤(Ctrl)")
        text _("누르고 있는 동안 대사를 스킵.")

    hbox:
        label _("탭(Tab)")
        text _("대사 스킵 토글.")

    hbox:
        label _("페이지 업(Page Up)")
        text _("이전 대사로 롤백.")

    hbox:
        label _("페이지 다운(Page Down)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label "H"
        text _("UI를 숨김.")

    hbox:
        label "S"
        text _("스크린샷 저장.")


screen mouse_help():

    hbox:
        label _("클릭")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("가운데 버튼이나 휠버튼 클릭")
        text _("UI를 숨김.")

    hbox:
        label _("우클릭")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("휠 위로")
        text _("이전 대사로 롤백.")

    hbox:
        label _("휠 아래로")
        text _("이후 대사로 롤포워드.")


screen gamepad_help():

    hbox:
        label _("오른쪽 트리거(RT)\nA버튼/아래 버튼")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("왼쪽 트리거\n왼쪽 어깨")
        text _("이전 대사로 롤백.")

    hbox:
        label _("오른쪽 범퍼(RB)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label _("D-Pad, 아날로그 스틱")
        text _("UI 이동.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("Y버튼/위 버튼")
        text _("UI를 숨김.")

    textbutton _("조정") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## 그 외 스크린
################################################################################


## Confirm 스크린 #################################################################
##
## 게임 입력 관련 예/아니오 질문을 플레이어에게 할 때 이 스크린을 표시합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 이 스크린이 출력 중일 때 다른 스크린과 상호작용할 수 없게 합니다.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("네") action yes_action
                textbutton _("아니오") action no_action

    ## 우클릭과 esc는 '아니오'를 입력하는 것과 같습니다.
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator 스크린 ##########################################################
##
## Skip_indicator 스크린은 스킵 중일 때 "스킵 중"을 표시하기 위해 출력됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("넘기는 중")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 이 transform으로 화살표를 순서대로 페이드인/페이드아웃합니다.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## BLACK RIGHT-POINTING SMALL TRIANGLE 글리프가 있는 글꼴을 사용해야 합니다.
    font "DejaVuSans.ttf"


## Notify 스크린 ##################################################################
##
## Notify 스크린으로 플레이어에게 메시지를 출력합니다. (예를 들어 '퀵세이브 완
## 료'나 '스크린샷 저장 완료')
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 스크린 #####################################################################
##
## NVL모드 대사와 선택지를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## vpgrid나 vbox 내에 대사를 출력합니다.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 주어진 경우 메뉴를 표시합니다. config.narrator_menu가 True로 설정된
        ## 경우 메뉴가 잘못 표시될 수 있습니다.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 동시에 출력될 수 있는 NVL 대사의 최대치를 조정합니다.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## 말풍선 화면은 말풍선을 사용할 때 플레이어에게 대화를 표시하는 데 사용됩니다.
## 말풍선 화면은 말풍선 화면과 동일한 매개변수를 사용하며, "what" 아이디로 표시
## 가능 항목을 생성해야 하며, "namebox", "who", "window" 아이디로 표시 가능 항목
## 을 생성할 수 있습니다.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 모바일 버전
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 마우스가 없고 화면이 작을 가능성이 높으므로, 퀵메뉴 버튼의 크기를 키우고 가짓
## 수를 줄입니다.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu and renpy.get_screen("window"):

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            yoffset -100

            textbutton _("되감기") action Rollback()
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("메뉴") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
