setup-api:
	cd ./back-end && \
	python3 -m venv venv && \
	. venv/bin/activate && \
	pip install -r requirements.txt

setup-ui:
	cd ./front-end && \
	npm install

run-api:
	cd ./back-end && \
	. venv/bin/activate && \
	python3 -m app.main

run-ui:
	cd ./front-end && \
	npm run dev
