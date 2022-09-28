"""
This is a program for maintaining a programmer healthy during the work time,
this program deals with alerting the programmer of various activities to perform,
in order to maintain a healthy schedule.
This includes:
    1. Drinking 3.6litre water.
    2. Exercising Eyes in every 35 minutes.
    3. Physical exercise in every 45 minutes.
"""


import datetime as dt
import time as tm
from pygame import mixer
import os

eyes = 'eyes.wav'
exercise = 'exercise.wav'
water = 'water.wav'

mixer.init()
m1 = None


def play_sound(song):
    global m1
    m1 = mixer.Sound(song)
    mixer.music.set_volume(1)
    m1.play(-1)


def stop_sound():
    global m1
    m1.stop()

# setting the working times
work_start = tm.strptime(f"9:00 AM {dt.datetime.now().date().isoweekday()} {dt.datetime.now().date()}", "%I:%M %p %w %Y-%m-%d")
work_end = tm.strptime(f"05:00 PM {dt.datetime.now().date().isoweekday()} {dt.datetime.now().date()}", "%I:%M %p %w %Y-%m-%d")
current_time = tm.localtime()

# water to drink is 3600 ml which is in every 14 minutes 30 times 120 ml per time
water_time = tm.mktime(work_start) + 14*60
eyes_time = tm.mktime(work_start) + 35*60
exercise_time = tm.mktime(work_start) + 45*60
water_count = 480/30  # total time is 480 mins


def write_to_file(task, time):
    """ function to log the timings of the activities """
    file_name = task + '.txt'
    with open(file_name, 'a') as f:
        if os.path.getsize(file_name) == 0:
            header = '\t\t\t' + 'Date/Time'.ljust(40, ' ')
            f.write(header)
        f.write(f"\n\t\t{time}".ljust(40, ' '))


def handle_water():
    """ function to handle drinking water alarm """
    global water_time, water_count
    play_sound(water)
    write_to_file('water', tm.asctime(tm.localtime(water_time)))
    water_time += (14*60)
    if str(input("Enter 'Done' if You Drank water: ")).lower() == 'done':
        water_count -= 1
        stop_sound()


def handle_eye():
    """ function to handle eye exercise alarm """
    global eyes_time
    write_to_file('eyes', tm.asctime(tm.localtime(eyes_time)))
    eyes_time += (30 * 60)
    play_sound(eyes)
    if str(input("Enter 'Done' if You Did Eye Exercise: ")).lower() == 'done':
        stop_sound()


def handle_exercise():
    """ function to handle physical exercise alarm """
    global exercise_time
    write_to_file('exercise', tm.asctime(tm.localtime(exercise_time)))
    play_sound(exercise)
    exercise_time += (45 * 60)
    if str(input("Enter 'Done' if You did Exercise: ")).lower() == 'done':
        stop_sound()


def run_program():
    global water_time, eyes_time, exercise_time, current_time, water_count
    current_time = tm.localtime()
    if current_time == tm.localtime(water_time) and water_count > 0:
        handle_water()
    if current_time == tm.localtime(eyes_time):
        handle_eye()
    if current_time == tm.localtime(exercise_time):
        handle_exercise()
    else:
        pass


while work_start < tm.localtime() < work_end:
    run_program()
