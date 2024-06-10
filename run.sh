set -x
while true; do
    while read p; do
        p="$p"
        curl -X POST localhost:5000 -d "{\"question\": \"$p\"}"  -H 'Content-Type: application/json'
    done <questions.txt
done