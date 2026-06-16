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


def main() -> None:
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print(num.validate(0))
    print(num.validate("s"))

    print(text.validate("s"))
    print(text.validate(0))

    print(log.validate("s"))
    print(log.validate({"s": "s"}))

    try:
        num.ingest("s")

    except Exception as e:
        print(e)

    try:
        text.ingest(0)

    except Exception as e:
        print(e)

    try:
        log.ingest("s")

    except Exception as e:
        print(e)

    num.ingest(4)
    num.ingest([20, 30, 40])

    while True:
        try:
            print(num.output())
        except IndexError:
            break

    text.ingest("O")
    text.ingest(["m", "a", "r"])

    while True:
        try:
            print(text.output())
        except IndexError:
            break

    log.ingest({"log_level": "Omar", "log_message": "Al_abed"})
    log.ingest([{"log_level": "O", "log_message": "m"},
                {"log_level": "a", "log_message": "r"}])

    while True:
        try:
            print(log.output())
        except IndexError:
            break


if __name__ == "__main__":
    main()
