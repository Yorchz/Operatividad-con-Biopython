from src.config.Config import Config
from src.orchestrator.MainOrchestrator import MainOrchestrator


def main(filename=None, download=False, file_ids=None):

    orchestrator = MainOrchestrator(Config)

    if download and file_ids:
        orchestrator.execute_download(file_ids)

    if filename:
        orchestrator.execute_read_single(filename)
    else:
        orchestrator.execute_read_all()


if __name__ == "__main__":
    main()
