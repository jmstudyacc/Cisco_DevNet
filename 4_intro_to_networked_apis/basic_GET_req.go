package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	// variable to hold the URL of the API server
	dnacURL := "https://sandboxdnac2.cisco.com"
	tokenURI := "/dna/system/api/v1/auth/token"

	// variable to store the HTTP verb
	method := "POST"

	// not sure here!
	client := &http.Client{ }
	req, err := http.NewRequest(method, dnacURL + tokenURI, nil)

	// if there is an error
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
		return
	}

	// adds an auth header to the HTTP post
	req.Header.Add("Authorization", "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=")

	// res is equal to the result of the client doing the req var
	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
		return
	}
	defer res.Body.Close()

	// body is assigned to the readout from server
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
		return
	}
	token := string(body)
	fmt.Println(token)

	token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2MDRlNTc0ZDdiM2FhOTA2ZWRmMjA3M2QiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYxNzgzNzQzNSwiaWF0IjoxNjE3ODMzODM1LCJqdGkiOiI3NzYyNzZjMi00MjM0LTRhOTktOGM2ZC0xYjJlODMyMDJkNTkiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.O3C8bvmDvTfOiEakHCxVEWcfZb-KRCWzF9A4OayBtlK_Jj4Eq9DF8GgiA9y7MEVScx9ANcEgKUMo7UOechinquzf7-9erSHGGCF_6uWiCgizq8E89mBZs-GPsEJcAv2xn8frq_y_PlrMnbbo3oweiNF5dOwMgVM8vygTxIvjgyTYPEq8e7bUvBezGwBBbv1WtmS1BZYzVwo4_g0MN7ocPfNzcm8LFOsY_EdXb2ihrfFnfp6hgtFDndIkZ71kG7a3FnpSZ57zj1wP24ioxeHSaWqDJLgsRIGR3egUcCpZV7u4vBLVKYzPA69PJd_yGqfSuXg2AjhLp6vZItkW6OImRA"

	// variable to hold the network device api
	deviceApi := fmt.Sprintf("%s/dna/intent/api/v1/network-device", dnacURL)

	method = "GET"

	req, err = http.NewRequest(method, deviceApi, nil)

	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
		return
	}

	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("Accept", "application/json")
	req.Header.Add("X-Auth-Token", token)

	res, err = client.Do(req)
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
		return
	}
	defer res.Body.Close()

	body, err = ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
		return
	}
	fmt.Println(string(body))
}
