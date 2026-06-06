from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.result: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.result:
            raise IndexError("no data")

        return self.result.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self.result.append((self.rank, str(item)))
                self.rank += 1
        else:
            self.result.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self.result.append((self.rank, item))
                self.rank += 1
        else:
            self.result.append((self.rank, data))
            self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_log(log: Any) -> bool:
            return (
                isinstance(log, dict)
                and all(isinstance(k, str) for k in log.keys())
                and all(isinstance(v, str) for v in log.values())
            )

        if valid_log(data):
            return True

        if isinstance(data, list):
            return all(valid_log(item) for item in data)

        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(log: dict[str, str]) -> str:
            level = log.get("log_level", "")
            message = log.get("log_message", "")
            return f"{level}: {message}"

        if isinstance(data, list):
            for item in data:
                self.result.append((self.rank, format_log(item)))
                self.rank += 1
        else:
            self.result.append((self.rank, format_log(data)))
            self.rank += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handeld = False

            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    handeld = True
                    break

            if not handeld:
                print("error")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")

        for proc in self.processors:
            print(
                f"{proc.__class__.__name__}: "
                f"total {proc.rank} items processed, "
                f"remaining {len(proc.result)} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    print("Initialize Data Stream...")
    ds = DataStream()

    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    numeric = NumericProcessor()
    ds.register_processor(numeric)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)

    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    logs = LogProcessor()

    ds.register_processor(text)
    ds.register_processor(logs)

    print("Send the same batch again")
    ds.process_stream(batch)

    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Consume some elements from the data processors: Numeric 3, Text 2,"
          " Log 1")

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    logs.output()

    print("== DataStream statistics ==")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
