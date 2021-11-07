from behave import *


@given(u'launch chrome browser')
def step_impl(context):
    assert 1==1


@when(u'user get the URL')
def step_impl(context):
    assert 3==3


@then(u'check the logo')
def step_impl(context):
    assert 3==3


@then(u'close')
def step_impl(context):
    assert 3==4
