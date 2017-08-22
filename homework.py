import random
cook_book =dict()
with open('C:/Users/Ksenia/Documents/homework.txt') as f:
  for line in f:
    cook = f.readline().rstrip().lower()
    num_ingredients = int(f.readline().rstrip())
    description =[]
    for x in range(num_ingredients):
      dic_ingredient = dict()
      desc_ingredient = f.readline().lower()
      desc_ingredient = desc_ingredient.split(' ')
      dic_ingredient['ingredient_name'] = desc_ingredient[0]
      dic_ingredient['quantity'] = int(desc_ingredient[1])
      dic_ingredient['measure'] = desc_ingredient[2]
      description.append (dic_ingredient)  
    cook_book[cook] = description  
  #print (cook_book)   

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      new_shop_list_item = dict(ingredient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingredient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item 
      else:
        shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list, person_count):    
  print ('Ужин на {}'.format(person_count) )
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
  dishes = input('Какие будете блюда?(ввод через пробел)').lower().split(' ')
  person_count = int(random.choice([1, 2, 3, 4, 5]))
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list, person_count)

print ('МЕНЮ')
print (', '.join(cook_book.keys()))  
create_shop_list()
