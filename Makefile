

install-dependency:
	@python3 -m venv venv && venv/bin/pip install -r svc/backendsvc/requirements.txt
	@cd svc/frontendsvc && yarn install

run-backend:
	@venv/bin/fastapi dev svc/backendsvc/drivers/rest/main.py

run-frontend:
	@cd svc/frontendsvc && yarn run dev