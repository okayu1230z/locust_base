from locust import HttpUser, task, constant_throughput
import random, string, os

host = os.environ['HOST']

def create_name(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def create_number():
    return random.randint(0, 300)

class UserScinario(HttpUser):
    host = "http://" + host + ":3001"
    wait_time = constant_throughput(1)
    
    @task(1)
    def find_user(self):
        id = create_number()
        with self.client.get("/%s" % (id), catch_response=True) as response:
            if response.status_code != 200:
                response.failure("get status code is not 200")

    @task(2)
    def create_user(self):
        name = create_name(1000)
        data = {"name": name}
        with self.client.post(url="/", headers={"Content-Type": "application/json"},
                                json=data, catch_response=True) as response:
            if response.status_code != 201:
                response.failure("post status code is not 201")