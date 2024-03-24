pip install Flask

# create a named pipe
mkfifo pipe4

# init the flask and vuejs server
(
    # init flask server
    cd backend/ && python3 run.py > pipe4 &
    flask_pid=$! # save process PID

    # init vuejs server
    cd vuetify-project && npm install && npm run dev > pipe4 &
    vue_pid=$! # save process PID

    echo "backend running on http://localhost:3000/transport"
    echo "frontend running on http://localhost:8080/"
    echo "press ctrl + c to stop the backend and frontend"

    wait
)

# stop both servers
kill $flask_pid $vue_pid