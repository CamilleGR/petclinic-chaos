package main


import (
    "flag"
    "fmt"
    "strings"
    "net/http"
    "time"
    "os"
    "os/signal"
    "syscall"
)

func main(){

  u := flag.String("u","nil","Url to monitor (required).")
  period := flag.Int("p",15,"Period between each execution of the monitor.")
  flag.Parse()
  cancelChan := make(chan os.Signal, 1)
  // catch SIGETRM or SIGINTERRUPT
  signal.Notify(cancelChan, syscall.SIGTERM, syscall.SIGINT)


  fmt.Println("-----------------------------------------")
  fmt.Println("Start monioting for : ",*u)
  fmt.Println("Period : ", *period," seconds")
  fmt.Println("-----------------------------------------")

  if strings.Compare(*u,"nil") == 0 {
    fmt.Println("Error : You must provide an URL to monitor. use -h to get help.")
    os.Exit(1)
  }

  go func(){
      for{
      resp,err := http.Get(*u)

      if err != nil {
        fmt.Println("[",time.Now().Format("01-02-2006 15:04:05"),"] - Error: ",err)
      }else{
        fmt.Println("[",time.Now().Format("01-02-2006 15:04:05"),"] - ",resp.Status)
        defer resp.Body.Close()
      }
      time.Sleep(time.Second * time.Duration(*period))
    }
  }()
  sig := <-cancelChan
  fmt.Println("---------------------------------------")
  fmt.Println("Caught SIGTERM : ", sig)


}
