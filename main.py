def on_pin_pressed_p0():
    music.play_tone(196, music.beat(BeatFraction.DOUBLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.DOUBLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(247, music.beat(BeatFraction.DOUBLE))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.DOUBLE))
    music.play_tone(196, music.beat(BeatFraction.DOUBLE))
    music.play_tone(330, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(196, music.beat(BeatFraction.DOUBLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.DOUBLE))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.DOUBLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(247, music.beat(BeatFraction.DOUBLE))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.BREVE))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
