@namespace
class SpriteKind:
    NonTouchableObject = SpriteKind.create()
    BallLauncher = SpriteKind.create()
    BallStrip = SpriteKind.create()
    Target = SpriteKind.create()
    DecoyBall = SpriteKind.create()
    DuckHitter = SpriteKind.create()
    YellowDuck = SpriteKind.create()
    Reloading = SpriteKind.create()
    RedDuck = SpriteKind.create()
    GreenDuck = SpriteKind.create()
    EndAnimation = SpriteKind.create()

def on_a_pressed():
    global TargetActive, DecoyBallSpr
    if IfFPSCarnivalGameActive == True:
        if TargetActive != 1 and TargetSpr.y < 59 and ReadyController == 1:
            controller.move_sprite(TargetSpr, 0, 0)
            TargetActive = 1
            TargetSpr.vx = 0
            sprites.destroy_all_sprites_of_kind(SpriteKind.BallLauncher)
            DecoyBallSpr = sprites.create(assets.image("""
                Ball
            """), SpriteKind.DecoyBall)
            DecoyBallSpr.y = 114
            DecoyBallSpr.x = TargetSpr.x
            DecoyBallSpr.z = 10
            DecoyBallSpr.vy = -50
            music.play(music.create_sound_effect(WaveShape.NOISE,
                    137,
                    2808,
                    255,
                    0,
                    750,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.IN_BACKGROUND)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def Anim():
    
    def on_after():
        global ReadyController, TargetActive, EndAnimation2
        ReadyController = 0
        TargetActive = 0
        DecoyBallSpr.set_kind(SpriteKind.DecoyBall)
        sprites.destroy(DecoyBallSpr)
        EndAnimation2 = sprites.create(assets.image("""
            Reloading
        """), SpriteKind.Reloading)
        animation.run_image_animation(EndAnimation2,
            assets.animation("""
                ReloadingAnim
            """),
            25,
            False)
        EndAnimation2.y = 112
        EndAnimation2.z = 11
        
        def on_after2():
            ResetBall()
            
            def on_after3():
                global ReadyController
                sprites.destroy_all_sprites_of_kind(SpriteKind.Reloading)
                controller.move_sprite(TargetSpr, 0, 100)
                ReadyController = 1
            timer.after(100, on_after3)
            
        timer.after(475, on_after2)
        
    timer.after(200, on_after)
    

def on_on_overlap(sprite, otherSprite):
    otherSprite.set_kind(SpriteKind.NonTouchableObject)
    otherSprite.vx = 0
    otherSprite.vy = -40
    info.change_countdown_by(6)
    
    def on_after4():
        otherSprite.ay = 60
    timer.after(50, on_after4)
    
sprites.on_overlap(SpriteKind.DuckHitter, SpriteKind.GreenDuck, on_on_overlap)

def on_countdown_end():
    global EndAnimation2, ReadyController
    if IfFPSCarnivalGameActive == True:
        EndAnimation2 = sprites.create(assets.image("""AnimPlaceHolder"""),
            SpriteKind.EndAnimation)
        EndAnimation2.z = 12
        ReadyController = 0
        if info.score() >= 100:
            animation.run_image_animation(EndAnimation2,
                assets.animation("""
                    Good Animation
                """),
                400,
                False)
            
            def on_after5():
                game.reset()
            timer.after(2800, on_after5)
            
        else:
            animation.run_image_animation(EndAnimation2,
                assets.animation("""
                    Bad Animation
                """),
                400,
                False)
            
            def on_after6():
                game.reset()
            timer.after(2800, on_after6)
            
info.on_countdown_end(on_countdown_end)

def ResetBall():
    global Ball
    sprites.destroy_all_sprites_of_kind(SpriteKind.BallLauncher)
    Ball = sprites.create(assets.image("""
        Ball
    """), SpriteKind.BallLauncher)
    Ball.z = 10
    Ball.set_position(TargetSpr.x, 114)
    Ball.set_stay_in_screen(True)
def GreenduckFuncF():
    global GreenDuckSpr
    GreenDuckSpr = sprites.create(assets.image("""
        GreenDuck
    """), SpriteKind.GreenDuck)
    GreenDuckSpr.z = 3
    GreenDuckSpr.set_position(0, 13)
    GreenDuckSpr.vx = 60
    GreenDuckSpr.set_flag(SpriteFlag.AUTO_DESTROY, True)
    animation.run_image_animation(GreenDuckSpr,
        assets.animation("""
            DuckAnimationGF
        """),
        200,
        True)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.set_kind(SpriteKind.NonTouchableObject)
    otherSprite2.vx = 0
    otherSprite2.vy = -40
    info.change_score_by(4)
    
    def on_after7():
        otherSprite2.ay = 60
    timer.after(50, on_after7)
    
sprites.on_overlap(SpriteKind.DuckHitter, SpriteKind.YellowDuck, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    otherSprite3.set_kind(SpriteKind.NonTouchableObject)
    otherSprite3.vx = 0
    otherSprite3.vy = -40
    info.change_score_by(-6)
    info.change_countdown_by(-3)
    
    def on_after8():
        otherSprite3.ay = 60
    timer.after(50, on_after8)
    
sprites.on_overlap(SpriteKind.DuckHitter, SpriteKind.RedDuck, on_on_overlap3)

def InitalizeInGameTools():
    global Ball, TargetSpr
    Ball = sprites.create(assets.image("""
        Ball
    """), SpriteKind.BallLauncher)
    Ball.z = 10
    Ball.set_position(80, 114)
    TargetSpr = sprites.create(assets.image("""
        Target
    """), SpriteKind.Target)
    TargetSpr.set_position(80, 114)
    TargetSpr.z = 9
    controller.move_sprite(TargetSpr, 0, 100)
    Ball.set_stay_in_screen(True)
    TargetSpr.set_stay_in_screen(True)

def on_left_pressed():
    if IfFPSCarnivalGameActive == True:
        if TargetActive == 0 and ReadyController == 1:
            Ball.vx = -50
            TargetSpr.vx = -50
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    if IfFPSCarnivalGameActive == True:
        if TargetActive == 0 and ReadyController == 1:
            Ball.vx = 50
            TargetSpr.vx = 50
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def FPSCarnivalSetup():
    global IfFPSCarnivalGameActive, BackwardialWaves, FrontalWaves, FrontalDrapes, TargetActive, ReadyController
    IfFPSCarnivalGameActive = True
    BackwardialWaves = sprites.create(assets.image("""
            BackwardialWaves
        """),
        SpriteKind.NonTouchableObject)
    BackwardialWaves.z = 4
    FrontalWaves = sprites.create(assets.image("""
            FrontalWaves
        """),
        SpriteKind.NonTouchableObject)
    FrontalWaves.z = 6
    FrontalDrapes = sprites.create(assets.image("""
        CarnivalBG
    """), SpriteKind.player)
    FrontalDrapes.z = 8
    TargetActive = 0
    ReadyController = 1
    animation.run_image_animation(FrontalWaves,
        assets.animation("""
            FrontalWavesAnim
        """),
        200,
        True)
    animation.run_image_animation(BackwardialWaves,
        assets.animation("""
            BackwardialWavesAnim
        """),
        250,
        True)
    InitalizeInGameTools()
    info.start_countdown(35)
def GreenduckFunc():
    global GreenDuckSpr
    GreenDuckSpr = sprites.create(assets.image("""
        GreenDuck
    """), SpriteKind.GreenDuck)
    GreenDuckSpr.z = 5
    GreenDuckSpr.set_position(160, 50)
    GreenDuckSpr.vx = -30
    GreenDuckSpr.set_flag(SpriteFlag.AUTO_DESTROY, True)
    animation.run_image_animation(GreenDuckSpr,
        assets.animation("""
            DuckAnimationG
        """),
        200,
        True)
RedDuckSpr: Sprite = None
YellowDuckSpr: Sprite = None
FrontalDrapes: Sprite = None
FrontalWaves: Sprite = None
BackwardialWaves: Sprite = None
GreenDuckSpr: Sprite = None
Ball: Sprite = None
EndAnimation2: Sprite = None
DecoyBallSpr: Sprite = None
ReadyController = 0
TargetSpr: Sprite = None
TargetActive = 0
IfFPSCarnivalGameActive = False
FPSCarnivalSetup()

def on_update_interval():
    if IfFPSCarnivalGameActive == True:
        if TargetActive == 1:
            if DecoyBallSpr.y < TargetSpr.y + 20:
                if TargetSpr.y < 50:
                    DecoyBallSpr.scale += -0.3
                else:
                    DecoyBallSpr.scale += -0.15
            else:
                DecoyBallSpr.scale += 0.1
game.on_update_interval(1, on_update_interval)

def on_update_interval2():
    if IfFPSCarnivalGameActive == True:
        if TargetActive == 1:
            if DecoyBallSpr.y <= TargetSpr.y:
                DecoyBallSpr.vy = 0
                DecoyBallSpr.set_kind(SpriteKind.DuckHitter)
                Anim()
game.on_update_interval(1, on_update_interval2)

def on_update_interval3():
    global YellowDuckSpr, RedDuckSpr
    if IfFPSCarnivalGameActive == True:
        if Math.percent_chance(80):
            if Math.percent_chance(90):
                YellowDuckSpr = sprites.create(assets.image("""
                    Duck
                """), SpriteKind.YellowDuck)
                YellowDuckSpr.z = 5
                YellowDuckSpr.set_position(160, 50)
                YellowDuckSpr.vx = -30
                YellowDuckSpr.set_flag(SpriteFlag.AUTO_DESTROY, True)
                animation.run_image_animation(YellowDuckSpr,
                    assets.animation("""
                        DuckAnimation
                    """),
                    200,
                    True)
            else:
                GreenduckFunc()
        else:
            if Math.percent_chance(90):
                RedDuckSpr = sprites.create(assets.image("""
                    RedDuck
                """), SpriteKind.RedDuck)
                RedDuckSpr.z = 5
                RedDuckSpr.set_position(160, 50)
                RedDuckSpr.vx = -30
                RedDuckSpr.set_flag(SpriteFlag.AUTO_DESTROY, True)
                animation.run_image_animation(RedDuckSpr,
                    assets.animation("""
                        DuckAnimation0
                    """),
                    200,
                    True)
            else:
                GreenduckFunc()
game.on_update_interval(2000, on_update_interval3)

def on_update_interval4():
    global YellowDuckSpr, RedDuckSpr
    if IfFPSCarnivalGameActive == True:
        if Math.percent_chance(80):
            if Math.percent_chance(90):
                YellowDuckSpr = sprites.create(assets.image("""
                    Duck
                """), SpriteKind.YellowDuck)
                YellowDuckSpr.z = 3
                YellowDuckSpr.set_position(0, 13)
                YellowDuckSpr.vx = 60
                YellowDuckSpr.set_flag(SpriteFlag.AUTO_DESTROY, True)
                animation.run_image_animation(YellowDuckSpr,
                    assets.animation("""
                        DuckAnimationF0
                    """),
                    200,
                    True)
            else:
                GreenduckFuncF()
        else:
            if Math.percent_chance(90):
                RedDuckSpr = sprites.create(assets.image("""
                    RedDuck
                """), SpriteKind.RedDuck)
                RedDuckSpr.z = 3
                RedDuckSpr.set_position(0, 13)
                RedDuckSpr.vx = 60
                RedDuckSpr.set_flag(SpriteFlag.AUTO_DESTROY, True)
                animation.run_image_animation(RedDuckSpr,
                    assets.animation("""
                        DuckAnimationF
                    """),
                    200,
                    True)
            else:
                GreenduckFuncF()
game.on_update_interval(1000, on_update_interval4)
