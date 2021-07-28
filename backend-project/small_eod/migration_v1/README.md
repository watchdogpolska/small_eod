
### Bootstrap on dev:

To run migrator locally:
1. Place v1 SQL DB dump in `./backend-project/small_eod/migration_v1/sql_scripts`, make sure it takes precedence
   before `step_2_create_views.sql`.
2. Bring project up: `docker-compose up -d --build`
3. Check that source DB is up: `docker-compose run --rm backend bash -c 'wait-for-it migration_db:3306'`
4. Migrate v1 data to v2 database: `docker-compose run --rm backend python manage.py migrate_v1`
