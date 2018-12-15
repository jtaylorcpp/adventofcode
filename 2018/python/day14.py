def part_1():
    def new_recipe(rec_a, rec_b):
        rec_c = rec_a + rec_b
        if rec_c <= 9:
            return [rec_c]
        else:
            rec_c, rec_d = str(rec_c)[0],str(rec_c)[1]
            return [int(rec_c), int(rec_d)]

    recipes = [3,7]
    elf1, elf2 = 0,1
    rec_count = 0
    recipe_num = 9
    extra = 10
    while len(recipes) < (recipe_num + extra):
        new_rec = new_recipe(recipes[elf1], recipes[elf2])
        for rec in new_rec:
            recipes.append(rec)
        #print(elf1, elf2, recipes)
        rec_count += 1
        elf1 += 1 + recipes[elf1]
        elf2 += 1 + recipes[elf2]
        while elf1 >= len(recipes):
            elf1 -= len(recipes)
        while elf2 >= len(recipes):
            elf2 -= len(recipes)
        #print(elf1, elf2, recipes)

    print(recipes)

def part_2():
    def new_recipe(rec_a, rec_b):
        rec_c = rec_a + rec_b
        if rec_c <= 9:
            return [rec_c]
        else:
            rec_c, rec_d = str(rec_c)[0],str(rec_c)[1]
            return [int(rec_c), int(rec_d)]

    recipes = [3,7]
    rec_str = "37"
    elf1, elf2 = 0,1
    recipe_num = "327901"
    while recipe_num not in rec_str:
        new_rec = new_recipe(recipes[elf1], recipes[elf2])
        for rec in new_rec:
            recipes.append(rec)
            rec_str += str(rec)


        #print(elf1, elf2, recipes)
        elf1 += 1 + recipes[elf1]
        elf2 += 1 + recipes[elf2]
        elf1 = elf1 % len(recipes)
        elf2 = elf2 % len(recipes)
        #print(elf1, elf2, rec_count, recipes)

    print(recipes)


part_2()
