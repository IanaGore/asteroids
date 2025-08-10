import pygame
import json
import os
from constants import *


class Score:
    def __init__(self):
        self.current_score = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.Font(None, 36)
        
    def add_points(self, points):
        self.current_score += points
        
    def get_current_score(self):
        return self.current_score
        
    def get_high_score(self):
        return self.high_score
        
    def is_new_high_score(self):
        return self.current_score > self.high_score
        
    def update_high_score(self):
        if self.is_new_high_score():
            self.high_score = self.current_score
            self.save_high_score()
            
    def load_high_score(self):
        try:
            if os.path.exists("high_score.json"):
                with open("high_score.json", "r") as f:
                    data = json.load(f)
                    return data.get("high_score", 0)
        except:
            pass
        return 0
        
    def save_high_score(self):
        try:
            with open("high_score.json", "w") as f:
                json.dump({"high_score": self.high_score}, f)
        except:
            pass
            
    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.current_score}", True, "white")
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, "white")
        
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 50))
        
    def draw_game_over(self, screen):
        game_over_font = pygame.font.Font(None, 72)
        score_font = pygame.font.Font(None, 48)
        
        game_over_text = game_over_font.render("GAME OVER", True, "white")
        final_score_text = score_font.render(f"Final Score: {self.current_score}", True, "white")
        high_score_text = score_font.render(f"High Score: {self.high_score}", True, "white")
        
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        
        screen.blit(game_over_text, game_over_rect)
        screen.blit(final_score_text, final_score_rect)
        screen.blit(high_score_text, high_score_rect)
        
        if self.is_new_high_score():
            new_high_text = score_font.render("NEW HIGH SCORE!", True, "yellow")
            new_high_rect = new_high_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
            screen.blit(new_high_text, new_high_rect)