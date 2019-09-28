docker exec -it iis-database bash -c "psql iis-database -c \"`cat $1`\""
