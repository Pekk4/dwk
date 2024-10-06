package main

import (
	"fmt"
	"net/http"
	"sync"
)

var (
	mutex sync.Mutex
	count int
)

func pingPongHandler(w http.ResponseWriter, r *http.Request) {
	mutex.Lock()
	defer mutex.Unlock()

	fmt.Fprintf(w, "pong %d", count)

	count++
}

func main() {
	http.HandleFunc("/pingpong", pingPongHandler)

	fmt.Println("Server is listening on port 8080...")

	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Failed to start server:", err)
	}
}
