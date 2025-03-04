import argparse
import docker

def restart_container(container_name):
    client = docker.from_env()
    try:
        container = client.containers.get(container_name)
        container.restart()
        print(f"Container '{container_name}' restarted successfully.")
    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found.")
    except docker.errors.APIError as e:
        print(f"Failed to restart container '{container_name}'. Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Restart Docker containers.')
    parser.add_argument("-c", "--container", type=str, nargs='+', help='The names of the containers to restart')
    args = parser.parse_args()

    for container_name in args.container_names:
        restart_container(container_name)
