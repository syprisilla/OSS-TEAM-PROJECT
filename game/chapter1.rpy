define p = Character(" ")
# define s1 = Character("학생 1")
# define s2 = Character("학생 2")
# define s3 = Character("학생 3")
define prof = Character("김봉재 교수님")

label chapter1:

    # 강의실에 들어서며 시나리오 시작
    scene classroom with fade
    "[player_name]" "벌써 방학이 끝났다니ㅠㅠ 드디어 2학기 시작이다"
    "[player_name]" "2학기에는 연애하고 싶은데 할 수 있을까?"
    p "설레는 마음으로 강의실에 들어간다."
    p "앞자리에 학생 1이 앉아 있고, 뒷자리에 학생 2가 앉아 있다."
    "[player_name]" "벌써부터 자리가 꽉 차있네 사람없는 중간 자리에 앉아야 되겠다"
    
    # 학생 3과의 상호작용
    s "안녕! 여기 앉아도 돼?"
    
    menu:
        "인사를 받아준다":
            "[player_name]" "그래, 앉아."
            s "고마워! 방학 잘 지냈어?" 
            $ s3_affection += 1 # 호감도 상승
            "[player_name]" "응, 잘 보냈어. 너는 어땠어?"
            s "나도, 나름대로 재밌게 지냈어! 다음 방학에 같이 어디 놀러 갈래?" 
            "[player_name]" "나야 좋지, 담에 같이 놀러 가자!"
        "인사를 받아주지 않는다":
            "[player_name]" "내 옆에 자리 있어가지고.."
            s "아, 그래... 알겠어." 
            $ s3_affection -= 1 # 호감도 하락
            s "뒷자리로 가야겠다." 
            
    # 교수님 등장
    p "강의실에 교수님이 들어온다."
    prof "여러분, 방학 잘 보내셨나요? 오늘은 학기의 첫날인 만큼 간단히 앞으로의 수업 계획을 설명드리고, 조별 과제를 배정하도록 하겠습니다"
    "[player_name]" "아니, 첫날부터 조별과제라니... 너무 빡센 거 아냐? 방학 끝난 지 얼마나 됐다고ㅠㅠ"
    prof "여러분, 조별 과제는 학기 중에 진행될 주요 프로젝트입니다. 과제의 주제는 '앱 개발'이고, 조는 제가 랜덤으로 정할게요."
    prof "물론 부담스러울 수 있다는 걸 압니다만, 이번 과제를 통해 여러분이 실력을 쌓고 서로 협력하는 기회를 얻길 기대합니다."
    p "제비뽑기를 통해 조가 정해졌고, 같은 조원은 [c],[a],[s]이었다."
    "[player_name]" "(어떤 사람들이랑 한 조가 될지 긴장됐는데... 조가 나쁘지 않아서 다행이다.)"
    c "안녕! 같은 조가 됐네. 난 [c]이야. 앞으로 잘 부탁해!"  
    "[player_name]" "응, 잘 부탁해. 난 [player_name]이야."  
    a "난 [a]라고 해. 조별 과제는 솔직히 부담스럽지만... 다들 화이팅 해보자ㅎㅎ" 
    s "와, 팀 분위기 좋은데? 난 [s]! 힘든 과제라도 다 같이 하면 재밌을 거야!"  
    # 조 주제 결정
    c "우리 어떤 앱을 만들지 주제를 정해야 하는데, 다들 좋은 아이디어 있어?"
    c "나는 게임 앱을 개발하는 게 좋을 것 같아. 그렇게 복잡하지도 않고, 잘 할 수 있을 것 같거든."
    a "나는 파트 타임 스터디 같은 공부 시간 기록 앱을 생각해 봤어."
    s "이 주제는 어때? 언제 몇 번 빠졌는지 체크해주는 출석부 앱이야."
    
    menu:
        "여학생들의 의견을 따른다":
            "[player_name]" "우와 다들 아이디어가 넘치네"
            $ final_topic = "여학생들이 선택한 주제"
        "다른 의견을 낸다":
            p "내가 생각하기에는 다른 게 더 좋아 보여."
            $ final_topic = "내가 제안한 주제"

    # 팀 해산 후, 채팅
    p "그날 밤, 단체 채팅방에서 PPT와 관련된 이야기를 나누기로 했다."
    c "어떻게 해야 할지 모르겠어요. 도와줄 수 있나요?"

    menu:
        "좋다":
            p "알겠어. 내가 도와줄게."
            c "정말 고마워요!" 
            $ s1_affection += 1 # 호감도 상승
        "싫다":
            p "미안, 지금은 바빠."
            c "아, 알겠어요..." 
            $ s1_affection -= 1 # 호감도 하락

    # 발표 연습
    p "발표자는 제비뽑기로 정하기로 했고, 나와 학생 2가 발표자로 뽑혔다."
    p "발표 연습 중, 학생 2가 제안했다."
    a "여기 부분은 이렇게 하는 게 어때요?"
    
    menu:
        "제안을 받아들인다":
            p "좋은 생각이야."
            a "고마워! 같이 더 완벽히 만들자." 
            $ s2_affection += 1 # 호감도 상승
        "제안을 거절한다":
            p "내 생각엔 그냥 이렇게 하는 게 나아."
            a "아, 알겠어..." 
            $ s2_affection -= 1 # 호감도 하락

    # 발표 성공
    p "발표는 성공적으로 마무리되었고, 교수님께 좋은 평가를 받았다."
    prof "잘했어요! 여러분 팀워크가 돋보였어요."

    p "이렇게 Chapter 1이 끝났다."
    
    return
