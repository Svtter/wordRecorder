run:
	nohup python3 main.py &

clean:
	rm nohup.out

install:
	mkdir ~/Config
	pip install pipenv
	pipenv install

show:
	cat ~/Config/word.json
