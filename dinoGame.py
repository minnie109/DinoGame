from ursina import *
import time
import random as r

timer = 0

app = Ursina()
window.fullscreen = True
window.color = color.white


dino = Animation('assets\dino',
                 collider='box',
                 x=-5)

ground1 = Entity(
  model='quad',
  texture='assets\ground',
  scale=(50,0.5,1),
  z=1
)
ground2 = duplicate(ground1, x=50)
pair = [ground1, ground2]



cactus = Entity(
  model='quad',
  texture='assets\cacti',
  x = 20,
  collider='box'
)
cacti = []
def newCactus():
  new = duplicate(cactus,
                  x=12+r.randint(0,5))
  new.has_been_scored = False
  cacti.append(new)
  invoke(newCactus, delay=2)

newCactus()



label = Text(
  text = f'Points: {0}',
  color=color.black,
  position=(-0.5, 0.4)
)
timeLabel = Text(
  text = f'Time: {0}',
  color=color.black,
  position=(-0.5, 0.35)
)
points = 0
game_duration = 30  # Set the game duration to 10 seconds

def update():
  global points
  global timer
  if timer < game_duration:
    timer += time.dt
    timeLabel.text = f'Time: {int(timer)}'
    for ground in pair:
      ground.x -= 6*time.dt
      if ground.x < -35:
        ground.x += 100
    for c in cacti:
      c.x -= 6*time.dt
      if c.x < dino.x and not c.has_been_scored:
        c.has_been_scored = True
        points += 1
        label.text = f'Points: {points}'
    if dino.intersects().hit:
      dino.texture= 'assets\hit'
      application.pause()
      points -= 1
      time.sleep(1)
      application.resume()
  else:
    application.pause()

sound = Audio(
  'assets\\beep',
  autoplay=False
)


def input(key):
  print(f'Key pressed: {key}')
  if key == 'enter':
    print('Jumping...')
    if dino.y < 0.01:
      sound.play()
      dino.animate_y(
        2,
        duration=0.4,
        curve= curve.out_sine
      )
      dino.animate_y(
        0,
        duration=0.4,
        delay=0.4,
        curve = curve.in_sine
      )

app.run()
