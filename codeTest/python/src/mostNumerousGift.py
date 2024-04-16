def solution(
    friends:list,
    gifts:list
) -> int:
    """ 프로그래머스 코딩 테스트 Lv 1. 가장 많이 받은 선물
    
    """
    print('\n\n\n  메소드 시작')
    answer = 0
    friends_encode = {}
    friend_length = len(friends)

    for i, v in enumerate(friends):
        friends_encode[v] = i

    print(f"친구 암호화 : {friends_encode}")
    path_table = [[0 for c in range(friend_length)] for r in range(friend_length)]
    print(f"선물 방향 테이블 : {path_table}")
    gift_path = [v.split(' ') for v in gifts]
    print(f"선물 방향 : {gift_path}")

    for v in gift_path :
        print(f"선물 준 사람 : {v[0]}({friends_encode.get(v[0])})")
        print(f"선물 받은 사람 : {v[1]}({friends_encode.get(v[1])})")
        path_table[friends_encode.get(v[0])][friends_encode.get(v[1])] += 1
        print(f"gift_table[{friends_encode.get(v[0])}][{friends_encode.get(v[1])}] : {path_table[friends_encode.get(v[0])][friends_encode.get(v[1])]}")

    print(f"선물 증정이 끝난 후 테이블 : {path_table}")
    friends_decode = {v:k for k, v in friends_encode.items()}
    print(f"친구 복호화 : {friends_decode}")
    gift_table = [[0 for c in range(3)] for r in range(friend_length)]
    print(f"선물 지수 테이블 : {gift_table}")

    for i,iv in enumerate(path_table) :
        for j,jv in enumerate(iv) :
            gift_table[i][0] += jv
            gift_table[i][1] += path_table[j][i]
        gift_table[i][2] = gift_table[i][0] - gift_table[i][1]
    
    print(f"계산이 끝난 선물 지수 테이블 : {gift_table}")
    predict_table = {v:0 for k, v in friends_encode.items()}
    print(f"예측 테이블 : {predict_table}")

    for i in range(friend_length) :
        for j in range(friend_length) :
            print(f"{friends_decode.get(i)}({i})와 {friends_decode.get(j)}({j}) 선물 수 비교 : {path_table[i][j]} : {path_table[j][i]}")
            if path_table[i][j] > path_table[j][i] :
                predict_table[i] += 1
                print(f"{friends_decode.get(i)}({i})가 선물을 받을 것이라 예측 : {predict_table[i]}")
            elif path_table[i][j] < path_table[j][i] :
                predict_table[j] += 1
                print(f"{friends_decode.get(j)}({j})가 선물을 받을 것이라 예측 : {predict_table[j]}")
            else :
                if gift_table[i][2] > gift_table[j][2] :
                    predict_table[i] += 1
                    print(f"{friends_decode.get(i)}({i})가 선물을 받을 것이라 예측 : {predict_table[i]}")
                elif gift_table[i][2] < gift_table[j][2] :
                    predict_table[j] += 1
                    print(f"{friends_decode.get(j)}({j})가 선물을 받을 것이라 예측 : {predict_table[j]}")

    for i in range(friend_length) :
        predict_table[i] = predict_table.get(i) / 2

    print(f"계산이 끝난 예측 테이블 : {predict_table}")
    answer = int(max(predict_table.values()))
    print(f"다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수 : {answer}")
    print('\n\n\n')

    return answer

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
answer = solution(friends, gifts)

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
answer = solution(friends, gifts)

friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
answer = solution(friends, gifts)