from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        collected = []

        for proc in self.processors:
            for _ in range(nb):
                if proc.result:
                    collected.append(proc.output())

        plugin.process_output(collected)


class CSV:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []
        for _, value in data:
            items.append(f"{value}")

        csv_output = ",".join(items)
        print(csv_output)


class JSON:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []
        for rank, value in data:
            items.append(f'"item_{rank}": "{value}"')

        json_output = "{" + ", ".join(items) + "}"
        print(json_output)


def main() -> None:
    stream = DataStream()

    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    stream.process_stream([
        3.14,
        "Hello world",
        {"log_level": "INFO", "log_message": "system started"},
        -7,
        "Hi",
        {"log_level": "WARNING", "log_message": "low disk"}
    ])

    stream.print_processors_stats()

    print("\nCSV OUTPUT:")
    stream.output_pipeline(3, CSV())

    stream.process_stream([
        2.71,
        "Another text",
        {"log_level": "ERROR", "log_message": "crash detected"}
    ])

    print("\nJSON OUTPUT:")
    stream.output_pipeline(2, JSON())


if __name__ == "__main__":
    main()
