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
        if isinstance(data, dict):
            return (
                all(isinstance(k, str) for k in data.keys())
                and all(isinstance(v, str) for v in data.values())
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(isinstance(k, str) for k in item.keys())
                and all(isinstance(v, str) for v in item.values())
                for item in data
            )

        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        if isinstance(data, dict):
            get_line = f"{data['log_level']}: {data['log_message']}"
            self.result.append((self.rank, get_line))
            self.rank += 1

        else:
            for item in data:
                get_line = f"{item['log_level']}: {item['log_message']}"
                self.result.append((self.rank, get_line))
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
    r = DataStream()
    r.register_processor(TextProcessor())
    r.register_processor(LogProcessor())
    r.register_processor(NumericProcessor())

    data = [
        "Omar al_abed",
        ["Hello", "world"],
        42,
        [3.14, -1, 2.71],
        {"log_level": "Omar", "log_message": "Al_abed"},
    ]

    r.process_stream(data)
    r.print_processors_stats()

    for proc in r.processors:
        print(proc.output())

    r.print_processors_stats()


if __name__ == "__main__":
    main()
