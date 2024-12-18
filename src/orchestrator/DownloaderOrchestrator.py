import json
from typing import List, Optional
from src.conections.Connection import NCBIConnection
from src.downloader.FastaDownloader import FastaDownloader
from src.downloader.IdFetcher import IdFetcher
from src.downloader.SingleFastaDownloader import SingleFastaDownloader
from src.validator.FormatValidator import FormatValidator
from src.validator.NonEmptyValidator import NonEmptyValidator
from src.validator.SequenceValidator import SequenceValidator
from src.utils.FilePathHelper import FilePathHelper


class DownloaderOrchestrator:
    def __init__(self, config: json):
        self.connection = NCBIConnection(config["email"]["address"])

        self.id_fetcher = IdFetcher(config)

        self.single_fasta_downloader = SingleFastaDownloader(config["download"])
        self.downloader = FastaDownloader(self.single_fasta_downloader)

        self.validators = [
            FormatValidator(),
            SequenceValidator(),
            NonEmptyValidator()
        ]

    def download_files(self, count: Optional[int] = None, ids: Optional[List[str]] = None) -> List[str]:
        self.connection.connect()

        identifiers = self._get_identifiers(count, ids)
        downloaded_files = self.downloader.download_fasta_files(identifiers)
        valid_files = self.validate_files(downloaded_files)

        print("\nArchivos FASTA válidos:", valid_files)
        return valid_files

    def validate_files(self, files: List[str]) -> List[str]:
        valid_files: List[str] = []
        for file_name in files:
            if file_name and all(validator.validate(file_name) for validator in self.validators):
                valid_files.append(FilePathHelper.get_filename_only(file_name))
        return valid_files

    def _get_identifiers(self, count: Optional[int], ids: Optional[List[str]]) -> List[str]:
        return ids or (self.id_fetcher.fetch_ids(count) if count is not None else self._raise_missing_argument_error())

    def _raise_missing_argument_error(self) -> None:
        raise ValueError("Debe proporcionar 'count' o 'ids' para ejecutar el proceso.")
