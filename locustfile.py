from locust import HttpUser, task


class TestClass(HttpUser):
    @task
    def go_to_homepage(self):
        self.client.get("/")
