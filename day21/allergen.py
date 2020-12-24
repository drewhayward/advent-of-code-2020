
def get_input():
    foods = []
    with open('day21/input') as f:
        for line in f.readlines():
            line = line.strip()
            split_point = line.index('(')
            ingredients = line[:line.index('(') - 1].split(' ')
            
            allergens = line[line.index('('):].strip('()')[9:].split(', ')
            foods.append((ingredients, allergens))

    return foods

def find_allergen_names(foods):
    ingredients = {ing for food in foods for ing in food[0]}
    allergens = {allergen for food in foods for allergen in food[1]}
    alg_ing = {a: set(ingredients) for a in allergens}

    for food_ing, food_alg in foods:
        for alg in food_alg:
            alg_ing[alg].intersection_update(food_ing)

    while any([len(ings) > 1 for ings in alg_ing.values()]):
        for allergen in alg_ing.keys():
            other_foods = {list(ings)[0] for a, ings in alg_ing.items() if len(ings) == 1 and a != allergen}
            alg_ing[allergen].difference_update(other_foods)

    return {allergen:list(ings)[0] for allergen, ings in alg_ing.items()}

def part_1():
    foods = get_input()
    allergen_map = find_allergen_names(foods)
    allergens = allergen_map.values()

    total = 0
    for ingrs, algs in foods:
        total += len([i for i in ingrs if i not in allergens])

    return total

def part_2():
    foods = get_input()
    allergen_map = find_allergen_names(foods)
    names = [(a, i) for a, i in allergen_map.items()]
    names.sort(key= lambda x: x[0])
    return ','.join([name[1] for name in names])


if __name__ == "__main__":
    print(part_1())
    print(part_2())
