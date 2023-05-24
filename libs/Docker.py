import docker

class Docker:
    def __init__(self, base_url, container_name) -> None:
        self.base_url = base_url
        self.container_name = container_name
        self.cl = self.client()
        super().__init__()

    def client(self) -> docker.client.DockerClient:
        return docker.from_env(base_url=self.base_url)
    
    def images(self) -> list:
        return self.cl.images.list()
    
    def containers(self) -> list:
        return self.cl.containers.list()
    
    def container(self) -> docker.models.containers.Container:
        return self.cl.containers.get(self.container_name)
    
    def start_container_by_name(self) -> str:
        self.container().start()
        return self.container().status

    def stop_container_by_name(self) -> str:
        self.container().stop()
        return self.container().status

    def restart_container_by_name(self) -> str:
        self.container().restart()
        return self.container().status