from behave import *
from time import sleep

@when(u'wait')
def step_impl(context):
    sleep(3)