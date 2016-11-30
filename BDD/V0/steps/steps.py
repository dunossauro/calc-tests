from behave import when, then
from functions import soma, divisao, multiplicacao, subtracao


@when('o cliente somar "{num_1:d}" com "{num_2:d}"')
def test(context, num_1, num_2):
    context.result = soma(num_1, num_2)

@when('o cliente subtrair "{num_1:d}" com "{num_2:d}"')
def test(context, num_1, num_2):
    context.result = subtracao(num_1, num_2)

@when('o cliente multiplicar "{num_1:d}" com "{num_2:d}"')
def test(context, num_1, num_2):
    context.result = multiplicacao(num_1, num_2)

@when('o cliente divir "{num_1:d}" com "{num_2:d}"')
def test(context, num_1, num_2):
    context.result = divisao(num_1, num_2)


@then('o resultado deve ser "{result:d}"')
def test(context, result):
    assert context.result == result
