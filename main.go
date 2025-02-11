package main

import (
	"fmt"
	"net/http"
	"html/template"
	"log"
	"os"
	"encoding/json"
	"github.com/go-chi/chi/v5"
)

var port string = ":3000"

type AircraftResponse struct {
	Time float32 `json:"time"`
	Aircraft []Aircraft `json:"aircraft"`
}

type Aircraft struct {
	Hex string `json:"hex"`
	ID string `json:"id"`
	Speed string `json:"speed"`
	Flight string `json:"flight"`
	Alt string `json:"alt"`
	Img string `json:"img"`
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	baseUrl := os.Getenv("API_URL")
	path := "/api/aircraft"
	url := baseUrl + path
	
	resp, err := http.Get(url)
	if err != nil {
		log.Println("Error making request:", err)
		http.Error(w, "Failed to fetch aircraft data.", http.StatusInternalServerError)
		return
	}

	defer resp.Body.Close()
	
	var apiResponse AircraftResponse
	err = json.NewDecoder(resp.Body).Decode(&apiResponse)
	if err != nil {
		log.Println("Error decoding JSON:", err)
		http.Error(w, "Failed to decode aircraft data.", http.StatusInternalServerError)
		return
	}

	aircraftList := apiResponse.Aircraft

	tpl, err := template.ParseFiles("templates/index.html")
	if err != nil {
			log.Printf("Parsing template: %v", err)
			http.Error(w, "There was an error parsing the template.", http.StatusInternalServerError)
			return
	}

	err = tpl.Execute(w, aircraftList)
	if err != nil {
			log.Printf("Executing template: %v", err)
			http.Error(w, "There was an error executing the template.", http.StatusInternalServerError)
			return
	}
}

func main() {

	r := chi.NewRouter()
	r.Get("/", homeHandler)

	fmt.Fprintln(os.Stdout, "Starting the server on " + port + "...")
	
	http.ListenAndServe(port, r)
}