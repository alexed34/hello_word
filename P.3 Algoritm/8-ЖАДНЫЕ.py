# (цена, вес)
# list_all_orders =[ (150,1000),(400,2000),(350,1500) ]
list_all_orders=[(150,1000),(400,2000),(350,1500), (150,500),(150,500)]

print(list_all_orders)
list_all_orders.sort(reverse=True)
carrying = 3500
list_out = list ()
print(list_all_orders)
i=0
while carrying> 0:
    list_out.append(list_all_orders[i])
    carrying = carrying - list_all_orders[i][1]
    i=i+1
print(list_out)
total_value = 0
total_weight = 0
counter_box=0
for value,weight  in list_out:
    counter_box+=1
    total_value += value
    total_weight += weight
print(f"Взяли  коробок  {counter_box},  общая  стоимость  {total_value},  общий  вес  {total_weight},  еще  можно  взять {carrying } кг")

# 2 пример

all_city= set(["Ма","СП","Ха","Ва","Хе","Вл","Ки","Ми","Ка","Но"])
all_elfs = {}
all_elfs["elf_one"] = set(["Ма", "СП", "Ми"])
all_elfs["elf_two"] = set(["СП", "Ха", "Хе"])
all_elfs["elf_three"] = set(["Ха", "Ва"])
all_elfs["elf_four"] = set(["Ки", "Ми", "Но"])
all_elfs["elf_five"] = set(["Вл", "Ка"])
all_elfs["elf_six"] = set(["Ха", "Вл", "Ки", "Ми", "Ка"])
final_set_elfs=set()
print(all_elfs)
print(len(all_city))

while len(all_city) > 0:
    largest_area = set()
    best_elf = ""
    for name, cities in all_elfs.items():
        current_area = all_city & cities
        # current_area = cities
        if len(current_area) > len(largest_area):
            largest_area = current_area
            best_elf = name
    final_set_elfs.add(best_elf)
    all_city -= largest_area
print(final_set_elfs)



