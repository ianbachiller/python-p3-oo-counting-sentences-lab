#!/usr/bin/env python3


class MyString:

  def __init__(self, value=''):
    self._value = ''
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return True if self._value[-1] == "." else False

  def is_question(self):
    return True if self._value[-1] == "?" else False

  def is_exclamation(self):
    return True if self._value[-1] == "!" else False

  def count_sentences(self):
    sent_count = 0
    prev_char = None
    for char in self._value:
        if char in ('.', '!', '?'):
            if prev_char not in ('.', '!', '?'):
                sent_count += 1
        prev_char = char 
    return sent_count