package main

import (
	"fmt"
)

func stringInArray(str string, array []uint8) bool {
	if len(str) > len(array) {
		return false
	}

	for idx, char := range str {
		//fmt.Printf("comparing %v and %v\n", string(char), array[len(array)-len(str)+idx])

		if fmt.Sprintf("%v", string(char)) != fmt.Sprintf("%v", array[len(array)-len(str)+idx]) {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("Day 14 Part B")
	recipes := []uint8{3, 7}
	elf1, elf2 := 0, 1
	recipeToFind := "327901"
	count := 0
	for (stringInArray(recipeToFind, recipes) == false) && (stringInArray(recipeToFind, recipes[0:len(recipes)-1]) == false) {
		sum := recipes[elf1] + recipes[elf2]
		if sum < 10 {
			recipes = append(recipes, sum)
		} else {
			recipes = append(recipes, sum/10)
			recipes = append(recipes, sum-10)
		}

		//fmt.Println(recipes)
		elf1 = (elf1 + 1 + int(recipes[elf1])) % len(recipes)
		elf2 = (elf2 + 1 + int(recipes[elf2])) % len(recipes)

		count += 1

		if (count % 1000000) == 0 {
			fmt.Println(count)
		}

	}

	if stringInArray(recipeToFind, recipes) {
		print(len(recipes) - len(recipeToFind))
	} else {
		print(len(recipes) - len(recipeToFind) - 1)
	}

}
