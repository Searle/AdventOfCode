package main

import (
	"fmt"
	"sync/atomic"
)

func main() {
	var ops int32 = 9 * 9 * 9 * 9

	var w1 = func() {
		if ops > 0 {

			atomic.AddInt32(&ops, -1)

			var n0 int32 = (ops/(9*9*9))%9 + 1
			var n1 int32 = (ops/(9*9))%9 + 1
			var n2 int32 = (ops/(9))%9 + 1
			var n3 int32 = (ops)%9 + 1

			fmt.Println("OPS", n0, n1, n2, n3)

			var nums = [14]int32{9, n0, n1, n2, n3, 9, 9, 9, 9, 9, 9, 9, 9, 9}

			var running = true
			for running {

				var _, _, _, z = code(nums)
				if z == 0 {
					fmt.Println("FOUND", nums)
				}

				for i := 13; ; i-- {
					if i == 4 {
						running = false
						break
					}
					if nums[i] > 1 {
						nums[i]--
						break
					}
					nums[i] = 9
				}
			}
		}
	}

	var worker = func(id int, jobs <-chan int, results chan<- int) {
		for j := range jobs {
			fmt.Println("worker", id, "started  job", j)
			w1()
			fmt.Println("worker", id, "finished job", j)
			results <- j * 2
		}
	}

	const numJobs = 9 * 9 * 9 * 9
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	for w := 1; w <= 20; w++ {
		go worker(w, jobs, results)
	}

	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	for a := 1; a <= numJobs; a++ {
		<-results
	}

	// fmt.Println("LARGEST", largest)
}
