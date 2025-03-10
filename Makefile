.PHONY: compile run run-debug clean

compile:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python3 src/main.py && deactivate

run-debug:
	. venv/bin/activate && python3 src/main.py -debug && deactivate

clean:
	rm -rf venv
