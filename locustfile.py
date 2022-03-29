from locust import HttpUser, task


class TestClass(HttpUser):
    @task
    def go_to_homepage(self):
        self.client.get("/")

    @task
    def go_to_edit_page(self):
        self.client.get("/Restaurants/Edit/2")

    @task
    def go_to_details_page(self):
        self.client.get("/Restaurants/Detail/2")

    @task
    def go_to_privacy(self):
        self.client.get("/Privacy")
