# despliegue-apps
prueba 1 despliegue

use jamuq$confival_db1; source confival.sql;
mkvirtualenv --python=python3.7 confival
git clone https://github.com/desarrollo-confival/despliegue-apps.git
(confival) 21:22 ~ $ cd despliegue-apps/
(confival) 21:33 ~/despliegue-apps (master)$ pip install -r requirements.txt
which python

mysql -h jamuq.mysql.pythonanywhere-services.com -u jamuq 'jamuq$confival_db1' -p --local-infile=1
 "--local-infile=1"