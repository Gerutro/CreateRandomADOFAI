import CreateRandomADOFAI

chart = CreateRandomADOFAI.gameplay.Gameplay("tl", 10000)
chart.generate_level()
chart.add_twirls()
chart.add_set_speed(speed_type="random", min_bpm=5000, max_bpm=10000, min_multiplier=8, max_multiplier=32)
chart.add_pause_on_beats()
