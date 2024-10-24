from src.config.Config import Config
from src.orchestrator.DownloaderOrchestrator import DownloaderOrchestrator


def main() -> None:
    orchestrator = DownloaderOrchestrator(Config)

    #count = Config.get('data').get('count')
    #orchestrator.execute(count=count)

    ids = Config.get('data').get('ids')
    orchestrator.execute(ids=ids)


if __name__ == "__main__":
    main()
