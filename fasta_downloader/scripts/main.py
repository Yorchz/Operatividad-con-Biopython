from api_connection_download.config.Config import Config
from api_connection_download.orchestrator.Main_orchestrator import MainOrchestrator


def main() -> None:
    orchestrator = MainOrchestrator(Config)

    #count = Config.get('data').get('count')
    #orchestrator.execute(count=count)

    ids = Config.get('data').get('ids')
    orchestrator.execute(ids=ids)


if __name__ == "__main__":
    main()
