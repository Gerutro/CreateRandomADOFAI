from CreateRandomADOFAI.adofai_exceptions import FlashlightException
from CreateRandomADOFAI.gameplay import Gameplay, INVIOLATE_TILES, decimal_count
from random import randint, uniform, choice
import CreateRandomADOFAI.handler
import json


class VisualEffects(Gameplay):
    def __init__(self, name, tiles_count):
        super().__init__(name, tiles_count)

    def add_flashlights(self,
                        min_duration: float = 1,
                        max_duration: float = 2,
                        plane: str = "background",
                        min_start_opacity: float = 100,
                        max_start_opacity: float = 100,
                        min_end_opacity: float = 0,
                        max_end_opacity: float = 0,
                        ease: str = "Linear") -> None:

        list_flashlights = []

        for i in range(self.tiles_count):

            num = randint(0, 8)
            duration_random = round(uniform(min_duration, max_duration), decimal_count)
            start_opacity_random = round(uniform(min_start_opacity, max_start_opacity), decimal_count)
            end_opacity_random = round(uniform(min_end_opacity, max_end_opacity))
            if plane.lower() == "background":
                plane_random = "Background"
            elif plane.lover() == "foreground":
                plane_random = "Foreground"
            elif plane.lower() == "random":
                plane_random = choice(["Background", "Foreground"])
            else:
                raise FlashlightException("Invalid type. Use 'background', 'foreground' or 'random'")

            if ease.lower() == "random":
                ease_choice = choice(handler.eases_all)
            else:
                ease_found = handler.eases_find(ease)
                ease_choice = choice(ease_found)

            if num == 8:
                list_flashlights.append({"floor": i,
                                         "eventType": "Flash",
                                         "duration": duration_random,
                                         "plane": plane_random,
                                         "startColor": "ffffff",
                                         "startOpacity": start_opacity_random,
                                         "endColor": "ffffff",
                                         "endOpacity": end_opacity_random,
                                         "angleOffset": 0,
                                         "ease": ease_choice,
                                         "eventTag": ""})
