package main
import (
	"fmt"
	"net/http"
)

func main(){
    // simple get request
    resp, err := http.Get("http://google.com/")
	
	// posting form data
    // resp, err = http.PostForm("http://google.com",
	// url.Values{"key": {"Value"}, "id": {"123"}})
	
	fmt.Println("Resp : ", resp.Header)
	fmt.Printf("\n")
	fmt.Println("err : ", err)
}