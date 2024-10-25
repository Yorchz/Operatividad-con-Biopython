from src.config.Config import Config
from src.orchestrator.MainOrchestrator import MainOrchestrator


def main(filename=None, download=None, file_ids=None):

    orchestrator = MainOrchestrator(Config)

    if download and file_ids:
        print(2)
        orchestrator.execute_download(file_ids)

    if filename:
        orchestrator.execute_read_single(filename)
    else:
        orchestrator.execute_read_all()


if __name__ == "__main__":
    main("NM_001301717", True, ["NM_001301717", "NM_001374413", "NM_001301720"])
