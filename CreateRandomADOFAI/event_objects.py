from typing import Dict


#
# GENERATION LEVEL LAYER
#


def add_to_file(name: str,
                list_to_add: list,
                list_to_write: str):
    with open(f"../levels/{name}.adofai", "r+", encoding="utf-8") as f:
        level = json.load(f)
        level[list_to_write] = list_to_add
        f.seek(0)
        json.dump(level, f, indent=4)
        f.truncate()
    f.close()


def add_twirls(iteration: int) -> Dict:
    return {"floor": iteration, "eventType": "Twirl"}


def add_set_speed(iteration: int,
                  speed_type: str,
                  bpm: int,
                  multiplier: float,
                  angle: int) -> Dict:
    return {"floor": iteration,
            "eventType": "SetSpeed",
            "speedType": speed_type,
            "beatsPerMinute": bpm,
            "bpmMultiplier": multiplier,
            "angleOffset": angle}


def add_pause_beats(iteration: int,
                    duration: float,
                    countdown_ticks: int,
                    angle_correction_dir: int) -> Dict:
    return {"floor": iteration,
            "eventType": "Pause",
            "duration": duration,
            "countdownTicks": countdown_ticks,
            "angleCorrectionDir": angle_correction_dir}


#
# EFFECTS LAYER
#


def add_flashlights(iteration,
                    duration,
                    plane,
                    start_opacity,
                    end_opacity,
                    ease) -> Dict:
    return {"floor": iteration,
            "eventType": "Flash",
            "duration": duration,
            "plane": plane,
            "startColor": "ffffff",
            "startOpacity": start_opacity,
            "endColor": "ffffff",
            "endOpacity": end_opacity,
            "angleOffset": 0,
            "ease": ease,
            "eventTag": ""}
