<b>Example code for a django app with periodic tasks (using celery) running on Cloud Foundry</b>

1. Create 2 services called celerymysql and celeryrabbit
2. cf push --no-route -c "bash ./init_db.sh"
3. cf push
4. Navigate to /app to see a counter which increases by 1 every 10 seconds
