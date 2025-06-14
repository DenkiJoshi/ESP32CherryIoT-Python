# 関数宣言
import random 


ELEMENT_SYMBOLS ={
    '火': '$',
    '水': '~',
    '風': '@',
    '土': '#',
    '命': '&',
    '無': ' '
}
ELEMENT_COLORS={
    '火': '41',
    '水': '44',
    '風': '42',
    '土': '43',
    '命': '45',
    '無': '47'
}


# 行が自分、列が相手
# '火', '水', '風', '土', 
ELEMENT_BOOST = [
    [1,   0.5, 2,   1], # 火
    [2,   1,   1,  0.5], # 水
    [0.5, 1,   1,   2], # 風
    [1,   2,   0.5, 1]  # 土
]


GEM_ELEMENT = ['火', '水', '風', '土', '命'] 
COMMAND = "ABCDEFGHIJKLMN"

def print_monster_name(monster):
    global ELEMENT_SYMBOLS, ELEMENT_COLORS
    element = monster['element']
    symbol = ELEMENT_SYMBOLS[element]
    color = ELEMENT_COLORS[element]

    print(f'\033[{color}m{symbol}{monster["name"]}{symbol}\033[0m', end='')

    
    
def main():
    player_name = input('プレイヤー名を入力してください>>')
    if player_name == '':
        print('エラー:プレイヤー名を入力してください。')
    else:
        print('### Puzzle & Monsters ###')
        # 敵モンスター
        slime = {'name':'スライム', 'hp':100, 'max_hp':100, 'element':'水', 'ap':10, 'dp':1}
        goblin = {'name':'ゴブリン', 'hp':200, 'max_hp':200, 'element':'土', 'ap':20, 'dp':5}
        big_bat = {'name':'オオコウモリ', 'hp':300, 'max_hp':300, 'element':'風', 'ap':30, 'dp':10}
        wolf = {'name':'ウェアウルフ', 'hp':400, 'max_hp':400, 'element':'風', 'ap':40, 'dp':15}
        dragon = {'name':'ドラゴン', 'hp':600, 'max_hp':600, 'element':'火', 'ap':50, 'dp':20}

        #味方モンスター
        suzaku ={'name':'朱雀', 'hp':150, 'max_hp':150, 'element':'火', 'ap':25, 'dp':10}
        seiryu ={'name':'青龍', 'hp':150, 'max_hp':150, 'element':'風', 'ap':15, 'dp':10}
        byakko ={'name':'白虎', 'hp':150, 'max_hp':150, 'element':'土', 'ap':20, 'dp':5}
        genbu ={'name':'玄武', 'hp':150, 'max_hp':150, 'element':'水', 'ap':20, 'dp':15}

        # global slime,goblin, big_bat,wolf, dragon
        enemies =[slime, goblin, big_bat, wolf, dragon]
        # global suzaku, seiryu, byakko, genbu
        friends =[suzaku, seiryu, byakko, genbu]
        party = organize_party(player_name,friends)
        number = go_dungeon(party, enemies) 
        if number == 5:
            print('### GAME CLEARED!! ###')
        else:
            print('### GAME OVER!! ###')

        print(f'倒したモンスター数={number}')
        
def organize_party(player_name, friends):
    total_hp = sum([f['hp'] for f in friends])
    dp = [f['dp'] for f in friends]
    dp_avg = sum(dp)/len(friends)
    
    party={'player_name':player_name, 'friends':friends,
          'max_hp':total_hp, 'hp':total_hp, 'dp': dp_avg}
    return party

def show_party(party):
    print('<パーティー編成>----------------')
    
    for friend in party['friends']:
        print_monster_name(friend)
        print(f'HP={friend["hp"]} 攻撃={friend["ap"]} 防御={friend["dp"]}')
    print('-----------------------------')

def go_dungeon(party, enemies):
    
    print(f'{party["player_name"]}のパーティ(HP={party["max_hp"]})はダンジョンに到着した')
    show_party(party)
    # monsters= ['スライム', 'ゴブリン', 'オオコウモリ', 'ウェアウルフ', 'ドラゴン']
    win_flg = 0
    for enemy in enemies:
        # enemy_name = enemy['name']
        win_flg += do_battle(party, enemy)
        if party['hp'] <= 0:
            print(f'{party["player_name"]}はダンジョンから逃げ出しました')
            return win_flg
        else:
            print(f'{party["player_name"]}は更に奥に進んだ')
            print(f'=======================================')
            
    print(f'{party["player_name"]}はダンジョンを制覇した')
    return win_flg


def do_battle(party, enemy):
    enemy_name = enemy['name']
    print_monster_name(enemy)
    print(f'が現れた!')    
    gems = [] # random.choices(list(ELEMENT_SYMBOLS.keys()), k=14)
    gems = list('火水水火土火水')# fill_gems(gems)
    gems = fill_gems(gems)
    battle_field ={
        'enemy': enemy,
        'party': party,
        'gems':gems
    }

    while True:
        on_player_turn(battle_field)
        if enemy['hp'] <= 0:
            break
        print("")
        on_enemy_turn(party, enemy)
        if party['hp'] <= 0:
            print("パーティのHPは０になりました")
            return 0
    
    print_monster_name(enemy)
    print(f'を倒した!')
    
    return 1



def show_battle_field(battle_field):
    print("バトルフィールド")

    enemy = battle_field['enemy']
    party = battle_field['party']
    print_monster_name(enemy)
    print(f"HP = {enemy['hp']} / {enemy['max_hp']}")
    print("    ")
    for f in party['friends']:
        print_monster_name(f)
        print("", end=" ")
    print("")
    
    print(f"HP = {party['hp']} / {party['max_hp']}")
    
    print("-"*20)
    for c in COMMAND:
        print(c, end=" ")
    print("")
    print_gems(battle_field['gems'])
    print("")
    print("-"*20)
    
    
    

def on_player_turn(battle_field):
    
    party, enemy = battle_field['party'], battle_field['enemy']
    print(f"【{party['player_name']}のターン(HP={party['hp']})】")
    
    show_battle_field(battle_field)
    
    command = input("コマンド?>>")
    while not check_valid_command(command):
        print('入力されたコマンドは不適切です')
        command = input("コマンド?>>")
        
    move_gem(command=command, gems=battle_field['gems'])
    
    evaluate_gems(battle_field, command)
    # do_attack(enemy, command)

    

def on_enemy_turn(party, enemy):
    print(f"【{enemy['name']}のターン(HP={enemy['hp']})】")
        
    do_enemy_attack(party, enemy)
        

def fill_gems(gems):
    global ELEMENT_SYMBOLS
    new_gems = gems[:]
    now_gems_len = len(gems)
    required_gems = 14 - now_gems_len
    new_gems += [  random.choice(GEM_ELEMENT) for i in  range(required_gems)]
    
    
    return new_gems



def print_gems(gems):
    gems_with_color_code = [f'\033[{ELEMENT_COLORS[f]}m{ELEMENT_SYMBOLS[f]}\033[0m' for f in gems]
    for i in gems_with_color_code:
        print(i, end=' ')
        
def swap_gems(gems, designated_gem_idx, direction):
    """
    direction:  右なら１、　左なら−１に動かす
    """
    tmp = gems[designated_gem_idx+ direction]
    # print(tmp, designated_gem_idx)
    gems[designated_gem_idx+direction] = gems[designated_gem_idx]
    gems[designated_gem_idx] = tmp
    
def check_valid_command(command):
    """
        正しいコマンドなら　True
        不適切なコマンドなら　False
    """
    if len(command) == 2:
        if command[0] in COMMAND and command[1] in COMMAND and command[0] != command[1]:
            return True
        else:
            return False
    else:
        return False
    
    



def move_gem(command, gems):
    global COMMAND
    start_index = COMMAND.index(command[0])
    end_index = COMMAND.index(command[1])

    # start_index < end_indexと仮定
    if start_index < end_index:
        direc = 1
        num = end_index - start_index
    else:
        direc = -1
        num = start_index - end_index

    print_gems(gems)
    print("")
    print("")


    for i in range(0, num):
        swap_gems(gems,start_index+(i*direc), direction= direc)
        print_gems(gems)
        print("")
        print("")
    # print(COMMAND[start_index+i], COMMAND[start_index+i+1])
    
    
def banish_gems(battle_field, start_idx, end_idx, commbo=1):
    
    element = battle_field['gems'][start_idx]
    for i in range(start_idx, end_idx+1):
        battle_field['gems'][i] = '無'
    print_gems(battle_field['gems'])
    print("")
    
    element_num = end_idx - start_idx
    if element != '命':
        do_attack(element, element_num, battle_field, commbo)
        # do_attack(element, element_num, battle_field, commbo=1)
    else:
        do_recover(battle_field, element_num, commbo)
        
        
def blur_damage(damage_value):
    ten_percent = damage_value*0.1
    return int(random.uniform(damage_value-ten_percent, damage_value+ten_percent))
    
def do_recover(battle_field, element_num, commbo=1):
    value = 20 * 1.5**(element_num - 2 + commbo)
    blur_value = blur_damage(value)
    
    if battle_field['party']['hp'] + blur_value < battle_field['party']['max_hp']:
        print(f'パーティの体力は{blur_value}回復しました {commbo}COMMNO!')
        battle_field['party']['hp'] += blur_value
    else:
        recover_value = battle_field['party']['max_hp']- battle_field['party']['hp']
        print(f'パーティの体力は{recover_value}回復しました {commbo}COMMNO!')
        battle_field['party']['hp'] = battle_field['party']['max_hp']

def do_calc_damage(my_ap, element, element_num, enemy, commbo=1):
    enemy_idx = GEM_ELEMENT.index(enemy['element'])
    my_idx = GEM_ELEMENT.index(element)
    boost = ELEMENT_BOOST[my_idx][enemy_idx]
    damage = (my_ap - enemy['dp']) * boost *(1.5**(element_num - 2 + commbo))
    damage = blur_damage(damage)
    damage =  damage if damage > 0 else 1
    return damage
    
    
def do_attack(element, element_num, battle_field, commbo=1):
    # damage = hash(command) % 50
    enemy = battle_field['enemy']
    party = battle_field['party'] # ['friend']
    try:
        temp_friend = list(filter(lambda x: x['element'] == element, party['friends']))
        friend = temp_friend[0]
    except:
        print(element)
        print(party)
        print(party['friends'])
        print(temp_friend)
    my_ap = friend['ap']
    damage = do_calc_damage(my_ap, element, element_num, enemy, commbo)
    print_monster_name(friend)
    
    
    if commbo == 1:
        print(f"の攻撃!")
    else:
        print(f"の攻撃! {commbo} Commbo!!")
    print(f"敵モンスターに{damage}のダメージを与えた")
    enemy['hp'] -= damage
    if enemy['hp'] <= 0:
        enemy['hp'] = 0
        
        
def do_enemy_attack(party, enemy):
    
    damage = blur_damage(enemy['ap'] - party['dp'])
    if damage <= 0:
        damage = 1
    party['hp'] -= damage
    print_monster_name(enemy)
    print(f"の攻撃でパーティに{damage}のダメージを与えた")
    print(f"")
    if party['hp'] <0:
        party['hp'] = 0

def shift_gems(g, start_idx, end_idx):
    
    if end_idx == 13:
        return g
    
    empty_num = end_idx - start_idx
    
    print_gems(g)
    print("")
    for j in range(empty_num+1):
        
        temp_g = g[:start_idx] + ["無" for i in range(empty_num-j)] + g[end_idx+1:] + ["無" for k in range(j+1)]
        print_gems(temp_g)
        print("")
    return temp_g

def swawn_gems(gems):
    if '無' in gems:
        for i, g in enumerate(gems):
            if g != "無":
                continue
            gems[i] = GEM_ELEMENT[random.randint(0,4)]
        print_gems(gems)
        print("")
        
def evaluate_gems(battle_field, command):
    commbo = 0
    is_waki_turn = False
    while True:
        enemy, party = battle_field['enemy'], battle_field['party']
        gems = battle_field['gems']
        
        
        first_idx, end_idx = check_banishable(gems)    
        if first_idx is not None:
            commbo += 1
            banish_gems(battle_field, first_idx, end_idx, commbo)
            battle_field['gems'] = shift_gems(gems, first_idx, end_idx)
        
        
        else:
            swawn_gems(battle_field['gems'])
            first_idx, end_idx = check_banishable(gems)
            if first_idx is None:
                break
        
        
        
        
    
    

def check_banishable(gems):
    banish_idx = None
    # is_final_gem = False
    for i in range(0,12):
        start_element= gems[i]
        cnt = 0
        
        for j in range(i+1, len(gems)):
            element = gems[j]
            if start_element == element:
                cnt += 1
                if j == 13:
                    j = 14
            else:
                break

        if cnt >= 2:
            banish_idx = i
            break
    if banish_idx is not None:
        banish_element = gems[banish_idx]
        banish_idx = None if banish_element == "無" else banish_idx
    return banish_idx,j-1

main()