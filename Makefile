build:
	docker build -f Dockerfile -t mongo_exploration:latest .

run:
	docker run -exec -it -v /users/jchemburkar/projects/exploring-mongo:/usr/src mongo_exploration /bin/sh
