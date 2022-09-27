from pygame import mixer
mixer.init()
mixer.music.load('Main Tumhara.mp3 ')
mixer.music.set_volume(0.7)
mixer.music.play()
while True:
   print("Press ' p ' to pause, 'r' to resume")
   print("Press ' any  other key ' to exit the program")
   query=input(" ")
   if query == 'p':
      mixer.music.pause()
   elif query == 'r':
      mixer.music.unpause()
   else:
      mixer.music.stop()
      break
   
