def _reverse(_text):
  _output = []
  _reverse_text = list(_text)
  _reverse_text.reverse()
  for _text_letter in _reverse_text:
    _output.append(_text_letter)
  return ''.join(_output)
