# PythonServer
Cloned from: https://gist.github.com/nitaku/10d0662536f37a087e1b


start with: python server.py 8009

Test the Stuff with:

curl -d '{"test":"nix"}' --header "Content-Type: application/json" http://localhost:8008
curl -d '{"url":"nix"}' --header "Content-Type: application/json" http://localhost:8008
curl -d '{"uuid":"nix"}' --header "Content-Type: application/json" http://localhost:8008

curl -d '{"iregendwas":"nix"}' --header "Content-Type: application/json" http://localhost:8008
