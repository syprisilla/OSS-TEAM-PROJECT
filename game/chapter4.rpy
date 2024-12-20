define p = Character(" ")

image festival_ready = "background/festival_ready.jpg"
image festival_enjoy = "background/festival_enjoy.jpg"
image festival_merrygoround = "background/festival_merrygoround.jpg"
image festival_concert = "background/festival_concert.jpg"
image select_chanmi = "background/select_chanmi.png"
image select_ari = "background/select_ari.png"
image select_sena = "background/select_sena.png"


label chapter4:
    $ load_game_state()
    $ sync_player_name()

    play music "audio/CR5_Sugary_Love_FULL_End.ogg"

    show festival_ready with fade
    p "캠퍼스는 축제 준비로 북적이고 있었다. 학과 부스도 점점 모양을 갖춰가고 있다."

    p"[player_name]은 학교에 일찍 도착해 축제 준비를 구경하고 있었다."
    show chanmi at right 
    "[player_name]""어? 뭐야 찬미 누나 안녕?"
    c"어 [player_name] 일찍 왔네. 안녕~~"
    "[player_name]""누나 축제 부스도 운영했었어? 몰랐네.."
    c "어 맞아 맞아 말 안했던가.."
    c"마침 잘 왔다 일손이 부족한데 여기 좀 도와줄래..?"

    menu:
        c"마침 잘왔다 일손이 부족한데 여기 좀 도와줄래..?{fast}"
        "도와준다":
            "[player_name]" "당근이지 맡겨만 두라고!"
            hide chanmi
            show chanmi_happy at right with dissolve
            $ chanmi.increase_affection(15)
            c"ㅋㅋㅋㅋㅋㅋㅋ 그래그래 고맙네"
            "[player_name]""그러면 난 뭐를 도와주면 되는데??"
            hide chanmi_happy
            show chanmi at right
            c"음.. 이리 와서 이거 한 번만 봐주라"
            c"여기 장식품 좀 더 붙이려 하는데 네가 보기엔 어디에 붙이는 게 더 나을까?"

            menu:
                c"여기 장식품 좀 더 붙이려 하는데 네가 보기엔 어디에 붙이는 게 더 나을까?{fast}"
                "중앙에 붙인다":
                    "[player_name]" "중앙에 붙이는 게 더 눈에 띄겠지?"
                    c"역시 네 눈썰미는 믿을만해. 좋았어, 그렇게 하자."
            
                "가장자리에 붙인다":
                    "[player_name]""가장자리에 붙이는 게 더 깔끔해 보일 것 같아."
                    c "음, 그렇게 하면 전체적으로 조화롭겠네. 좋은 생각이야."
                
                "장식품이 여기 있네..":
                    "[player_name]""어 뭐야 이미 장식품이 부스 안에 있는데?"
                    c"어?? 무슨 소리야?"
                    "[player_name]""누나가 장식품 아니냐고 ㅋ"
                    "[player_name]""장식품이 이미 충분해서 안붙여도 되겠는데?"
                    hide chanmi
                    show chanmi_happy at right with dissolve
                    $ chanmi.increase_affection(15)
                    p"찬미의 볼이 붉게 물들었다."
                    c"아니 ㅋㅋㅋ 뭐라는 거야"
                    hide chanmi_happy
                    show chanmi at right
                    c"그래서 장난치지 말고 어디에 붙일까?"
                    menu:
                        c"그래서 장난치지 말고 어디에 붙일까?{fast}"
                        "중앙에 붙인다":
                            "[player_name]" "중앙에 붙이는게 더 눈에 띄겠지?"
                            c"역시 네 눈썰미는 믿을만해. 좋았어, 그렇게 하자."
            
                        "가장자리에 붙인다":
                            "[player_name]""가장자리에 붙이는 게 더 깔끔해 보일 것 같아."
                            c "음, 그렇게 하면 전체적으로 조화롭겠네. 좋은 생각이야."

            "[player_name]" "우리는 장식물을 붙이면서 대화를 이어갔다. 찬미 누나 손놀림은 항상 빠랐고 동시에 깔끔했다."

            c "그런데, 있잖아... 너는 축제 끝나고 뭐 할 계획 있어?"

            menu:
                c "그런데, 있잖아... 너는 축제 끝나고 뭐 할 계획 있어?{fast}"
                "뭐 특별한 계획은 없어":
                    "[player_name]" "별다른 계획은 없어. 아마 돌아가서 쉬지 않을까?"
                    c "그럼 나랑 같이 술 마실래? 축제 준비한 사람끼리 모이는 자리 있는데, 너도 왔으면 좋겠어."
                    "[player_name]""어 근데, 내가 그 자리에 껴도 되는 거 맞아??"
                    c"응응! 상관없어 아까 우리 부스 사람들이 너 부르라고 하더라"
                    "[player_name]""그래? 그럼 좋아! 이따 끝나고 연락해!"
                    hide chanmi
                    show chanmi_happy at right with dissolve
                    $ chanmi.increase_affection(10)
                    c"알았어~ 이따 보자"
            
                "혼자 시간을 보내고 싶어":
                    "[player_name]" "아마 혼자 있을 것 같아. 이런 때에 혼자만의 시간도 중요하잖아."
                    hide chanmi
                    show chanmi_sad at left with dissolve
                    $ chanmi.decrease_affection(10)
                    c "같이 술 마시자고 하려 했는데.. 알았어..."

        "거절한다":
            "[player_name]""미안, 지금은 좀 어려울 것 같아. 다른 일이 있어서."
            hide chanmi
            show chanmi_sad at left with dissolve
            $ chanmi.decrease_affection(10)
            c "아, 알았어. 괜찮아. 내가 조금 더 힘내면 되겠지.."

        "도망간다":
            p"[player_name]이(가) 전화를 받는척하며 어딘가로 달려간다"
            c"?"
            hide chanmi
            show chanmi_sad at left with dissolve
            $ chanmi.decrease_affection(10)
            "[player_name]""후,, 따돌렸나.. 귀찮게 뭘 도와줘 쯧"

    show festival_enjoy with fade
    p"축제가 본격적으로 시작되었다." 
    p"사람들이 하나둘 축제 현장으로 모여들기 시작했다."
    
    "[player_name]""와.. 사람들 왜 이렇게 많아.."
    "[player_name]" "나도 한번 본격적으로 축제를 즐겨볼까? 후훗"
    "[player_name]" "바로 소개팅부터 조져야겠다.."
    p"[player_name]은(는) 소개팅 부스에 인스타 아이디를 적고 돌아왔다."
    "[player_name]" "빨리 연락이 왔으면 좋겠다~~~ 다른 곳도 좀 둘러볼까~"
    "[player_name]은(는) 다른 부스들을 둘러보다가 아리와 마주쳤다"
    show ari at left
    a"어 안녕? 너 축제 구경 중이었구나?"
    "[player_name]""어어 나도 대학생이니까 한번 경험은 해보고 싶었어 ㅎㅎ"
    a "그치, 저기 먹거리 부스 엄청 많던데 같이 돌아볼래?"
    menu:
        a "그치, 저기 먹거리 부스 엄청 많던데 같이 돌아볼래?{fast}"
        "좋아":
            "[player_name]" "좋아! 그럼 뭐 먹어볼래?"
            hide ari
            show ari_happy at left with dissolve
            $ ari.increase_affection(10)
            a "저기 봐봐, 핫도그도 있고, 떡볶이도 있고... 음, 난 저 와플이 좀 끌리는데!"
            menu:
                a "저기 봐봐, 핫도그도 있고, 떡볶이도 있고... 음, 난 저 와플이 좀 끌리는데!{fast}"
                "와플 먹자고 한다":
                    $ ari.increase_affection(10)
                    "[player_name]" "와플 좋아~ 같이 먹자."
                    a"좋아! 나는 딸기 크림 얹은 걸로 할래. 너는?"
                    "[player_name]" "나는 초코 소스 잔뜩 얹은 걸로 할게."
                    a "역시 너도 단 걸 좋아하네! 이렇게 같이 먹으니까 더 맛있는 것 같아."
                    "[player_name]""맛있누~~"
                    hide ari_happy
                    show ari at left with dissolve
                "떡볶이를 추천한다":
                    "[player_name]" "와플도 좋지만, 떡볶이 한번 먹어볼래? 저기 줄 서 있는 거 보니까 엄청 인기 많아 보여."
                    hide ari_happy
                    show ari at left with dissolve
                    c "그것도 좋지! 매운 거 잘 먹는 편이야?"
                    "[player_name]" "응, 매운 거 좋아해. 같이 먹으면 더 맛있을 거야."
                    c "그럼 얼른 가자! 네가 추천해준 거니까 더 기대된다."
                "핫도그를 추천한다":
                    "[player_name]" "와플도 좋지만, 핫도그 한번 먹어볼래? 저기 줄 서 있는 거 보니까 엄청 인기 많아 보여."
                    hide ari_happy
                    show ari at left with dissolve
                    c "그것도 좋지! 나 핫도그 좋아한다룡~"
                    "[player_name]" "아 진짜?? 나도 좋아한다능"
                    c "그럼 얼른 가자! 네가 추천해 준 거니까 더 기대된다."
            p"둘은 음식을 맛있게 먹고 서로 할 것을 하러 갔다."

        "거절한다":
            "[player_name]" "미안, 지금은 별로 배가 안 고파서.. (배고픔)"
            c "아, 그래?? 알았어.."
            p"[player_name]은(는) 아리를 버리고 빠르게 도망갔다."

    hide ari
            
    p"혼자 축제를 둘러보던 중.."
    show sena at right
    "[player_name]""오!! 세나야 안녕 방가방가"
    s"어!!!! 여기서 만나네"
    s"나 마침 하고 싶은 거 있는데 같이할래??"
    "[player_name]""어? 뭔데~??"
    s"같이 회전목마 타러 갈래? 축제 오면 이런 건 꼭 해야지!"
    menu:
        s"같이 회전목마 타러 갈래? 축제 오면 이런 건 꼭 해야지!{fast}"
        "좋아":
            "[player_name]" "그래, 회전목마 국룰이지~~"
            hide sena
            show sena_happy at right with dissolve
            $ sena.increase_affection(10)
            s"그치 그치! 뭘 아는군~! 나랑 타면 더 재밌어질걸?"
            show festival_merrygoround with fade
            show sena at right
            menu:
                s"그치 그치! 뭘 아는군~! 나랑 타면 더 재밌어질걸?{fast}"
                "너랑 타니까 더 즐거워.":
                    "[player_name]""응, 너랑 타니까 더 즐거워."
                    show sena_happy at right with dissolve
                    $ sena.increase_affection(15)
                    s "진짜? 헤헤 갑자기 기분이 좋아지는구먼~~!"
                "조금 어색하지만 네 덕분에 괜찮아.":
                    "[player_name]" "좀 어색하지만 네가 리드해주니까 괜찮아."
                    s "역시 내가 다 이끌어줘야지! 앞으로도 따라와~"
        "괜찮아":
            "[player_name]" "노노노노, 네가 다른 친구랑 타는 게 더 좋을 것 같아."
            hide sena
            show sena_sad at left with dissolve
            $ sena.decrease_affection(10)
            s "ㅋㅋㅋㅋ 나도 너랑 타기 싫었어 ㅅㄱ~"

    p"[player_name]은(는) 이후 쓸쓸하게 걸어 다니며 연애하고 싶다고 생각하고 있었다."
    "[player_name]" "드디어 축제 마지막 꽃인 콘서트다. 대학 축제를 마무리하는 대규모 콘서트가 열린다는데..."
    "[player_name]""나도 콘서트나 보러 가볼까.. 근데 혼자 보기는 싫은데 한번 같이 보자고 해볼까?"
    "[player_name]" "누구와 함께 이 특별한 밤을 보낼지 고민된다. 아니면 그냥 혼자 즐길까?"

    jump concert_decision

label concert_decision:
    menu:
        "찬미와 함께 가기로 한다" if chanmi_affection >= 70:
            jump concert_with_chanmi

        "세나와 함께 가기로 한다" if sena_affection >= 70:
            jump concert_with_sena

        "아리와 함께 가기로 한다" if ari_affection >= 70:
            jump concert_with_ari

        "혼자 콘서트를 보러 간다":
            jump solo_ending

label concert_with_chanmi:
    show select_chanmi with fade
    c "와, 진짜 왔구나! 역시 너는 내가 믿는 대로야!"
    c "이 콘서트, 정말 엄청난 거 알아? 오늘을 얼마나 기다렸는지 몰라. 내가 너랑 함께 오고 싶어서 얼마나 고민했는지 알아?"
    "[player_name]" "찬미는 항상 밝고 활기찬 모습이지만, 지금은 그 어느 때보다 더 기뻐 보인다."
    c "사실... 내가 이렇게 열정적인 거 너도 알잖아. 근데 오늘은 특히 더 기분이 좋아. 너랑 같이 있으니까."
    "[player_name]" "찬미가 나를 보며 활짝 웃는 모습에 나도 모르게 미소가 번진다. 이 순간은 정말 잊지 못할 것 같다."
    c "봐봐, 다음 곡이 내가 제일 좋아하는 노래야. 이 노래 나올 때 다들 엄청난 에너지를 보여줘. 나랑 같이 뛰자!"
    c "약속해. 오늘, 이 밤은 우리 둘만의 기억으로 남길 거야."
    "[player_name]" "그녀와 함께 춤추며 밤이 깊어진다. 그리고 우리는 축제의 마지막 밤을 누구보다도 뜨겁게 즐겼다."
    jump chapter4_end

label concert_with_sena:
    show select_sena with fade
    s "이렇게 와줘서 정말 고마워. 사실 나 혼자 오기에는 조금 두려웠거든."
    s "이 콘서트, 노래 하나하나가 정말 감동적일 거라고 들었어. 하지만 그 감동을 혼자 느끼는 건 싫더라고."
    "[player_name]" "세나는 조용한 목소리로 말하면서도 눈에는 설렘이 가득 담겨 있었다."
    s "오늘 하루, 정말 특별했으면 좋겠어. 너와 함께하는 마지막 순간이 이렇게 아름답게 기억될 수 있도록..."
    "[player_name]" "그녀의 말에 무심코 고개를 끄덕였다. 세나와 함께라면 그 어떤 노래도 특별할 것 같다."
    s "저기, 다음 곡은 내가 정말 좋아하는 곡이야. 가사도 멜로디도 내 마음을 꼭 닮은 것 같아서 들을 때마다 마음이 흔들리곤 해."
    s "너랑 같이 들으면 더 특별할 것 같아. 그냥... 너랑 공유하고 싶은 느낌이야."
    "[player_name]" "공연이 끝나갈 무렵, 세나는 내 쪽으로 고개를 돌려 작은 목소리로 말했다."
    s "오늘의 이 감정... 절대 잊지 않을 거야. 너도, 나도."
    "[player_name]" "그녀의 손길이 살짝 닿은 순간, 이 밤이 우리의 마음속 깊이 새겨질 것임을 느낄 수 있었다."
    jump chapter4_end

label concert_with_ari:
    show select_ari with fade
    a "음, 생각보다 시끄럽지는 않네. 나쁘지 않아."
    "[player_name]" "아리는 평소와 같은 차분한 목소리였지만, 약간 긴장한 듯 보였다."
    a "솔직히 말해서, 나는 이런 축제에 큰 기대를 하지 않았어. 하지만 너랑 있다면 좀 다르겠지, 싶었어."
    a "그래서... 네가 나와 같이 와준 게 정말 고마워. 내가 원래는 이런 말 잘 안 하는 거 알지? 그러니까 더 의미 있게 받아들여 줘."
    "[player_name]" "그녀는 말끝마다 조금씩 망설였지만, 그 진심은 분명히 전해졌다."
    a "아, 저 곡. 저 곡은 가사가 정말 아름다워. 들을 때마다 가슴 깊이 울려. 너도 들어봤으면 좋겠다."
    a "너도 그 감정을 느꼈으면 좋겠어. 이런 걸 나 혼자 느끼는 건 아깝잖아."
    "[player_name]" "아리의 눈빛이 반짝였다. 그녀가 음악에 몰입하는 모습을 보며 나도 점점 빠져들었다."
    a "오늘의 이 시간은... 나에게 정말 의미 있는 순간이 될 거야. 네가 있어서 가능했어. 고마워."
    "[player_name]" "그녀와 함께 조용히 공연장을 빠져나오며, 나는 그녀가 말하지 않아도 전해지는 감정을 느꼈다."
    jump chapter4_end

label solo_ending:
    show festival_concert with fade
    "[player_name]" "혼자 콘서트를 보러 온 건 처음이었다. 공연장은 활기찼지만, 나의 마음은 조금 공허했다."
    "[player_name]" "사람들은 저마다 소중한 사람과 함께 웃고, 떠들고, 노래를 즐기고 있었다. 그런 모습을 보니 조금 부럽기도 했다."
    "[player_name]" "하지만 이 밤, 이 음악을 혼자라도 온전히 즐기기로 했다. 축제의 마지막 밤은 나만의 방식으로 특별하게 만들어야지."
    "[player_name]" "마지막 곡이 울려 퍼질 때, 나는 문득 고개를 들어 밤하늘을 바라봤다. 별빛이 반짝이는 하늘 아래, 나 혼자지만 외롭지 않았다."
    "[player_name]" "이 순간은 나 자신에게 주는 선물이다. 그리고 다음에는, 이 축제를 함께 나눌 누군가를 찾을 수 있을지도 모른다."
    jump chapter4_end

    return

label chapter4_end:
    window hide
    $ quick_menu = False
    call credits
    return