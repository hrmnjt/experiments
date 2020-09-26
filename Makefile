# Makefile

RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m


.PHONY: deploy
deploy:
	@echo "${GREEN}Cleaning build${NC}"
	@rm -rf ./docs
	@echo "${GREEN}Generating build${NC}"
	@hugo
	@echo "www.hrmnjt.dev" > ./docs/CNAME
	@echo "${GREEN}Publishing build on Github${NC}"
	@git add .
	@git commit -m "New deploy @ `date +'%Y-%m-%d %H:%M:%S'`"
	@git push origin master
	@echo "${GREEN}Deployed the latest build on Github${NC}"
	@echo "${GREEN}Please visit https://www.hrmnjt.dev for new stuff${NC}"