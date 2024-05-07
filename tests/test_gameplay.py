import CreateRandomADOFAI


if __name__ == '__main__':
    chart = CreateRandomADOFAI.Gameplay("tl", 2000, add_timestamp=False)
    chart.generate_level()
    chart.add_twirls()
    chart.add_set_speed(speed_type="random",
                        min_bpm=5000,
                        max_bpm=10000,
                        min_multiplier=8,
                        max_multiplier=32)
    chart.add_beats_pause()
    visual = CreateRandomADOFAI.VisualEffects(name="tl", tiles_count=2000, add_timestamp=False)
    visual.add_flashlights()
