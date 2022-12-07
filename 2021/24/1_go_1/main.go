package main

import "fmt"

func main() {
	var nums = [14]int32{9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9}
	var largest [14]int32 = nums
	var running = true
	var li = 0

	for running {

		li++
		if li > 10000000 {
			fmt.Println("AT", nums)
			li = 0
		}

		var _, _, _, z = code(nums)
		if z == 0 {
			fmt.Println("FOUND", nums)
			largest = nums
		}

		for i := 13; i >= 0; i-- {
			if nums[i] > 1 {
				nums[i]--
				break
			}
			nums[i] = 9
			if i == 0 {
				running = false
			}
		}
	}

	fmt.Println("LARGEST", largest)
}
