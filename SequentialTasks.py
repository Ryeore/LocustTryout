from locust import SequentialTaskSet, HttpUser, task, constant

# SequentialTaskSet allows to execute tests 1 by 1 "in order" not randomly as in TasksSet


class SeqTask(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get 200")

    @task
    def get_status500(self):
        self.client.get("/500")
        print("Get 500")


class LoadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [SeqTask]