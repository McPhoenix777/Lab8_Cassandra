from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider

def cassandra_conn():

   auth_provider = PlainTextAuthProvider(username='cassandra', password='password')
   cluster = Cluster(['127.0.0.1'], load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='US-WEST'), port=9042, auth_provider=auth_provider)

   session = cluster.connect()
   session.execute('USE cityinfo')
   rows = session.execute('SELECT * FROM users')
   for row in rows:
       print(row.age, row.name, row.username)