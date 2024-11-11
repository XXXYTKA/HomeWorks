calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    len_in = len(string)
    up_string = string.upper()
    low_string = string.lower()
    return  len_in, up_string, low_string
def is_contains(string, list_to_search):
  count_calls()
  for item in list_to_search:
    if string.lower() == item.lower():
      return True
  return False
