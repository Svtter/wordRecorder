run:
	nohup python3 main.py &

clean:
	rm nohup.out

install:
	mkdir ~/Config
	pip install -r requirements.pip

show:
	cat ~/Config/word.json
