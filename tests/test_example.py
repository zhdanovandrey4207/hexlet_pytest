from hexlet_pytest.example import reverse
import pytest

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert reverse('') == ''

def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack

def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()

def test_with_fix():
    with open('tests/fixtures/start.txt') as f:
        start_text = f.read()
    with open('tests/fixtures/fin.txt') as h:
        fin_text = h.read()
    assert reverse(start_text).strip() == fin_text.strip()
