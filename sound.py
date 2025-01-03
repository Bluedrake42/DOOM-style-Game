import pygame as pg
from settings import MUSIC_VOLUME, NPC_ATTACK_VOLUME, NPC_PAIN_VOLUME, NPC_DEATH_VOLUME, PLAYER_PAIN_VOLUME, SHOTGUN_VOLUME


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.shotgun.set_volume(SHOTGUN_VOLUME)
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_pain.set_volume(NPC_PAIN_VOLUME)
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_death.set_volume(NPC_DEATH_VOLUME)
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_shot.set_volume(NPC_ATTACK_VOLUME)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.player_pain.set_volume(PLAYER_PAIN_VOLUME)
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(MUSIC_VOLUME)