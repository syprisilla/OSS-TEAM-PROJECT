define p = Character(" ")
# define s1 = Character("학생 1")
# define s2 = Character("학생 2")
# define s3 = Character("학생 3")
label chapter2:

    $ load_game_state()
    $ sync_player_name()

    scene bg_beach_day
    with dissolve

    "새 학기가 시작된 지 한 달쯤 되었을 무렵, 우리 모두는 MT를 떠나 대천해수욕장에 도착했다."
    "버스에서 내리자마자 우리는 짐을 풀고, 간단한 게임으로 시간을 보냈다."

    scene bg_bbq_evening
    with fade

    "저녁 시간이 다가오자, 우리는 바비큐 준비를 시작했다."
    "학생 1이 상추, 수저, 포크 같은 것들을 정리하고 있는 모습이 보인다."

    menu:
        "도와준다":
            $ affection_1 += 10
            "나는 학생 1을 도와주기로 했다."
            s1 "고마워! 덕분에 준비가 빨리 끝났어. 나중에 편의점에서 맛있는 거 사줄게!"
            return

        "도와주지 않는다":
            "나는 멀리서 바라만 보고 있었다."
            return

    "바비큐가 시작되고, 우리는 고기를 구우며 서로 이야기를 나누었다."
    
    s3 "주인공! 고기 태우지 말고 맛있게 구워봐~ (웃음)"
    menu:
        "장난으로 맞받아친다":
            "나는 학생 3에게 장난스럽게 대꾸했다."
            s3 "아하하! 역시 재밌네."
            return

        "진지하게 대꾸한다":
            "나는 진지하게 대꾸하며 고기에 더 집중했다."
            s3 "앗, 미안! 그냥 농담이었어. (웃음)"
            return

    "잠시 후, 학생 2가 내게 쌈을 싸서 내밀었다."

    menu:
        "쌈을 받아 먹는다":
            "나는 학생 2가 준 쌈을 맛있게 먹었다."
            s2 "맛있지? 더 줄까?"
            "나는 고기를 학생 2의 접시에 올려주며 고마움을 표했다."
            return

        "거절한다":
            "나는 쌈을 거절하고 고기를 굽는 데 집중했다."
            return

    "바비큐가 마무리되고, 우리는 술을 마시며 게임을 시작했다."

    if affection_1 >= 10:
        "학생 1이 편의점에 가서 아이스크림과 숙취 해소제를 사왔다."
        s1 "우리 잠깐 맥주 한 잔 더 하고 들어갈까요?"
        menu:
            "같이 간다":
                "나는 학생 1과 함께 맥주를 마시며 대화를 나누었다."
                "학생 1의 다양한 이야기를 들으며 더 가까워진 느낌이었다."
                return

            "거절한다":
                "나는 잠시 쉬고 싶다며 숙소로 돌아갔다."
                return

    "밤이 되자, 우리는 해변으로 산책을 나섰다."
    "술에 취한 학생 2가 걸려 넘어질 뻔했다."

    menu:
        "학생 2를 잡아준다":
            "나는 학생 2를 잡아주었다."
            s2 "고마워. 덕분에 안 넘어졌어. (미소)"
            return

        "모른 척 지나간다":
            "나는 그냥 지나쳤다. 아무 일도 없었던 것처럼 산책은 계속되었다."
            return

    "불꽃놀이를 하기로 했다."
    s3 "우리 바닷가 근처에서 더 해보는 거 어때?"

    menu:
        "좋아요":
            "나는 학생 3과 함께 바닷가 근처에서 불꽃놀이를 즐겼다."
            s3 "우와, 정말 예쁘다!"
            return

        "싫어요":
            "나는 다른 사람들과 함께 불꽃놀이를 마무리했다."
            return

    "불꽃놀이 후, 우리는 숙소로 돌아가 잠을 잤다."
    "다음 날 아침, 우리는 학교로 돌아가는 버스에 올랐다."

    return

label chapter2_end:
    $ chapter2_cleared = True  # 챕터 2 완료 상태 설정
    call screen chapter_select
    return
