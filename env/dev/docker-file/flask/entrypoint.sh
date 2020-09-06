pip3 install -r /home/web/requirements.txt
python /init_db.py -p /home/web/sql
gunicorn -w 1 -b 0.0.0.0:5000 app:app --access-logfile /var/log/flask/gunicorn-access.log --error-logfile /var/log/flask/gunicorn-error.log