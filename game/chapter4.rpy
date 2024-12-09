define p = Character(" ")

label chapter4:
    $ load_game_state()
    $ sync_player_name()

    p "캠퍼스는 축제 준비로 북적이고 있었다. 학과 부스도 점점 모양을 갖춰가고 있다."

    p"[player_name]은 학교에 일찍 도착해 축제 준비를 구경하고 있었다."

    "[player_name]""어? 뭐야 찬미누나 안녕?"
    c"어 [player_name] 일찍왔네 안녕~~"
    "[player_name]""누나 축제부스도 운영했었어? 몰랐네.."
    c "어 맞아맞아 말 안했던가.."
    c"아무튼 잘왔다 여기좀 도와줄래..? 일손이 부족한데.."

    menu:
        "도와준다":
            $ chanmi.increase_affection(5)
            p "그래, 나도 축제 준비에 한몫하고 싶어."
        
            scene booth_preparation
            with fade
        
            e "여기 장식품 좀 더 붙이려 하는데, 네가 보기엔 어디에 붙이는 게 더 나을까?"

            menu:
                "중앙에 붙인다":
                    $ affection_e += 5
                    p "중앙에 붙이는 게 더 눈에 띄겠지?"
                    e "역시 네 눈썰미는 믿을만해. 좋았어, 그렇게 하자."
            
                "가장자리에 붙인다":
                    p "가장자리에 붙이는 게 더 깔끔해 보일 것 같아."
                    e "음, 그렇게 하면 전체적으로 조화롭겠네. 좋은 생각이야."

            p "우리는 장식물을 붙이면서 대화를 이어갔다. 그녀의 손놀림은 항상 빠르고 정돈되어 있었다."

            e "그런데, 있잖아... 너는 축제 끝나고 뭐 할 계획 있어?"

            menu:
                "뭐 특별한 계획은 없어":
                    p "별다른 계획은 없어. 그냥 좀 쉬려고."
                    e "그럼 나랑 같이 저녁 먹으러 갈래? 축제 준비한 팀끼리 모이는 자리 있는데, 너도 왔으면 좋겠어."
                    $ affection_e += 10
            
                "혼자 시간을 보내고 싶어":
                    p "아마 혼자 있을 것 같아. 이런 때에 혼자만의 시간도 중요하잖아."
                    e "음... 알았어. 그래도, 네가 와줬으면 좋겠다고 생각했어."
                    $ affection_e -= 5

        "거절한다":
            $ affection_e -= 5
            p "미안, 지금은 좀 어려울 것 같아. 다른 일이 있어서."
            e "아, 알았어. 괜찮아. 다른 사람에게 부탁해볼게."

    # 학생 3 이벤트
    if affection_m >= 50:
        m "같이 회전목마 타러 갈래요? 축제 오면 이런 건 꼭 해야지!"
        menu:
            "좋아":
                $ affection_m += 10
                p "그래, 좋아."
                m "생각보다 너 이런 거 좋아하네. 나랑 있으면 더 재밌어질걸?"
                menu:
                    "너랑 있으니까 더 즐거워.":
                        $ affection_m += 5
                        p "응, 너랑 있으니까 더 즐거워."
                        m "진짜? 너 이런 말도 할 줄 아는구나. 생각보다 재밌는 사람이네!"
                    "조금 어색하지만 네 덕분에 괜찮아.":
                        p "좀 어색하지만 네가 리드해주니까 괜찮아."
                        m "역시 내가 다 이끌어줘야지! 앞으로도 따라와~"
            "괜찮아":
                p "음, 나는 괜찮아. 네가 다른 친구랑 타는 게 더 좋을 것 같아."
                m "알았어. 아쉬운걸?"
    else:
        p "학생 3은 친구들과 즐겁게 시간을 보내고 있었다. 나는 그냥 걸어갔다."

    # 학생 2 이벤트
    if affection_c >= 50:
        c "여기 자리 잡았어요! 같이 봐요."
        menu:
            "같이 본다":
                $ affection_c += 10
                p "그래, 고마워. 여기 괜찮아 보이네."
                c "너랑 이렇게 앉아 있으니까 편안하다. 이런 경험은 처음이야."
                menu:
                    "넌 지금도 충분히 너다워. 걱정하지 마.":
                        $ affection_c += 5
                        p "넌 지금도 충분히 너다워. 걱정하지 마."
                        c "고마워. 너랑 이야기하면 항상 마음이 편해."
                    "너 자신을 위해 더 많은 시간을 써봐.":
                        p "너 자신을 위해 시간을 더 써봐. 너도 즐겨야지."
                        c "맞아, 그게 필요한 것 같아."
            "거절한다":
                p "미안, 나는 다른 데 가볼게."
                c "괜찮아요. 다음에 이야기하죠."
    else:
        p "학생 2는 조용히 공연을 보고 있었다. 나는 다른 곳으로 갔다."

    # 불꽃놀이 (최종 엔딩 결정)
    scene fireworks_night
    with fade

    p "축제의 하이라이트인 불꽃놀이가 시작되었다. 나는 하늘을 올려다보며 생각에 잠겼다."

    if affection_e >= 70:
        e "여기 앉아서 같이 볼래요?"
        p "그래, 그러자."
        e "사실 너랑 있으면 조금 더 나 자신을 믿게 돼. 네가 정말 고마워."
        menu:
            "나도 너랑 함께하고 싶어.":
                p "나도 너랑 더 많은 시간을 보내고 싶어."
                e "정말? 그럼 앞으로도 나와 함께해줄 거지?"
                return
            "우린 친구로 남는 게 좋을 것 같아.":
                p "미안, 그냥 친구로 남는 게 좋을 것 같아."
                e "그렇구나... 그래도 고마워. 좋은 친구가 되어줄게."
                return
    elif affection_m >= 70:
        m "우리 더 가까이 가서 볼까? 너랑 있으면 진짜 좋아."
        menu:
            "나도 네가 좋아.":
                p "나도 네가 좋아. 이런 순간이 계속되면 좋겠어."
                m "역시 나의 센스는 통한다니까! 앞으로도 재밌게 지내자!"
                return
            "우린 친구로 남자.":
                p "미안, 우린 친구로 남는 게 좋을 것 같아."
                m "알겠어. 그래도 너랑 친구로 남아도 행복할 거야."
                return
    elif affection_c >= 70:
        c "조용한 곳에서 같이 볼래요?"
        p "그래, 그게 좋을 것 같아."
        c "너랑 있으니까 모든 게 더 특별해. 나 정말 많이 의지하고 싶어."
        menu:
            "그럴 수 있다면 나도 행복해.":
                p "너랑 같이라면 나도 행복할 것 같아."
                c "정말 고마워. 앞으로 잘 부탁해요."
                return
            "우리 관계는 지금이 좋아.":
                p "우리 관계는 지금이 좋아. 부담 없이 지내고 싶어."
                c "그렇구나... 그래도 고마워. 친구로 남아줘."
                return
    else:
        # 솔로 엔딩
        p "나는 혼자서 불꽃놀이를 보았다. 이번 학기는 나 자신에 대해 많이 배운 시간이었다."
        p "다음번에는 더 나은 내가 될 수 있을 거야. 그리고 그때는, 누군가와 함께일지도 모르지."
        return
    jump chapter4_end

    return

label chapter4_end:
    "플레이 해주셔서 감사합니다!!"
    
    return