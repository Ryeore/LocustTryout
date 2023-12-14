from locust import HttpUser, TaskSet, task


class WebsiteTasks(TaskSet):
    @task(3)
    def main_page(self):
        self.client.get("/")
        print("test main")

    @task(1)
    def top_posts(self):
        self.client.get("/top")
        print("test top")

class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    host = "https://www.reddit.com"

    min_wait = 2 * 1000
    max_wait = 6 * 1000