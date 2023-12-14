from locust import HttpUser, task, constant, SequentialTaskSet


class VerifyResponse(SequentialTaskSet):

    @task
    def get_xml(self):
        result = self.client.get("/xml", name="XML")
        print(result)

    @task
    def get_json(self):
        expected_response = "Wake up to WonderWidget"

        with self.client.get("/json", catch_response=True, name="JSON") as response:
            result = True if expected_response in response.text else False
            print(self.get_json.__name__, result)
            response.success()

    @task
    def get_robots(self):
        expected_response = '*'
        result = "Success"

        with self.client.get("/robots.txt", catch_response=True, name="Robots") as response:
            if expected_response in response:
                result = "Success"
                # response.failure("Not a failure")
        print(self.get_robots.__name__, result)

    @task
    def get_failure(self):
        expected_response = 404
        with self.client.get("/status/404", catch_response=True, name="HTTP 404") as response:
            if response.status_code == expected_response:
                response.failure("404 hit")
            else:
                response.success()


class LoadTest(HttpUser):
    host = "https://httpbin.org"
    tasks = [VerifyResponse]