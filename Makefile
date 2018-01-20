run:
	nohup python3 main.py &

clean:
	rm nohup.out

install:
	pip install pipenv
	pipenv install
