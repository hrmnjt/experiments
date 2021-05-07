package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/google/go-github/v35/github"
	"github.com/spf13/viper"
	"golang.org/x/oauth2"
)

type Configurations struct {
	Token string
}

type FileNames struct {
	FileName string
}

var (
	OuputLogger *log.Logger
)

func init() {
	file, err := os.OpenFile("output.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		log.Fatal(err)
	}

	OuputLogger = log.New(file, "", log.Lshortfile)
}

func main() {

	// expects a file config.yml in same root with the content similar to below
	// token: "GITHUB_AUTH_TOKEN"
	viper.SetConfigName("secrets")
	viper.AddConfigPath(".")
	viper.SetConfigType("yml")
	var config Configurations

	if err := viper.ReadInConfig(); err != nil {
		fmt.Printf("Error reading config file, %s", err)
	}

	err := viper.Unmarshal(&config)
	if err != nil {
		fmt.Printf("Unable to decode into struct, %v", err)
	}

	ctx := context.Background()
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: fmt.Sprintf("%s", config.Token)},
	)
	tc := oauth2.NewClient(ctx, ts)

	client := github.NewClient(tc)

	opt := &github.ListOptions{PerPage: 10}

	var allFiles []*github.CommitFile
	for {
		files, resp, err := client.PullRequests.ListFiles(ctx, "majidalfuttaim", "de-airflow", 890, opt)

		if err != nil {
			fmt.Printf("Unable to list all the files, %v", err)
		}
		allFiles = append(allFiles, files...)
		if resp.NextPage == 0 {
			break
		}
		opt.Page = resp.NextPage
		for _, value := range files {
			OuputLogger.Println(*value.Filename)
		}
	}
}
