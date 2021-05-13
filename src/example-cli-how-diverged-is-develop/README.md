# How diverged is my develop?

At work, `airflow` repostitory has `master` and `develop` branch. `develop` is 
setup to test out the `airflow` DAGs in a test environment but there are times 
developers tend to abuse the workflow and never productionalize DAGs. This 
causes a lot of problems for someone who is developing new features.

The intention of this program is to log all the files which are causing the 
issue so that appropriate stinkers could be sent :P

As of now, this is beta version. Please run with caution.


## Usage

```bash
cat << EOF > secrets.yml
token: "GITHUB_AUTH_TOKEN"
EOF

go run main.go
```


## TODO

- Put progress on the data fetch process
- Parse the results into better data structure
- Showcase results as folder tree based on depth
