from CreateRandomADOFAI.adofai_exceptions import FlashlightException
from CreateRandomADOFAI.gameplay import Gameplay, INVIOLATE_TILES
from random import randint, uniform, choice
from CreateRandomADOFAI.handler import eases_find
import config
import json


class VisualEffects(Gameplay):
    def __init__(self, name: str = config.default_name, tiles_count: int = 10, add_timestamp: bool = True):
        super().__init__(name, tiles_count, add_timestamp=add_timestamp)

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
            duration_random = round(uniform(min_duration, max_duration), config.decimal_count)
            start_opacity_random = round(uniform(min_start_opacity, max_start_opacity), config.decimal_count)
            end_opacity_random = round(uniform(min_end_opacity, max_end_opacity))

            if plane.lower() == "random":
                plane_random = choice(["Background", "Foreground"])
            elif plane.lower() == "background":
                plane_random = "Background"
            elif plane.lover() == "foreground":
                plane_random = "Foreground"
            else:
                raise FlashlightException("Invalid type. Use 'background', 'foreground' or 'random'")

            if ease.lower() == "random":
                ease_choice = choice(handler.eases_all)
            else:
                ease_found = eases_find(ease)
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

        with open(f"../levels/{self.name}.adofai", 'r+') as f:
            data = json.load(f)
            data["actions"].extend(list_flashlights)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        print("  Flashlights:", str(list_flashlights[:2]).strip("]") + ", ..." + "]")
