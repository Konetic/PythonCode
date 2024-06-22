import os
from behave import *

import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 



@given(u'I put Red Tree Frog in a blender,')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I put Red Tree Frog in a blender,')


@when(u'I switch the blender on')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I switch the blender on')


@then(u'it should transform into mush')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it should transform into mush')


@given(u'I put iPhone in a blender,')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I put iPhone in a blender,')


@then(u'it should transform into toxic waste')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it should transform into toxic waste')


@given(u'I put Galaxy Nexus in a blender,')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I put Galaxy Nexus in a blender,')