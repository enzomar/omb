echo '===> installing user requirements'
pip3 install -r /home/web/requirements.txt
echo '===> execute sql'
python /init_db.py -p /home/web/sql
echo '===> start flask via gunicorn, workers: '$GUN_WORKERS
#gunicorn -w $GUN_WORKERS -b 0.0.0.0:5000 app:app --access-logfile /var/log/flask/gunicorn-access.log --error-logfile /var/log/flask/gunicorn-error.log
gunicorn -w $GUN_WORKERS -b 0.0.0.0:5000 app:app


