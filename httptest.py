from locust import task, TaskSet, constant, HttpUser
import random


class HttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("get status of 200")

    @task
    def get_random_status(self):
        status_codes = [100, 101, 200, 201, 202, 204, 206, 300, 301, 302, 304, 307, 400, 401, 403, 404, 405, 408, 429,
                        500, 501, 503]
        random_url = '/' + str(random.choice(status_codes))
        self.client.get(random_url)
        print("random code check")


class LoadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [HttpCat]

'''
Type     Name            # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|--------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /101                 3     0(0.00%) |     61      15     153     16 |    0.10        0.00
GET      /200                10     0(0.00%) |     21      15      59     16 |    0.34        0.00
GET      /201                 1     0(0.00%) |    121     121     121    121 |    0.03        0.00
GET      /204                 2     0(0.00%) |     16      16      16     16 |    0.07        0.00
GET      /300                 1     0(0.00%) |    130     130     130    130 |    0.03        0.00
GET      /301                 3     0(0.00%) |     84      15     223     15 |    0.10        0.00
GET      /307                 2     0(0.00%) |     18      16      19     16 |    0.07        0.00
GET      /400                 1     0(0.00%) |    126     126     126    126 |    0.03        0.00
GET      /401                 1     0(0.00%) |     15      15      15     15 |    0.03        0.00
GET      /403                 2     0(0.00%) |     17      16      19     16 |    0.07        0.00
GET      /404                 1     0(0.00%) |     16      16      16     16 |    0.03        0.00
GET      /408                 1     0(0.00%) |    118     118     118    118 |    0.03        0.00
GET      /429                 1     0(0.00%) |    103     103     103    103 |    0.03        0.00
--------|--------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated          29     0(0.00%) |     47      15     223     17 |    0.98        0.00
'''