import random

class TestModel:
    def __init__(self):
        self.cards = [False, False]
        self.clicks = 0
        self.game_over = False

    def display_cards(self):
        #print(self.cards) -> e.g. [True, False]
        return self.cards

    def assign_red_to_card(self):
        red_card_index = random.choice([0,1])
        self.cards[red_card_index] = True

    def reset_game(self):
        self.cards = [False, False]
        self.clicks = 0
        self.game_over = False


class TestController:
    def __init__(self):
        self.model = TestModel()

    def get_card_colour(self):
        self.model.assign_red_to_card()
        return self.model.cards

    def check_game_over(self):
        if self.model.clicks < 2:
            self.model.game_over = False
        else:
            self.model.game_over = True

    def reset_game(self):
        self.model.reset_game()



if __name__ == "__main__":
    game = TestModel()
    game.assign_red_to_card()
    game.display_cards()

