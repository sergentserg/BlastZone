import src.config as cfg
from src.sprites.animated_sprite import AnimatedSprite

class Explosion(AnimatedSprite):
    _IMAGES = [f'explosion{i}.png' for i in range(1, 6)]
    def __init__(self, x, y, groups):
        self._layer = cfg.EFFECTS_LAYER
        frame_info = [{'start_frame': 0, 'num_frames': len(Explosion._IMAGES)}]
        AnimatedSprite.__init__(self, x, y, groups['all'],
                                            Explosion._IMAGES, frame_info)
        self.anim_fps = 48.0

    def update(self, dt):
        self.update_anim(dt)

    def _handle_last(self):
        self.current_frame = 0
        self.kill()
