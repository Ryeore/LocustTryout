from locust import HttpUser, task, constant, SequentialTaskSet


class RequestOrder(SequentialTaskSet):

    @task
    def place_order(self):

        form = {
            "comments": "some sample instructions here",
            "custemail": "mail@gmail.com",
            "custname": "John Doe",
            "custtel": "1234567",
            "delivery": "18:00",
            "size": "medium",
            "topping": "onion"}

        name = "Order for " + form['custname']

        with self.client.post("/post", catch_response=True, name=name, data=form) as response:
            if response.status_code == 200 and form['custname'] in response.text:
                response.success()
            else:
                response.failure("Failure in processing the order")


class LoadTest(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [RequestOrder]