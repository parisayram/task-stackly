from pydantic import BaseModel, Field


class UserStatisticsResponse(BaseModel):
    total_users: int = Field(..., description="Total number of users")

    active_users: int = Field(
        ...,
        description="Number of active users"
    )

    inactive_users: int = Field(
        ...,
        description="Number of inactive users"
    )

    active_percentage: float = Field(
        ...,
        description="Percentage of active users"
    )

    new_users_today: int = Field(
        ...,
        description="Users registered today"
    )

    new_users_this_week: int = Field(
        ...,
        description="Users registered this week"
    )

    new_users_this_month: int = Field(
        ...,
        description="Users registered this month"
    )

    users_by_role: dict[str, int] = Field(
        ...,
        description="Number of users grouped by role"
    )