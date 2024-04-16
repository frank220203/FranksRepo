def solution(
        bandage:list,
        health:int,
        attacks:list
) -> int :
    """ 프로그래머스 코딩 테스트 Lv 1. 붕대 감기
    
    """
    print('\n\n\n  메소드 시작')
    answer = 0
    heal_amount = 0
    max_health = health
    last_attack = attacks[-1][0] + 1
    monster = {e[0]:e[1] for e in attacks}
    success = 0
    print_success_event = success
    print_heal_event = "+0"
    for e in range(last_attack):
        if health < 0 : break
        monster_attack = True if monster.get(e) is not None else False
        if monster_attack:
            health -= monster.get(e)
            success = 0
            print_heal_event = "-" + str(monster.get(e))
            print_success_event = success
        else:
            if e > 0 : success += 1

            if success == bandage[0] :
                heal_amount = bandage[1] + bandage[2]
                print_success_event = success
                success = 0
            elif e > 0 and health < max_health :
                heal_amount = bandage[1]
            else : heal_amount = 0

            if health < max_health:
                health += heal_amount
                if health > max_health : health = max_health
                print_heal_event = "+" + str(heal_amount)

            print_success_event = success
        print(f"시간 : {e}, 현재 체력(변화량) : {health}({print_heal_event}), 연속 성공 : {print_success_event}, 몬스터 공격 : {monster_attack}")
    
    if health <= 0 :
        answer = -1
    else :
        answer = health
    
    print(f"캐릭터 체력 : {answer}")

    return answer

bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
solution(bandage=bandage, health=health, attacks=attacks)

bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]
solution(bandage=bandage, health=health, attacks=attacks)

bandage = [4, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]
solution(bandage=bandage, health=health, attacks=attacks)

bandage = [1, 1, 1]
health = 5
attacks = [[1, 2], [3, 2]]
solution(bandage=bandage, health=health, attacks=attacks)

bandage = [2, 4, 4]
health = 100
attacks = [[1, 96], [18, 1]]
solution(bandage=bandage, health=health, attacks=attacks)