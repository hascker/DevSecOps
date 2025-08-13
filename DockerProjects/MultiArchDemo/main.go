package main

import (
	"fmt"
	"net/http"
	"runtime"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello from %s/%s!\n", runtime.GOOS, runtime.GOARCH)
	fmt.Fprintf(w, "Container running on: %s\n", runtime.Version())
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Printf("Server starting on :8080 (%s/%s)\n", runtime.GOOS, runtime.GOARCH)
	http.ListenAndServe(":8080", nil)
}