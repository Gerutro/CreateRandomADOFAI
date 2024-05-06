from CreateRandomADOFAI.adofai_exceptions import AngleException, SetSpeedException, PauseBeatsException
from random import randint, uniform, choice
import CreateRandomADOFAI.handler
import shutil
import json

protected_start = 5
decimal_count = 6


INVIOLATE_TILES = [i for i in range(0, 5)]


class Gameplay:
    def __init__(self,
                 name: str = "test_level",
                 tiles_count: int = 10,
                 default_speed: float = 150):
        self.name = name
        self.tiles_count = tiles_count
        self.default_speed = default_speed

    def generate_level(self,
                       min_angle: float = -359.999999,
                       max_angle: int = 359.999999) -> None:
        """
        Generates a tiles for level. MUST BE FIRST ON CREATE PROCESS!!!
        :param min_angle: min angle from -359 to 359
        :param max_angle: max angle from -359 to 359
        :raise AngleException: something wrong with angles
        :return:
        """

        if min_angle > max_angle:
            raise AngleException("Invalid value. The min value cannot be greater than th max value")
        elif min_angle <= -360 or max_angle >= 360:
            raise AngleException("Invalid value. The values cannot be greater than or less than 359 deg. and -359 deg.")

        list_tiles = []

        for i in range(self.tiles_count):
            num = uniform(round(min_angle, decimal_count), round(max_angle, decimal_count))
            list_tiles.append(num)

        shutil.copy("../src/template.json", f"{self.name}.adofai")

        with open(f"{self.name}.adofai", "r+") as f:
            level = json.load(f)
            level["angleData"] = list_tiles
            f.seek(0)
            json.dump(level, f, indent=4)
            f.truncate()

        print("Tiles:", list_tiles)

    def add_twirls(self) -> None:
        """
        Add event 'Twirl' to level
        :return:
        """
        list_twirls = []

        for i in range(self.tiles_count):
            num = randint(0, 8)
            if num == 8:
                list_twirls.append({"floor": i, "eventType": "Twirl"})

        with open(f"{self.name}.adofai", 'r+') as f:
            data = json.load(f)
            data["actions"].extend(list_twirls)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        print("Twirls:", list_twirls)

    def add_set_speed(self,
                      speed_type: str = "bpm",
                      min_bpm: int = 100,
                      max_bpm: int = 300,
                      min_multiplier: float = 0.5,
                      max_multiplier: float = 2,
                      min_angle: int = 0,
                      max_angle: int = 0) -> None:
        """
        Add event 'Set Speed' to level
        :param speed_type: type of set_speed event. Takes 3 values: 'bpm', 'multiplier', 'random'
        :param min_bpm: minimum bpm
        :param max_bpm: maximum bpm
        :param min_multiplier: minimum multiplier value
        :param max_multiplier: maximum multiplier value
        :param min_angle: minimum angle to set_speed event
        :param max_angle: maximum angle to set_speed event
        :raise SetSpeedException: something wrong with values of BPM or multiplier
        :return:
        """
        if max_multiplier > 128 or min_multiplier <= 0:
            raise SetSpeedException(f"Invalid min or max multiplier: {min_multiplier}x, {max_multiplier}x")
        elif min_bpm < 1 or max_bpm > 10000:
            raise SetSpeedException(f"Invalid min or max bpm: {min_bpm}, {max_bpm}")
        else:
            pass

        list_speeds = []

        for i in range(self.tiles_count):

            type_choice = choice(["Bpm", "Multiplier"])
            bpm_random = randint(min_bpm, max_bpm)
            multiplier_random = round(uniform(min_multiplier, max_multiplier), decimal_count)
            angle_random = round(uniform(min_angle, max_angle), decimal_count)

            min_multiplier = round(min_multiplier, decimal_count)
            max_multiplier = round(max_multiplier, decimal_count)
            min_angle = round(min_angle, decimal_count)
            max_angle = round(max_angle, decimal_count)

            num = randint(0, 8)

            if i in INVIOLATE_TILES:
                pass
            else:
                if str(speed_type.lower()) == "bpm" and num == 8:
                    list_speeds.append({"floor": i,
                                        "eventType": "SetSpeed",
                                        "speedType": "Bpm",
                                        "beatsPerMinute": bpm_random,
                                        "bpmMultiplier": 1,
                                        "angleOffset": angle_random})
                elif speed_type.lower() == "multiplier" and num == 8:
                    list_speeds.append({"floor": i,
                                        "eventType": "SetSpeed",
                                        "speedType": "Multiplier",
                                        "beatsPerMinute": 100,
                                        "bpmMultiplier": multiplier_random,
                                        "angleOffset": angle_random})
                elif speed_type.lower() == "random" and num == 8:
                    list_speeds.append({"floor": i,
                                        "eventType": "SetSpeed",
                                        "speedType": type_choice,
                                        "beatsPerMinute": bpm_random,
                                        "bpmMultiplier": multiplier_random,
                                        "angleOffset": angle_random})
                elif num != 8:
                    pass
                else:
                    raise SetSpeedException("Invalid type. Use 'bpm', 'multiplier' or 'random'.")

        with open(f"{self.name}.adofai", 'r+') as f:
            data = json.load(f)
            data["actions"].extend(list_speeds)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        print("Set_speed:", list_speeds)

    def add_beats_pause(self,
                        min_duration: float = 1,
                        max_duration: float = 2,
                        min_countdownTicks: int = 0,
                        max_countdownTicks: int = 0,) -> None:

        """
        Add event 'Pause Beats' to level
        :param min_duration: min duration to event
        :param max_duration: max duration to event
        :param min_countdownTicks: min duration of  to event
        :param max_countdownTicks: max duration to event
        :return:
        """

        if max_duration > 1000:
            raise PauseBeatsException("Invalid duration value. Value cannot be greater 1000")

        if max_countdownTicks > 12:
            raise PauseBeatsException("Invalid countdown ticks value. Value cannot be greater 12")

        if angleCorrectionDir != -1 and angleCorrectionDir != 0 and angleCorrectionDir != 1:
            raise PauseBeatsException("Invalid angle correction value. Value must be -1 or 0 or 1")

        list_pauses = []

        for i in range(self.tiles_count):

            num = randint(0, 8)
            duration_random = round(uniform(min_duration, max_duration), 6)
            countdown_ticks_random = randint(min_countdownTicks, max_countdownTicks)
            angle_correction_dir_random = int(choice([-1, 0, 1]))

            if num == 8:
                if i in INVIOLATE_TILES:
                    pass
                else:
                    list_pauses.append({"floor": i,
                                        "eventType": "Pause",
                                        "duration": duration_random,
                                        "countdownTicks": countdown_ticks_random,
                                        "angleCorrectionDir": angle_correction_dir_random})
            else:
                pass

        with open(f"{self.name}.adofai", 'r+') as f:
            data = json.load(f)
            data["actions"].extend(list_pauses)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        print("BOP:", list_pauses)
