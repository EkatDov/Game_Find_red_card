import pygame
from red_card_model import TestController

# colours:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (235, 235, 235)
RED = (230, 22, 16)
BlUE = (0, 191, 255)

class TestGameView():
    def __init__(self, controller):
        pygame.init()
        pygame.display.set_caption("Test Game")
        self.controller = controller
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((650, 300))
        self.current_instruction = "Which card is red?"
        self.card_one = {"coordinates": (50, 50, 100, 150), "rect": pygame.Rect(50, 50, 100, 150), "colour": GREY}
        self.card_two = {"coordinates": (250, 50, 100, 150), "rect": pygame.Rect(250, 50, 100, 150), "colour": GREY}
        self.card_three = {"coordinates": (450, 50, 100, 150), "rect": pygame.Rect(450, 50, 100, 150), "colour": GREY}



    def run(self):
        self.display_gameboard()
        self.distribute_colours()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.handle_events(event)

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.controller.model.game_over == False:
                mouse = pygame.mouse.get_pos()

                if self.card_one["rect"].collidepoint(mouse):
                    self.reveal_card(self.card_one)

                elif self.card_two["rect"].collidepoint(mouse):
                    self.reveal_card(self.card_two)

                elif self.card_three["rect"].collidepoint(mouse):
                    self.reveal_card(self.card_three)


            elif event.button == 3 and self.controller.model.game_over == True:
                self.controller.reset_game()
                self.clear_card_colours()
                self.distribute_colours()


    def display_gameboard(self):

        # fonts
        instructions_font = pygame.font.Font(None, 25)

        # draw screen
        self.screen.fill(WHITE)
        # draw instruction
        instruction_surface = instructions_font.render(self.current_instruction, True, BLACK)
        instruction_rect = instruction_surface.get_rect(topleft=(self.screen.get_width() // 3, (self.screen.get_height() // 4) * 3))
        self.screen.blit(instruction_surface, instruction_rect)
        #draw hidden cards
        self.clear_card_colours()



    def clear_card_colours(self):
        pygame.draw.rect(self.screen, GREY, self.card_two["coordinates"])
        pygame.draw.rect(self.screen, GREY, self.card_one["coordinates"])
        pygame.draw.rect(self.screen, GREY, self.card_three["coordinates"])

    def distribute_colours(self):
        red = self.controller.get_card_colour()
        self.card_one["colour"] = red[0]
        self.card_two["colour"] = red[1]
        self.card_three["colour"] = red[2]

    def reveal_card(self, card: dict):
        colour = TestGameView.get_colour(card["colour"])
        pygame.draw.rect(self.screen, colour, card["coordinates"])
        self.controller.model.revealed_cards += 1
        self.controller.check_game_over()


    @staticmethod
    def get_colour(red):
        if red:
            return RED
        else:
            return WHITE




if __name__ == "__main__":
    controller = TestController()
    game = TestGameView(controller)
    game.run()


