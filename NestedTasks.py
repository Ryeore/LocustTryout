from locust import HttpUser, constant, task, TaskSet


class GetHttpCat(TaskSet):

    @task
    def get_status200(self):
        self.client.get("/200")
        print("Get 200")
        self.interrupt(reschedule=False)


class GetAnotherHttpCat(TaskSet):
    @task
    def get_status500(self):
        self.client.get("/500")
        print("Get 500")
        # reschedule - set up the "timer" between jumps to parent class | False for break
        self.interrupt(reschedule=False)



class LoadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [GetHttpCat, GetAnotherHttpCat]