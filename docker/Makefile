
# Note: creates "rworkshop" image and "rworkshop-instance" container
# Make sure you're not already using these names!

build :
	docker build -t rworkshop rworkshop

start :
	docker run -d -p 127.0.0.1:8787:8787 \
		-e PASSWORD=testing \
		--name rworkshop-instance rworkshop
	@echo http://127.0.0.1:8787 username: rstudio, password: testing

stop :
	docker stop rworkshop-instance
	docker rm rworkshop-instance

push :
	docker tag rworkshop paulfharrison/rworkshop
	docker push paulfharrison/rworkshop

