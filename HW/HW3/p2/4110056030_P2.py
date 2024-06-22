import random

class LifeGame:
    def __init__(self):
        self.players = []
        self.gogo = True
        self.current_player_index = 0
        self.is_game_over = False
        self.setup_game()
        self.start_game()
        

    def setup_game(self):
        num_players = int(input("Enter the number of player: "))
        for i in range(num_players):
            player_name = f"Player {i + 1}"
            self.players.append({'name': player_name, 'money': 10000, 'position': 0, 'skip_turn': False})

    def play_turn(self):
        current_player = self.players[self.current_player_index]

        if current_player['skip_turn']:
            print(f"{current_player['name']} 本回合禁止移動")
            current_player['skip_turn'] = False
        else:
            action = input(f"(0.exit 1.骰出道具卡)")

            if action == '0':
                self.is_game_over = True
                self.announce_winner()
                return

            elif action == '1':
                self.use_tool_card(current_player)
                if self.gogo:
                    dice_roll = random.randint(1, 6)
                    print(f"{current_player['name']} 移動 {dice_roll} 步")
                    self.move_player(current_player, dice_roll)
                else:
                    self.gogo = True

            else:
                dice_roll = random.randint(1, 6)
                print(f"{current_player['name']} 移動 {dice_roll} 步")
                self.move_player(current_player, dice_roll)
        print(f"=========={current_player['name']}==========")
        self.print_status(current_player)
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def use_tool_card(self, player):
        player['money'] -= 500
        card = random.choice(["隨機後退", "指定後退", "跳動指定格數", "均貧卡"])
        print(f"{player['name']} 抽到了道具卡: {card}")

        if card == "隨機後退":
            target_player = random.choice(self.players)
            self.move_player(target_player, -3)
            print(f"{target_player['name']}  受到影響,往後3格")

        elif card == "指定後退":
            target_player_index = int(input("指定玩家的編號: ")) - 1
            target_player = self.players[target_player_index]
            self.move_player(target_player, -3)
            print(f"{target_player['name']} 移動 -3 步")

        elif card == "跳動指定格數":
            steps = int(input("跳躍格數:"))
            self.move_player(player, steps)
            print(f"{player['name']} 移動 {steps} 步")
            self.gogo = False

        elif card == "均貧卡":
            target_player_index = int(input("指定玩家的編號: ")) - 1
            target_player = self.players[target_player_index]
            total_money = player['money'] + target_player['money']
            player['money'] = total_money // 2
            target_player['money'] = total_money // 2
            # print(f"{player['name']} 和 {target_player['name']} 均貧後的金額為 {player['money']} 元")

    def move_player(self, player, steps):
        if player['position'] + steps >= 10:
            player['money'] += 5000
            print("繞行一周,得到特別獎金5000元")
        player['position'] = (player['position'] + steps) % 10

        self.trigger_event(player)

    def trigger_event(self, player):
        position = player['position']
        if position == 0:
            player['money'] += 200
            print(f"中發票+200元")
        elif position == 1:
            player['money'] -= 200
            print(f"闖紅燈-200元")
        elif position == 2:
            player['money'] += 10000
            print(f"中樂透+10000元")
        elif position == 3:
            player['money'] -= 600
            print(f"紅線停車-600元")
        elif position == 4:
            player['money'] -= 2000
            print(f"繳汽車稅-2000元")
        elif position == 5:
            player['money'] -= 3000
            print(f"繳房屋稅-3000元")
        elif position == 6:
            player['skip_turn'] = True
            print(f"停止一次")
        elif position == 7:
            player['money'] += 1000
            print(f"得到股息+1000元")
        elif position == 8:
            player['money'] += 3000
            print(f"工作得到獎金+3000元")
        elif position == 9:
            player['money'] -= 400
            print(f"繳停車費-400元")

    def print_status(self, player):
        print(f"money:{player['money']}\nposition:{player['position']}")
        print()
    def announce_winner(self):
        max_money = max(self.players, key=lambda p: p['money'])['money']
        winners = [p['name'] for p in self.players if p['money'] == max_money]
        if len(winners) > 1:
            print(f"Player(s) {' '.join(winners)}")
        else:
            winner = winners[0]
            print(f"Player(s) {winner} win!")

    def start_game(self):
        while not self.is_game_over:

            self.play_turn()

if __name__ == "__main__":
    game = LifeGame()
