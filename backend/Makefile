start:
	nohup uvicorn app.main:app --reload --port 3111 &
	echo "Uvicorn app started on port 3111."

stop:
	pkill -f 'uvicorn app.main:app'
	echo "Uvicorn app stopped."

restart: stop start
