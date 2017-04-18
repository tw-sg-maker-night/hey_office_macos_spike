import snowboydecoder

def detected_callback():
  print "hotword detected"

detector = snowboydecoder.HotwordDetector("resources/Hey_Office.pmdl", sensitivity=0.45, audio_gain=1)
detector.start(detected_callback)
