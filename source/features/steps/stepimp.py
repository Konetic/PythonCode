from behave import *

@given('I reach office at "{time}" shift')
def step_implpy(context, time):
      print("Shift is: {}".format(time))