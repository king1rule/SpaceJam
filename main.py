# Define your functions
def coffee_bot():
  print('Welcome to the Cafe!' )
  size = get_size()
  drink_type = get_drink_type()
  type_latte = order_latte()
  print('Alright, that\'s a {} {} {}!'.format(size, drink_type, type_latte))
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>')

  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else: 
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n>')
  if res == 'a':
    return 'brewed coffee'

  elif res ==  'b':
    return 'mocha'
  elif res == 'c':
    return 'latte'
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n>')
  if res == 'a':
    return '2% milk'

  elif res ==  'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'Soy milk'
  else:
    print_message()
    return get_drink_type()
# Call coffee_bot()!
coffee_bot()



