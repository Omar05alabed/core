from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Self


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with [M]")
        k = []
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                k.append(member)
        if len(k) == 0:
            raise ValueError("Mission must have at least one Commander or "
                             "Captain")
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience < 5:
                    raise ValueError("the crew member need to have atleast "
                                     "5years of experience")

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 7, 20),
        duration_days=900,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=35,
                specialization="Mission Command",
                years_experience=10
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=6
            )
        ],
        budget_millions=2500.0
    )
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destinantion: {mission.destination}")
    print(f"Duaration: {mission.duration_days}")
    print(f"Budget: {mission.budget_millions}")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value})"
              f" - {member.specialization}")

    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Deep Space Survey",
            destination="Jupiter",
            launch_date=datetime(2026, 8, 1),
            duration_days=200,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=30,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="C002",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Engineering",
                    years_experience=7
                )
            ],
            budget_millions=1500.0
        )

    except ValidationError as e:
        print("=========================================")
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    main()
